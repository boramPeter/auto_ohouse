from flask_active.parallel_runner import run_parallel_process
from production.braze.aos_braze_runner import main_braze_aos
from production.braze.ios_braze_runner import main_braze_ios
def _test_runner():

    run_test = lambda: run_parallel_process(main_braze_aos, main_braze_ios)
    run_test()

    return "테스트 완료"



if __name__ == '__main__':
    _test_runner()