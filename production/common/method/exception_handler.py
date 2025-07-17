import time,os,re
from selenium.common.exceptions import TimeoutException,ElementClickInterceptedException, WebDriverException, StaleElementReferenceException
from app.common.base_method.app_start_func import AppStart
from app.common.base_method.logger_func import *
from app.common.base_method.screenshot_func import CaptureClass
from app.common.base_method.recording_func import ScreenRecoder
from web.BasicSetting.exception_func import capture_screenshot
from production.common.method.result_binary import TestResult
from production.app.android.android_locator.all_locator.locator import ProviderLocatorAndroid
from production.app.ios.ios_locator.all_locator.locator import ProviderLocatorIos

from functools import partial


import pytest
from app.common.base_method.appium_method import ProviderCommonMethod
import web.BasicSetting.logger_func as lf
logger_web = lf.logger_web

logger_ios = make_logger_ios("prod_ios_log.py")
logger_aos = make_logger_aos("prod_aos_log.py")
'''
모도님과 테오님을 위한 간략한 설명
- 바이너리에 있는 키값은             
            if 'case_no' in key:
                case_no = value
            if 'service_name' in key:
                service_name = value
            if 'failure_yn' in key:
                failure_yn = value
            if 'description' in key:
                description = value
            if 'result' in key:
                result = value
            if 'platform' in key:
                platform = value
            if 'run_date' in key:
                current_time = value
요 조건으로 할당하니, 각 구간마다 키값에 저 텍스트를 넣어줘야해요
- 결과보고할때는 
TestResult().write_result(f"{case_no}_Result", f'*Fail*')
요런식으로 작성된 키값과 밸류를 보내야해요. 위의 케이스 예시는 common00033_Result : Fail 식으로 날라가는게 기대결과 임니다. 바이너리 키/밸류 파싱할때 로직은 없어도 될듯해요 데이터를 가공해서 바이너리에 넣을예정
'''


class ExceptionHandler:
    def timeout_handler(self,code_execution, locator):
        current_dir = os.getcwd()
        if "ios" in current_dir:
            platform = "ios"
        elif "android" in current_dir:
            platform = "android"
        else:
            platform = "web"

        def _handle_popups(platform):
            try:
                if platform == "android":
                    try:
                        time.sleep(1)
                        prod_locator = ProviderLocatorAndroid(self.driver)
                        prod_locator.click(ProviderLocatorAndroid.ad_close_btn)
                    except TimeoutException:
                        print("aos 광고 예외처리")
                elif platform == "ios":
                    try:
                        prod_locator = ProviderLocatorIos(self.driver)
                        prod_locator.click(ProviderLocatorIos.braze_ad_close_btn)
                    except TimeoutException:
                        print("ios 광고 예외처리2")
            except TimeoutException:
                print("팝업 종료 예외처리")

        try:
            return code_execution()
        except TimeoutException:
            try:
                _handle_popups(platform)
                return code_execution()
            except TimeoutException:
                raise TimeoutException(f"요소 확인 필요: {str(locator)}")
        except StaleElementReferenceException:
            time.sleep(1)
            try:
                return code_execution()
            except StaleElementReferenceException:
                raise TimeoutException(f"StaleElementReferenceException가 재발생함. 로직 체크필요")
            except TimeoutException:
                raise TimeoutException(f"요소 확인 필요: {str(locator)}")
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
            opt_result_exception2=None
    ):
        # value역할 (e.g. common001)
        case_no = current_function_name.split("prod_")[1].split("_ios")[0]
        # 서비스명 역할 (e.g. common)
        service_name = case_no[:-5]
        # case_no 저장 함수
        TestResult().write_result(f"{current_function_name}_case_no", case_no)
        # 서비스명 저장
        TestResult().write_result(f"{current_function_name}_service_name", service_name)
        # 플랫폼
        TestResult().write_result(f"{current_function_name}_test_os", "ios")
        # 재시작 함수
        app_restart = lambda: AppStart.ios_app_store_restart(self) if "precondition" in current_function_name else lambda: AppStart.ios_ohou_restart(self)
        try:
            retries = 0
            max_retries=2
            while retries < max_retries:
                ScreenRecoder.start_recording(self,current_function_name)
                if step is not None:
                    try:
                        step()
                        ScreenRecoder.stop_recording(self,current_function_name)
                        #ScreenRecoder.delete_recording(self, current_function_name)
                        break
                    except TimeoutException as e:
                        if "prod_commerce_platform00001_ios_step3" in current_function_name or "prod_commerce_platform00003_ios_step" in current_function_name or "prod_commerce_platform00005_ios_step3" in current_function_name:
                            if retries == 1:
                                ScreenRecoder.stop_recording(self,current_function_name)

                                # 실패 이미지 캡쳐
                                CaptureClass.capture_screenshot_put_name(self, current_function_name)
                                # 앱 재시작
                                if current_function_name not in "precondition":
                                    app_restart()()                    # 로깅
                                logger_ios.debug(f"{current_function_name}: {e}")
                                # 결과보고용(슬랙)에서 사용할 값
                                TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')
                                # result 컬럼에 들어갈 값
                                TestResult().write_result(f"{current_function_name}_result", "fail")
                                # desc 컬럼에 들어갈 값
                                TestResult().write_result(f"{current_function_name}_description", str(e))
                                # desc 컬럼에 들어갈 값
                                TestResult().write_result(f"{current_function_name}_failure_yn", 0)

                                # logger_ios.debug(
                                #     f"카운트 : {ProviderCommonMethod.count_xml_class(self, 'iOS'), ProviderCommonMethod.count_img_xml_class(self, 'iOS')}")
                                #
                                #
                                # class_count_1, class_count_2 = (5, 2) if current_function_name in "common" else (9, 8)
                                # if ProviderCommonMethod.count_xml_class(self, 'iOS') < class_count_1 and ProviderCommonMethod.count_img_xml_class(self, 'iOS') < class_count_2:
                                #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)

                                # if ProviderCommonMethod.get_xml_depth(self) < 160:
                                #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)
                                # 커스텀 결과 입력
                                if opt_title_exception2 is not None:
                                    TestResult().write_result(opt_title_exception2, f'{opt_result_exception2}')
                                # check 함수일대만 결과를 받기때문에 스텝 단계는 별도로 명시하고 스킵시켜야
                                if "step" in current_function_name:
                                    TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')
                                self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")
                                return
                            else:
                                retries += 1
                                time.sleep(2)
                                ScreenRecoder.stop_recording(self,current_function_name)
                                AppStart.ios_ohou_restart(self)
                                print(f"재시도 횟수 {retries}회")
                                continue
                        else:
                            ScreenRecoder.stop_recording(self, current_function_name)

                            # 실패 이미지 캡쳐
                            CaptureClass.capture_screenshot_put_name(self, current_function_name)
                            # 앱 재시작
                            if current_function_name not in "precondition":
                                app_restart()()  # 로깅
                            logger_ios.debug(f"{current_function_name}: {e}")
                            # 결과보고용(슬랙)에서 사용할 값
                            TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')
                            # result 컬럼에 들어갈 값
                            TestResult().write_result(f"{current_function_name}_result", "fail")
                            # desc 컬럼에 들어갈 값
                            TestResult().write_result(f"{current_function_name}_description", str(e))
                            # desc 컬럼에 들어갈 값
                            TestResult().write_result(f"{current_function_name}_failure_yn", 0)

                            # logger_ios.debug(
                            #     f"카운트 : {ProviderCommonMethod.count_xml_class(self, 'iOS'), ProviderCommonMethod.count_img_xml_class(self, 'iOS')}")

                            # class_count_1, class_count_2 = (5, 2) if current_function_name in "common" else (9, 8)
                            # if ProviderCommonMethod.count_xml_class(self,
                            #                                         'iOS') < class_count_1 and ProviderCommonMethod.count_img_xml_class(
                            #         self, 'iOS') < class_count_2:
                            #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)

                            # if ProviderCommonMethod.get_xml_depth(self) < 160:
                            #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)
                            # 커스텀 결과 입력
                            if opt_title_exception2 is not None:
                                TestResult().write_result(opt_title_exception2, f'{opt_result_exception2}')
                            # check 함수일대만 결과를 받기때문에 스텝 단계는 별도로 명시하고 스킵시켜야
                            if "step" in current_function_name:
                                TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')
                            self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")
                            return

            if back_flow is not None:
                try:
                    back_flow()
                    print("back flow 실행 완료")
                except TimeoutException as e:
                    ScreenRecoder.stop_recording(self,current_function_name)
                    CaptureClass.capture_screenshot_put_name(self, current_function_name)
                    if current_function_name not in "precondition":
                        app_restart()()
                    logger_ios.debug(f"{current_function_name}: {e}")
                    TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')

                    # logger_ios.debug(f"카운트 : {ProviderCommonMethod.count_xml_class(self, 'iOS'), ProviderCommonMethod.count_img_xml_class(self, 'iOS')}")


                    TestResult().write_result(f"{current_function_name}_result", "fail")
                    TestResult().write_result(f"{current_function_name}_description", str(e))
                    TestResult().write_result(f"{current_function_name}_failure_yn", 0)
                    # class_count_1, class_count_2 = (5, 2) if current_function_name in "common" else (9, 8)
                    # if ProviderCommonMethod.count_xml_class(self,
                    #                                         'iOS') < class_count_1 and ProviderCommonMethod.count_img_xml_class(
                    #     self, 'iOS') < class_count_2:
                    #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)

                    # if ProviderCommonMethod.get_xml_depth(self) < 160:
                    #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)
                    return

            if "check" in current_function_name:
                logger_ios.debug(f"{current_function_name}: pass")
                # logger_ios.debug(
                #     f"카운트 : {ProviderCommonMethod.count_xml_class(self, 'iOS'), ProviderCommonMethod.count_img_xml_class(self, 'iOS')}")                # 슬랙 결과보고용
                TestResult().write_result(f"{case_no}_Result", f'*Pass*')
                # 장애컬럼에 적재용
                TestResult().write_result(f"{current_function_name}_failure_yn", 0)
                # 결과 컬럼에 적재용도
                TestResult().write_result(f"{current_function_name}_result", "pass")

                ScreenRecoder.stop_recording(self, current_function_name)

                ScreenRecoder.delete_recording(self, current_function_name)
            if opt_title2 is not None:
                TestResult().write_result(opt_title2, f'{opt_result2}')

        except AssertionError as exception:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            if back_flow is not None:
                try:
                    back_flow()
                except TimeoutException as e:
                    ScreenRecoder.stop_recording(self, current_function_name)

                    CaptureClass.capture_screenshot_put_name(self, current_function_name)
                    if current_function_name not in "precondition":
                        app_restart()()
                    logger_ios.debug(f"{current_function_name}: {e}")
                    TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')
                    TestResult().write_result(f"{current_function_name}_result", "fail")
                    TestResult().write_result(f"{current_function_name}_description", str(exception))
                    TestResult().write_result(f"{current_function_name}_failure_yn", 0)

                    # logger_ios.debug(
                    #     f"카운트 : {ProviderCommonMethod.count_xml_class(self, 'iOS'), ProviderCommonMethod.count_img_xml_class(self, 'iOS')}")
                    # class_count_1, class_count_2 = (5, 2) if current_function_name in "common" else (9, 8)
                    # if ProviderCommonMethod.count_xml_class(self,
                    #                                         'iOS') < class_count_1 and ProviderCommonMethod.count_img_xml_class(self, 'iOS') < class_count_2:
                    #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)

                    # if ProviderCommonMethod.get_xml_depth(self) < 160:
                    #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)
                    return
            logger_ios.debug(f"{current_function_name}: {exception}")
            TestResult().write_result(f"{case_no}_Result", f'*Fail* ({exception})')

            # logger_ios.debug(
            #     f"카운트 : {ProviderCommonMethod.count_xml_class(self, 'iOS'), ProviderCommonMethod.count_img_xml_class(self, 'iOS')}")
            TestResult().write_result(f"{current_function_name}_result", "fail")
            TestResult().write_result(f"{current_function_name}_description", str(exception))
            TestResult().write_result(f"{current_function_name}_failure_yn", 0)

            ScreenRecoder.stop_recording(self, current_function_name)

            if opt_title_assert2 is not None:
                TestResult().write_result(opt_title_assert2, f'{opt_result_assert2}')

        except TimeoutException as e:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            ScreenRecoder.stop_recording(self, current_function_name)

            if current_function_name not in "precondition":
                app_restart()()
            logger_ios.debug(f"{current_function_name}: {e}")
            TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')

            # logger_ios.debug(
            #     f"카운트 : {ProviderCommonMethod.count_xml_class(self, 'iOS'), ProviderCommonMethod.count_img_xml_class(self, 'iOS')}")
            TestResult().write_result(f"{current_function_name}_result", "fail")
            TestResult().write_result(f"{current_function_name}_description", str(e))
            TestResult().write_result(f"{current_function_name}_failure_yn", 0)

            # class_count = 5 if current_function_name in "common" else 9
            # class_count_1, class_count_2 = (5, 2) if current_function_name in "common" else (9, 8)
            # if ProviderCommonMethod.count_xml_class(self,
            #                                         'iOS') < class_count_1 and ProviderCommonMethod.count_img_xml_class(
            #     self, 'iOS') < class_count_2:
            #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)

            # if ProviderCommonMethod.get_xml_depth(self) < 160:
            #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)
            if opt_title_exception2 is not None:
                TestResult().write_result(opt_title_exception2, f'{opt_result_exception2}')
            self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")
            return


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
            opt_result_exception2=None
    ):
        # value역할 (e.g. common001)
        case_no = current_function_name.split("prod_")[1].split("_aos")[0]
        # 서비스명 역할 (e.g. common)
        service_name = case_no[:-5]
        # case_no 저장 함수
        TestResult().write_result(f"{current_function_name}_case_no", case_no)
        # 서비스명 저장
        TestResult().write_result(f"{current_function_name}_service_name", service_name)
        # 플랫폼
        TestResult().write_result(f"{current_function_name}_test_os", "android")
        # 재시작 함수
        app_restart = lambda: AppStart.google_store_restart(self) if "precondition" in current_function_name else lambda: AppStart.android_ohou_restart(self, current_function_name)

        try:
            ScreenRecoder.start_recording(self, current_function_name)
            if step is not None:
                try:
                    step()
                    ScreenRecoder.stop_recording(self, current_function_name)
                    # ScreenRecoder.delete_recording(self, current_function_name)

                except TimeoutException as e:
                    ScreenRecoder.stop_recording(self, current_function_name)
                    # 실패 이미지 캡쳐
                    CaptureClass.capture_screenshot_put_name(self, current_function_name)
                    # 앱 재시작
                    if current_function_name not in "precondition":
                        app_restart()()
                        # 로깅
                    logger_aos.debug(f"{current_function_name}: {e}")
                    # 결과보고용(슬랙)에서 사용할 값
                    TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')
                    # result 컬럼에 들어갈 값
                    TestResult().write_result(f"{current_function_name}_result", "fail")
                    # desc 컬럼에 들어갈 값
                    TestResult().write_result(f"{current_function_name}_description", str(e))
                    # desc 컬럼에 들어갈 값
                    TestResult().write_result(f"{current_function_name}_failure_yn", 0)

                    logger_aos.debug(
                        f"카운트 : {ProviderCommonMethod.count_xml_class(self, 'android'), ProviderCommonMethod.count_img_xml_class(self, 'android')}")

                    class_count = 5 if current_function_name in "common" else 17
                    if ProviderCommonMethod.count_xml_class(self, 'android') < class_count and ProviderCommonMethod.count_img_xml_class(self, 'android') < 11:
                        TestResult().write_result(f"{current_function_name}_failure_yn", 1)


                    # if ProviderCommonMethod.get_xml_depth(self) < 160:
                    #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)
                    # 커스텀 결과 입력
                    if opt_title_exception2 is not None:
                        TestResult().write_result(opt_title_exception2, f'{opt_result_exception2}')
                    # check 함수일대만 결과를 받기때문에 스텝 단계는 별도로 명시하고 스킵시켜야
                    if "step" in current_function_name:
                        TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')
                    self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")
                    return

            if back_flow is not None:
                try:
                    back_flow()
                    print("back flow 실행 완료")
                except TimeoutException as e:
                    ScreenRecoder.stop_recording(self,current_function_name)

                    CaptureClass.capture_screenshot_put_name(self, current_function_name)
                    if current_function_name not in "precondition":
                        app_restart()()
                    logger_aos.debug(f"{current_function_name}: {e}")
                    TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')
                    TestResult().write_result(f"{current_function_name}_result", "fail")
                    TestResult().write_result(f"{current_function_name}_description", str(e))
                    TestResult().write_result(f"{current_function_name}_failure_yn", 0)
                    logger_aos.debug(
                        f"카운트 : {ProviderCommonMethod.count_xml_class(self, 'android'), ProviderCommonMethod.count_img_xml_class(self, 'android')}")

                    class_count = 5 if current_function_name in "common" else 17
                    if ProviderCommonMethod.count_xml_class(self,
                                                            'android') < class_count and ProviderCommonMethod.count_img_xml_class(
                            self, 'android') < 11:
                        TestResult().write_result(f"{current_function_name}_failure_yn", 1)
                    # if ProviderCommonMethod.get_xml_depth(self) < 160:
                    #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)
                    return

            if "check" in current_function_name:
                logger_aos.debug(f"{current_function_name}: pass")
                logger_aos.debug(
                    f"카운트 : {ProviderCommonMethod.count_xml_class(self, 'android'), ProviderCommonMethod.count_img_xml_class(self, 'android')}")

                # 슬랙 결과보고용
                TestResult().write_result(f"{case_no}_Result", f'*Pass*')
                # 장애컬럼에 적재용
                TestResult().write_result(f"{current_function_name}_failure_yn", 0)
                # 결과 컬럼에 적재용도
                TestResult().write_result(f"{current_function_name}_result", "pass")

                ScreenRecoder.stop_recording(self, current_function_name)
                ScreenRecoder.delete_recording(self, current_function_name)

            if opt_title2 is not None:
                TestResult().write_result(opt_title2, f'{opt_result2}')

        except AssertionError as exception:
            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            if back_flow is not None:
                try:
                    back_flow()
                except TimeoutException as e:
                    ScreenRecoder.stop_recording(self,current_function_name)

                    CaptureClass.capture_screenshot_put_name(self, current_function_name)
                    if current_function_name not in "precondition":
                        app_restart()()
                    logger_aos.debug(f"{current_function_name}: {e}")
                    TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')
                    TestResult().write_result(f"{current_function_name}_result", "fail")
                    TestResult().write_result(f"{current_function_name}_description", str(exception))
                    TestResult().write_result(f"{current_function_name}_failure_yn", 0)

                    logger_aos.debug(
                        f"카운트 : {ProviderCommonMethod.count_xml_class(self, 'android'), ProviderCommonMethod.count_img_xml_class(self, 'android')}")

                    class_count = 5 if current_function_name in "common" else 17
                    if ProviderCommonMethod.count_xml_class(self,
                                                            'android') < class_count and ProviderCommonMethod.count_img_xml_class(
                        self, 'android') < 11:
                        TestResult().write_result(f"{current_function_name}_failure_yn", 1)


                    # if ProviderCommonMethod.get_xml_depth(self) < 160:
                    #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)
                    return
            logger_aos.debug(f"{current_function_name}: {exception}")
            TestResult().write_result(f"{case_no}_Result", f'*Fail* ({exception})')
            TestResult().write_result(f"{current_function_name}_result", "fail")
            TestResult().write_result(f"{current_function_name}_description", str(exception))
            TestResult().write_result(f"{current_function_name}_failure_yn", 0)

            if opt_title_assert2 is not None:
                TestResult().write_result(opt_title_assert2, f'{opt_result_assert2}')

            ScreenRecoder.stop_recording(self, current_function_name)

        except TimeoutException as e:
            ScreenRecoder.stop_recording(self, current_function_name)

            CaptureClass.capture_screenshot_put_name(self, current_function_name)
            if current_function_name not in "precondition":
                app_restart()()
            logger_aos.debug(f"{current_function_name}: {e}")
            TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')
            TestResult().write_result(f"{current_function_name}_result", "fail")
            TestResult().write_result(f"{current_function_name}_description", str(e))
            TestResult().write_result(f"{current_function_name}_failure_yn", 0)

            logger_aos.debug(f"카운트 : {ProviderCommonMethod.count_xml_class(self, 'android'), ProviderCommonMethod.count_img_xml_class(self, 'android')}")

            class_count = 5 if current_function_name in "common" else 17
            if ProviderCommonMethod.count_xml_class(self, 'android') < class_count and ProviderCommonMethod.count_img_xml_class(self, 'android') < 11:
                TestResult().write_result(f"{current_function_name}_failure_yn", 1)
            # if ProviderCommonMethod.get_xml_depth(self) < 160:
            #     TestResult().write_result(f"{current_function_name}_failure_yn", 1)
            if opt_title_exception2 is not None:
                TestResult().write_result(opt_title_exception2, f'{opt_result_exception2}')
            self.scenario.skip(reason=f"{e}에러로 시나리오 스킵")
            return
        
    def web_exceptions_handler(
            self,
            page, 
            current_function_name, 
            step, 
            check=False,
            opt_check=None,
            prev_page=None,
            max_retries=3
            ):
        
        # value역할 (e.g. common001)
        case_no = current_function_name.split("prod_")[1].split("_web")[0]
        # 서비스명 역할 (e.g. common)
        service_name = case_no[:-5]
        if service_name == 'oo':
            service_name = 'o2o'
        # case_no 저장 함수
        TestResult().write_result(f"{current_function_name}_case_no", case_no)
        # 서비스명 저장
        TestResult().write_result(f"{current_function_name}_service_name", service_name)
        # 플랫폼
        TestResult().write_result(f"{current_function_name}_test_os", "web")

        try:
            step()
        except Exception as e:
            # 실패 이미지 캡쳐
            try:
                capture_screenshot(page, current_function_name + f"_fail")

                logger_web.debug(f"{current_function_name}: Caught an Error! {e}")

            except Exception as e:
                print(f"웹 핸들러 임시 예외처리 {e}")
            # 로깅
            # 결과보고용(슬랙)에서 사용할 값
            TestResult().write_result(f"{case_no}_Result", f'*Fail* ({e})')
            # result 컬럼에 들어갈 값
            TestResult().write_result(f"{current_function_name}_result", "fail")
            # desc 컬럼에 들어갈 값 (200자 제한)
            if len(str(e)) > 200:
                e = str(e)[:200]
            TestResult().write_result(f"{current_function_name}_description", str(e))
            # desc 컬럼에 들어갈 값
            TestResult().write_result(f"{current_function_name}_failure_yn", 0)
            pytest.skip(f'{e}')
        
        if "check" in current_function_name or check :
            logger_web.debug(f"{current_function_name}: pass")
            # 슬랙 결과보고용
            TestResult().write_result(f"{case_no}_Result", f'*Pass*')
            # 장애컬럼에 적재용
            TestResult().write_result(f"{current_function_name}_failure_yn", 0)
            # 결과 컬럼에 적재용도
            TestResult().write_result(f"{current_function_name}_result", "pass")
        
        return page.url