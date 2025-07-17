# import pytest
from web.BasicSetting.import_list import *
# from app.common.app_config.data import Webhook
from flask_active.test_running_check.running_value_provider import get_terminate_value
from web.BasicSetting.logger_func import make_logger_web
# import web.BasicSetting.exception_func as ex
# import web.BasicSetting.logger_func as lf
logger_web = make_logger_web("jenkins_web_log.py")

# 드라이버 세팅
@pytest.fixture(scope='function')
def browser():
    working_directory = os.getcwd()
    parts = working_directory.split(os.sep)
    try:
        workspace_index = parts.index("workspace")
        os.sep.join(parts[:workspace_index + 2])
        path = "1"
    except Exception:
        index = working_directory.rfind("ohs-qa-automation")
        target_directory = working_directory[:index + len("ohs-qa-automation")]
        path = "2"

    browser_path = '/usr/bin/google-chrome' if path == "1" else '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(  # or "firefox" or "webkit".
            executable_path=browser_path,
            headless=True
        )
        yield browser
        browser.close()        

@pytest.fixture(scope='function')
def page(browser, request):
    page = browser.new_page()
    current_function_name = request.node.name
    logger_web.debug(f"{current_function_name} 시작")
    yield page
    page.close()

@pytest.fixture(scope="function", autouse=True)
def adjust_browser_resolution(page):
    if get_terminate_value("web") == True:
        pytest.skip("강제종료로 인한 테스트 스킵")
    # 원하는 해상도로 변경 (예: 1280x800)
    page.set_viewport_size({"width": 1920, "height": 1200})


# API Function
def send_api_post(api_url, data):
    response = requests.post(api_url, json=data, verify=False, timeout=10)
    return response

def send_api_get(api_url):
    response = requests.get(api_url, verify=False, timeout=10)
    return response

