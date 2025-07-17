import pytest,os
import shutil
from playwright.sync_api import sync_playwright
from app.common.app_config.data import VideoPath

from web.BasicSetting.logger_func import make_logger_web
# logger_web = make_logger_web("jenkins_prod_web_log.py")

from app.common.app_config.data import ScreenshotPath

# FFmpeg 경로를 환경 변수에 추가
ffmpeg_path = VideoPath.jenkins_ffmpeg_path
if ffmpeg_path not in os.environ['PATH']:
    os.environ['PATH'] = ffmpeg_path + os.pathsep + os.environ['PATH']

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            executable_path='/usr/bin/google-chrome',
            headless=True
        )
        yield browser
        browser.close()

@pytest.fixture(scope='session')
def context(browser, request):
    dir = ScreenshotPath.screenshot_jenkins_path
    context = browser.new_context(record_video_dir=dir)

    yield context

    context.close()
    video_files = [f for f in os.listdir(dir) if f.endswith(".webm")]

    if video_files:
        video_file = video_files[0]
        old_path = os.path.join(dir, video_file)
        new_name = "web_prod_recording.webm"
        new_path = os.path.join(dir, new_name)
        shutil.move(old_path, new_path)


@pytest.fixture(scope='session')
def page(context, request):
    page = context.new_page()
    page.on('response', on_response)

    yield page
    page.close()


@pytest.fixture(scope="session", autouse=True)
def adjust_browser_resolution(page):
    # 원하는 해상도로 변경 (예: 1280x800)
    page.set_viewport_size({"width": 1920, "height": 1200})

# 전역 변수로 시나리오 이름을 저장할 변수
current_scenario_name = None

def pytest_bdd_before_scenario(request, feature, scenario):
    global current_scenario_name
    current_scenario_name = scenario.name

@pytest.fixture
def get_scenario_name():
    global current_scenario_name
    return current_scenario_name

# 네트워크 응답을 모니터링하는 콜백 함수
def on_response(response):
    if response.status >= 400:
        # logger_web.debug(f"Response error(4xx): {response.url} - {response.status} {response.status_text}")
        print(f"Response error(4xx): {response.url} - {response.status} {response.status_text}")
    if response.status >= 500:
        # logger_web.debug(f"Response error(5xx): {response.url} - {response.status} {response.status_text}")
        print(f"Response error(5xx): {response.url} - {response.status} {response.status_text}")