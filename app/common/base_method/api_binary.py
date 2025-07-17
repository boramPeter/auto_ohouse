import pickle
from app.common.app_config.data import PicklePath


class ApiBinary:
    file_path = PicklePath.api_pickle_path

    def read_all_results(self):
        try:
            with open(self.file_path, 'rb') as f:
                loaded_result_data = pickle.load(f)
                print(loaded_result_data)
        except FileNotFoundError:
            print("파일이 존재하지 않습니다.")

    def read_binary(self, read):
        with open(self.file_path, 'rb') as f:
            loaded_result_data = pickle.load(f)

        # dict에서 key의 인자
        slack_result = str(loaded_result_data[read])
        return slack_result

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



