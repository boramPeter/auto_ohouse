from appium.webdriver.common.appiumby import AppiumBy
from app.common.base_method.appium_method import ProviderCommonMethod
from app.common.app_config.data import AccountInfo

class ProviderInstallLocator(ProviderCommonMethod):
    app_store_search_btn = (AppiumBy.ACCESSIBILITY_ID, 'AppStore.tabBar.search')

    app_textbox = (AppiumBy.ACCESSIBILITY_ID, 'AppStore.searchField')

    search_vk_btn = (AppiumBy.ACCESSIBILITY_ID, 'Search')

    ohou_title = (AppiumBy.ACCESSIBILITY_ID, '오늘의집 - 라이프스타일 슈퍼앱, 라이프스타일 트렌드, 쇼핑, 이사, 시공')

    install_btn = (AppiumBy.ACCESSIBILITY_ID, 'AppStore.offerButton[state=redownload]')

    app_open_btn = (AppiumBy.ACCESSIBILITY_ID, 'AppStore.offerButton[state=open]')
