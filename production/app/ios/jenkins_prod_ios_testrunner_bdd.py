import os, time, subprocess
from production.common.method.result_binary import TestResult
from production.common.data.automation_consts import PicklePath
from production.common.data.automation_consts import BddFeaturePath
import threading
from production.common.method.log_to_slack_func import ReadDictResult



'''
- 바이너리 경로 
- bdd 경로
- 슬랙 (log to slack)쪽 경 (슬랙 클래스 포함)
- 핸들러쪽 동영상,사진 경로
- 로그파일 경로
- 키워드쪽 경로체크 확인필요 / 핸들러
- 앱인스톨, 티씨 핸들러
- 로그인 키워드
'''
def run_behave(main_features):
    feature_files = []

    for feature_name in main_features:
        feature_files.append(f"{BddFeaturePath.jenkins_prod_ios_bdd_path}/{feature_name}.feature")
    # subprocess.run 명령어 실행
    result = subprocess.run(
        ["behave"] + feature_files + ["--tags=@PRE,@Prod", "--no-capture"]
    )

    return result.returncode

def main_ios_prod():
    print(f"main_ios_prod : {PicklePath.jenkins_prod_ios_pickle_path}")
    os.environ["IOS_AUTO_FLAG"] = "0"
    current_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_dir)
    # for stop_count in range(1, 4):
    #     if request_wda_stop(test_env="prod"):
    #         print(f"stop complete")
    #         break
    #     else:
    #         print(f"stop_count {stop_count} failed.")
    # else:
    #     pass
    #
    # for run_count in range(1, 4):
    #     if request_wda_run(test_env="prod"):
    #         print(f"run complete")
    #         break
    #     else:
    #         request_wda_stop(test_env="prod")
    #         print(f"run_count {run_count} failed.")
    # else:
    #     pass


    main_features = ["pre_condition","common","home","my_page","lifestyle","search","o2o","commerce_service", "commerce_platform"]
    # main_features = ["pre_condition","common"]

    try:
        os.remove(PicklePath.jenkins_prod_ios_pickle_path)
    except FileNotFoundError:
        print("파일없음 예외처리")

    print("자동화 시작")
    thread_behave = threading.Thread(target=lambda: [run_behave(main_features)])
    thread_behave.start()

    thread_behave.join()
    ReadDictResult().send_result_slack()

    TestResult().insert_results_from_binary_to_db(platform="ios")

    os.remove(PicklePath.jenkins_prod_ios_pickle_path)


if __name__ == '__main__':
    main_ios_prod()
