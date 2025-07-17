import pickle
from app.common.app_config.data import PicklePath
from web.BasicSetting.logger_func import make_logger_web
logger_web = make_logger_web("jenkins_web_log.py")

class ResultWeb:
    file_path = PicklePath.web_pickle_path
    run_file_path = PicklePath.web_run_pickle_path

    def read_all_results(self):
        try:
            with open(self.file_path, 'rb') as f:
                loaded_result_data = pickle.load(f)
                print(loaded_result_data)
        except FileNotFoundError:
            print("파일이 존재하지 않습니다.")

    def read_result_slack(self, read):
        try:
            with open(self.file_path, 'rb') as f:
                loaded_result_data = pickle.load(f)
        except FileNotFoundError:
            return ""
        
        # dict에서 key의 인자
        slack_result = str(loaded_result_data.get(read, ""))
        return slack_result

    def write_result(self, key, write):
        write_str = str(write)
        if "Fail" in write_str:
            logger_web.debug(f"{key}: Caught an Error! {write}")
            if len(write) > 100:
                write = write[:100]
        
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
    
    def write_run(self, key):
        # 함수 호출 시 함수명으로 리스트에 추가
        try:
            with open(self.run_file_path, 'rb') as f:
                saved_result_data = pickle.load(f)
        except FileNotFoundError:
            # 파일이 없을 경우 초기화
            saved_result_data = []

        # 파일 쓰기
        with open(self.run_file_path, 'wb') as f:
            saved_result_data.append(key)
            pickle.dump(saved_result_data, f)