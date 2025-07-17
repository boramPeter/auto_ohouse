from appium.webdriver.common.appiumby import AppiumBy
from app.common.base_method.appium_method import ProviderCommonMethod


class ProviderLocatorAndroid(ProviderCommonMethod):
    ############ 팝업 닫기 모음 ############

    review_later_btn = (AppiumBy.XPATH, '//*[contains(@text, "나중에 하기")]')

    info_alarm_later_btn = (AppiumBy.XPATH, '//*[contains(@text, "괜찮아요")]')

    ##################### 뒤로가기 모음
    '''
    보안을 위해 제거
    '''