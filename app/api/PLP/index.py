import requests, urllib3
import json
from app.common.app_config.data import ApiBaseUrl
from urllib3.exceptions import ProtocolError
from selenium.common.exceptions import TimeoutException


class IndexApi:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_base_url
        self.qa_api_url = ApiBaseUrl.qa_base_url

    def read_list(self, version, os, index):
        '''
                보안을 위해 제거
                '''



# 0으로 던져서 조회
# 조건에 맞은 타이틀을 반환함 (0번째 상품)
# 타이틀로 요소를 찾음
# 요소가 없을경우 인덱스+1로 재호출
# 조건에 맞은 타이틀을 반환함 (1번째 상품)
# 위에서 조건을 가져온걸 담아두고, 요소 찾는 코드에서 조건에 통과하면 아이디값을 저장함

