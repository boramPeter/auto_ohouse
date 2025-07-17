import time
import requests, urllib3
import json
from app.common.app_config.data import ApiBaseUrl
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError


class MobileShoppingHomeyAPI:
    def __init__(self):
        #self.api_url = ApiBaseUrl.prd_base_url
        self.qa_api_url = ApiBaseUrl.qa_mobile_shopping_home_url

    def get_carousel_chip(self, get_user_id, os_type, version, cookie_value, token):
        '''
                보안을 위해 제거
                '''