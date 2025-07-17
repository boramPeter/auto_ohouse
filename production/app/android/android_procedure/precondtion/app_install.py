import time
import subprocess
from production.app.android.android_locator.precondtion.app_install import ProviderInstallLocator
from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler
from app.common.base_method.app_start_func import AppStart
from app.common.app_config.data import PackageName
from selenium.common.exceptions import TimeoutException
from production.common.method.result_binary import TestResult

import os
class AppInstaller:
    def do_install(self):
        '''
        보안을 위해 제거
        '''