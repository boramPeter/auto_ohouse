from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler
from production.braze.aos.locator.braze_00059_00063 import ProviderBrazeLocator
import time
from app.common.base_method.appium_method import ProviderScrollMethod
from production.braze.api.braze_push import TriggerPush

class BrazePushAppActivate:
    def push_app(self):
        '''
        보안을 위해 제거
        '''
