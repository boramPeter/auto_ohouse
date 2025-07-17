import requests, urllib3
import json
import time
from app.common.app_config.data import ApiBaseUrl
from app.api.join.sign_in import SignInApi
from app.common.base_method.api_binary import ApiBinary
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError


class InterestFeedApi:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_base_url
        self.qa_api_url = ApiBaseUrl.qa_api_url

    def find_interest_feed(self, token, get_user_id, cookie_value,os_type, version):
        qa_api_url = f"{self.qa_api_url}/mapi/v1/home/discovery-feed?app=true&os_type={os_type}&size=10&v=1&version={version}"
        def qa_api_next_url(page_token):
            return f"{self.qa_api_url}/mapi/v1/home/discovery-feed?app=true&pageToken={page_token}&size=10&v=1&version={version}"

        header = {
                "Content-Type": "application/json",
                "ohouse-user-id": str(get_user_id),
                'Cookie': f'_ohouse_session_4={cookie_value}',
                "ohouse-os-type": os_type,
                "Authorization": f"Bearer {token}"

        }

        max_retries = 3
        retry_count = 0
        retry_count_idx = 0
        max_retries_idx = 5
        response = None
        next_tokens = []

        while retry_count_idx < max_retries_idx:
            ################# api 호출
            while retry_count < max_retries:
                try:
                    if retry_count_idx == 0:
                        response = requests.get(url=qa_api_url, headers=header, timeout=10)  # verify=False)
                        if response.status_code == 200:
                            break
                        else:
                            retry_count += 1
                            time.sleep(1)
                    elif retry_count_idx == 1:
                        response_token = requests.get(url=qa_api_url, headers=header, timeout=10)
                        next_token = response_token.json()["nextPageToken"]
                        next_tokens.append(next_token)
                        response = requests.get(url=qa_api_next_url(page_token=next_tokens[0]), headers=header, timeout=10)  # verify=False)
                        if response.status_code == 200:
                            break
                        else:
                            retry_count += 1
                            time.sleep(1)

                    else:
                        response_token = requests.get(url=qa_api_next_url(page_token=next_tokens[0]), headers=header, timeout=10)  # verify=False)
                        next_token = response_token.json()["nextPageToken"]
                        next_tokens[0] = next_token
                        response = requests.get(url=qa_api_next_url(page_token=next_tokens[0]), headers=header,
                                                 timeout=10)
                        if response.status_code == 200:
                            break
                        else:
                            retry_count += 1
                            time.sleep(1)

                except (requests.exceptions.ConnectionError, ProtocolError, OSError) as e:
                    print(f"ConnectionError,ProtocolError 발생: {e}")
                    retry_count += 1
                    time.sleep(1)
            else:
                raise TimeoutException(f"응답코드 : {response.status_code}로 인해 발견피드 탐색 실패")

            ################# 탐색 로직 시작
            for idx in range(10):
                print(f"현재 idx : {idx}")
                try:
                    if retry_count_idx > 0:
                        title = response.json()["feed"][idx]["data"]["body"]["title"]
                    else:
                        title = response.json()["feed"][idx]["data"]["body"]["title"]
                    print(f"현재 title : {title}")
                except IndexError:
                    raise TimeoutException("관심피드 index 에러 발생해서 케이스 종료")

                if len(title) >= 3:
                    id_value = response.json()["feed"][idx]["data"]["id"]
                    qa_api_interest_feed = f"{self.qa_api_url}/mapi/v1/home/interest-feed?app=true&contentId={id_value}&contentType=CARD_COLLECTION&os_type={os_type}&size=10&v=1&version={version}"
                    max_retries_2 = 3
                    retry_count_2 = 0
                    response_feed = None
                    while retry_count_2 < max_retries_2:
                        try:
                            response_feed = requests.get(url=qa_api_interest_feed, headers=header, timeout=10)
                            if response_feed.status_code == 200:
                                break
                            else:
                                retry_count_2 += 1
                                time.sleep(1)
                        except (requests.exceptions.ConnectionError, ProtocolError, OSError, IndexError) as e:
                            print(f"ConnectionError,ProtocolError,IndexError 발생: {e}")
                            retry_count_2 += 1
                            time.sleep(1)
                    else:
                        raise TimeoutException(f"응답코드 : {response_feed.status_code}로 인해 관심피드 카운팅 실패")

                    feed_length = len(response_feed.json().get('feed', []))

                    if feed_length > 5:
                        print(f"관심피드 찾음:{title}")
                        return title
                    else:
                        print(f"{feed_length}의 갯수를 가지고있어 넘어감")
                        continue
            else:
                retry_count_idx += 1
        else:
            raise TimeoutException(f"5번 싸이클 동안 5개 이상의 피드를 가진 관심피드를 찾았으나 없었으므로 실패처리")
