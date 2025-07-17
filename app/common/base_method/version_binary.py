import pickle
#from app.common.app_config.data import PicklePath
import os

### 해당함수는 jira api로 대체되면서 사용하지 않음
class VersionBinary:

    working_directory = os.getcwd()
    user_name = None
    parts = working_directory.split(os.path.sep)
    if "Users" in parts:
        user_index = parts.index("Users") + 1
        if user_index < len(parts):
            user_name = parts[user_index]
    file_path = f'/Users/{user_name}/PycharmProjects/app_version'

    def read_all_results(self):
        try:
            with open(self.file_path, 'rb') as f:
                loaded_result_data = pickle.load(f)
                print(loaded_result_data)
        except FileNotFoundError:
            print("파일이 존재하지 않습니다.")

    def read_binary(self, read):
        try:
            with open(self.file_path, 'rb') as f:
                loaded_result_data = pickle.load(f)

            # dict에서 key의 인자
            slack_result = str(loaded_result_data[read])
            return slack_result
        except FileNotFoundError:
            return None


    def write_binary(self, key, write):
        try:
            with open(self.file_path, 'rb') as f:
                saved_result_data = pickle.load(f)
        except FileNotFoundError:
            # 파일이 없을 경우 초기화
            saved_result_data = {}

        # dict key,value 순서
        test_result = str(saved_result_data.get(key, None))

        # 파일 쓰기
        with open(self.file_path, 'wb') as f:
            saved_result_data[key] = write
            pickle.dump(saved_result_data, f)

        return test_result



