from appium.webdriver.common.appiumby import AppiumBy
from app.common.base_method.appium_method import ProviderCommonMethod


class ProviderLocatorIos(ProviderCommonMethod):

    ##### safari ######
    url = (AppiumBy.ACCESSIBILITY_ID, 'TabBarItemTitle')

    url_text_box = (AppiumBy.ACCESSIBILITY_ID, 'URL')

    vk_enter_key = (AppiumBy.ACCESSIBILITY_ID, 'Go')

    url_clear_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="ClearTextButton"]')

    url_paste_btn = (AppiumBy.XPATH, '//XCUIElementTypeMenuItem[@name="붙여넣기"]')

    app_open_btn = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="열기"]')

    go_to_app_at_browser = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="오늘의집 앱으로 보기"]')
    ############ 팝업 닫기 모음 ############
    alarm_confirm_btn = (AppiumBy.ACCESSIBILITY_ID, '허용')





