import os.path
import re
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient import errors
from email.message import EmailMessage
from app.common.app_config.data import AuthPath
import base64

class GmailAosManager:
    def __init__(self):
        self.SCOPES = ['https://mail.google.com/']
        self.service = self.authenticate()
        self.change_service = self.authenticate_change_account()

    def authenticate(self):
        creds = None
        if os.path.exists(AuthPath.aos_token):
            creds = Credentials.from_authorized_user_file(AuthPath.aos_token, self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(AuthPath.aos_confidentilas, self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open(AuthPath.aos_token, 'w') as token:
                token.write(creds.to_json())
        return build('gmail', 'v1', credentials=creds)

    def authenticate_change_account(self):
        creds = None
        if os.path.exists(AuthPath.aos_change_token):
            creds = Credentials.from_authorized_user_file(AuthPath.aos_change_token, self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(AuthPath.aos_chane_confidentilas, self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open(AuthPath.aos_change_token, 'w') as token:
                token.write(creds.to_json())
        return build('gmail', 'v1', credentials=creds)

    def extract_six_auth_number(self, text):
        match = re.search(r'\b\d{6}\b', text)
        return match.group() if match else None

    def get_latest_six_auth_number(self):
        try:
            response = self.service.users().messages().list(userId='me', q='from:no-reply@bucketplace.net').execute()
            if 'messages' in response and len(response['messages']) >= 1:
                latest_email_id = response['messages'][0]['id']
                latest_email = self.service.users().messages().get(userId='me', id=latest_email_id).execute()
                print('메일수신 확인:', latest_email['snippet'])
                # 이메일 본문에서 6자리 숫자 추출
                six_auth_number = self.extract_six_auth_number(latest_email['snippet'])
                print(f"메일 1개이상 {six_auth_number}")
                return six_auth_number
            else:
                print('조건에 맞는 메일 없음')
                return False
        except errors.HttpError as error:
            print('인증번호 파싱 에러:', error)

    # 계정 변경용 인증번호 함수
    def get_latest_six_auth_number_to_change_account(self):
        try:
            response = self.change_service.users().messages().list(userId='me', q='from:no-reply@bucketplace.net').execute()
            if 'messages' in response and len(response['messages']) >= 1:
                latest_email_id = response['messages'][0]['id']
                latest_email = self.change_service.users().messages().get(userId='me', id=latest_email_id).execute()
                print('메일수신 확인:', latest_email['snippet'])
                # 이메일 본문에서 6자리 숫자 추출
                six_auth_number = self.extract_six_auth_number(latest_email['snippet'])
                print(f"메일 1개이상 {six_auth_number}")
                return six_auth_number
            else:
                print('조건에 맞는 메일 없음')
                return False
        except errors.HttpError as error:
            print('인증번호 파싱 에러:', error)

    def delete_emails(self):
        try:
            response = self.service.users().messages().list(userId='me', q='from:no-reply@bucketplace.net').execute()
            if 'messages' in response:
                messages = response['messages']
                for message in messages:
                    self.service.users().messages().delete(userId='me', id=message['id']).execute()
                print(f"{len(messages)} 메일 삭제")
                return True
            else:
                print('매일 수신안됨')
                return False
        except errors.HttpError as error:
            print('메일 전체삭제 실패', error)

    # 계정 변경용 이메일 삭제 루틴 함수
    def delete_emails_change_to_account(self):
        try:
            response = self.change_service.users().messages().list(userId='me', q='from:no-reply@bucketplace.net').execute()
            if 'messages' in response:
                messages = response['messages']
                for message in messages:
                    self.change_service.users().messages().delete(userId='me', id=message['id']).execute()
                print(f"{len(messages)} 메일 삭제")
                return True
            else:
                print('매일 수신안됨')
                return False
        except errors.HttpError as error:
            print('메일 전체삭제 실패', error)


class GmailIosManager:
    def __init__(self):
        self.SCOPES = ['https://mail.google.com/']
        self.service = self.authenticate()
        self.change_service = self.authenticate_change_account()

    def authenticate(self):
        creds = None
        if os.path.exists(AuthPath.ios_token):
            creds = Credentials.from_authorized_user_file(AuthPath.ios_token, self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(AuthPath.ios_confidentilas, self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open(AuthPath.ios_token, 'w') as token:
                token.write(creds.to_json())
        return build('gmail', 'v1', credentials=creds)

    def authenticate_change_account(self):
        creds = None
        if os.path.exists(AuthPath.ios_change_token):
            creds = Credentials.from_authorized_user_file(AuthPath.ios_change_token, self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(AuthPath.ios_chane_confidentilas, self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open(AuthPath.ios_change_token, 'w') as token:
                token.write(creds.to_json())
        return build('gmail', 'v1', credentials=creds)

    def extract_six_auth_number(self, text):
        match = re.search(r'\b\d{6}\b', text)
        return match.group() if match else None

    def get_latest_six_auth_number(self):
        try:
            response = self.service.users().messages().list(userId='me', q='from:no-reply@bucketplace.net').execute()
            if 'messages' in response and len(response['messages']) >= 1:
                latest_email_id = response['messages'][0]['id']
                latest_email = self.service.users().messages().get(userId='me', id=latest_email_id).execute()
                print('메일수신 확인:', latest_email['snippet'])
                # 이메일 본문에서 6자리 숫자 추출
                six_auth_number = self.extract_six_auth_number(latest_email['snippet'])
                print(f"메일 1개이상 {six_auth_number}")
                return six_auth_number
            else:
                print('조건에 맞는 메일 없음')
                return False
        except errors.HttpError as error:
            print('인증번호 파싱 에러:', error)

    def get_latest_six_auth_number_to_change_account(self):
        try:
            response = self.change_service.users().messages().list(userId='me', q='from:no-reply@bucketplace.net').execute()
            if 'messages' in response and len(response['messages']) >= 1:
                latest_email_id = response['messages'][0]['id']
                latest_email = self.change_service.users().messages().get(userId='me', id=latest_email_id).execute()
                print('메일수신 확인:', latest_email['snippet'])
                # 이메일 본문에서 6자리 숫자 추출
                six_auth_number = self.extract_six_auth_number(latest_email['snippet'])
                print(f"메일 1개이상 {six_auth_number}")
                return six_auth_number
            else:
                print('조건에 맞는 메일 없음')
                return False
        except errors.HttpError as error:
            print('인증번호 파싱 에러:', error)

    def delete_emails(self):
        try:
            response = self.service.users().messages().list(userId='me', q='from:no-reply@bucketplace.net').execute()
            if 'messages' in response:
                messages = response['messages']
                for message in messages:
                    self.service.users().messages().delete(userId='me', id=message['id']).execute()
                print(f"{len(messages)} 메일 삭제")
                return True
            else:
                print('매일 수신안됨')
                return False
        except errors.HttpError as error:
            print('메일 전체삭제 실패', error)

    def delete_emails_change_to_account(self):
        try:
            response = self.change_service.users().messages().list(userId='me', q='from:no-reply@bucketplace.net').execute()
            if 'messages' in response:
                messages = response['messages']
                for message in messages:
                    self.change_service.users().messages().delete(userId='me', id=message['id']).execute()
                print(f"{len(messages)} 메일 삭제")
                return True
            else:
                print('매일 수신안됨')
                return False
        except errors.HttpError as error:
            print('메일 전체삭제 실패', error)

# token 생성용 함수. 바로 수행해야 하므로 필요시 주석해제후 실행
# 구글 api 셋팅 완료 후 code를 얻어서 요청할때 보내야함. 파라미터에 access_type : offline 을 넣고 요청을 보내야 리프레시토큰까지 넘어옴
# 참고링크 : https://soda-dev.tistory.com/60, https://ahn3330.tistory.com/166
# 토큰 생성 형식
# {"token": "ya29.a0Ad52N3-gm2BB955Nl9hlRCmAdkUzW2WuNPwaUwe-YSE739ndZKJkOzYDX04GykEqOYBdLqqFj81aUbTBPUvuYq2LEyMdfBIEZ8svq98TqXhrNfxnrvBKlc4e3xuFLeOjcRiS5Jet7zAouSVQoT1pZ8C2K9F3UXDDAMWSaCgYKASESARESFQHGX2MiBK5XOYS4IKrd459kQwd62Q0171", "refresh_token": "1//0eZifx0QVgyfBCgYIARAAGA4SNwF-L9IrVqO343Kz-IOiD39Y9u0xgGp3f9z8RF4HL5WtRzcfc1budREoxDvmUaypX890ceTEoYQ", "token_uri": "https://oauth2.googleapis.com/token", "client_id": "368932924481-srl9av8eqpo4tag6d4ds4a3hpm8e8mjg.apps.googleusercontent.com", "client_secret": "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", "scopes": ["https://mail.google.com/"], "universe_domain": "googleapis.com", "account": "", "expiry": "2024-03-20T09:04:25.649255Z"}


