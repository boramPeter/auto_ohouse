import time,os
import unittest
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from app.common.base_method.app_start_func import AppStart
from app.common.base_method.logger_func import *
from app.common.base_method.screenshot_func import CaptureClass
from app.common.base_method.ios_result_binary import Result
from app.common.base_method.aos_result_binary import ResultAndroid
from app.ios.locator.precondition.app_install import ProviderInstallLocator
from selenium.common.exceptions import WebDriverException
from web.BasicSetting.logger_func import make_logger_web
import inspect
import report.goole_spread_sheet_func.update_spread_sheet_func as update_sheet
# from report.testrail_func.festrail_api import add_result_for_case

logger_ios = make_logger_ios("ios_log.py")
logger_aos = make_logger_aos("aos_log.py")
logger_web = make_logger_web("jenkins_web_log.py")


def timeout_handler(code_execution, locator,locator_method=None):
    global need_fix_locator,fix_locator_name
    try:
        return code_execution()
    except StaleElementReferenceException:
        raise TimeoutException(f"요소가 화면에서 사라짐. 확인 필요: {str(locator)}")
    except TimeoutException:
        # import mcp_automation.auto_ui_runner.android_AI_testrunner as ai_runner
        from mcp_automation.auto_locator_fix.AI_locator_handler import auto_repair_locator
        if os.environ.get("ANDROID_AUTO_FLAG") == "1" or os.environ.get("IOS_AUTO_FLAG") == "1":
            try:
                os.environ["NEED_FIX_LOCATOR"] = "1"
                os.environ["FIX_LOCATOR_NAME"] = str(locator)
                auto_repair_locator()
                print("auto_repair_locator 호출 완료")
                code_execution()
                return print("code_execution 호출 완료")
            except TimeoutException:
                print(f"보정 이후 요소 확인 필요: {str(locator)}")
                raise TimeoutException(f"보정 후 요소 확인 필요: {str(locator)}")
            finally:
                os.environ["NEED_FIX_LOCATOR"] = "0"
                os.environ["FIX_LOCATOR_NAME"] = "0"
        raise TimeoutException(f"요소 확인 필요: {str(locator)}")
    except ElementClickInterceptedException:
        raise TimeoutException(f"웹뷰 요소 확인 필요: {str(locator)}")
    except WebDriverException as e:
        error_message = str(e)
        raise TimeoutException(f"WebDriverException 발생. {error_message[:20] + '...' if len(error_message) > 20 else error_message}")
    except Exception as e: # web timeout (TimeoutError, AssertionError 등)
        print(e)
        raise TimeoutException(f"웹 요소 확인 필요: {str(locator)}")

def write_log(platform, msg):
    # 현재 호출한 프레임의 정보 얻기
    caller_frame = inspect.currentframe().f_back
    caller_info = inspect.getframeinfo(caller_frame)
    
    # 파일명, 라인 번호, 함수명 얻기
    filename = caller_info.filename.split('/')[-1]
    lineno = caller_info.lineno
    function_name = caller_info.function

    # 커스터마이즈된 로그 메시지 작성
    log_msg = f"{msg} (file:{filename}|Line:{lineno}|func:{function_name})"
    
    if platform == 'web':
        logger_web.debug(log_msg)
    elif platform == 'ios':
        logger_ios.debug(log_msg)
    elif platform == 'aos':
        logger_aos.debug(log_msg)

def extract_sheet_name(func_name):
    service_name = ''
    case_id = ''
    func_parts = func_name.split('_')
    if func_parts[1] == 'comm': # comm_service, comm_platform
        service_name = func_parts[1].capitalize() + '_' + func_parts[2][:-5].capitalize()
        case_id = func_parts[2][-5:]
    else:
        service_name = func_parts[1][:-5].capitalize()
        case_id = func_parts[1][-5:]
    
    if service_name in ('O2o', 'Mkt'):
        service_name = service_name.upper()

    return [service_name, case_id]

class ExceptionHandler:
    def ios_exceptions_handler(
            self,
            current_function_name,
            step=None,
            back_flow=None,
            opt_title2=None,
            opt_result2=None,
            opt_title_assert2=None,
            opt_result_assert2=None,
            opt_title_exception2=None,
            opt_result_exception2=None,
            max_retries=3

    ):
        try:
            sheet_id = Result().read_result_slack('iOS_spreadsheet')
        except (FileNotFoundError, KeyError):
            Result().write_result('iOS_spreadsheet', "")
            sheet_id = Result().read_result_slack('iOS_spreadsheet')

        # try:
        #     Result().read_result_slack('ios_testrail')
        # except (FileNotFoundError, KeyError):
        #     Result().write_result('ios_testrail', "None")

        sheet_info = extract_sheet_name(current_function_name)
        
        try:
            # 재시도 횟수 설정
            retries = 0
            while retries < max_retries:
                if step is not None:
                    try:
                        step()
                        break
                    except (TimeoutException,WebDriverException) as e:
                        if "step" in current_function_name:
                            if retries == 2:
                                ##### check
                                # if ProviderCommonMethod.get_xml_depth(self) < 300:
                                #     logger_ios.debug(
                                #         f"{current_function_name} xml depth: {ProviderCommonMethod.get_xml_depth(self)}")
                                CaptureClass.capture_screenshot_put_name(self, current_function_name)
                                AppStart.ios_ohou_restart(self)
                                logger_ios.debug(f"{current_function_name}: {e}, 재시도 횟수 {retries}회")
                                Result().write_result(current_function_name, f'*Fail* ({e},재시도 횟수 {retries}회)')
                                if sheet_id != "":
                                    update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Fail')

                                # if Result().read_result_slack("ios_testrail") == "pass":
                                #     add_result_for_case("iOS",current_function_name,"fail")

                                if opt_title_exception2 is not None:
                                    Result().write_result(opt_title_exception2, f'{opt_result_exception2}')
                                self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")
                                return
                            else:
                                retries += 1
                                time.sleep(2)
                                try:
                                    logout_btn = ProviderInstallLocator(self.driver)
                                    logout_btn.click_quick(ProviderInstallLocator.logout_btn)
                                    print("다시 시도하기 선택 완료(restart)")

                                except TimeoutException:
                                    print("다시 시도하기 없어서 스킵.(restart)")
                                AppStart.ios_ohou_restart(self)
                                print(f"재시도 횟수 {retries}회")
                                continue
                        else:
                            ##### check
                            # if ProviderCommonMethod.get_xml_depth(self) < 300:
                            #     logger_ios.debug(
                            #         f"{current_function_name} xml depth: {ProviderCommonMethod.get_xml_depth(self)}")
                            CaptureClass.capture_screenshot_put_name(self, current_function_name)
                            AppStart.ios_ohou_restart(self)
                            logger_ios.debug(f"{current_function_name}: {e}")
                            Result().write_result(current_function_name, f'*Fail* ({e})')
                            if sheet_id != "":
                                update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Fail')

                            # if Result().read_result_slack("ios_testrail") == "pass":
                            #     add_result_for_case("iOS", current_function_name, "fail")

                            if opt_title_exception2 is not None:
                                Result().write_result(opt_title_exception2, f'{opt_result_exception2}')
                            self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")
                            return

            if back_flow is not None:
                try:
                    back_flow()
                    print("back flow 실행 완료")
                except TimeoutException as e:
                    ##### check
                    # if ProviderCommonMethod.get_xml_depth(self) < 300:
                    #     logger_ios.debug(
                    #         f"{current_function_name} xml depth: {ProviderCommonMethod.get_xml_depth(self)}")
                    CaptureClass.capture_screenshot_put_name(self, current_function_name)
                    AppStart.ios_ohou_restart(self)
                    logger_ios.debug(f"{current_function_name}: {e}")
                    Result().write_result(current_function_name, f'*Fail* ({e},재시도 횟수 {retries}회)')
                    if sheet_id != "":
                        update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Fail')

                    # if Result().read_result_slack("ios_testrail") == "pass":
                    #     add_result_for_case("iOS", current_function_name, "fail")

                    return
            if "check" in current_function_name:
                logger_ios.debug(f"{current_function_name}: pass(재시도 횟수 {retries}회)")
                Result().write_result(current_function_name, f'*Pass*')
                if sheet_id != "":
                    update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Pass')

                # if Result().read_result_slack("ios_testrail") == "pass":
                #     add_result_for_case("iOS", current_function_name, "pass")
            if opt_title2 is not None:
                Result().write_result(opt_title2, f'{opt_result2}')

        except AssertionError as exception:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            # if ProviderCommonMethod.get_xml_depth(self) < 300:
            #     logger_ios.debug(
            #         f"{current_function_name} xml depth: {ProviderCommonMethod.get_xml_depth(self)}")
            if back_flow is not None:
                try:
                    back_flow()
                except TimeoutException as e:
                    CaptureClass.capture_screenshot_put_name(self, current_function_name)
                    AppStart.ios_ohou_restart(self)
                    logger_ios.debug(f"{current_function_name}: {e}")
                    Result().write_result(current_function_name, f'*Fail* ({e})')
                    if sheet_id != "":
                        update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Fail')

                    # if Result().read_result_slack("ios_testrail") == "pass":
                    #     add_result_for_case("iOS", current_function_name, "fail")
                    return
            logger_ios.debug(f"{current_function_name}: {exception}")
            Result().write_result(current_function_name, f'*Fail* ({exception})')
            if sheet_id != "":
                update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Fail')
            # if Result().read_result_slack("ios_testrail") == "pass":
            #     add_result_for_case("iOS", current_function_name, "fail")
            if opt_title_assert2 is not None:
                Result().write_result(opt_title_assert2, f'{opt_result_assert2}')


    def aos_exceptions_handler(
            self,
            current_function_name,
            step=None,
            back_flow=None,
            opt_title2=None,
            opt_result2=None,
            opt_title_assert2=None,
            opt_result_assert2=None,
            opt_title_exception2=None,
            opt_result_exception2=None,
            max_retries=3
    ):
        try:
            sheet_id = ResultAndroid().read_result_slack('android_spreadsheet')
        except (FileNotFoundError, KeyError):
            ResultAndroid().write_result('android_spreadsheet', "")
            sheet_id = ResultAndroid().read_result_slack('android_spreadsheet')

        # try:
        #     ResultAndroid().read_result_slack('android_testrail')
        # except (FileNotFoundError, KeyError):
        #     ResultAndroid().write_result('android_testrail', "None")

        sheet_info = extract_sheet_name(current_function_name)

        try:
            # 재시도 횟수 설정
            retries = 0
            while retries < max_retries:
                if step is not None:
                    try:
                        step()
                        break
                    except (TimeoutException,WebDriverException) as e:
                        if "step" in current_function_name:
                            if retries == 2:
                                ##### check
                                # if ProviderCommonMethod.get_xml_depth(self) < 300:
                                #     logger_aos.debug(
                                #         f"{current_function_name} xml depth: {ProviderCommonMethod.get_xml_depth(self)}")
                                CaptureClass.capture_screenshot_put_name(self, current_function_name)
                                AppStart.android_ohou_restart(self, current_function_name)
                                logger_aos.debug(f"{current_function_name}: {e}, 재시도 횟수 {retries}회")
                                ResultAndroid().write_result(current_function_name, f'*Fail* ({e}, 재시도 횟수 {retries}회))')
                                if sheet_id != "":
                                    update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Fail')
                                # if ResultAndroid().read_result_slack("android_testrail") == "pass":
                                #     add_result_for_case("android", current_function_name, "fail")
                                if opt_title_exception2 is not None:
                                    ResultAndroid().write_result(opt_title_exception2, f'{opt_result_exception2}')
                                self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")
                                return
                            else:
                                retries += 1
                                AppStart.android_ohou_restart(self, current_function_name)
                                print(f"재시도 횟수 {retries}회")
                                continue
                        else:
                            ##### check
                            # if ProviderCommonMethod.get_xml_depth(self) < 300:
                            #     logger_aos.debug(
                            #         f"{current_function_name} xml depth: {ProviderCommonMethod.get_xml_depth(self)}")
                            CaptureClass.capture_screenshot_put_name(self, current_function_name)
                            AppStart.android_ohou_restart(self, current_function_name)
                            logger_aos.debug(f"{current_function_name}: {e}")
                            ResultAndroid().write_result(current_function_name, f'*Fail* ({e})')
                            if sheet_id != "":
                                update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Fail')
                            # if ResultAndroid().read_result_slack("android_testrail") == "pass":
                            #     add_result_for_case("android", current_function_name, "fail")
                            if opt_title_exception2 is not None:
                                ResultAndroid().write_result(opt_title_exception2, f'{opt_result_exception2}')
                            self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")
                            return

            if back_flow is not None:
                try:
                    back_flow()
                    print("back flow 실행 완료")
                except TimeoutException as e:
                    ##### check
                    # if ProviderCommonMethod.get_xml_depth(self) < 300:
                    #     logger_aos.debug(
                    #         f"{current_function_name} xml depth: {ProviderCommonMethod.get_xml_depth(self)}")
                    CaptureClass.capture_screenshot_put_name(self, current_function_name)
                    AppStart.android_ohou_restart(self, current_function_name)
                    logger_aos.debug(f"{current_function_name}: {e}")
                    ResultAndroid().write_result(current_function_name, f'*Fail* ({e})')
                    if sheet_id != "":
                        update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Fail')
                    # if ResultAndroid().read_result_slack("android_testrail") == "pass":
                    #     add_result_for_case("android", current_function_name, "fail")
                    return

            if "check" in current_function_name:
                logger_aos.debug(f"{current_function_name}: pass")
                ResultAndroid().write_result(current_function_name, f'*Pass*')
                if sheet_id != "":
                    update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Pass')
                # if ResultAndroid().read_result_slack("android_testrail") == "pass":
                #     add_result_for_case("android", current_function_name, "pass")
            if opt_title2 is not None:
                ResultAndroid().write_result(opt_title2, f'{opt_result2}')

        except AssertionError as exception:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            # if ProviderCommonMethod.get_xml_depth(self) < 300:
            #     logger_aos.debug(
            #         f"{current_function_name} xml depth: {ProviderCommonMethod.get_xml_depth(self)}")
            if back_flow is not None:
                try:
                    back_flow()
                except TimeoutException as e:
                    CaptureClass.capture_screenshot_put_name(self, current_function_name)
                    AppStart.android_ohou_restart(self, current_function_name)
                    logger_aos.debug(f"{current_function_name}: {e}")
                    ResultAndroid().write_result(current_function_name, f'*Fail* ({e})')
                    if sheet_id != "":
                        update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Fail')
                    # if ResultAndroid().read_result_slack("android_testrail") == "pass":
                    #     add_result_for_case("android", current_function_name, "fail")
                    return
            logger_aos.debug(f"{current_function_name}: {exception}")
            ResultAndroid().write_result(current_function_name, f'*Fail* ({exception})')
            if sheet_id != "":
                update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Fail')
            # if ResultAndroid().read_result_slack("android_testrail") == "pass":
            #     add_result_for_case("android", current_function_name, "fail")
            if opt_title_assert2 is not None:
                ResultAndroid().write_result(opt_title_assert2, f'{opt_result_assert2}')

    def ios_testflight_exceptions_handler(
            self,
            current_function_name,
            step=None,
            back_flow=None,
            opt_title2=None,
            opt_result2=None,
            opt_title_assert2=None,
            opt_result_assert2=None,

    ):
        try:
            if step is not None:
                step()
                print("step 실행 완료")
            if back_flow is not None:
                back_flow()
                print("back flow 실행 완료")
            if "check" in current_function_name:
                logger_ios.debug(f"{current_function_name}: pass")
                Result().write_result(current_function_name, f'*Pass*')
            if opt_title2 is not None:
                Result().write_result(opt_title2, f'{opt_result2}')

        except AssertionError as exception:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            if back_flow is not None:
                back_flow()
            logger_ios.debug(f"{current_function_name}: {exception}")
            Result().write_result(current_function_name, f'*Fail* ({exception})')
            if opt_title_assert2 is not None:
                Result().write_result(opt_title_assert2, f'{opt_result_assert2}')

        except TimeoutException as e:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            AppStart.testflight_close(self)
            logger_ios.debug(f"{current_function_name}: {e}")
            Result().write_result(current_function_name, f'*Fail* ({e})')
            Result().write_result("앱 설치 precondition", "fail")
            self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")

    def aos_deploy_exceptions_handler(
            self,
            current_function_name,
            step=None,
            back_flow=None,
            opt_title2=None,
            opt_result2=None,
            opt_title_assert2=None,
            opt_result_assert2=None
    ):
        try:
            if step is not None:
                step()
                print("step 실행 완료")
            if back_flow is not None:
                back_flow()
                print("back flow 실행 완료")
            if "check" in current_function_name:
                logger_aos.debug(f"{current_function_name}: pass")
                ResultAndroid().write_result(current_function_name, f'*Pass*')
            if opt_title2 is not None:
                ResultAndroid().write_result(opt_title2, f'{opt_result2}')

        except AssertionError as exception:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            if back_flow is not None:
                back_flow()
            logger_aos.debug(f"{current_function_name}: {exception}")
            ResultAndroid().write_result(current_function_name, f'*Fail* ({exception})')
            if opt_title_assert2 is not None:
                ResultAndroid().write_result(opt_title_assert2, f'{opt_result_assert2}')

        except TimeoutException as e:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            AppStart.deploy_gate_close(self)
            logger_aos.debug(f"{current_function_name}: {e}")
            ResultAndroid().write_result(current_function_name, f'*Fail* ({e})')
            ResultAndroid().write_result("앱 설치 precondition", "fail")
            self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")

    ############################################################################################################
    def aos_exceptions_handler_pre_condition(
            self,
            current_function_name,
            step=None,
            back_flow=None,
            opt_result=None,
            opt_title2=None,
            opt_result2=None,
            opt_result_assert=None,
            opt_title_assert2=None,
            opt_result_assert2=None,
            opt_result_exception=None,
            opt_title_exception2=None,
            opt_result_exception2=None
    ):
        try:
            if step is not None:
                step()
            if back_flow is not None:
                back_flow()
            logger_aos.debug(f"{current_function_name}: pass")
            if opt_result is not None:
                ResultAndroid().write_result(current_function_name, f'*{opt_result}*')
            if opt_title2 is not None:
                ResultAndroid().write_result(opt_title2, f'{opt_result2}')

        except AssertionError as exception:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            if back_flow is not None:
                back_flow()
            logger_aos.debug(f"{current_function_name}: {exception}")
            if opt_result_assert is not None:
                ResultAndroid().write_result(current_function_name, f'*{opt_result_assert}*')
            if opt_title_assert2 is not None:
                ResultAndroid().write_result(opt_title_assert2, f'{opt_result_assert2}')
            self.scenario.skip(reason=f"{exception}에러로 시나리오 스킵")

        except TimeoutException as e:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            logger_aos.debug(f"{current_function_name}: {e}")
            if opt_result_exception is not None:
                ResultAndroid().write_result(current_function_name, f'*{opt_result_exception}*')
            if opt_title_exception2 is not None:
                ResultAndroid().write_result(opt_title_exception2, f'{opt_result_exception2}')
            self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")

    def ios_exceptions_handler_pre_condition(
            self,
            current_function_name,
            step=None,
            back_flow=None,
            opt_result=None,
            opt_title2=None,
            opt_result2=None,
            opt_result_assert=None,
            opt_title_assert2=None,
            opt_result_assert2=None,
            opt_result_exception=None,
            opt_title_exception2=None,
            opt_result_exception2=None
    ):
        try:
            if step is not None:
                step()
            if back_flow is not None:
                back_flow()
            logger_ios.debug(f"{current_function_name}: pass")
            if opt_result is not None:
                Result().write_result(current_function_name, f'*{opt_result}*')
            if opt_title2 is not None:
                Result().write_result(opt_title2, f'{opt_result2}')

        except AssertionError as exception:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            if back_flow is not None:
                back_flow()
            logger_ios.debug(f"{current_function_name}: {exception}")
            if opt_result_assert is not None:
                Result().write_result(current_function_name, f'*{opt_result_assert}*')
            if opt_title_assert2 is not None:
                Result().write_result(opt_title_assert2, f'{opt_result_assert2}')
            self.scenario.skip(reason=f"{exception}에러로 시나리오 스킵")

        except TimeoutException as e:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            logger_ios.debug(f"{current_function_name}: {e}")
            if opt_result_exception is not None:
                Result().write_result(current_function_name, f'*{opt_result_exception}*')
            if opt_title_exception2 is not None:
                Result().write_result(opt_title_exception2, f'{opt_result_exception2}')
            self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")
            