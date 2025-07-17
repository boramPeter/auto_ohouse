import pickle, os
from report.slack_webhook import SlackWebhook,SlackWebhookJenkins
from production.common.data.automation_consts import PicklePath
# from report.create_report import WebCreateSlackReport, AppCreateSlackReport
import time
from production.common.data.automation_consts import BddFeaturePath
import re
from app.common.base_method.screenshot_func import CaptureClass,CaptureClassJenkins
# from app.common.app_config.data import Webhook
from production.common.method.result_binary import TestResult
from app.common.base_method.recording_func import ScreenRecoder,ScreenRecoderJenkins
from datetime import datetime, timedelta, timezone

class ReadDictResult:

    def __init__(self):
        self.current_dir = os.getcwd()
        self.file_path = None
        self.os_name = None
        self.tc_func_os_name = None
        self.img_os_name = None
        self.bdd_path = None
        if "ios" in self.current_dir:
            self.file_path = PicklePath.jenkins_prod_ios_pickle_path
            self.bdd_path = BddFeaturePath.jenkins_prod_ios_bdd_path
            self.os_name = "iOS"
            self.tc_func_os_name = "_ios"
            self.img_os_name = "ios"
        elif "android" in self.current_dir:
            self.file_path = PicklePath.jenkins_prod_and_pickle_path
            self.bdd_path = BddFeaturePath.jenkins_prod_aos_bdd_path
            self.os_name = "Android"
            self.tc_func_os_name = "_aos"
            self.img_os_name = "aos"
        elif "web" in self.current_dir:
            self.file_path = PicklePath.jenkins_prod_web_pickle_path
            self.bdd_path = BddFeaturePath.jenkins_prod_web_bdd_path
            self.os_name = "Web"
            self.tc_func_os_name = "_web"
            self.img_os_name = "web"

        self.feature_names = ["commerce_platform","commerce_service","common","home",'search', 'o2o', 'lifestyle', "my_page"]
        self.func_names = ["prod_commerce_platform","prod_commerce_service","prod_common","prod_home",'prod_search', 'prod_o2o', 'prod_lifestyle', "prod_my_page"]

    def count_prod_test_run(self):
        korea_offset = timezone(timedelta(hours=9))
        now = datetime.now(korea_offset)
        current_hour = now.hour
        time_periods = [
            (0, 2, 1),
            (2, 4, 2),
            (4, 8, 0),
            (8, 10, 3),
            (10, 12, 4),
            (12, 14, 5),
            (14, 16, 6),
            (16, 18, 7),
            (18, 20, 8),
            (20, 22, 9),
            (22, 24, 10)
        ]

        for start, end, number in time_periods:
            if start <= current_hour < end:
                return number

        return 0

    def _load_and_process_data(self):
        try:
            with open(self.file_path, 'rb') as file:
                data = pickle.load(file)
            filtered_data = {k: v for k, v in data.items() if '_Result' in k}
            return filtered_data
        except FileNotFoundError:
            print("파일없음 예외처리")
            return {}

    def _count_tags_in_features(self, feature_names):
        total_tags_count = 0
        paths_to_check = self.bdd_path

        if not isinstance(feature_names, list):
            feature_names = [feature_names]

        for feature_name in feature_names:
            print(f"count_tags_in_features:{total_tags_count}")
            bdd_path = os.path.join(paths_to_check, f"{feature_name}.feature")
            print(bdd_path)
            if not os.path.exists(bdd_path):
                print(f"if not os.path.exists(bdd_path):{os.path.exists(bdd_path)}")
                continue

            with open(bdd_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 태그들의 개수 합산을 위한 패턴 생성
            tags_pattern = re.compile(r'@Prod\b')
            print(f"tags_pattern:{tags_pattern}")

            matches = re.findall(tags_pattern, content)
            feature_tags_count = len(matches)
            print(feature_tags_count)
            print(f"@Prod Tag Count in {bdd_path}: {feature_tags_count}")
            total_tags_count += feature_tags_count

        return total_tags_count

    def _count_key(self, data, target_string):
        return sum(1 for key in data.keys() if target_string in key)

    def _send_result_method(self, desc_filter, count, key_filter,title_suffix, log_id, ts_in=None, debug="prod"):
        # 이관 후 제거
        # SW = SlackWebhook() if self.os_name == "Web" else SlackWebhookJenkins()
        SW = SlackWebhookJenkins()

        desc = desc_filter
        data = self._load_and_process_data()
        print(f"data:{data}")
        param = ""
        is_passed = True
        for key, value in sorted(data.items()):
            if key_filter(key):
                param += f"{key}: {value}\n\n"
                if "Fail" in value:
                    is_passed = False
        title = f"*{self.os_name} {desc} 결과 {count}*"
        if ts_in is not None:
            SW.slack_result(title, param, f"{self.os_name} {desc} {title_suffix} {log_id}", ts_in, debug=debug)
        else:
            SW.slack_result(title, param, f"{self.os_name} {desc} {title_suffix} {log_id}",debug=debug)
        return is_passed

    def _send_not_run_result_method(self,title_suffix, log_id, ts_in=None, debug="prod"):
        # 이관 후 제거
        # SW = SlackWebhook() if self.os_name == "Web" else SlackWebhookJenkins()
        SW = SlackWebhookJenkins()

        is_passed = True
        not_run_func_list = TestResult().find_not_running_func()
        if len(not_run_func_list) > 0:
            is_passed = False
            param = ""
            title = "*미실행된 함수 리스트*"
            for item in not_run_func_list:
                param += f"미실행 함수명 : {item}\n\n"
            if ts_in is not None:
                SW.slack_result(title, param, f"{self.os_name} {title_suffix} {log_id}", ts_in, debug=debug)
            else:
                SW.slack_result(title, param, f"{self.os_name} {title_suffix} {log_id}",debug=debug)
        return is_passed

    def make_report(self, total_result, auto_log_link, log_id):
        info_area = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"{self.count_prod_test_run()}회차_{self.os_name} Prod Test : {total_result}"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "text": f"auto-log id : <{auto_log_link}|{log_id}>",
                        "type": "mrkdwn"
                    }
                ]
            }]
        
        payload = {}
        attachments_dict = {}

        # 색깔 지정
        if total_result == "Pass":
            attachments_dict["color"] = "#008000"  # green
        else:
            attachments_dict["color"] = "#f44336"  # red

        attachments_dict["blocks"] = info_area
        payload["attachments"] = [attachments_dict]
        
        return payload

    def get_result(self, log_id, service):
        data = self._load_and_process_data()
        not_run = {func_name: self._count_key(data, func_name) for func_name in self.feature_names}
        # 이관 후 제거
        # SW = SlackWebhook() if self.os_name == "Web" else SlackWebhookJenkins()
        SW = SlackWebhookJenkins()

        conv_in = SW.send_slack_message(message=f'{self.os_name} 자동화 테스트 로그 스레드 {self.count_prod_test_run()}회차 실행 (auto-log id : {log_id})',debug="prod")
        thread_ts_in = conv_in.data['ts']
        auto_log_link = SW.get_thread_link(conv_in)
        is_all_passed = True
        is_all_runned = True

        for test_func, feature_name in zip(self.func_names, self.feature_names):
            check_function_count = self._count_tags_in_features(feature_name)
            keyword_check = lambda key: feature_name in key # and ReadDictResult.tc_func_os_name in key
            count = not_run[feature_name]
            print(f"not_run_count({feature_name}) : {count}")
            if count >= check_function_count:
                count_text = ""
            else:
                count_text = f"(미실행 케이스 : {check_function_count - count}개)"


            is_passed = self._send_result_method(f"{feature_name} prod", f"{count_text}", keyword_check, "자동화 테스트 완료",
                            f"(auto-log id : {log_id})", ts_in=thread_ts_in)
            if not is_passed : is_all_passed = False # fail 케이스가 하나라도 있으면 False 로 남아야 함

        if not service:
            is_all_runned = self._send_not_run_result_method("미실행 함수 체크",
                            f"(auto-log id : {log_id})", ts_in=thread_ts_in)
            total_result = "Pass" if is_all_passed and is_all_runned else "Fail" # fail 0건 & 미실행 0건 이어야 최종 Pass
            payload = self.make_report(total_result, auto_log_link, log_id)
            SW.slack_result_report(payload,debug="prod_report")
        return thread_ts_in, auto_log_link

    def send_result_slack(self, debug="prod", service=False):
        unique_id = int(time.strftime("%Y%m%d%H%M%S"))
        result_reader = ReadDictResult()
        thread_ts_in, auto_log_link = result_reader.get_result(unique_id, service)


        # 영상을 먼저 압축
        ScreenRecoderJenkins().zip_recording_files(self.img_os_name)
        # 이미지 전송
        SlackWebhookJenkins().upload_images_and_send_message_prod(self.img_os_name, self.os_name, ts=thread_ts_in,
                                                           debug=debug)
        # 영상 전송
        SlackWebhookJenkins().upload_recording_zip_and_send_message(self.img_os_name, self.os_name, ts=thread_ts_in,
                                                             debug=debug)
        # 파일 영상 삭제
        ScreenRecoderJenkins().delete_mp4_zip_files(self.img_os_name)
        # 이미지 삭제
        CaptureClassJenkins().delete_png_files_prod(self.img_os_name)

        '''
        기존 코드 주석처리
        '''
        # ScreenRecoder().zip_recording_files(self.img_os_name)
        # # 이미지 전송
        # SlackWebhook().upload_images_and_send_message_prod(self.img_os_name, self.os_name, ts=thread_ts_in, debug=debug)
        # # 영상 전송
        # SlackWebhook().upload_recording_zip_and_send_message(self.img_os_name, self.os_name, ts=thread_ts_in, debug=debug)
        # # 파일 영상 삭제
        # ScreenRecoder().delete_mp4_zip_files(self.img_os_name)
        # # 이미지 삭제
        # CaptureClass().delete_png_files_prod(self.img_os_name)
