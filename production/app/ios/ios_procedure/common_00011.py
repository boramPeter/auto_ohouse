from app.common.base_method.appium_method import ProviderScrollMethod
from app.ios.locator.common.common_00035 import ProviderCommonLocator
from app.common.app_config.data import AccountInfo
from selenium.common.exceptions import TimeoutException
from app.common.base_method.app_start_func import AppStart
from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler


class ProdEmailLoginCheck:
    def is_login(self):
        try:
            email_login_btn = ProviderCommonLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: email_login_btn.click(ProviderCommonLocator.email_login_btn), "email_login_btn")
        except TimeoutException:

            try:
                ProdEmailLoginCheck.is_logout_prod(self)
            except TimeoutException:
                print("로그인 실패 예외처리")
                pass

            AppStart.ios_ohou_restart(self)
            email_login_btn = ProviderCommonLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: email_login_btn.click(ProviderCommonLocator.email_login_btn), "email_login_btn")

        email_input2 = ProviderCommonLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: email_input2.send_key(ProviderCommonLocator.email_input2,
                                                      AccountInfo.ios_account_email), "email_input2")

        next_btn = ProviderCommonLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: next_btn.click(ProviderCommonLocator.next_btn), "next_btn")

        pw_input = ProviderCommonLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: pw_input.send_key(ProviderCommonLocator.pw_input, AccountInfo.ios_account_pw), "pw_input")
        try:
            login_btn = ProviderCommonLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: login_btn.click(ProviderCommonLocator.login_btn), "login_btn")
        except TimeoutException:
            login_btn2 = ProviderCommonLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: login_btn2.click(ProviderCommonLocator.login_btn2), "login_btn2")

    def is_logout_prod(self):
        try:
            mypage_btn = ProviderCommonLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: mypage_btn.click(ProviderCommonLocator.mypage_btn), "mypage_btn")
        except TimeoutException:
            ProviderScrollMethod.xy_click(self,200,500)
            AppStart.ios_ohou_restart(self)
            mypage_btn = ProviderCommonLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: mypage_btn.click(ProviderCommonLocator.mypage_btn), "mypage_btn")

        set_btn = ProviderCommonLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: set_btn.click(ProviderCommonLocator.set_btn), "set_btn")

        ProviderScrollMethod.down_scroll(self)

        logout_btn = ProviderCommonLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: logout_btn.click(ProviderCommonLocator.logout_btn), "logout_btn")
        try:
            dont_again_btn = ProviderCommonLocator(self.driver)
            dont_again_btn.click(ProviderCommonLocator.dont_again_btn)
        except TimeoutException:
            print("전면광고  없음")