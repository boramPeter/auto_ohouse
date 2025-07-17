import time
import requests, urllib3
import json
from app.common.app_config.data import ApiBaseUrl
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError


class ProviderSearchData:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_api_url
        self.qa_api_url = ApiBaseUrl.qa_base_url

    def count_houses(self, text, version, user_id):
        '''
                보안을 위해 제거
                '''
