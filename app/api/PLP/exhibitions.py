import requests,urllib3
import time
from app.common.app_config.data import ApiBaseUrl
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError


class ExhibitionsAPI:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_base_url
        self.qa_api_url = ApiBaseUrl.qa_base_url

    def exhibitions_detail_list(self, os, version):
        '''
                보안을 위해 제거
                '''