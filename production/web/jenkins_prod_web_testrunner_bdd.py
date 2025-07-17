import os
import subprocess
from production.common.method.result_binary import TestResult
from production.common.data.automation_consts import PicklePath
from production.common.method.log_to_slack_func import ReadDictResult

def run_pytest(service=None):
    working_directory = os.getcwd()
    parts = working_directory.split(os.sep)

    workspace_index = parts.index("workspace")
    jenkins_target_directory = os.sep.join(parts[:workspace_index + 2])
    file_path = f"{jenkins_target_directory}/production/web/features/steps/web_testcase_bdd.py"
    file_name = file_path.split('/')[-1]
    if service is None: service = "Prod"

    # pytest 명령 실행
    try:
        subprocess.run(['pytest', file_name, '-s', '-m', service, '-p', 'no:pytest_reporter_html1'], cwd='/'.join(file_path.split('/')[:-1]), check=True)
    except subprocess.CalledProcessError as e: 
        print(f"{e}")

def check_and_delete_binary():
    file_path = PicklePath.jenkins_prod_web_pickle_path
    try:
        os.remove(file_path)
        print("remove binary")
    except FileNotFoundError:
        pass

def main_web_prod(service=None):
    check_and_delete_binary() #결과 파일이 있다면 초기화 
    # 웹러너 파이썬 파일 절대 경로로 일단 이동시켜서 방어
    current_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_dir)
    run_pytest(service)
    service_bool = False if service is None else True
    ReadDictResult().send_result_slack(service=service_bool)
    TestResult().insert_results_from_binary_to_db(platform="web",service=service_bool)
    os.remove(PicklePath.jenkins_prod_web_pickle_path)
    
if __name__ == '__main__':
    # service(str) : 하나의 서비스만 실행시킬 때 서비스 명 입력 (in ["common", "home", "lifestyle", "comm_s", "comm_p" , "o2o", "search", "my_page"])
    # 기본은 전체 실행, or 나 and 조건으로 다양한 마커 조합의 테스트를 할 수 있다 
    # 예시) "common or home" : @common, @home 실행
    # 예시2) "search and test" : @search 이면서 @test 인 케이스 실행
    main_web_prod(service=None)
