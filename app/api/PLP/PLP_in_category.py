import time,urllib3
import requests, urllib3
import json
from app.common.app_config.data import ApiBaseUrl
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError


class PlpCategoryAPI:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_base_url
        self.qa_api_url = ApiBaseUrl.qa_base_url

    def md_pick_list(self, category_id, os, version):
        '''
                보안을 위해 제거
                '''


