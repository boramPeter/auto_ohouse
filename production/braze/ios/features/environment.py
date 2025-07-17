import time

from appium import webdriver
from production.common.method.result_binary import TestResultBraze
from app.common.app_config.data import UDID
from app.common.app_config.data import XcodeOrgId
from app.common.app_config.data import PackageName
from selenium.common.exceptions import WebDriverException
from app.common.base_method.ios_remote_control_func import request_wda_del_opt, request_app_restart


def before_all(context):
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    context.driver = None
    print(f"before_all 완료(아이폰 피쳐1), {context.driver}")


def after_feature(context, feature):
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    context.driver = None
    print("after_feature 완료")

def before_feature(context, feature):
    # desired_caps = {
    #     'platformName': 'iOS',
    #     # 'platformVersion': '16.4.1',
    #     'automationName': 'XCUITest',
    #     'deviceName': '[auto] ios-59',
    #     'appium:udid': UDID.iphone12mini_udid,
    #     'xcodeOrgId': XcodeOrgId.team_orgid,
    #     'bundleId': PackageName.ios_testflight,
    #     'noReset': True,
    #     # "wdaLocalPort": 8100,
    #     "disableIosAnimation": True,
    #     "newCommandTimeout": 600,
    #     "enableMultiWindows": True,
    #     "appium:wdaStartupRetries": 10,
    #     "appium:wdaStartupRetryInterval": 20000,
    #     "appium:wdaLaunchTimeout": 100000
    # }
    desired_caps = {
        'platformName': 'iOS',
        # 'platformVersion': '16.4.1',
        'automationName': 'XCUITest',
        'deviceName': '[auto] ios-60',
        'udid': UDID.iphone_13_mini_udid,
        'xcodeOrgId': XcodeOrgId.team_orgid,
        'bundleId': PackageName.ios_testflight,
        'noReset': True,
        # "wdaLocalPort": 8102,
        "disableIosAnimation": True,
        "newCommandTimeout": 600,
        "enableMultiWindows": True,
        "appium:wdaStartupRetries": 10,
        "appium:wdaStartupRetryInterval": 20000,
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
                # context.driver = None
                print(f"1번 디바이스 드라이버 실행 시도 {attempt + 1}/{retry_count}")
                context.driver = webdriver.Remote('', desired_caps)
                print("1번 디바이스 드라이버 실행 성공")
                break  # 성공하면 루프 종료
            except WebDriverException as e:
                print(f"1번 디바이스 WebDriverException 발생 (시도 {attempt + 1}): {e}")
                if attempt < retry_count - 1:
                    for stop_count in range(1, 4):
                        if request_wda_del_opt(UDID.iphone_13_mini_udid):
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
        if request_app_restart(UDID.iphone_13_mini_udid):
            time.sleep(10)
            print(f"1번 디바이스 재시작 완료")
        else:
            print(f"1번 디바이스 재시작 실패")
        context.driver = webdriver.Remote('', desired_caps)
        print("1번 디바이스 드라이버 실행 성공")

def after_all(context):
    # 시나리오가 실행된 후에 WebDriver 종료
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    context.driver = None
    print("After all hook 종료")



def before_step(context, step):
    try:
        if TestResultBraze().read_result_slack("앱 설치 precondition","ios") == "fail":
            context.step.skip(reason="설치 실패로 스킵")
    except FileNotFoundError:
        print("예외처리용")
    time.sleep(1)

def before_scenario(context, scenario):
    try:
        if TestResultBraze().read_result_slack("앱 설치 precondition","ios") == "fail":
            context.scenario.skip(reason="설치 실패로 스킵")
    except FileNotFoundError:
        print("예외처리용")
    time.sleep(1)

def after_step(context, step):
    print("after_step 완료")
