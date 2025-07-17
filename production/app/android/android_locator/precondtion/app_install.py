from appium.webdriver.common.appiumby import AppiumBy
from app.common.base_method.appium_method import ProviderCommonMethod
from app.common.app_config.data import AccountInfo

class ProviderInstallLocator(ProviderCommonMethod):
    search_tab = (AppiumBy.XPATH, '//android.widget.TextView[@text="검색"]')

    app_textbox = (AppiumBy.XPATH, '//android.widget.TextView[@text="앱 및 게임 검색"]')

    app_textbox_input = (AppiumBy.XPATH, '//android.widget.EditText')

    search_vk_btn = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="검색"]/android.widget.ImageView')

    ohou_title = (AppiumBy.ACCESSIBILITY_ID, '오늘의집 - 라이프스타일 슈퍼앱\nBUCKETPLACE\n')

    install_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="설치"]', "설치 라는 문자열이 포함된 속성")

    app_open_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="열기"]')

    app_install_check_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="제거"]',"제거 라는 문자열이 포함된 속성")

    search_btn_vk = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "검색") or contains(@content-desc, "완료") or contains(@content-desc, "다음") or contains(@content-desc, "엔터")]')
