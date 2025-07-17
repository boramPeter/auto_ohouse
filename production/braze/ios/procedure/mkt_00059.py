from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler
from production.braze.ios.locator.braze_00059_00063 import ProviderBrazeLocator
from app.common.base_method.app_start_func import AppStart
from app.common.base_method.appium_method import ProviderScrollMethod
from selenium.common.exceptions import TimeoutException
from app.common.app_config.data import AppVersion
from production.common.method.result_binary import TestResultBraze
import os
import time
from production.app.ios.ios_procedure.common_00011 import ProdEmailLoginCheck
from app.common.base_method.ios_remote_control_func import request_app_del
from app.common.base_method.recording_func import ScreenRecoderJenkins
from datetime import datetime

class MKTBrazeOffSet:
    def given_test(self):
        TestResultBraze().write_result("앱 설치 precondition", "fail","ios")
        # app_del = f'/opt/homebrew/bin/ideviceinstaller -u {UDID.iphone12mini_udid} -U {PackageName.ios_bundle_id}'
        request_app_del(test_env="prod")
        # os.system(app_del)
        time.sleep(5)

        AppStart.testflight_close(self)
        time.sleep(1)
        AppStart.testflight_start(self)

        try:
            testflight_title = ProviderBrazeLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: testflight_title.click(ProviderBrazeLocator.testflight_title),
                            "testflight_title")
        except TimeoutException:
            AppStart.testflight_close(self)
            time.sleep(2)
            AppStart.testflight_start(self)
            time.sleep(2)


            try:
                testflight_title = ProviderBrazeLocator(self.driver)
                JenkinsExceptionHandler.timeout_handler(self,lambda: testflight_title.click(ProviderBrazeLocator.testflight_title),
                                "testflight_title")

            except TimeoutException:
                AppStart.testflight_close(self)
                time.sleep(2)
                AppStart.testflight_start(self)
                time.sleep(3)

                testflight_title = ProviderBrazeLocator(self.driver)
                JenkinsExceptionHandler.timeout_handler(self,lambda: testflight_title.click(ProviderBrazeLocator.testflight_title),
                                "testflight_title1")
        try:
            time.sleep(4)
            ProviderScrollMethod.down_scroll(self)
            ProviderScrollMethod.down_scroll(self)
            ProviderScrollMethod.down_scroll(self)
            version_group = ProviderBrazeLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: version_group.click(ProviderBrazeLocator.version_group),
                            "version_group")
        except TimeoutException:
            ProviderScrollMethod.xy_click(self, 130, 490)  # 크래시 좌표 (2번단말 기준)
            print("crash btn check pass")

            try:
                testflight_title = ProviderBrazeLocator(self.driver)
                JenkinsExceptionHandler.timeout_handler(self,lambda: testflight_title.click(ProviderBrazeLocator.testflight_title),
                                "testflight_title")
                time.sleep(4)
                ProviderScrollMethod.down_scroll(self)
                ProviderScrollMethod.down_scroll(self)
                ProviderScrollMethod.down_scroll(self)
                version_group = ProviderBrazeLocator(self.driver)
                JenkinsExceptionHandler.timeout_handler(self,lambda: version_group.click(ProviderBrazeLocator.version_group),
                                "version_group")
            except TimeoutException:
                ProviderScrollMethod.xy_click(self, 200, 505)  # 알림허용 좌표 (1번단말 기준, 추후 분기 필요 ->udid 기준)
                print("accept_btn check pass")

                testflight_title = ProviderBrazeLocator(self.driver)
                JenkinsExceptionHandler.timeout_handler(self,lambda: testflight_title.click(ProviderBrazeLocator.testflight_title),
                                "testflight_title2")
                time.sleep(4)
                ProviderScrollMethod.down_scroll(self)
                ProviderScrollMethod.down_scroll(self)
                ProviderScrollMethod.down_scroll(self)
                version_group = ProviderBrazeLocator(self.driver)
                JenkinsExceptionHandler.timeout_handler(self,lambda: version_group.click(ProviderBrazeLocator.version_group),
                                "version_group")

        version_name = ProviderBrazeLocator(self.driver)
        version_name_input = ProviderBrazeLocator.version_name(AppVersion.version("iOS"))
        JenkinsExceptionHandler.timeout_handler(self,lambda: version_name.click(version_name_input), "version_name")

        RegularRelease_text = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: RegularRelease_text.is_enabled(ProviderBrazeLocator.RegularRelease_text),
                        "RegularRelease_text")

        try:
            install_btn = ProviderBrazeLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,
                lambda: install_btn.click(
                    ProviderBrazeLocator.install_btn), "install_btn")

        except TimeoutException:
            install_btn2 = ProviderBrazeLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,
                lambda: install_btn2.click(
                    ProviderBrazeLocator.install_btn2),
                "install_btn2")

        MAX_WAIT_TIME = 300  # 최대 대기 시간
        start_time = time.time()

        while time.time() < start_time + MAX_WAIT_TIME:
            try:
                app_open_btn = ProviderBrazeLocator(self.driver)
                JenkinsExceptionHandler.timeout_handler(self,
                    lambda: app_open_btn.is_enabled(ProviderBrazeLocator.app_open_btn), "app_open_btn")

                JenkinsExceptionHandler.timeout_handler(self,
                    lambda: app_open_btn.click(ProviderBrazeLocator.app_open_btn), "app_open_btn")
                TestResultBraze().write_result("앱 설치 precondition", "pass","ios")

                break
            except TimeoutException:
                time.sleep(1)
                if time.time() >= start_time + MAX_WAIT_TIME:
                    TestResultBraze().write_result("앱 설치 precondition", "fail","ios")
                    raise TimeoutException("300초 경과되어도 설치가 안되어 fail처리")

        AppStart.testflight_close(self)

        AppStart.ios_ohou_start(self)
        time.sleep(10)
        try:
            os_confirm_btn = ProviderBrazeLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: os_confirm_btn.click(ProviderBrazeLocator.os_confirm_btn), "os_confirm_btn")

        except TimeoutException:
            print("os_confirm_btn pass")

    def is_login(self):
        try:
            os_confirm_btn = ProviderBrazeLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: os_confirm_btn.click(ProviderBrazeLocator.os_confirm_btn), "os_confirm_btn")

        except TimeoutException:
            print("os_confirm_btn pass")
        ProdEmailLoginCheck.is_login(self)

    def go_noti_set(self):
        now = datetime.now()
        current_time = now.strftime("%H%M%S")

        ScreenRecoderJenkins.start_recording(self, f"go_noti_set_ios_{current_time}")

        no_push_btn = ProviderBrazeLocator(self.driver)
        os_no_push_btn = ProviderBrazeLocator(self.driver)
        try:
            JenkinsExceptionHandler.timeout_handler(self,lambda: no_push_btn.click(ProviderBrazeLocator.no_push_btn),"no_push_btn")
        except TimeoutException:
            print("no_push_btn 예외처리")
        try:
            JenkinsExceptionHandler.timeout_handler(self,lambda: os_no_push_btn.click(ProviderBrazeLocator.os_confirm_btn), "os_confirm_btn")
        except TimeoutException:
            print("os_confirm_btn 예외처리")
        try:
            back_set_btn = ProviderBrazeLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: back_set_btn.click(ProviderBrazeLocator.back_set_btn), "back_set_btn")
        except TimeoutException:
            print("back_set_btn 예외처리")
        try:
            os_confirm_btn = ProviderBrazeLocator(self.driver)
            JenkinsExceptionHandler.timeout_handler(self,lambda: os_confirm_btn.click(ProviderBrazeLocator.os_confirm_btn), "os_confirm_btn")

        except TimeoutException:
            print("os_confirm_btn pass")
        my_btn = ProviderBrazeLocator(self.driver)
        set_btn = ProviderBrazeLocator(self.driver)
        noti_btn = ProviderBrazeLocator(self.driver)
        try:
            JenkinsExceptionHandler.timeout_handler(self,lambda: my_btn.click(ProviderBrazeLocator.my_btn), "my_btn")
        except TimeoutException:
            ProdEmailLoginCheck.is_login(self)
            JenkinsExceptionHandler.timeout_handler(self,lambda: my_btn.click(ProviderBrazeLocator.my_btn), "my_btn")
        try:
            JenkinsExceptionHandler.timeout_handler(self,lambda: set_btn.click(ProviderBrazeLocator.set_btn), "set_btn")
        except TimeoutException:
            ProviderScrollMethod.xy_click(self,200,100)
            JenkinsExceptionHandler.timeout_handler(self,lambda: set_btn.click(ProviderBrazeLocator.set_btn), "set_btn")

        JenkinsExceptionHandler.timeout_handler(self,lambda: noti_btn.click(ProviderBrazeLocator.noti_btn), "noti_btn")

        JenkinsExceptionHandler.timeout_handler(self,lambda: noti_btn.click(ProviderBrazeLocator.noti_off_btn_ohouse), "noti_on_btn_ohouse")

        JenkinsExceptionHandler.timeout_handler(self,lambda: noti_btn.click(ProviderBrazeLocator.noti_close_confirm), "noti_close_confirm")

        JenkinsExceptionHandler.timeout_handler(self,lambda: noti_btn.click(ProviderBrazeLocator.noti_close_confirm2), "noti_close_confirm2")

        ProviderScrollMethod.pull_to_refresh(self)

        AppStart.ios_ohou_restart(self)
        time.sleep(2)
        AppStart.ios_ohou_restart(self)
        time.sleep(2)
        JenkinsExceptionHandler.timeout_handler(self,lambda: my_btn.click(ProviderBrazeLocator.my_btn), "my_btn")

        try:
            JenkinsExceptionHandler.timeout_handler(self, lambda: set_btn.click(ProviderBrazeLocator.set_btn),
                                                    "set_btn")
        except TimeoutException:
            ProviderScrollMethod.xy_click(self, 200, 100)
            JenkinsExceptionHandler.timeout_handler(self, lambda: set_btn.click(ProviderBrazeLocator.set_btn),
                                                    "set_btn")

        JenkinsExceptionHandler.timeout_handler(self,lambda: noti_btn.click(ProviderBrazeLocator.noti_btn), "noti_btn")
        time.sleep(2)
        ScreenRecoderJenkins.stop_recording(self, f"go_noti_set_ios_{current_time}")


    def back_flow(self):
        back_btn = ProviderBrazeLocator(self.driver)
        back_set_btn = ProviderBrazeLocator(self.driver)
        home_btn = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: back_btn.click(ProviderBrazeLocator.back_btn), "back_btn")
        JenkinsExceptionHandler.timeout_handler(self,lambda: back_set_btn.click(ProviderBrazeLocator.back_set_btn),"back_set_btn")
        JenkinsExceptionHandler.timeout_handler(self,lambda: home_btn.click(ProviderBrazeLocator.home_btn), "home_btn")