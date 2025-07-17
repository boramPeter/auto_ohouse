from appium.webdriver.common.appiumby import AppiumBy
from app.common.base_method.appium_method import ProviderCommonMethod


class ProviderBrazeLocator(ProviderCommonMethod):

    testflight_title = (AppiumBy.ACCESSIBILITY_ID, '오늘의집 - 라이프스타일 슈퍼앱')

    version_group = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="버전 및 빌드 그룹"]')

    def version_name(version):
        version_name = (AppiumBy.ACCESSIBILITY_ID, f'{version}')
        return version_name
