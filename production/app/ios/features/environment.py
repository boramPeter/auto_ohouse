import time
from appium import webdriver
from production.common.method.result_binary import TestResult
from app.common.app_config.data import UDID
from app.common.app_config.data import XcodeOrgId
from app.common.app_config.data import PackageName
import warnings
from selenium.common.exceptions import WebDriverException
from app.common.base_method.ios_remote_control_func import request_wda_del, request_app_restart



def before_all(context):
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    context.driver = None
    print(f"before_all 완료(아이폰 prod")


    print(f"before_all 완료, {context.driver}")
def after_all(context):
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    context.driver = None
    print("아이폰 prod after_all 완료")


def after_feature(context, feature):
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    context.driver = None
    print("prod after_feature 완료")

def before_feature(context, feature):
    feature_name = feature.name

    if feature_name == "자동화 실행 전 사전조건":
        print("앱스토어 실행")
        bundle_id = PackageName.ios_testflight
    else:
        print("오집 실행")
        bundle_id = PackageName.ios_bundle_id

    desired_caps = {
        'platformName': 'iOS',
        # 'platformVersion': '16.4.1',
        'automationName': 'XCUITest',
        'deviceName': '[auto] ios-60',
        'udid': UDID.iphone_13_mini_udid,
        'xcodeOrgId': XcodeOrgId.team_orgid,
        'bundleId': bundle_id,
        'noReset': True,
        # "wdaLocalPort": 8102,
        "disableIosAnimation": True,
        "newCommandTimeout": 600,
        "enableMultiWindows": True,
        "ffmpegPath": "/usr/local/bin/ffmpeg",
        "appium:wdaStartupRetries": 10,
        "appium:wdaStartupRetryInterval": 20000,
        "appium:wdaLaunchTimeout": 100000
    }
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    # context.driver = None
    #
    retry_count = 2  # 최대 2번까지 재시도 가능
    if context.driver is None:
        for attempt in range(retry_count):
            try:
                try:
                    if context.driver:
                        context.driver.quit()
                except Exception:
                    pass
                context.driver = None
                print(f"드라이버 실행 시도 {attempt + 1}/{retry_count}")
                context.driver = webdriver.Remote('', desired_caps)
                print("prod 드라이버 실행 성공")
                break  # 성공하면 루프 종료
            except WebDriverException as e:
                print(f"WebDriverException 발생 (시도 {attempt + 1}): {e}")
                if attempt < retry_count - 1:
                    for stop_count in range(1, 4):
                        if request_wda_del(test_env="prod"):
                            print(f"del complete")
                            break
                        else:
                            print(f"del_count {stop_count} failed.")
                    else:
                        pass
                else:
                    print("최대 재시도 횟수 초과. 테스트 종료")
                    context.driver = None

    if context.driver is None:
        # context.driver = webdriver.Remote('', desired_caps)
        print("1번 디바이스 드라이버 실행 실패했으므로 앱 재시작 후 재연결 시도")
        if request_app_restart(UDID.iphone_13_mini_udid,):
            time.sleep(10)
            print(f"1번 디바이스 재시작 완료")
        else:
            print(f"1번 디바이스 재시작 실패")
        context.driver = webdriver.Remote('', desired_caps)
        print("1번 디바이스 드라이버 실행 성공")


    if feature_name != "자동화 실행 전 사전조건":
        print("프리컨디션 수행이 아니므로 조건 확인")
        if TestResult().read_result_slack("pre-condition") != "pass":
            print(f"Pre-condition이 pass되지 않아 '{feature_name}' 피처 전체를 스킵합니다.")
            feature.skip("Pre-condition이 pass되지 않아 피처 전체 스킵")
        else:
            print(f"{feature_name} 수행시작")


def before_step(context, step):
    try:
        if TestResult().read_result_slack("pre-condition") == "fail":
            context.step.skip(reason="설치 실패로 스킵")
    except FileNotFoundError:
        print("예외처리용")
    except KeyError:
        TestResult().write_result("pre-condition", "pass")
    print("before_step 완료")


def after_step(context, step):
    print("after_step 완료")
