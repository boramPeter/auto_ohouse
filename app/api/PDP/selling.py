import requests,urllib3
import json
from app.common.app_config.data import ApiBaseUrl
import time
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError


class SellingApi:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_base_url
        self.qa_api_url = ApiBaseUrl.qa_base_url

    def get_options(self, version, os, product_id):
        '''
                보안을 위해 제거
                '''

