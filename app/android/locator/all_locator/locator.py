from appium.webdriver.common.appiumby import AppiumBy
from app.common.base_method.appium_method import ProviderCommonMethod


class ProviderLocatorAndroid(ProviderCommonMethod):
    #### 브라우저

    url = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.sec.android.app.sbrowser:id/location_bar_edit_text"]')

    url_clear_btn = (
    AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="지우기"]')

    url_text_box = (
        AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.sec.android.app.sbrowser:id/location_bar_edit_text"]')

    #pdp_q cam 링크 확인
    pdp_url_text_box = (
        AppiumBy.XPATH, '//android.widget.EditText[@text="https://qa-web.dailyhou.se/productions/624075/selling"]')

