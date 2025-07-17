import os, subprocess
from app.common.app_config.data import PicklePath
from app.common.app_config.data import BddFeaturePath
import subprocess
from app.common.base_method.aos_result_binary import ResultAndroid
from datetime import datetime


def run_behave_local(log_file):
    with open(log_file, 'w') as f:
        result = subprocess.run(
            ["behave", f"{BddFeaturePath.aos_bdd_path_local}/common.feature", "--tags=@ST,@RT", "--no-capture"],
            stdout=f,
            stderr=subprocess.STDOUT
        )
    return result.returncode


def main_aos():
    os.environ["ANDROID_AUTO_FLAG"] = "1"
    current_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_dir)

    log_file = f"android_AI_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    try:
        os.remove(PicklePath.aos_pickle_path)
    except FileNotFoundError:
        print("파일없음 예외처리")

    run_behave_local(log_file)

    results = ResultAndroid().read_all_results()
    result_status = next(
        (v.replace('*', '').split()[0] for v in results.values() if '*Pass*' in v or '*Fail*' in v),
        "결과 값이 없습니다."
    )
    os.environ["ANDROID_AUTO_RESULT"] = result_status


    try:
        os.remove(PicklePath.aos_pickle_path)
    except FileNotFoundError:
        print("파일없음 예외처리")

    os.environ["ANDROID_AUTO_FLAG"] = "0"

    return "테스트 완료"
if __name__ == '__main__':
    main_aos()


