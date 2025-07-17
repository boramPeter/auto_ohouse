from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler
from production.braze.aos.locator.braze_00059_00063 import ProviderBrazeLocator
from app.common.base_method.app_start_func import AppStart
from app.common.app_config.data import PackageName
from selenium.common.exceptions import TimeoutException
from app.common.app_config.data import AppVersion
from production.common.method.result_binary import TestResultBraze
import time,os
import subprocess
from app.common.base_method.recording_func import ScreenRecoderJenkins
from datetime import datetime

from production.app.android.android_procedure.common_00011 import EmailLoginCheck
from app.common.base_method.appium_method import ProviderScrollMethod
from app.common.base_method.permission_func import grant_permission_jenkins
from app.common.app_config.data import UDID

class MKTBrazeOffSet:
    def given_deploy_test(self,device_udid):
        TestResultBraze().write_result("앱 설치 precondition", "fail","android")
        try:
            npm_path = "/usr/bin/npm"
            os.environ["PATH"] += os.pathsep + os.path.dirname(npm_path)
            udid = device_udid
            subprocess.run(["adb", "-s", udid, "uninstall", PackageName.aos_package_name], check=True)
        except subprocess.CalledProcessError:
            print("미설치 상태이므로 예외처리 후 진행")
        AppStart.deploy_gate_start(self)
        time.sleep(1)
        AppStart.deploy_gate_close(self)
        time.sleep(1)
        AppStart.deploy_gate_start(self)
        time.sleep(1)
        available_tab = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: available_tab.click(ProviderBrazeLocator.available_tab),"available_tab")
        ohouse_btn = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: ohouse_btn.click(ProviderBrazeLocator.ohouse_btn),"ohouse_btn")
        package_archive_btn = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: package_archive_btn.click(ProviderBrazeLocator.package_archive_btn),
            "package_archive_btn")

        idx = 1
        count = 1
        while True:
            version_name = ProviderBrazeLocator(self.driver)
            version_name_input = ProviderBrazeLocator.version_name(idx)
            version_text = JenkinsExceptionHandler.timeout_handler(self,lambda: version_name.get_text(version_name_input),
                                           "version_name")

            if AppVersion.version("aOS") in version_text:
                version_name = ProviderBrazeLocator(self.driver)
                JenkinsExceptionHandler.timeout_handler(self,lambda: version_name.click(version_name_input), "version_name")
                try:
                    regular_release_text = ProviderBrazeLocator(self.driver)
                    JenkinsExceptionHandler.timeout_handler(self,
                        lambda: regular_release_text.is_enabled_quick(ProviderBrazeLocator.regular_release_text),
                        "regular_release_text")
                    break
                except TimeoutException:
                    print("정기릴리즈 버전이 아니므로, revision 클릭")
                    package_archive_btn = ProviderBrazeLocator(self.driver)
                    package_archive_btn.click(
                        ProviderBrazeLocator.package_archive_btn)
                    idx += 1
                    if count == 3:
                        raise TimeoutException("리스트에서 버전명 확인불가")
                    if idx == 9:
                        idx = 1
                        count += 1
                        ProviderScrollMethod.down_scroll2(self)
            else:
                print("버전명이 다르므로 요소 변경")
                idx += 1
                if count == 3:
                    raise TimeoutException("리스트에서 버전명 확인불가")
                if idx == 9:
                    idx = 1
                    count += 1
                    ProviderScrollMethod.down_scroll2(self)

        install_btn = ProviderBrazeLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: install_btn.click(ProviderBrazeLocator.install_btn),
            "install_btn")
        MAX_WAIT_TIME_BTN = 60  # 최대 대기 시간
        start_time_btn = time.time()

        while time.time() < start_time_btn + MAX_WAIT_TIME_BTN:
            try:
                yes_btn = ProviderBrazeLocator(self.driver)
                JenkinsExceptionHandler.timeout_handler(self,lambda: yes_btn.click(ProviderBrazeLocator.yes_btn), "yes_btn")
                break
            except TimeoutException:
                time.sleep(1)
'''
보안을 위해 제거
'''