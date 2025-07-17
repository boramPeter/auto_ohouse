from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler
from production.braze.ios.locator.braze_00059_00063 import ProviderBrazeLocator
from app.common.base_method.app_start_func import AppStart
import time
from datetime import datetime, timedelta
from selenium.common.exceptions import TimeoutException
from app.common.base_method.appium_method import ProviderScrollMethod


class MKTBrazeOnSet:
    def given_test(self):
        utc_now = datetime.utcnow()
        time_now = (utc_now + timedelta(hours=9)).strftime('%Y-%m-%d %H:%M')
        try:
            AppStart.ios_ohou_start(self)
            print(f"given_test ios 앱 실행 complete.{time_now}")
        except Exception:
            print(f"given_test ios 앱 실행 실패.{time_now}")
            AppStart.setting_app_restart(self)

            AppStart.ios_ohou_start(self)

        my_btn = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: my_btn.click(ProviderBrazeLocator.my_btn), "my_btn")
        set_btn = ProviderBrazeLocator(self.driver)
        try:
            JenkinsExceptionHandler.timeout_handler(self,lambda: set_btn.click(ProviderBrazeLocator.set_btn), "set_btn")
        except TimeoutException:
            ProviderScrollMethod.xy_click(self,200,100)
            JenkinsExceptionHandler.timeout_handler(self,lambda: set_btn.click(ProviderBrazeLocator.set_btn), "set_btn")
        noti_btn = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: noti_btn.click(ProviderBrazeLocator.noti_btn), "noti_btn")

    def go_noti_on_set(self):
        utc_now = datetime.utcnow()
        time_now = (utc_now + timedelta(hours=9)).strftime('%Y-%m-%d %H:%M')

        noti_on_btn = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: noti_on_btn.click(ProviderBrazeLocator.noti_on_btn), "noti_on_btn 최초 체크용")

        agree_btn = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: agree_btn.click(ProviderBrazeLocator.agree_btn), "agree_btn")
        print(f"오늘의집 앱에서 동의하기 선택완료 {time_now}")
        # noti_on_setting_btn = ProviderBrazeLocator(self.driver)
        # try:
            # noti_on_btn = ProviderBrazeLocator(self.driver)
            # JenkinsExceptionHandler.timeout_handler(self,lambda: noti_on_btn.click(ProviderBrazeLocator.noti_on_btn), "noti_on_btn 최초 체크용")
            # noti_setting_toggle_btn = ProviderBrazeLocator(self.driver)
            #
            # JenkinsExceptionHandler.timeout_handler(self,lambda: noti_on_setting_btn.click(ProviderBrazeLocator.noti_on_setting_btn),
            #     "noti_on_setting_btn")
            # print(f"noti_on_btn 클릭 완료 {time_now}")
            #
            # noti_on_setting_agree_btn = ProviderBrazeLocator(self.driver)
            #
            # try:
            #     JenkinsExceptionHandler.timeout_handler(self,lambda: noti_on_setting_agree_btn.click(ProviderBrazeLocator.noti_on_setting_agree_btn),
            #                     "noti_on_setting_agree_btn")
            # except TimeoutException:
            #     print("noti_on_setting_agree_btn except")
            # AppStart.setting_app_start(self)
            # print(f"설정앱 실행 완료 {time_now}")
            # noti_setting_toggle_btn = ProviderBrazeLocator(self.driver)
            #
            # try:
            #     JenkinsExceptionHandler.timeout_handler(self,lambda: noti_setting_toggle_btn.click(ProviderBrazeLocator.noti_setting_toggle_btn),
            #                     "noti_setting_toggle_btn")
            # except TimeoutException:
            #     AppStart.ios_ohou_start(self)
            #     AppStart.ios_ohou_restart(self)
            #     print(f" noti_setting_toggle_btn 예외발생 {time_now}")
            #     raise TimeoutException("noti_setting_toggle_btn이 없어서 오늘의집 앱 실행 후 재시작.")
            #
            # print(f"설정앱 토글 탭 완료 {time_now}")
            # AppStart.setting_app_restart(self)
            # try:
            #     AppStart.ios_ohou_start(self)
            # except Exception:
            #     print(f"ios 앱 실행 실패.{time_now}")
            #     AppStart.setting_app_restart(self)
            #
            #     AppStart.ios_ohou_start(self)
            #
            # print(f"오늘의집 앱에서 실행완료 {time_now}")
            # noti_on_btn = ProviderBrazeLocator(self.driver)
            #
            # JenkinsExceptionHandler.timeout_handler(self,lambda: noti_on_btn.click(ProviderBrazeLocator.noti_on_btn), "noti_on_btn(설정앱 on이후)")
            # agree_btn = ProviderBrazeLocator(self.driver)
            # JenkinsExceptionHandler.timeout_handler(self,lambda: agree_btn.click(ProviderBrazeLocator.agree_btn), "agree_btn")
            # print(f"오늘의집 앱에서 동의하기 선택완료 {time_now}")
        # except TimeoutException:
        #
        #     MKTBrazeOnSet.given_test(self)
        #     print(f"try구간 실패 했고, given_test 완료 {time_now}")
        #     try:
        #         noti_on_btn = ProviderBrazeLocator(self.driver)
        #
        #         JenkinsExceptionHandler.timeout_handler(self,lambda: noti_on_btn.is_enabled_quick(ProviderBrazeLocator.noti_on_btn), "noti_on_btn 체크용")
        #         JenkinsExceptionHandler.timeout_handler(self,lambda: noti_on_btn.click(ProviderBrazeLocator.noti_on_btn),
        #                         "noti_on_btn(given_test 이후)")
        #         noti_on_setting_btn = ProviderBrazeLocator(self.driver)
        #
        #         JenkinsExceptionHandler.timeout_handler(self,lambda: noti_on_setting_btn.click(ProviderBrazeLocator.noti_on_setting_btn),
        #                         "noti_on_setting_btn")
        #         CaptureClass.capture_screenshot_put_name(self, f"noti_on_setting_agree_btn before{time_now}")
        #
        #         try:
        #             noti_on_setting_agree_btn = ProviderBrazeLocator(self.driver)
        #
        #             JenkinsExceptionHandler.timeout_handler(self,
        #                 lambda: noti_on_setting_agree_btn.click(ProviderBrazeLocator.noti_on_setting_agree_btn),
        #                 "noti_on_setting_agree_btn")
        #         except TimeoutException:
        #             print("noti_on_setting_agree_btn except")
        #         CaptureClass.capture_screenshot_put_name(self, f"noti_on_setting_agree_btn after{time_now}")
        #         AppStart.setting_app_start(self)
        #         print(f"try구간 실패 했고, 설정앱 실행 완료 {time_now}")
        #         noti_setting_toggle_btn = ProviderBrazeLocator(self.driver)
        #
        #
        #         try:
        #             JenkinsExceptionHandler.timeout_handler(self,lambda: noti_setting_toggle_btn.click(ProviderBrazeLocator.noti_setting_toggle_btn),
        #                             "noti_setting_toggle_btn")
        #         except TimeoutException:
        #             AppStart.ios_ohou_start(self)
        #             AppStart.ios_ohou_restart(self)
        #             print(f"try구간 noti_setting_toggle_btn 예외발생 {time_now}")
        #             raise TimeoutException("try구간 noti_setting_toggle_btn이 없어서 오늘의집 앱 실행 후 재시작.")
        #
        #         print(f"try구간 실패 했고, 설정앱 토글 탭 완료 {time_now}")
        #         AppStart.setting_app_restart(self)
        #         try:
        #             AppStart.ios_ohou_start(self)
        #         except Exception:
        #             print(f"try구간 실패 했고, ios 앱 실행 실패.{time_now}")
        #             AppStart.setting_app_restart(self)
        #
        #             AppStart.ios_ohou_start(self)
        #         AppStart.ios_ohou_start(self)
        #         print(f"try구간 실패 했고, 오늘의집 실행완료 {time_now}")
        #         noti_on_btn = ProviderBrazeLocator(self.driver)
        #         JenkinsExceptionHandler.timeout_handler(self,lambda: noti_on_btn.click(ProviderBrazeLocator.noti_on_btn), "noti_on_btn(설정앱 on이후)")
        #         agree_btn = ProviderBrazeLocator(self.driver)
        #
        #         JenkinsExceptionHandler.timeout_handler(self,lambda: agree_btn.click(ProviderBrazeLocator.agree_btn), "agree_btn")
        #
        #         print(f"try구간 실패 했고, 오늘의집 동의 선택 완료 {time_now}")
        #     except TimeoutException:
        #         print("노티 설정 on 된상태이므로 패스")

        back_btn = ProviderBrazeLocator(self.driver)
        noti_btn = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: back_btn.click(ProviderBrazeLocator.back_btn),"back_btn")
        print(f"뒤로가기 선택 완료 {time_now}")

        JenkinsExceptionHandler.timeout_handler(self,lambda: noti_btn.click(ProviderBrazeLocator.noti_btn),"noti_btn")
        time.sleep(1)
        AppStart.ios_ohou_restart(self)
