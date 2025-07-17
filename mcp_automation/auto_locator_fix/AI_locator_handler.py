from mcp_automation.auto_locator_fix.AI_find_locator import HealingUiLocator
from datetime import datetime
import time,os,re
from app.common.base_method.logger_func import *

working_directory = os.getcwd()
parts = working_directory.split(os.sep)
timestamp = datetime.now().strftime("%Y%m%d_%H")

try:
    index = working_directory.rfind("ohs-qa-automation")
    target_directory = working_directory[:index + len("ohs-qa-automation")]
    user_name = None
    parts = working_directory.split(os.path.sep)
    if "Users" in parts:
        user_index = parts.index("Users") + 1
        if user_index < len(parts):
            user_name = parts[user_index]
    ai_logger = make_logger_ios(f"ai_fix_log_{timestamp}.py",
                                path=f'/Users/{user_name}/Downloads/ai_fix_log_{timestamp}.log')
except Exception:
    workspace_index = parts.index("workspace")
    jenkins_target_directory = os.sep.join(parts[:workspace_index + 2])
    print("app_config/data: 젠킨스 환경에서의 예외처리")
    ai_logger = make_logger_ios(f"ai_fix_log_{timestamp}.py", path=f'{jenkins_target_directory}/ai_fix_log_{timestamp}.log')
class LocatorState:
    def __init__(self):
        self.asis_locator = None
        self.tobe_locator = None
        self.page_source = None
        self.locator_fix_count = 0

locator_state = LocatorState()

def auto_repair_locator(locator=None,xml=None):
    need_fix_locator = os.environ.get("NEED_FIX_LOCATOR")
    fix_locator_name = os.environ.get("FIX_LOCATOR_NAME")
    android_auto_flag = os.environ.get("ANDROID_AUTO_FLAG")
    ios_auto_flag = os.environ.get("IOS_AUTO_FLAG")

    if android_auto_flag == "1":
        platform = "android"
    elif ios_auto_flag == "1":
        platform = "ios"
    else:
        print("AI 대상이 아니므로 스킵")
        return locator

    if android_auto_flag == "1" or ios_auto_flag == "1":
        print("auto_repair_locator 시작")
        if locator is not None:
            locator_state.asis_locator = locator
            locator_state.page_source = xml
            print(f"asis_locator 실행 완료 {locator_state.asis_locator}")
        if need_fix_locator == '1':
            print("자동 보정 시작")
            if user_name is None:
                dir = jenkins_target_directory
            else:
                dir = f"/Users/{user_name}/PycharmProjects/ohs-qa-automation"
            locator_state.tobe_locator = HealingUiLocator().find_locator(locator_state.asis_locator,page_source=locator_state.page_source)
            from mcp_automation.auto_locator_fix.locator_update_method import update_locator
            print(f"update_locator 체크 {locator_state.asis_locator,locator_state.tobe_locator,fix_locator_name}")

            update_locator(platform,fix_locator_name,locator_state.tobe_locator,dir)
            print("update_locator 실행 완료")
            locator_state.locator_fix_count += 1  # 카운트 증가
            ai_logger.debug(
                f"[{locator_state.locator_fix_count}회] 요소명 {fix_locator_name} -> as-is:{locator_state.asis_locator}, to-be : {locator_state.tobe_locator}")
            return locator_state.tobe_locator

    return locator

