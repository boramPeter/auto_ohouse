import time
from selenium.common.exceptions import WebDriverException
from app.common.app_config.data import PackageName
from app.common.base_method.appium_method import ProviderScrollMethod
from app.ios.locator.common.common_00033 import ProviderCommonLocator
from app.android.locator.comm_service.comm_service_00014 import ProviderCommServiceLocator
from selenium.common.exceptions import TimeoutException
import subprocess


class AppStart:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def force_app_restart(self, package_name):
        try:
            command = f"adb shell am force-stop {package_name}"
            subprocess.run(command, shell=True)
            time.sleep(2)
        except WebDriverException as e:
            print(f"앱 재시작 예외처리: {e}")

        # 앱 다시 시작 시도
        restarted = False
        while not restarted:
            try:
                self.driver.activate_app(PackageName.aos_package_name)
                time.sleep(2)
                restarted = True
            except WebDriverException as e:
                print(f"앱 재시작 예외처리: {e}")
        time.sleep(1)
        ProviderScrollMethod.back_key(self)

    def android_ohou_restart(self, current_function_name):
        try:
            time.sleep(1)
            self.driver.terminate_app(PackageName.aos_package_name)
            time.sleep(2)
        except WebDriverException as e:
            print(f"앱 종료 예외처리: {e}")

        # 재시작 시도 횟수 제한 설정
        max_restart_attempts = 5
        restart_attempts = 0

        # 앱 다시 시작 시도
        restarted = False
        while not restarted and restart_attempts < max_restart_attempts:
            try:
                time.sleep(1)
                self.driver.activate_app(PackageName.aos_package_name)
                time.sleep(2)
                restarted = True
            except WebDriverException as e:
                print(f"앱 시작 예외처리: {e}")
                restart_attempts += 1
                time.sleep(1)

        if not restarted:
            print("재시작이 실패했습니다. 최대 재시작 시도 횟수에 도달했습니다.")
            raise TimeoutException("재시작을 10회 실패했으므로 시나리오 강제종료.")

        if any(keyword in current_function_name for keyword in
               ["common00005","common00007","common00012""common00022", "common00024", "common00029", "common00030", "common00031", "common00032", "common00033",
                "common00034", "common00035", "common00036", "common00037", "common00041","test_common00179_aos_st_rt_step3","test_common00179_aos_st_rt_step1","test_lifestyle00014_aos_st_rt_step1"]):
            print("뒤로가기 수행하지 않음")
        else:
            time.sleep(8)
            try:
                dont_again_btn = ProviderCommServiceLocator(self.driver)
                dont_again_btn.click_quick(ProviderCommServiceLocator.dont_again_btn)
            except TimeoutException:
                print("광고 미노출되어서 스킵")
            time.sleep(2)

    def android_ohou_start(self):
        self.driver.activate_app(PackageName.aos_package_name)
        time.sleep(2)

    def android_ohou_close(self):
        ProviderScrollMethod.back_key(self)
        ProviderScrollMethod.back_key(self)
        ProviderScrollMethod.back_key(self)
        time.sleep(2)

    def android_browser_app_start(self):
        self.driver.activate_app(PackageName.aos_browser_name)

    def android_browser_app_close(self):
        self.driver.terminate_app(PackageName.aos_browser_name)

    def ios_safari_app_start(self):
        self.driver.activate_app(PackageName.ios_safari)

    def ios_safari_app_close(self):
        self.driver.terminate_app(PackageName.ios_safari)

    def ios_ohou_close(self):
        self.driver.terminate_app(PackageName.ios_bundle_id)

    def android_gmail_start(self):
        self.driver.activate_app("com.google.android.gm")

    def android_set_ads_start(self):
        self.driver.activate_app("com.android.settings")

    def android_set_ads_close(self):
        self.driver.terminate_app("com.android.settings")

    def ios_gmail_start(self):
        self.driver.activate_app("com.google.Gmail")

    def android_home(self):
        self.driver.press_keycode(3)

    def ios_ohou_start(self):
        self.driver.activate_app(PackageName.ios_bundle_id)

    def ios_ohou_restart(self):
        try:
            self.driver.terminate_app(PackageName.ios_bundle_id)
            time.sleep(2)
        except WebDriverException as e:
            print(f"앱 종료 예외처리: {e}")

        # 재시작 시도 횟수 제한 설정
        max_restart_attempts = 5
        restart_attempts = 0

        # 앱 다시 시작 시도
        restarted = False
        while not restarted and restart_attempts < max_restart_attempts:
            try:
                self.driver.activate_app(PackageName.ios_bundle_id)
                time.sleep(1)
                restarted = True
            except WebDriverException as e:
                print(f"앱 시작 예외처리: {e}")
                restart_attempts += 1
                time.sleep(1)
                try:
                    self.driver.terminate_app(PackageName.ios_bundle_id)
                    time.sleep(2)
                except WebDriverException as e:
                    print(f"시작할때 예외 -> 앱 종료 예외처리: {e}")

        if not restarted:
            print("재시작이 실패했습니다. 최대 재시작 시도 횟수에 도달했습니다.")

        try:
            dont_again_btn = ProviderCommonLocator(self.driver)
            dont_again_btn.click(ProviderCommonLocator.dont_again_btn)
        except TimeoutException:
            print("전면광고  없음")

    def deploy_gate_start(self):
        # 재시작 시도 횟수 제한 설정
        max_restart_attempts = 10
        restart_attempts = 0

        # 앱 다시 시작 시도
        restarted = False
        while not restarted and restart_attempts < max_restart_attempts:
            try:
                time.sleep(1)
                self.driver.activate_app('com.deploygate')
                time.sleep(2)
                restarted = True
            except WebDriverException as e:
                print(f"deploy_gate_start 앱 시작 예외처리: {e}")
                restart_attempts += 1
                time.sleep(1)

        if not restarted:
            print("재시작이 실패했습니다. 최대 재시작 시도 횟수에 도달했습니다.")
            raise WebDriverException("재시작을 10회 실패했으므로 시나리오 강제종료.")

    def deploy_gate_close(self):
        try:
            time.sleep(1)
            self.driver.terminate_app('com.deploygate')
            time.sleep(2)
        except WebDriverException as e:
            print(f"deploy_gate_close 앱 종료 예외처리: {e}")

    def google_store_start(self):
        # 재시작 시도 횟수 제한 설정
        max_restart_attempts = 10
        restart_attempts = 0

        # 앱 다시 시작 시도
        restarted = False
        while not restarted and restart_attempts < max_restart_attempts:
            try:
                time.sleep(1)
                self.driver.activate_app('com.android.vending')
                time.sleep(2)
                restarted = True
            except WebDriverException as e:
                print(f"google_store_start 앱 시작 예외처리: {e}")
                restart_attempts += 1
                time.sleep(1)

        if not restarted:
            print("재시작이 실패했습니다. 최대 재시작 시도 횟수에 도달했습니다.")
            raise WebDriverException("재시작을 10회 실패했으므로 시나리오 강제종료.")

    def google_store_close(self):
        try:
            time.sleep(1)
            self.driver.terminate_app('com.android.vending')
            time.sleep(2)
        except WebDriverException as e:
            print(f"google_store_close 앱 종료 예외처리: {e}")
    def google_store_restart(self):
        try:
            time.sleep(1)
            self.driver.terminate_app('com.android.vending')
            time.sleep(2)
        except WebDriverException as e:
            print(f"google_store_close 앱 종료 예외처리: {e}")

    def testflight_start(self):
        self.driver.activate_app('com.apple.TestFlight')

    def testflight_close(self):
        self.driver.terminate_app('com.apple.TestFlight')

    def setting_app_start(self):
        self.driver.activate_app('com.apple.Preferences')

    def setting_app_close(self):
        self.driver.terminate_app('com.apple.Preferences')

    def setting_app_restart(self):
        self.driver.activate_app('com.apple.Preferences')
        self.driver.terminate_app('com.apple.Preferences')

    def ios_app_store_start(self):
        self.driver.activate_app('com.apple.AppStore')

    def ios_app_store_close(self):
        self.driver.terminate_app('com.apple.AppStore')

    def ios_app_store_restart(self):
        self.driver.terminate_app('com.apple.AppStore')
        self.driver.activate_app('com.apple.AppStore')
