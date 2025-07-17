from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler
from production.braze.ios.locator.braze_00059_00063 import ProviderBrazeLocator
from production.braze.api.braze_push import TriggerPush
from selenium.common.exceptions import TimeoutException

class BrazePushAppTerminate:
    def push_app(self):
        TriggerPush().send_push("9bd4fcab-eafa-6f06-c59f-1f69f4370db6", "24653062")
        push_receive = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: push_receive.click(ProviderBrazeLocator.push_receive),"push_receive")
    def actual_result(self):
        try:
            banner_close_btn = ProviderBrazeLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: banner_close_btn.click(
                ProviderBrazeLocator.banner_close_btn), "banner_close_btn")

        except TimeoutException:
            print("팝업 미노출되어 스킵")

        push_result1 = ProviderBrazeLocator(self.driver)
        actual_result = JenkinsExceptionHandler.timeout_handler(self,lambda: push_result1.is_enabled(ProviderBrazeLocator.push_result1),"push_result1")

        return actual_result