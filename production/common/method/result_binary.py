import pickle, os, re
from datetime import datetime
from app.common.base_method.mysql_query import QaDataBaseManager
from production.common.data.automation_consts import PicklePath, BddFeaturePath
try:
    working_directory = os.getcwd()
    index = working_directory.rfind("ohs-qa-automation")
    target_directory = working_directory[:index + len("ohs-qa-automation")]
    user_name = None
    parts = working_directory.split(os.path.sep)
    if "Users" in parts:
        user_index = parts.index("Users") + 1
        if user_index < len(parts):
            user_name = parts[user_index]
    jenkins_target_directory = target_directory
except ValueError:
    print("젠킨스 환경을 위한 예외처리")

try:
    working_directory = os.getcwd()
    parts = working_directory.split(os.sep)
    workspace_index = parts.index("workspace")
    jenkins_target_directory = os.sep.join(parts[:workspace_index + 2])
except ValueError:
    print("기존 환경을 위한 예외처리")



class TestResult:
    def __init__(self):
        self.file_path = None
        self._set_file_paths()

    # 함수 실행되는 경로가 중요함
    def _set_file_paths(self):
        current_dir = os.getcwd()
        if "ios" in current_dir:
            self.file_path = PicklePath.jenkins_prod_ios_pickle_path
            self.tc_path = f"{jenkins_target_directory}/production/app/ios/features/steps/ios_testcase_bdd.py"
            self.feature_path = BddFeaturePath.jenkins_prod_ios_bdd_path
        if "android" in current_dir:
            self.file_path = PicklePath.jenkins_prod_and_pickle_path
            self.tc_path = f"{jenkins_target_directory}/production/app/android/features/steps/android_testcase_bdd.py"
            self.feature_path = BddFeaturePath.jenkins_prod_aos_bdd_path
        if "web" in current_dir:
            self.file_path = PicklePath.jenkins_prod_web_pickle_path
            self.tc_path = f"{jenkins_target_directory}/production/web/features/steps/web_testcase_bdd.py"
            self.feature_path = BddFeaturePath.jenkins_prod_web_bdd_path

    def read_all_results(self):
        try:
            with open(self.file_path, 'rb') as f:
                loaded_result_data = pickle.load(f)
                print(f"loaded_result_data:{loaded_result_data}")
                return loaded_result_data
        except FileNotFoundError:
            print("파일이 존재하지 않습니다.")

    def remove_result(self,func):
        try:
            with open(self.file_path, 'rb') as f:
                loaded_result_data = pickle.load(f)
                keys_to_delete = [key for key in loaded_result_data if str(func) in key]
                for key in keys_to_delete:
                    del loaded_result_data[key]
                with open(self.file_path, 'wb') as f:
                    pickle.dump(loaded_result_data, f)

        except FileNotFoundError:
            print("파일이 존재하지 않습니다.")
    def read_result_slack(self, read):
        with open(self.file_path, 'rb') as f:
            loaded_result_data = pickle.load(f)

        # dict에서 key의 인자
        slack_result = str(loaded_result_data[read])
        return slack_result

    def write_result(self, key, write):
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

    # 함수명을 리스트에 넣고, 리스트 기준으로 바이너리 데이터 그루핑 할때 사용할 함수
    def _get_function_names(self,test_case_file_path):
        if "ios" in test_case_file_path:
            re_text = "ios"
        if "android" in test_case_file_path:
            re_text = "aos"
        if "web" in test_case_file_path:
            re_text = "web"
        function_names = set()
        with open(test_case_file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip().startswith("def "):
                    function_name = re.search(r'prod_(.*?)_' + re_text, line).group(1)
                    function_names.add(function_name)
        sorted_names = sorted(function_names)
        return sorted_names
    
    def _get_function_name_from_feature(self, file_path):
        from gherkin.parser import Parser

        paths_to_check = file_path
        function_names = set()
        feature_names = ["commerce_platform","commerce_service","common","home",'search', 'o2o', 'lifestyle', "my_page"]

        for feature_name in feature_names:
            bdd_path = os.path.join(paths_to_check, f"{feature_name}.feature")
            if not os.path.exists(bdd_path):
                print(f"if not os.path.exists(bdd_path):{os.path.exists(bdd_path)}")
                continue

            with open(bdd_path, 'r', encoding='utf-8') as file:
                content = file.read()

            parsed = Parser().parse(content)
            for feature in parsed['feature']['children']:
                dict_feature = feature.get('scenario',None)
                if dict_feature is not None:
                    if dict_feature['keyword'] in ('Scenario Outline', 'Scenario'):
                        function_names.add(dict_feature['name'].split(' ')[0])
                        #function_names.append(dict_feature['name'].split(' ')[0])
        sorted_names = sorted(function_names)
        return sorted_names

    def insert_results_from_binary_to_db(self,platform,service=False):
        if not service:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            TestResult().write_result("run_date", current_time)

            result_binary = TestResult().read_all_results()

            #function_names = TestResult()._get_function_names(self.tc_path)
            function_names = TestResult()._get_function_name_from_feature(self.feature_path)
            output_lists = []
            all_output_dicts = []
            for function_name in function_names:
                output_dict = {}
                for key, value in result_binary.items():
                    if function_name in key or 'run_date' in key:
                        output_dict[key] = value

                # 테스트 시작은 되었는데 결과까지 가기전에 중단될경우, 미수행 함수가 해당케이스를 못찾음.
                if all("_result" not in key for key in output_dict):
                    for key, value in output_dict.items():
                        # 따라서 결과 미입력케이스를 찾은뒤에, 함수명으로 검색해서 바이너리에서 제거한다.
                        if "_case_no" in key:
                            case_no = value
                            self.remove_result(case_no)
                            break

                if any(function_name in key for key in output_dict.keys()):
                    output_lists.append(output_dict)
                    all_output_dicts.append(output_dict)
                    QaDataBaseManager().insert_test_result(output_dict)

            if self.find_not_running_func():
                QaDataBaseManager().insert_not_running_result(self.find_not_running_func(),all_output_dicts,platform)

    # 함수명과 바이너리 키값을 비교해서 포한되지 않은 함수명만 리스트로 리턴함
    def find_not_running_func(self):
        def _get_name_from_tc(file_path):
            if "ios" in file_path:
                re_text = "ios"
            if "android" in file_path:
                re_text = "aos"
            if "web" in file_path:
                re_text = "web"
            function_names = set()
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    if line.strip().startswith("def "):
                        function_name = re.search(r'prod_(.*?)_' + re_text, line).group(1)
                        function_names.add(function_name)
                        # function_name_origin = line.split("def ")[1].split("(")[0].strip()
                        # function_name = function_name_origin.split("_")[1]
                        function_names.add(function_name)

            function_names = list(function_names)
            return function_names

        def _get_name_from_feature(file_path):
            from gherkin.parser import Parser

            paths_to_check = file_path
            function_names = []
            feature_names = ["commerce_platform", "commerce_service", "common", "home", 'search', 'o2o', 'lifestyle',
                             "my_page"]

            for feature_name in feature_names:
                bdd_path = os.path.join(paths_to_check, f"{feature_name}.feature")
                if not os.path.exists(bdd_path):
                    print(f"if not os.path.exists(bdd_path):{os.path.exists(bdd_path)}")
                    continue

                with open(bdd_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                parsed = Parser().parse(content)
                for feature in parsed['feature']['children']:
                    dict_feature = feature.get('scenario', None)
                    if dict_feature is not None:
                        tags = dict_feature.get('tags', [])
                        if tags and tags[0]['name'] == '@Prod' and dict_feature['keyword'] in (
                        'Scenario Outline', 'Scenario'):
                            function_names.append(dict_feature['name'].split(' ')[0])
            return function_names

        def _get_key_from_binary(binary_path):
            with open(binary_path, "rb") as file:
                data = pickle.load(file)
            keys = list(data.keys())
            return keys

        file_functions = _get_name_from_tc(self.tc_path)
        pickle_keys = _get_key_from_binary(self.file_path)
        feature_functions = _get_name_from_feature(self.feature_path)
        # 함수명 리스트의 함수명들을 요소에 할당한뒤에 바이너리 키를 할당한 리스트와 비교해서 포함이 안되어있다면 리스트에 넣음
        # feature_functions 에 포함된 요소를 func에 할당한뒤에 pickle_keys의 요소를 key에 할당하고 func가 key에 포함되어있는질 확인함. 포함되어있지 않다면 (true) 리스트로 반환
        not_running_functions = sorted([func for func in feature_functions if not any(func in key for key in pickle_keys)])
        return not_running_functions


class TestResultBraze:

    def _set_file_paths(self,test_os):
        if test_os == "ios":
            file_path = PicklePath.jenkins_prod_ios_pickle_path
        elif test_os == "android":
            file_path = PicklePath.jenkins_prod_and_pickle_path
        else:
            file_path = PicklePath.jenkins_prod_web_pickle_path

        return file_path
    def read_all_results(self,test_os):
        file_path = self._set_file_paths(test_os)
        try:
            with open(file_path, 'rb') as f:
                loaded_result_data = pickle.load(f)
                print(f"loaded_result_data:{loaded_result_data}")
                return loaded_result_data
        except FileNotFoundError:
            print("파일이 존재하지 않습니다.")

    def remove_result(self, func,test_os):
        file_path = self._set_file_paths(test_os)

        try:
            with open(file_path, 'rb') as f:
                loaded_result_data = pickle.load(f)
                keys_to_delete = [key for key in loaded_result_data if str(func) in key]
                for key in keys_to_delete:
                    del loaded_result_data[key]
                with open(file_path, 'wb') as f:
                    pickle.dump(loaded_result_data, f)

        except FileNotFoundError:
            print("파일이 존재하지 않습니다.")

    def read_result_slack(self, read,test_os):
        file_path = self._set_file_paths(test_os)
        with open(file_path, 'rb') as f:
            loaded_result_data = pickle.load(f)

        # dict에서 key의 인자
        slack_result = str(loaded_result_data[read])
        return slack_result

    def write_result(self, key, write,test_os):
        file_path = self._set_file_paths(test_os)
        try:
            with open(file_path, 'rb') as f:
                saved_result_data = pickle.load(f)
        except FileNotFoundError:
            # 파일이 없을 경우 초기화
            saved_result_data = {}

        # dict key,value 순서
        test_result = str(saved_result_data.get(key, None))

        # 파일 쓰기
        with open(file_path, 'wb') as f:
            saved_result_data[key] = write
            pickle.dump(saved_result_data, f)

        return test_result
