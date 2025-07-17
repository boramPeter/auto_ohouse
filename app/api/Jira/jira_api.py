import requests, json
import re
import time
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta

class JiraApi:
    def __init__(self):
        self.username = ""
        self.api_token = ""

    def get_latest_version(self, platform):
        '''
                보안을 위해 제거
                '''


