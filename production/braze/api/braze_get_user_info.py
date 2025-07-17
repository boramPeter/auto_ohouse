import requests
import json
import re
import time
from app.common.app_config.data import ApiBaseUrl
from selenium.common.exceptions import TimeoutException



class GetUserData:
    def get_data_user(self,user_id):
        '''
        보안을 위해 제거
        '''


