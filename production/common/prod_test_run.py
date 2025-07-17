from report.slack_webhook import SlackWebhook
from flask_active.parallel_runner import run_parallel, run_parallel_process
from production.common.method.log_to_slack_func import ReadDictResult
# from production.app.ios.prod_ios_testrunner_bdd import main_ios_prod
from production.app.android.prod_aos_testrunner_bdd import main_aos_prod
from production.web.prod_web_testrunner_bdd import main_web_prod
from flask_active.jenkins_trigger import jenkins_trigger
def _test_runner():
    msg = f"{ReadDictResult().count_prod_test_run()}회차 Prod 자동화가 실행되었습니다."
    SlackWebhook().start_slack_msg(msg, debug="prod")

    # run_test = lambda: run_parallel_process(main_aos_prod, main_ios_prod, main_web_prod)
    jenkins_trigger("iOS-Automation-Prod",test_execution="prod")

    # jenkins_trigger("Android-Automation-Prod",test_execution="prod")

    jenkins_trigger("Web-Automation-Prod",test_execution="prod")

    # run_test()

    return "테스트 완료"



if __name__ == '__main__':
    _test_runner()