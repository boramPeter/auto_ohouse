import pickle, os
from report.slack_webhook import SlackWebhook,SlackWebhookJenkins
from app.common.app_config.data import PicklePath
from report.create_report import WebCreateSlackReport, AppCreateSlackReport
import time
from app.common.app_config.data import BddFeaturePath, WebTestCasePath
import re
from app.common.base_method.screenshot_func import CaptureClass,CaptureClassJenkins
from app.common.app_config.data import Webhook

class AosReadDictResult:
    file_path = PicklePath.aos_pickle_path

    def __init__(self):
        '''
                보안을 위해 제거
                '''