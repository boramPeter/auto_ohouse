import time
from selenium.common.exceptions import TimeoutException
from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler
from production.braze.aos.locator.braze_00059_00063 import ProviderBrazeLocator
from app.common.base_method.app_start_func import AppStart
from app.common.app_config.data import PackageName

class MKTBrazeOnSet:
    def go_noti_set(self):
        AppStart.android_ohou_restart(self,"mkt_00059_aos_step")
        try:
            later_review_btn = ProviderBrazeLocator(self.driver)
            later_review_btn.click_quick(ProviderBrazeLocator.later_review_btn)

        except TimeoutException:
            print("리뷰쓰기 예외처리")
        time.sleep(2)
        my_btn = ProviderBrazeLocator(self.driver)
        set_btn = ProviderBrazeLocator(self.driver)
        noti_btn = ProviderBrazeLocator(self.driver)
        time.sleep(2)
        JenkinsExceptionHandler.timeout_handler(self,
            lambda: my_btn.click(ProviderBrazeLocator.my_btn), "my_btn")
        time.sleep(1)
        JenkinsExceptionHandler.timeout_handler(self,
            lambda: set_btn.click(ProviderBrazeLocator.set_btn), "set_btn")
        time.sleep(1)
        JenkinsExceptionHandler.timeout_handler(self,
            lambda: noti_btn.click(ProviderBrazeLocator.noti_btn), "noti_btn")

        noti_on_check_btn = ProviderBrazeLocator(self.driver)
        checked = JenkinsExceptionHandler.timeout_handler(self,lambda: noti_on_check_btn.is_checked(ProviderBrazeLocator.noti_on_check_btn),"noti_on_check_btn")
        if checked == "False":
            noti_on_check_btn = ProviderBrazeLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: noti_on_check_btn.click(ProviderBrazeLocator.noti_on_check_btn),"noti_on_check_btn")

        agree_btn = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: agree_btn.click(ProviderBrazeLocator.agree_btn),
            "agree_btn")
        time.sleep(2)
        AppStart.force_app_restart(self, PackageName.aos_package_name)
        '''
        보안을 위해 제거
        '''