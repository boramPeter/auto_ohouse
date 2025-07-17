import time,requests

from appium import webdriver
from production.common.method.result_binary import TestResultBraze
from app.common.app_config.data import PackageName
from app.common.app_config.data import ChromeDriverPath
from behave import fixture, use_fixture
import warnings
from app.common.app_config.data import UDID

def wait_for_appium_server(port, timeout):
    def appium_server_is_running(port):
        try:
            response = requests.get(f'http://localhost:{port}/wd/hub/status')
            if response.status_code == 200:
                return True
        except requests.ConnectionError:
            return False
    start_time = time.time()
    while time.time() - start_time < timeout:
        if appium_server_is_running(port):
            print("앱피움서버 실행완료")
            time.sleep(5)
            return True
        time.sleep(1)

    print("앱피움 서버가 실행되지 않은 것으로 보임.")
    return False
def before_all(context):
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    context.driver = None

def after_all(context):
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    context.driver = None

def after_feature(context, feature):
    # 시나리오가 실행된 후에 WebDriver 종료
    try:
        if context.driver:
            context.driver.quit()
    except Exception:
        pass
    context.driver = None
    print("After all hook 종료")
def before_feature(context, feature):
    feature_name = feature.name

    if feature_name == "앱 설치 사전조건":
        print("디플 실행")
        app_package = PackageName.aos_deploy_gate_name
        app_activity = "com.deploygate.activity.MainActivity"
    else:
        print("오집 실행")
        app_package = PackageName.aos_package_name
        app_activity = "se.ohou.screen.splash.SplashActivity"

    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '13.0',
        'appPackage': app_package,
        'appActivity': app_activity,
        "automationName": "uiautomator2",
        'noReset': True,
        "enableMultiWindows": True,
        "chromedriverExecutable": ChromeDriverPath.chrome_driver_path,
        "udid": UDID.aos_prod_udid,
        "uiautomator2ServerInstallTimeout": 600000
    }

    # Appium 서버에 WebDriver 초기화 및 context에 추가
    context.driver = webdriver.Remote('http://localhost:4727/wd/hub', desired_caps)


def before_step(context, step):
    try:
        if TestResultBraze().read_result_slack("앱 설치 precondition","android") == "fail":
            context.step.skip(reason="설치 실패로 스킵")
    except (FileNotFoundError,KeyError):
        print("예외처리용")
    time.sleep(1)

def before_scenario(context, scenario):
    try:
        if TestResultBraze().read_result_slack("앱 설치 precondition","android") == "fail":
            context.scenario.skip(reason="설치 실패로 스킵")
    except (FileNotFoundError, KeyError):
        print("예외처리용")
    time.sleep(1)

def after_step(context, step):
    print("after_step 완료")
