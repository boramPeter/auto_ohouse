import requests, urllib3
import json
import re
import time
from app.common.app_config.data import ApiBaseUrl
from selenium.common.exceptions import TimeoutException


class PlaceholderApi:
    def is_placeholder_text(self):
        prd_base_url = ApiBaseUrl.prd_base_url
        api_url = f"{prd_base_url}/meta-data/v1/properties?service=home"

        qa_base_url = ApiBaseUrl.qa_base_url
        qa_api_url = f"{qa_base_url}/meta-data/v1/properties?service=home"

        header = {"Content-Type": "application/json"}

        response = requests.get(url=qa_api_url, headers=header, timeout=10)#verify=False)
        text = response.json()['placeholder']['text']
        print(text)
        return text
    
    def is_placeholder_text_shop_home(self):
        prd_base_url = ApiBaseUrl.prd_base_url
        api_url = f"{prd_base_url}/meta-data/v1/properties?service=storeHome"

        qa_base_url = ApiBaseUrl.qa_base_url
        qa_api_url = f"{qa_base_url}/meta-data/v1/properties?service=storeHome"

        header = {"Content-Type": "application/json"}

        response = requests.get(url=qa_api_url, headers=header, timeout=10)#verify=False)
        text = response.json()['placeholder']['text']
        print(text)
        return text


