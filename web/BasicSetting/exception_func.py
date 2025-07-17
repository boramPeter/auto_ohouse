from web.BasicSetting.web_result_binary import ResultWeb
from app.common.app_config.data import ScreenshotPath
from selenium.common.exceptions import TimeoutException
import os
import pytest
from web.BasicSetting.logger_func import make_logger_web

import report.goole_spread_sheet_func.update_spread_sheet_func as update_sheet
# from report.testrail_func.festrail_api import add_result_for_case

logger_web = make_logger_web("jenkins_web_log.py")
sheet_id = ResultWeb().read_result_slack('web_spreadsheet')

def web_exceptions_handler(
        page, 
        current_function_name, 
        step, 
        check=False,
        opt_check=None,
        prev_page=None,
        max_retries=3
    ):
    # try:
    #     ResultWeb().read_result_slack('web_testrail')
    # except (FileNotFoundError, KeyError):
    #     ResultWeb().write_result('web_testrail', "None")

    sheet_info = extract_sheet_name(current_function_name)
    
    try:
        retries = 0
        while retries < max_retries:
            try:
                step()
                break
            except Exception as e:
                retries += 1
                capture_screenshot(page, current_function_name + f"_retry{retries}")
                
                if retries == 3:
                    logger_web.debug(f"{current_function_name} {e}: 재시도 {retries}번 실행 완료")
                    print(f"재시도 {retries}번 실행 완료")
                    ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
                    # if ResultWeb().read_result_slack("web_testrail") == "pass":
                    #     add_result_for_case("web", current_function_name, "fail")
                    update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Fail')
                    pytest.skip(f'{e}')

                try:
                    if prev_page is not None:
                        page.goto(prev_page, timeout= 0)
                        logger_web.debug(f"{current_function_name} {e}: retry_{retries}번째, goto prev page 실행")
                        print(f"goto prev page {retries}번 실행")
                        continue
                    else:
                        if page.get_by_role("button", name="다시 시도하기").is_visible():
                            page.get_by_role("button", name="다시 시도하기").click()
                            page.wait_for_timeout(1000) # '다시 시도하기' 버튼 클릭 후 대기 필요
                            logger_web.debug(f"{current_function_name} {e}: retry_{retries}번째, 다시 시도하기 btn 실행")
                            print(f"다시 시도하기 btn {retries}번 실행")
                        else:
                            page.reload()
                            logger_web.debug(f"{current_function_name} {e}: retry_{retries}번째, reload 실행")
                            print(f"reload {retries}번 실행")
                        continue
                except Exception as e1:
                    logger_web.debug(f"{current_function_name}: 재시도 실패 - test fail ({e1})")
                    print(f"재시도 실패 - test fail")
                    capture_screenshot(page, current_function_name)
                    ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
                    # if ResultWeb().read_result_slack("web_testrail") == "pass":
                    #     add_result_for_case("web", current_function_name, "fail")
                    update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Fail')
                    pytest.skip(f'{e1}')
        
        if check:
            if opt_check is not None:
                opt_check()
            ResultWeb().write_result(current_function_name, f'*Pass*')
            # if ResultWeb().read_result_slack("web_testrail") == "pass":
            #     add_result_for_case("web", current_function_name, "pass")
            update_sheet.write_to_sheet(sheet_id, sheet_info[0], sheet_info[1], 'Pass')
        return page.url

    except Exception as e:
        logger_web.debug(f"{current_function_name}: Caught an Error! {e}")
        print(f"\nCaught an Error! {e}")
        capture_screenshot(page, current_function_name)
        ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
        # if ResultWeb().read_result_slack("web_testrail") == "pass":
        #     add_result_for_case("web", current_function_name, "fail")
        pytest.skip(f'{e}')

def capture_screenshot(page, current_func_name):
    # 파일 경로 및 이름 지정
    file_path = ScreenshotPath.screenshot_path
    file_name = current_func_name + '_web.png'
    file_full_path = os.path.join(file_path, file_name)
    try:
        # 스크린샷 촬영
        page.screenshot(path=file_full_path)
    except Exception as e:
        logger_web.debug(f"{current_func_name} Fail 스크린샷 저장 실패: {e}")

    return file_full_path

def jenkins_capture_screenshot(page, current_func_name):
    # 파일 경로 및 이름 지정
    file_path = ScreenshotPath.screenshot_jenkins_path
    file_name = current_func_name + '_web.png'
    file_full_path = os.path.join(file_path, file_name)
    try:
        # 스크린샷 촬영
        page.screenshot(path=file_full_path)
    except Exception as e:
        # logger_web.debug(f"{current_func_name} Fail 스크린샷 저장 실패: {e}")
        # 젠킨스 환경이라 로그파일 일단 주석처리
        print(f"{current_func_name} Fail 스크린샷 저장 실패: {e}")
    return file_full_path

def extract_sheet_name(func_name):
    service_name = ''
    case_id = ''
    func_parts = func_name.split('_')
    if len(func_parts) == 3:
        service_name = func_parts[1].capitalize() if func_parts[1] != 'o2o' else 'O2O'
        case_id = func_parts[2]
    elif len(func_parts) == 4:
        service_name = func_parts[1].capitalize() + '_' + func_parts[2].capitalize()
        case_id = func_parts[3]
    return [service_name, case_id]