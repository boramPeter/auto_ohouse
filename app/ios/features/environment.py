import time
from report.create_report import AppCreateSlackReport
from appium import webdriver
from app.common.base_method.ios_result_binary import Result
from app.common.app_config.data import UDID
from app.common.app_config.data import XcodeOrgId
from app.common.app_config.data import PackageName
import warnings
from selenium.common.exceptions import NoSuchDriverException
from report.goole_spread_sheet_func.make_spread_sheet_func import delete_sheet
from selenium.common.exceptions import WebDriverException
from app.common.base_method.ios_remote_control_func import request_wda_del_opt, request_app_restart
from flask_active.test_running_check.running_value_provider import get_terminate_value
# from report.testrail_func.festrail_api import delete_test_run

def before_all(context):

    tags = str(context.config.tags)
    context.debug = True if 'True' in tags else False

    context.test_execution = "RT" if 'RT' in tags else "ST"


    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    context.driver = None
    print(f"before_all 완료(아이폰 피쳐1")

# 조건들 피쳐파일명으로 걸어둬야
def after_all(context):
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    context.driver = None
    print("아이폰 피쳐1 after_all 완료")


def after_feature(context, feature):
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    context.driver = None
    print("1번단말 after_feature 완료")

def before_feature(context, feature):
    feature_name = feature.name
    print(f'feature_name:{feature_name} 아이폰1')
    try:
        if Result().read_result_slack("is_ios_running") == "false" or get_terminate_value("ios") == True:
            print(f'테스트 스킵.:{feature_name} 아이폰1')
            feature.skip("테스트 강제 skip")
            return
    except (FileNotFoundError, EOFError):
        print("예외처리용")
    except KeyError:
        pass

    if feature_name == "자동화 실행 전 사전조건":
        print("테플로 실행")
        bundle_id = PackageName.ios_testflight

    elif feature_name == "mkt ST,RT":
        print("사파리로 실행")
        bundle_id = PackageName.ios_safari

    else:
        print("오집 실행")
        bundle_id = PackageName.ios_bundle_id

    autoAcceptAlerts_bool = True if feature_name == ("자동화 실행 전 사전조건" or "mkt ST,RT") else False

    desired_caps = {
        'platformName': 'iOS',
        'automationName': 'XCUITest',
        'deviceName': '[auto] ios-59',
        'appium:udid': UDID.iphone12mini_udid,
        'xcodeOrgId': XcodeOrgId.team_orgid,
        'bundleId': bundle_id,
        'noReset': True,
        "disableIosAnimation": True,
        "newCommandTimeout": 600,
        "enableMultiWindows": True,
        "appium:wdaStartupRetries":10,
        "appium:wdaStartupRetryInterval":20000,
        "appium:autoAcceptAlerts":autoAcceptAlerts_bool,
        "appium:wdaLaunchTimeout": 100000
    }

    retry_count = 2  # 최대 2번까지 재시도 가능
    # context.driver = None
    if context.driver is None:
        for attempt in range(retry_count):
            try:
                try:
                    if context.driver:
                        context.driver.quit()
                except Exception:
                    pass
                print(f"1번 디바이스 드라이버 실행 시도 {attempt + 1}/{retry_count}")
                context.driver = webdriver.Remote('', desired_caps)
                print("1번 디바이스 드라이버 실행 성공")
                break  # 성공하면 루프 종료
            except WebDriverException as e:
                print(f"1번 디바이스 WebDriverException 발생 (시도 {attempt + 1}): {e}")
                if attempt < retry_count - 1:
                    for stop_count in range(1, 4):
                        if request_wda_del_opt(UDID.iphone12mini_udid):
                            print(f"1번 디바이스 del complete")
                            break
                        else:
                            print(f"1번 디바이스 del_count {stop_count} failed.")
                    else:
                        pass
                else:
                    print("최대 재시도 횟수 초과. 테스트 종료")
                    context.driver = None

    if context.driver is None:
        print("1번 디바이스 드라이버 실행 실패했으므로 앱 재시작 후 재연결 시도")
        if request_app_restart(UDID.iphone12mini_udid):
            time.sleep(10)
            print(f"1번 디바이스 재시작 완료")
        else:
            print(f"1번 디바이스 재시작 실패")
        context.driver = webdriver.Remote('', desired_caps)
        print("1번 디바이스 드라이버 실행 성공")


    try:
        if feature_name not in ["자동화 실행 전 사전조건","common ST,RT"]:
            print("프리컨디션 수행이 아니므로 조건 확인")
            if Result().read_result_slack("pre-condition") == "fail" or Result().read_result_slack("pre-condition2") == "fail" or Result().read_result_slack("pre-condition3") == "fail":
                print(f"Pre-condition이 pass되지 않아 '{feature_name}' 피처 전체를 스킵합니다.{Result().read_result_slack('pre-condition')}, {Result().read_result_slack('pre-condition2')}")
                Result().write_result("pre-condition", "fail")
                feature.skip("Pre-condition이 pass되지 않아 피처 전체 스킵")
                delete_sheet(Result().read_result_slack("iOS_spreadsheet"))

                # 빠른 중단을위한 false처리
                Result().write_result("is_ios_running", "false")
                return
            else:
                print(f"{feature_name} 수행시작(아이폰1)")
    except KeyError:
        pass

    if feature_name in ["comm_service ST,RT","home ST,RT","ads ST,RT","search ST,RT"]:
        print("count_run_case 실행")
        count_run_case(context.test_execution, debug=context.debug)

    print(f"아이폰1 Before feature hook 시작{feature_name}")

def before_step(context, step):
    try:
        if Result().read_result_slack("pre-condition") == "fail" or Result().read_result_slack("pre-condition2") == "fail" or Result().read_result_slack("pre-condition3") == "fail":
            Result().write_result("pre-condition", "fail")

    except (FileNotFoundError, EOFError):
        print("예외처리용")
    except KeyError:
        pass

def before_scenario(context, feature):
    try:
        if Result().read_result_slack("pre-condition") == "fail" or Result().read_result_slack("pre-condition2") == "fail" or Result().read_result_slack("pre-condition3") == "fail":
            Result().write_result("pre-condition", "fail")
            context.scenario.skip(reason="설치 실패로 스킵")
            delete_sheet(Result().read_result_slack("iOS_spreadsheet"))

            print(
                f'Pre-condition pass되지 않아 1번 시나리오 전체를 스킵합니다. {Result().read_result_slack("pre-condition"), Result().read_result_slack("pre-condition2"), Result().read_result_slack("pre-condition3")}')
    except FileNotFoundError:
        print("예외처리용")


    try:
        if Result().read_result_slack("is_ios_running") == "false" or get_terminate_value("ios") == True:
            context.scenario.skip(reason="테스트 강제 스킵")
    except (FileNotFoundError, EOFError):
        print("예외처리용")
    except KeyError:
        pass


def after_step(context, step):
    print("after_step 완료")

def count_run_case(test_execution,debug=None):
    return AppCreateSlackReport().is_run_rate("iOS", test_execution, debug=debug, idx=None)