import time, os
from production.common.method.result_binary import TestResult
from app.common.base_method.appium_method import ProviderCommonMethod,ProviderScrollMethod
from selenium.common.exceptions import TimeoutException
from production.app.android.android_locator.all_locator.locator import ProviderLocatorAndroid
from production.app.ios.ios_locator.all_locator.locator import ProviderLocatorIos
# from production.common.data.automation_consts import PicklePath
from app.common.base_method.app_start_func import AppStart
# from app.common.base_method.logger_func import *
from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler


# working_directory = os.getcwd()
# index = working_directory.rfind("ohs-qa-automation")
# target_directory = working_directory[:index + len("ohs-qa-automation")]
#
# user_name = None
# parts = working_directory.split(os.path.sep)
# if "Users" in parts:
# if "Users" in parts:
#     user_index = parts.index("Users") + 1
#     if user_index < len(parts):
#         user_name = parts[user_index]

class Keywords:
    current_dir = os.getcwd()

    if "ios" in current_dir:
        re_text = "ios"

    if "android" in current_dir:
        re_text = "aos"

    def scenario_skip(self,func_name):
        try:
            re_text = "_aos" if "_aos" in func_name else "_ios" if "_ios" in func_name else None
            case_no = func_name.split("prod_")[1].split(re_text)[0]
            result = TestResult().read_result_slack(f"{case_no}_Result")
            if "*Fail*" in result:
                self.scenario.skip(reason="시나리오 스킵")
        except KeyError:
            pass

    def email_login(self,account):
        if account == "qabucketaos":
            from production.app.android.android_procedure.common_00011 import EmailLoginCheck
            EmailLoginCheck.is_login2(self)
        if account == "qabucketios":
            from production.app.ios.ios_procedure.common_00011 import ProdEmailLoginCheck
            ProdEmailLoginCheck.is_login(self)

    def restart_app(self):
        if Keywords.re_text == "ios":
            AppStart.ios_ohou_restart(self)
        if Keywords.re_text == "aos":
            AppStart.android_ohou_restart(self,"common00001")


    def navigate(self, *args):
        for arg in args:
            print(f"arg : {arg}")
            exception_handler = JenkinsExceptionHandler
            if "aos" in Keywords.re_text:
                ProviderLocator = ProviderLocatorAndroid
                platform = "aos"

            else:
                ProviderLocator = ProviderLocatorIos
                platform = "ios"

            if "미실행" in arg:
                pass
            if "스와이프" in arg:
                time.sleep(2)
                swipe_data_str = arg.get("스와이프", "")
                swipe_data = eval(swipe_data_str)
                scroll_list = [int(num) for num in swipe_data]
                ProviderScrollMethod.xy_swipe(self, scroll_list[0], scroll_list[1], scroll_list[2], scroll_list[3])

            if "좌표_클릭" in arg:
                time.sleep(2)
                click_data_str = arg.get("좌표_클릭", "")
                click_data = eval(click_data_str)
                xy_locator = [int(num) for num in click_data]
                ProviderScrollMethod.xy_click(self, xy_locator[0], xy_locator[1])

            if "입력" in arg:
                prod_locator = ProviderLocator(self.driver)
                parts = arg["입력"].split(' ')
                locator_value = parts[0]
                input_keyword = parts[2]
                locator = getattr(ProviderLocator, locator_value)
                exception_handler.timeout_handler(self,lambda: prod_locator.send_key(locator,input_keyword), arg["입력"])

            if "클릭" in arg:
                time.sleep(2)
                prod_locator = ProviderLocator(self.driver)
                locator = getattr(ProviderLocator, arg["클릭"])
                exception_handler.timeout_handler(self,lambda: prod_locator.click(locator), arg["클릭"])

            if "1초클릭" in arg:
                time.sleep(2)
                prod_locator = ProviderLocator(self.driver)
                locator = getattr(ProviderLocator, arg["1초클릭"])
                exception_handler.timeout_handler(self,lambda: prod_locator.long_click(locator), arg["1초클릭"])

            if "롱프레스" in arg:
                prod_locator = ProviderLocator(self.driver)
                locator = getattr(ProviderLocator, arg["롱프레스"])
                exception_handler.timeout_handler(self,lambda: prod_locator.click(locator), arg["롱프레스"])

            if "아래로_스크롤" in arg:
                count = int(arg["아래로_스크롤"].replace("회", ""))
                for _ in range(count):
                    time.sleep(0.5)
                    ProviderScrollMethod.down_scroll(self)

            if "아래로_조금_스크롤" in arg:
                count = int(arg["아래로_조금_스크롤"].replace("회", ""))
                for _ in range(count):
                    time.sleep(0.5)
                    ProviderScrollMethod.down_scroll2(self)
            if "위로_스크롤" in arg:
                count = int(arg["위로_스크롤"].replace("회", ""))
                for _ in range(count):
                    time.sleep(0.5)
                    ProviderScrollMethod.up_scroll(self)

            if "위로_조금_스크롤" in arg:
                count = int(arg["위로_조금_스크롤"].replace("회", ""))
                for _ in range(count):
                    time.sleep(0.5)
                    ProviderScrollMethod.up_scroll2(self)

            if "찾을때까지_스크롤" in arg:
                prod_locator = ProviderLocator(self.driver)
                locator_name = arg["찾을때까지_스크롤"]
                locator = getattr(ProviderLocator,locator_name)
                max_scrolls = 25
                scroll_count = 0
                while scroll_count < max_scrolls:
                    try:
                        prod_locator.is_enabled_quick(locator)
                        break
                    except TimeoutException:
                        scroll_count += 1
                        if scroll_count == 24:
                            raise TimeoutException(f"{locator_name} 못찾아서 케이스 종료")
                        else:
                            ProviderScrollMethod.down_scroll(self)
                            pass

            if "찾을때까지_조금씩_스크롤" in arg:
                prod_locator = ProviderLocator(self.driver)
                locator_name = arg["찾을때까지_조금씩_스크롤"]
                locator = getattr(ProviderLocator,locator_name)
                max_scrolls = 35
                scroll_count = 0
                while scroll_count < max_scrolls:
                    try:
                        prod_locator.is_enabled_quick(locator)
                        break
                    except TimeoutException:
                        scroll_count += 1
                        ProviderScrollMethod.down_scroll2(self)
                else:
                    raise TimeoutException(f"{locator_name} 못찾아서 케이스 종료")

            if "요소출력" in arg:
                print(ProviderCommonMethod.get_xml(self))


            if "뒤로가기" in arg:
                ProviderScrollMethod.back_key(self)

            if "앱_재시작" in arg:
                if platform == "aos":
                    AppStart.android_ohou_restart(self, "precondition")
                else:
                    AppStart.ios_ohou_restart(self)

            if "쉬고" in arg:
                time.sleep(int(arg["쉬고"].replace("초", "")))

            if "순서대로_클릭" in arg:
                locator = ProviderLocator(self.driver)
                click_str = arg["순서대로_클릭"]
                click_list = click_str.split(',')

                for click in click_list:
                    print(click,click_list)
                    locator_method = getattr(ProviderLocator, click)
                    time.sleep(0.5)
                    exception_handler.timeout_handler(self,lambda: locator.click(locator_method), click)

            if "활성화" in arg:
                prod_locator = ProviderLocator(self.driver)
                locator = getattr(ProviderLocator, arg["활성화"])
                time.sleep(2.5)
                exception_handler.timeout_handler(self,lambda: prod_locator.is_enabled(locator), arg["활성화"])

            if "광고_제거_클릭" in arg:
                try:
                    time.sleep(2)
                    prod_locator = ProviderLocator(self.driver)
                    locator = getattr(ProviderLocator, arg["광고_제거_클릭"])
                    prod_locator.click_quick(locator)
                except TimeoutException:
                    print(f"광고 예외처리")

            if "if_순서대로_클릭" in arg:
                prod_locator = ProviderLocator(self.driver)
                click_str = arg["if_순서대로_클릭"]
                click_list = click_str.split(',')
                try:
                    locator_method = getattr(ProviderLocator, click_list[0])
                    if prod_locator.is_enabled(locator_method):
                        for click in click_list[1:]:
                            print(click, click_list)
                            locator_method = getattr(ProviderLocator, click)
                            time.sleep(0.5)
                            exception_handler.timeout_handler(self,lambda: prod_locator.click(locator_method), click)
                except TimeoutException:
                    pass

            if "만약" in arg:
                try:
                    prod_locator = ProviderLocator(self.driver)
                    locator_1 = getattr(ProviderLocator, arg["만약"]["활성화"])
                    exception_handler.timeout_handler(self,lambda: prod_locator.is_enabled_quick(locator_1), arg["만약"]["활성화"])
                    try:
                        locator_2 = getattr(ProviderLocator, arg["만약"]["클릭1"])
                        exception_handler.timeout_handler(self,lambda: prod_locator.click(locator_2), arg["만약"]["클릭1"])
                    except TimeoutException:
                        print("조건 예외처리")
                    except KeyError:
                        pass

                    try:
                        locator_3 = getattr(ProviderLocator, arg["만약"]["클릭2"])
                        exception_handler.timeout_handler(self,lambda: prod_locator.click(locator_3), arg["만약"]["클릭2"])
                    except TimeoutException:
                        print("조건 예외처리")
                    except KeyError:
                        pass

                    try:
                        click_data_str = arg["만약"]["좌표_클릭"]
                        click_data = eval(click_data_str)
                        xy_locator = [int(num) for num in click_data]
                        time.sleep(1)
                        ProviderScrollMethod.xy_click(self, xy_locator[0], xy_locator[1])
                    except TimeoutException:
                        print("조건 예외처리")
                    except KeyError:
                        pass

                    try:
                        locator_4 = getattr(ProviderLocator, arg["만약"]["클릭2"])
                        exception_handler.timeout_handler(self,lambda: prod_locator.click(locator_4), arg["만약"]["클릭2"])
                    except TimeoutException:
                        print("조건 예외처리")
                    except KeyError:
                        pass
                except TimeoutException:
                    print("조건 예외처리")


    def actual_result(self, *args):
        results = []
        for arg in args:
            if "aos" in Keywords.re_text:
                ProviderLocator = ProviderLocatorAndroid
                exception_handler = JenkinsExceptionHandler
            else:
                ProviderLocator = ProviderLocatorIos
                exception_handler = JenkinsExceptionHandler

            prod_locator = ProviderLocator(self.driver)
            if "미실행" in arg:
                pass
            if "텍스트확인" in arg:
                locator = getattr(ProviderLocator, arg["텍스트확인"])
                time.sleep(2)
                result = exception_handler.timeout_handler(self,lambda: prod_locator.get_text(locator), arg["텍스트확인"])
                results.append(result)
            if "이름확인" in arg:
                locator = getattr(ProviderLocator, arg["이름확인"])
                time.sleep(2)
                result = exception_handler.timeout_handler(self,lambda: prod_locator.get_name(locator), arg["이름확인"])
                results.append(result)
            if "활성화" in arg:
                locator = getattr(ProviderLocator, arg["활성화"])
                time.sleep(2.5)
                result = exception_handler.timeout_handler(self,lambda: prod_locator.is_enabled(locator), arg["활성화"])
                results.append(result)
            if "요소미노출" in arg:
                locator = getattr(ProviderLocator, arg["요소미노출"])
                try:
                    time.sleep(2)
                    prod_locator.is_enabled_quick(locator)
                    results.append(False)
                except TimeoutException:
                    results.append(True)

        if len(results) == 1:
            return str(results[0])
        return str(results)
    def verify(self, type, expected, *actual_args):
        actual = Keywords.actual_result(self,*actual_args)
        if type == "equal":
            ProviderCommonMethod.assert_equal(self,expected,actual)
        if type == "in":
            ProviderCommonMethod.assert_in(self,expected,actual)
        if type == "list_in":
            ProviderCommonMethod.assert_in_list(self,expected,actual)

