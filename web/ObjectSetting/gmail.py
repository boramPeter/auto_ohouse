from web.BasicSetting.conftest import *
import ssl

user_name = None
working_directory = os.getcwd()
parts = working_directory.split(os.path.sep)
if "Users" in parts:
    user_index = parts.index("Users") + 1
    if user_index < len(parts):
        user_name = parts[user_index]

# Gmail 인증용
web_default_confidentilas = f'/Users/{user_name}/PycharmProjects/auth/web/credentials_default.json'
web_default_token = f'/Users/{user_name}/PycharmProjects/auth/web/token_default.json'
web_change_confidentilas = f'/Users/{user_name}/PycharmProjects/auth/web/credentials.json'
web_change_token = f'/Users/{user_name}/PycharmProjects/auth/web/token.json'

class GmailWebManager:
    def __init__(self, account):
        self._account = account
        self.SCOPES = ['https://mail.google.com/']
        self.service = self.authenticate(self._account)

    def authenticate(self, account):
        creds = None
        web_token = web_change_token if account == "change" else web_default_token
        if os.path.exists(web_token):
            creds = Credentials.from_authorized_user_file(web_token, self.SCOPES)
            creds.refresh(Request())
            
            with open(web_token, 'w') as token:
                token.write(creds.to_json())
        return build('gmail', 'v1', credentials=creds)

    def extract_six_auth_number(self, text):
        match = re.search(r'\b\d{6}\b', text)
        return match.group() if match else None

    def get_gmail_auth_number(self):
        time.sleep(2)
        self.get_latest_six_auth_number()
        attempts = 0
        while attempts < 3:
            result = self.get_latest_six_auth_number()
            if result is not False:
                print(result)
                self.delete_emails()
                return result
            attempts += 1
            time.sleep(2)
        return False
    
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

