import time

from app.android.locator.common.common_00035 import ProviderCommonLocator
from app.common.app_config.data import AccountInfo
from selenium.common.exceptions import TimeoutException
from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler
from app.common.base_method.appium_method import ProviderScrollMethod
from app.common.base_method.app_start_func import AppStart
from production.braze.aos.locator.braze_00059_00063 import ProviderBrazeLocator

class EmailLoginCheck:
    def is_login2(self):
        time.sleep(4)
        try:
            email_login_btn = ProviderCommonLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: email_login_btn.click(ProviderCommonLocator.email_login_btn), "email_login_btn")
        except TimeoutException:
            AppStart.android_ohou_restart(self,"common00005")
            time.sleep(1)
            email_login_btn = ProviderCommonLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: email_login_btn.click(ProviderCommonLocator.email_login_btn), "email_login_btn")

    '''
    보안을 위해 제거
    '''

