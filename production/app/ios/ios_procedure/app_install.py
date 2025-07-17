import time

from production.app.ios.ios_locator.precondtion.app_install import ProviderInstallLocator
from app.common.base_method.appium_method import ProviderScrollMethod
from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler
from app.common.base_method.app_start_func import AppStart
from selenium.common.exceptions import TimeoutException
import os
from app.common.base_method.ios_remote_control_func import request_app_del

class AppInstaller:
    def del_app(self):
        request_app_del(test_env="prod")

    def app_install_method(self):
        AppStart.ios_app_store_start(self)
        time.sleep(1)
        ProviderScrollMethod.xy_click(self,200,500)
        time.sleep(1)
        AppStart.ios_app_store_close(self)
        time.sleep(1)
        AppStart.ios_app_store_start(self)
        time.sleep(2)

        time.sleep(3)
        max_try = 10
        try_count = 0
        time.sleep(1)
        while try_count < max_try:
            try:
                app_store_search_btn = ProviderInstallLocator(self.driver)
                app_store_search_btn.click(ProviderInstallLocator.app_store_search_btn)
                break
            except TimeoutException:
                try_count += 1
                time.sleep(1)
        else:
            raise TimeoutException("app_store_search_btn 안보여서 케이스 종료")

        time.sleep(3)

        app_textbox = ProviderInstallLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: app_textbox.click(ProviderInstallLocator.app_textbox),
                        "app_textbox_1")


        JenkinsExceptionHandler.timeout_handler(self,lambda: app_textbox.send_key(ProviderInstallLocator.app_textbox,"오늘의집"),
                        "app_textbox_2")

        search_vk_btn = ProviderInstallLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: search_vk_btn.click(ProviderInstallLocator.search_vk_btn),
                        "search_vk_btn")
        max_try2 = 10
        try_count2 = 0
        time.sleep(1)
        while try_count2 < max_try2:
            try:
                ohou_title = ProviderInstallLocator(self.driver)
                ohou_title.click(ProviderInstallLocator.ohou_title)
                break
            except TimeoutException:
                try_count2 += 1
                time.sleep(1)
        else:
            raise TimeoutException("app_store_search_btn 안보여서 케이스 종료")


        install_btn = ProviderInstallLocator(self.driver)
        JenkinsExceptionHandler.timeout_handler(self,lambda: install_btn.click(ProviderInstallLocator.install_btn),
                        "install_btn")

    def app_install(self):
        try:
            AppInstaller.app_install_method(self)
        except TimeoutException:
            AppStart.ios_app_store_close(self)
            time.sleep(2)
            request_app_del(test_env="prod")
            time.sleep(2)
            AppInstaller.app_install_method(self)

    def actual_result(self):
        MAX_WAIT_TIME = 400  # 최대 대기 시간
        start_time = time.time()
        while time.time() < start_time + MAX_WAIT_TIME:
            try:
                app_open_btn = ProviderInstallLocator(self.driver)
                result = JenkinsExceptionHandler.timeout_handler(self,lambda: app_open_btn.is_enabled(ProviderInstallLocator.app_open_btn), "app_open_btn")
                return result
            except TimeoutException:
                time.sleep(1)
        else:
            raise TimeoutException("400초 이상 설치에 실패해서 fail처리")

    def back_flow(self):
        AppStart.ios_app_store_close(self)