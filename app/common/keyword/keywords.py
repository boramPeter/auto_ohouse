import time, os
from datetime import datetime
from app.common.base_method.appium_method import ProviderCommonMethod,ProviderScrollMethod
from selenium.common.exceptions import TimeoutException
from app.android.locator.all_locator.locator import ProviderLocatorAndroid
from app.ios.locator.all_locator.locator import ProviderLocatorIos
from app.common.base_method.exception_func import timeout_handler
from app.android.procedure.common.common_00035 import EmailLoginCheck
from app.ios.procedure.common.common_00035 import IosRTEmailLoginCheck
from app.common.base_method.app_start_func import AppStart
from app.common.base_method.ios_result_binary import Result
from app.common.base_method.aos_result_binary import ResultAndroid
from app.android.procedure.common.common_00034 import AosLogoutCheck
from app.ios.procedure.common.common_00034 import IosLogoutCheck
from app.api.report.del_block import BlockDeleteClass
from app.common.base_method.screenshot_func import CaptureClass
from app.common.base_method.mysql_query import UserManager
from app.api.home.place_holder import PlaceholderApi
from app.api.admin.orders_test import OrderTestClass
from app.api.my_page.get_point_api import PointAPI
from app.api.CDP.community_write import ProviderCommunityWriteAPI
from app.api.join.sign_in import SignInApi
from app.common.app_config.data import AppVersion, AccountInfo
from app.api.CDP.like_commnet_api import ProviderCommentAPI
from app.api.PDP.scrap_check import PDPScrapApi

working_directory = os.getcwd()
index = working_directory.rfind("ohs-qa-automation")
target_directory = working_directory[:index + len("ohs-qa-automation")]

user_name = None
parts = working_directory.split(os.path.sep)
if "Users" in parts:
    user_index = parts.index("Users") + 1
    if user_index < len(parts):
        user_name = parts[user_index]


class HighLevelKeywords:
    # current_dir = os.getcwd()
    #
    # if "ios" in current_dir:
    #     re_text = "ios"
    # if "android" in current_dir:
    #     re_text = "aos"
    # def __init__(self, re_text):
    #     self.re_text = re_text

    def email_login(self,*args,re_text=None):
        for arg in args:
            id_pw = arg["로그인"]
            id_pw_list = id_pw.split(',')
            id = id_pw_list[0]
            pw = id_pw_list[1]
            if re_text == "aos":
                EmailLoginCheck.is_login_keyword(self,id,pw)
            if re_text == "ios":
                IosRTEmailLoginCheck.is_login_ios_keyword(self,id,pw)

    def email_logout(self,re_text=None):
        if re_text == "aos":
            AosLogoutCheck.is_logout(self)
        if re_text == "ios":
            IosLogoutCheck.is_logout(self)

    def app_restart(self,re_text=None):
        if re_text == "ios":
            AppStart.ios_ohou_restart(self)
        if re_text == "aos":
            AppStart.android_ohou_restart(self,"comm_service00000")

    def search(self, *args ,re_text=None):
        for arg in args:
            print(f"arg : {arg}")

            if "aos" in re_text:
                ProviderLocator = ProviderLocatorAndroid
            else:
                ProviderLocator = ProviderLocatorIos

            if "홈화면_검색" in arg:
                # now = datetime.now()
                # current_time = now.strftime("%H%M%S")
                # ScreenRecoder.start_recording(self, f"search{current_time}")

                locator = ProviderLocator(self.driver)
                placeholder_text = PlaceholderApi().is_placeholder_text() 
                placeholder = ProviderLocator.search_btn(placeholder_text)
                timeout_handler(lambda: locator.click(placeholder), "search_btn")
                search_text_box = ProviderLocator.search_text_box
                timeout_handler(lambda: locator.click(search_text_box), "search_text_box")
                time.sleep(1)
                timeout_handler(lambda: locator.send_key(search_text_box,arg["홈화면_검색"]), arg["홈화면_검색"])
                # Android only) 엔터키 or vk_btn 으로 검색
                if "aos" in re_text:
                    ProviderScrollMethod.enter_key(self) #enter 넣어보고 SRP 로 이동안되면 vk 버튼 클릭
                    try:
                        search_icon = ProviderLocator.search_icon
                        check = locator.is_enabled(search_icon)
                        if check:
                            print("엔터로 SRP 이동 못함")
                            ProviderScrollMethod.back_key(self) # 대기화면으로 이동
                            ProviderScrollMethod.back_key(self)
                            timeout_handler(lambda: locator.send_key(search_text_box,arg["홈화면_검색"]), arg["홈화면_검색"]) # 키워드 재입력
                            
                            search_vk_btn = ProviderLocator.search_vk_btn
                            timeout_handler(lambda: locator.click(search_vk_btn), "search_vk_btn")
                    except TimeoutException:
                        print("엔터로 SRP 이동 잘함")
                else:
                    search_vk_btn = ProviderLocator.search_vk_btn
                    timeout_handler(lambda: locator.click(search_vk_btn), "search_vk_btn")

                # ScreenRecoder.stop_recording(self, f"search{current_time}")

            if "쇼핑홈_검색" in arg:
                locator = ProviderLocator(self.driver)
                gnb_shopping_btn = ProviderLocator.gnb_shopping_btn
                timeout_handler(lambda: locator.click(gnb_shopping_btn), "gnb_shopping_btn")
                time.sleep(1)
                placeholder_text = PlaceholderApi().is_placeholder_text_shop_home() 
                placeholder = ProviderLocator.search_btn(placeholder_text)
                timeout_handler(lambda: locator.click(placeholder), "shopping_home_search_btn")
                search_text_box = ProviderLocator.search_text_box
                timeout_handler(lambda: locator.click(search_text_box), "search_text_box")
                time.sleep(1)
                timeout_handler(lambda: locator.send_key(search_text_box,arg["쇼핑홈_검색"]), arg["쇼핑홈_검색"])
                # Android only) 엔터키 or vk_btn 으로 검색
                if "aos" in re_text:
                    ProviderScrollMethod.enter_key(self) #enter 넣어보고 SRP 로 이동안되면 vk 버튼 클릭
                    try:
                        search_icon = ProviderLocator.search_icon
                        check = locator.is_enabled(search_icon)
                        if check:
                            print("엔터로 SRP 이동 못함")
                            ProviderScrollMethod.back_key(self) # 대기화면으로 이동
                            ProviderScrollMethod.back_key(self)
                            timeout_handler(lambda: locator.send_key(search_text_box,arg["쇼핑홈_검색"]), arg["쇼핑홈_검색"]) # 키워드 재입력
                            
                            search_vk_btn = ProviderLocator.search_vk_btn
                            timeout_handler(lambda: locator.click(search_vk_btn), "search_vk_btn")
                    except TimeoutException:
                        print("엔터로 SRP 이동 잘함")
                else:
                    search_vk_btn = ProviderLocator.search_vk_btn
                    timeout_handler(lambda: locator.click(search_vk_btn), "search_vk_btn")


class Keywords:
    # current_dir = os.getcwd()
    #
    # if "ios" in current_dir:
    #     re_text = "ios"
    # if "android" in current_dir:
    #     re_text = "aos"
    # def __init__(self, re_text):
    #     self.re_text = re_text

    def scenario_skip(self,func_name,re_text=None):
        try:
            re_text = "_aos" if "_aos" in func_name else "_ios" if "_ios" in func_name else None
            case_no = func_name.split("test_")[1].split(re_text)[0]
            if re_text == "_aos":
                try:
                    result = ResultAndroid().read_result_slack(f"{case_no}_check")
                    if "*Fail*" in result:
                        self.scenario.skip(reason="시나리오 스킵")
                except KeyError:
                    self.scenario.skip(reason="KeyError로 인한 시나리오 스킵")
            else:
                try:
                    result = Result().read_result_slack(f"{case_no}_check")
                    if "*Fail*" in result:
                        self.scenario.skip(reason="시나리오 스킵")
                except KeyError:
                    self.scenario.skip(reason="step에서 실패로 가정하고 시나리오 스킵")

        except KeyError:
            pass

    def navigate(self, *args,re_text=None):
        for arg in args:
            print(f"arg : {arg}")

            if "aos" in re_text:
                ProviderLocator = ProviderLocatorAndroid
                binary_result = ResultAndroid()
                platform = "aos"
            else:
                ProviderLocator = ProviderLocatorIos
                platform = "ios"
                binary_result = Result()


            if None in arg:
                pass

            #사파리, 삼성브라우저
            if "브라우저_실행" in arg:
                browser_name = arg["브라우저_실행"]
                if browser_name == "사파리":
                    AppStart.ios_safari_app_start(self)
                    time.sleep(0.5)
                    AppStart.ios_safari_app_close(self)
                    time.sleep(0.5)
                    AppStart.ios_safari_app_start(self)
                    time.sleep(1)

                if browser_name == "삼성브라우저":
                    AppStart.android_browser_app_start(self)
                    time.sleep(0.5)
                    AppStart.android_browser_app_close(self)
                    time.sleep(0.5)
                    AppStart.android_browser_app_start(self)
                    time.sleep(1)

            #사파리 켜서 링크 이동까지 함
            if "사파리_링크_이동" in arg:
                AppStart.ios_safari_app_start(self)
                time.sleep(0.5)
                AppStart.ios_safari_app_close(self)
                time.sleep(0.5)
                AppStart.ios_safari_app_start(self)
                time.sleep(1)
                url = ProviderLocatorIos(self.driver)
                timeout_handler(lambda: url.click(ProviderLocatorIos.url),
                                "url")

                link = arg["사파리_링크_이동"]


                url_text_box = ProviderLocatorIos(self.driver)
                timeout_handler(lambda: url_text_box.send_key(ProviderLocatorIos.url_text_box, link), "url_text_box")

                vk_enter_key = ProviderLocatorIos(self.driver)
                timeout_handler(lambda: vk_enter_key.click(ProviderLocatorIos.vk_enter_key),
                                "vk_enter_key")

            if "삼성브라우저_링크_이동" in arg:
                AppStart.android_browser_app_start(self)
                time.sleep(0.5)
                AppStart.android_browser_app_close(self)
                time.sleep(0.5)
                AppStart.android_browser_app_start(self)
                time.sleep(1)
                url = ProviderLocatorAndroid(self.driver)
                timeout_handler(lambda: url.click(ProviderLocatorAndroid.url),
                                "url")
                try:
                    url_clear_btn = ProviderLocatorAndroid(self.driver)
                    timeout_handler(lambda: url_clear_btn.click(ProviderLocatorAndroid.url_clear_btn),
                                    "url_clear_btn")
                except TimeoutException:
                    pass

                link = arg["삼성브라우저_링크_이동"]

                url_text_box = ProviderLocatorAndroid(self.driver)
                timeout_handler(lambda: url_text_box.send_key(ProviderLocatorAndroid.url_text_box, link), "url_text_box")

                vk_enter_key = ProviderLocatorAndroid(self.driver)
                timeout_handler(lambda: vk_enter_key.click(ProviderLocatorAndroid.vk_enter_key),
                                "vk_enter_key")

                time.sleep(2)

            if "cdp_공간_초기화" in arg:
                id = arg["cdp_공간_초기화"]
                UserManager().update_place_for_card_collection(id)

            if "cdp_태그_초기화" in arg:
                id = arg["cdp_태그_초기화"]
                UserManager().update_tag_for_card_collection(id)

            if "커뮤니티_글작성" in arg:
                platform = arg["커뮤니티_글작성"]
                if platform == "iOS":
                    id = AccountInfo.ios_account_email3
                    pw = AccountInfo.ios_account_pw
                    report = None
                    test_os = None
                elif platform == "신고":
                    id = AccountInfo.aos_account_email2
                    pw = AccountInfo.aos_account_pw
                    report = "신고"
                    test_os = None
                else:
                    id = AccountInfo.aos_account_email3
                    pw = AccountInfo.aos_account_pw
                    report = None
                    test_os = "android"

                code = SignInApi().get_user_id(id,pw)[0]
                if code == 200:
                    result = SignInApi().is_sign_in(id, pw)
                    token = result[0]
                    cookie = result[1]
                    user_id = result[2]
                else:
                    raise TimeoutException ("get_user_id api 200안떨어짐. api 확인필요")
                post_id = ProviderCommunityWriteAPI().write_post(user_id, cookie, token,report=report,test_os=test_os)
                binary_result.write_result(f"{platform}_post_id", post_id)

            if "포인트_조회" in arg:
                platform = arg["포인트_조회"]
                if platform == "iOS":
                    id = AccountInfo.ios_account_email2
                    pw = AccountInfo.ios_account_pw
                else:
                    id = AccountInfo.aos_account_email2
                    pw = AccountInfo.aos_account_pw

                code = SignInApi().get_user_id(id,pw)[0]
                if code == 200:
                    result = SignInApi().is_sign_in(id, pw)
                    token = result[0]
                    cookie = result[1]
                    user_id = result[2]
                else:
                    raise TimeoutException ("get_user_id api 200안떨어짐. api 확인필요")
                point = PointAPI().get_point(user_id, cookie, token)
                binary_result.write_result(f"{platform}_point", point)

            if "커뮤니티_글삭제" in arg:
                platform = arg["커뮤니티_글삭제"]
                if platform == "iOS":
                    id = AccountInfo.ios_account_email3
                    pw = AccountInfo.ios_account_pw
                elif platform == "신고":
                    id = AccountInfo.aos_account_email2
                    pw = AccountInfo.aos_account_pw
                else:
                    id = AccountInfo.aos_account_email3
                    pw = AccountInfo.aos_account_pw

                code = SignInApi().get_user_id(id,pw)[0]
                if code == 200:
                    result = SignInApi().is_sign_in(id, pw)
                    token = result[0]
                    cookie = result[1]
                    user_id = result[2]
                else:
                    raise TimeoutException ("get_user_id api 200안떨어짐. api 확인필요")
                post_id = binary_result.read_result_slack(f"{platform}_post_id")
                ProviderCommunityWriteAPI().del_post(user_id, cookie, token,post_id)

            # 특정아이디의 스크랩폴더 횟수를 비교한다. 다르다면 폴더아이디에 상품아이디를 스크랩한다. "계정(이메일),pw,스크랩폴더이름,스크랩 카운트의 기대결과,상품아이디" e.g., "qabucketios3@gmail.com,qwertyu1,service00264,2,624075","스크랩_폴더_확인후_상품_스크랩"
            if "스크랩_폴더_확인후_상품_스크랩" in arg:
                check_count_list = arg["스크랩_폴더_확인후_상품_스크랩"]
                check_count_split = check_count_list.split(',')
                id = check_count_split[0]
                pw = check_count_split[1]
                folder_name = check_count_split[2]
                count = check_count_split[3]
                item_id = check_count_split[4]
                code = SignInApi().get_user_id(id,pw)[0]
                if code == 200:
                    result = SignInApi().is_sign_in(id, pw)
                    token = result[0]
                    cookie = result[1]
                    user_id = result[2]
                else:
                    raise TimeoutException ("get_user_id api 200안떨어짐. api 확인필요")
                folder_count = PDPScrapApi().get_scrap_folder_count(token,user_id,cookie,folder_name)
                print(f"folder_count:{folder_count},count:{count}")
                if folder_count != count:
                    PDPScrapApi().do_scrap(token, user_id, cookie, item_id,folder_name)

            if "관심댓글작성" in arg:
                id = AccountInfo.ios_account_email2
                pw = AccountInfo.ios_account_pw
                platform = arg["관심댓글작성"]
                if platform == "iOS":
                    cdp_id = "364040788836480"
                else:
                    #아이폰3 게시글 (자동화용 알림 안드)
                    cdp_id = "368625801097344"

                code = SignInApi().get_user_id(id,pw)[0]
                if code == 200:
                    result = SignInApi().is_sign_in(id, pw)
                    token = result[0]
                    cookie = result[1]
                    user_id = result[2]
                else:
                    raise TimeoutException ("get_user_id api 200안떨어짐. api 확인필요")
                commnet_id = ProviderCommentAPI().write_comment(cdp_id, user_id, cookie, token)
                print(f"관심댓글작성 commnet_id : {commnet_id}")
                binary_result.write_result(f"{platform}_comment_id", commnet_id)


            if "관심댓글삭제" in arg:
                id = AccountInfo.ios_account_email2
                pw = AccountInfo.ios_account_pw
                platform = arg["관심댓글삭제"]
                if platform == "iOS":
                    try:
                        comment_id = binary_result.read_result_slack(f"{platform}_comment_id")
                    except Exception as e:
                        print(f"comment_id 확인해주세요.{e}")

                else:
                    try:
                        comment_id = binary_result.read_result_slack(f"{platform}_comment_id")
                    except Exception as e:
                        print(f"comment_id 확인해주세요.{e}")

                code = SignInApi().get_user_id(id,pw)[0]
                if code == 200:
                    result = SignInApi().is_sign_in(id, pw)
                    token = result[0]
                    cookie = result[1]
                    user_id = result[2]
                else:
                    raise TimeoutException ("get_user_id api 200안떨어짐. api 확인필요")
                ProviderCommentAPI().del_comment(comment_id, user_id, cookie, token)

            if "미실행" in arg:
                pass

            # 좌표기준 스크롤 용도로도 사용가능 e.g., "[start_x,start_y,end_x,end_y]","스와이프"
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

            # 특정 요소 좌표에서 + 몇 만큼 좌표클릭한다. "요소명,+x좌표,+y좌표","+요소_좌표_클릭" 형식. 없으면 0으로 입력
            if "+요소_좌표_클릭" in arg:
                locator = ProviderLocator(self.driver)
                xy_str = arg["+요소_좌표_클릭"]
                xy_list = xy_str.split(',')

                locator_method = getattr(ProviderLocator, xy_list[0])
                xy = locator.get_location_xy(locator_method)
                x_locator = int(xy_list[1])
                y_locator = int(xy_list[2])
                print(f'+요소_좌표_클릭 : {xy[0]+x_locator, xy[1]+y_locator}')

                ProviderScrollMethod.xy_click(self, xy[0]+x_locator, xy[1]+y_locator)

            # 특정 요소 좌표에서 - 몇 만큼 좌표클릭한다. "요소명,x좌표,y좌표","-요소_좌표_클릭" 형식. 없으면 0으로 입력
            if "-요소_좌표_클릭" in arg:
                locator = ProviderLocator(self.driver)
                xy_str = arg["-요소_좌표_클릭"]
                xy_list = xy_str.split(',')

                locator_method = getattr(ProviderLocator, xy_list[0])
                xy = locator.get_location_xy(locator_method)
                x_locator = int(xy_list[1])
                y_locator = int(xy_list[2])
                print(f'-요소_좌표_클릭 : {xy[0]-x_locator, xy[1]-y_locator}')
                ProviderScrollMethod.xy_click(self, xy[0]-x_locator, xy[1]-y_locator)

            if "입력" in arg:
                locator = ProviderLocator(self.driver)
                parts = arg["입력"].split(' ')
                locator_value = parts[0]
                input_keyword = parts[2]
                locator_method = getattr(ProviderLocator, locator_value)
                timeout_handler(lambda: locator.send_key(locator_method,input_keyword), arg["입력"])

            #문장마다 줄바꿈을 넣고, 순서대로 입력필요할때 사용합니다. e.g., "입력필드 요소명,첫문장,두번째문장...","순서대로_입력"
            if "순서대로_입력" in arg:
                locator = ProviderLocator(self.driver)
                parts = arg["순서대로_입력"].split(',')
                locator_value = parts[0]
                # input_keyword = parts[2]
                locator_method = getattr(ProviderLocator, locator_value)
                for keyword in parts[1:]:
                    print(keyword, parts)
                    time.sleep(0.5)
                    timeout_handler(lambda: locator.send_key(locator_method,keyword), keyword)
                    timeout_handler(lambda: locator.click(ProviderLocator.search_vk_btn),"search_vk_btn")
                    timeout_handler(lambda: locator.click(locator_method,keyword),keyword)

            #동일한 입력이 아닌, 텍스트 +오늘날짜를 결합해서 유니크한 키워드로 결합한다.
            if "동적_입력" in arg:
                locator = ProviderLocator(self.driver)
                parts = arg["동적_입력"].split(' ')
                locator_value = parts[0]
                input_keyword_origin = parts[2]
                input_keyword = input_keyword_origin+datetime.today().strftime("%Y-%m-%d")
                locator_method = getattr(ProviderLocator, locator_value)
                timeout_handler(lambda: locator.send_key(locator_method,input_keyword), arg["동적_입력"])

            # bounds y축 높이를 비교합니다. e.g., "요소명,숫자","y축_bounds_비교" -> 3번 인덱스 - 1번 인덱스 >= 숫자. 맞다면 성공. 아니라면 fail.
            if "y축_bounds_비교" in arg:
                locator = ProviderLocator(self.driver)
                xy_str = arg["y축_bounds_비교"]
                xy_list = xy_str.split(',')
                print(xy_list)
                # input_method = getattr(ProviderLocator, xy_list[0])
                criteria_value = int(xy_list[1])

                get_bounds_locator = getattr(ProviderLocator, xy_list[0])
                get_bounds_value = timeout_handler(lambda: locator.get_bounds(get_bounds_locator), xy_list[0])
                first_value = get_bounds_value[1]
                sec_value = get_bounds_value[3]
                print(sec_value, first_value, criteria_value)
                if sec_value - first_value >= criteria_value:
                    pass
                else:
                    TimeoutException(f"y축_bounds_비교 실패 : 높이값({sec_value - first_value})")

            # 요소의 height를 체크합니다. e.g., "요소명,숫자","height_체크" 요소의 height값 >= 숫자 라면 pass, 아니라면 fail.
            if "height_체크" in arg:
                locator = ProviderLocator(self.driver)
                xy_str = arg["height_체크"]
                xy_list = xy_str.split(',')
                print(xy_list)
                criteria_value = int(xy_list[1])

                get_height_locator = getattr(ProviderLocator, xy_list[0])
                get_height_value = timeout_handler(lambda: locator.get_height(get_height_locator), xy_list[0])

                print(get_height_value, criteria_value)
                if get_height_value >= criteria_value:
                    pass
                else:
                    TimeoutException(f"height_체크 실패 : height ({get_height_value})")

            if "클릭" in arg:
                time.sleep(2)
                locator = ProviderLocator(self.driver)
                locator_method = getattr(ProviderLocator, arg["클릭"])
                timeout_handler(lambda: locator.click(locator_method), arg["클릭"])

            # 요소의 이름을 바이너리에 저장한다. 요소명이 키가 되고, 이름이 값이 된다. 형식 : "요소명","이름_저장" -> 나중에 이름_저장_비교 키워드와 합쳐서 사용가능.
            if "이름_저장" in arg:
                time.sleep(1)
                locator = ProviderLocator(self.driver)
                locator_method = getattr(ProviderLocator, arg["이름_저장"])
                name = timeout_handler(lambda: locator.get_name(locator_method), arg["이름_저장"])
                print(arg["이름_저장"],name)
                binary_result.write_result(arg["이름_저장"],name)

            # 요소의 이름을 바이너리에 저장한다. 요소명이 키가 되고, 이름이 값이 된다. 형식 : "요소명","이름_저장" -> 나중에 이름_저장_비교 키워드와 합쳐서 사용가능.
            if "텍스트_저장" in arg:
                time.sleep(1)
                locator = ProviderLocator(self.driver)
                locator_method = getattr(ProviderLocator, arg["텍스트_저장"])
                name = timeout_handler(lambda: locator.get_text(locator_method), arg["텍스트_저장"])
                print(arg["텍스트_저장"],name)
                binary_result.write_result(arg["텍스트_저장"],name)

            if "desc_저장" in arg:
                time.sleep(1)
                locator = ProviderLocator(self.driver)
                locator_method = getattr(ProviderLocator, arg["desc_저장"])
                desc = timeout_handler(lambda: locator.get_content_desc(locator_method), arg["desc_저장"])
                print(arg["desc_저장"],desc)
                binary_result.write_result(arg["desc_저장"], desc)

            #키워드 : "결제완료,user_id,item_no,option_no,order_count","주문생성"
            if "주문생성" in arg:
                info_order = arg["주문생성"]
                order_list = info_order.split(',')
                status_mapping = {
                    "결제완료": "PAYMENT_COMPLETE",
                    "배송준비": "READY_FOR_DELIVERY",
                    "배송중": "ON_DELIVERY",
                    "배송완료": "DELIVERY_COMPLETE",
                    "구매확정": "CONFIRMED"
                }
                order_status = status_mapping.get(order_list[0], "PAYMENT_COMPLETE")

                user_id = order_list[1]
                item_no = order_list[2]
                option_no = order_list[3]
                order_count = order_list[4]
                print(order_status,user_id,item_no,option_no,order_count)
                OrderTestClass().do_test_order(order_status,user_id,item_no,option_no,order_count)

            if "요소출력" in arg:
                ProviderCommonMethod.get_xml(self)

            if "요소찾기" in arg:
                time.sleep(0.5)
                ProviderCommonMethod.find_xml_text(self,arg["요소찾기"])

            if "요소_스크린샷" in arg:
                img_name = f'{arg["요소_스크린샷"]}.png'
                locator = ProviderLocator(self.driver)
                locator_method = getattr(ProviderLocator, arg["요소_스크린샷"])
                timeout_handler(lambda: locator.capture_element_screenshot(locator_method,img_name),arg["요소_스크린샷"])

            # Fail 원인을 찾기 위한 화면 스크린샷 남기기 
            if "화면_스크린샷" in arg:
                img_name = f'{arg["화면_스크린샷"]}.png'
                CaptureClass.capture_screenshot_put_name(self, img_name)

            if "신고_삭제" in arg:
                BlockDeleteClass().del_block(arg["신고_삭제"])

            if "순서대로_클릭" in arg:
                locator = ProviderLocator(self.driver)
                click_str = arg["순서대로_클릭"]
                click_list = click_str.split(',')

                for click in click_list:
                    print(click,click_list)
                    locator_method = getattr(ProviderLocator, click)
                    time.sleep(0.5)
                    timeout_handler(lambda: locator.click(locator_method), click)

            # 조건에 맞다면, 클릭을 연속으로 수행한다.
            if "if_순서대로_클릭" in arg:
                locator = ProviderLocator(self.driver)
                click_str = arg["if_순서대로_클릭"]
                click_list = click_str.split(',')
                try:
                    locator_method = getattr(ProviderLocator, click_list[0])
                    if locator.is_enabled(locator_method):
                        for click in click_list[1:]:
                            print(click, click_list)
                            locator_method = getattr(ProviderLocator, click)
                            time.sleep(0.5)
                            timeout_handler(lambda: locator.click(locator_method), click)
                except TimeoutException:
                    pass

            # 조건에 맞다면, 좌표를 클릭한다.
            if "if_좌표_클릭" in arg:
                locator = ProviderLocator(self.driver)
                click_str = arg["if_좌표_클릭"]
                click_list = click_str.split(',')
                try:
                    locator_method = getattr(ProviderLocator, click_list[0])
                    if locator.is_enabled(locator_method):
                        x_locator = int(click_list[1])
                        y_locator = int(click_list[2])
                        ProviderScrollMethod.xy_click(self, x_locator, y_locator)
                except TimeoutException:
                    pass

            # 0번요소가 있다면 1번요소를 클릭하고, 그렇지않다면 2번요소를 클릭한다.
            if "if_else_클릭" in arg:
                locator = ProviderLocator(self.driver)
                click_str = arg["if_else_클릭"]
                click_list = click_str.split(',')
                try:
                    locator_method = getattr(ProviderLocator, click_list[0])
                    if locator.is_enabled(locator_method):
                        locator_method = getattr(ProviderLocator, click_list[1])
                        time.sleep(0.5)
                        locator.click(locator_method)
                        print(f"if_else_클릭:{click_list[1]}")
                except TimeoutException:
                    locator_method = getattr(ProviderLocator, click_list[2])
                    time.sleep(0.5)
                    timeout_handler(lambda: locator.click(locator_method), click_list[2])
                    print(f"if_else_클릭:{click_list[2]}")
            # 0번요소가 없다면 1번요소를 클릭한다 (e.g., "0번요소,1번요소","else_클릭"
            if "else_클릭" in arg:
                locator = ProviderLocator(self.driver)
                click_str = arg["else_클릭"]
                click_list = click_str.split(',')
                try:
                    locator_method = getattr(ProviderLocator, click_str[0])
                    if locator.is_enabled(locator_method):
                        pass
                except TimeoutException:
                    locator_method = getattr(ProviderLocator, click_list[1])
                    timeout_handler(lambda: locator.click(locator_method), click_list[1])


            # 0번요소가 없다면 xy를 좌표클릭한다
            if "else_좌표클릭" in arg:
                locator = ProviderLocator(self.driver)
                xy_str = arg["else_좌표클릭"]
                xy_list = xy_str.split(',')

                x_locator = int(xy_list[1])
                y_locator = int(xy_list[2])
                print(f"else_좌표클릭:{xy_list}")
                try:
                    locator_method = getattr(ProviderLocator, xy_list[0])
                    if locator.is_enabled(locator_method):
                        locator_method = getattr(ProviderLocator, xy_list[0])
                        time.sleep(0.5)
                        timeout_handler(lambda: locator.is_enabled(locator_method), xy_list[0])
                except TimeoutException:
                    ProviderScrollMethod.xy_click(self, x_locator, y_locator)

            # 0번요소를 찾을때까지 좌표값 기준으로 스크롤
            if "찾을때까지_좌표_스크롤" in arg:
                locator = ProviderLocator(self.driver)
                xy_str = arg["찾을때까지_좌표_스크롤"]
                xy_list = xy_str.split(',')

                x_locator = int(xy_list[1])
                y_locator = int(xy_list[2])
                x_end_locator = int(xy_list[3])
                y_end_locator = int(xy_list[4])
                print(f"찾을때까지_좌표_스크롤:{xy_list}")
                max_scrolls = 10
                scroll_count = 0
                locator_method = getattr(ProviderLocator, xy_list[0])

                while scroll_count < max_scrolls:
                    try:
                        locator.is_enabled_quick(locator_method)
                        break
                    except TimeoutException:
                        scroll_count += 1
                        time.sleep(0.5)
                        ProviderScrollMethod.xy_swipe(self, x_locator, y_locator, x_end_locator, y_end_locator)

                else:
                    raise TimeoutException(f"{xy_list[0]} 못찾아서 케이스 종료")


            if "롱프레스" in arg:
                locator = ProviderLocator(self.driver)
                locator_method = getattr(ProviderLocator, arg["롱프레스"])
                timeout_handler(lambda: locator.click(locator_method), arg["롱프레스"])

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
                locator = ProviderLocator(self.driver)
                locator_name = arg["찾을때까지_스크롤"]
                locator_method = getattr(ProviderLocator,locator_name)
                max_scrolls = 35
                scroll_count = 0
                while scroll_count < max_scrolls:
                    try:
                        locator.is_enabled_quick(locator_method)
                        break
                    except TimeoutException:
                        scroll_count += 1
                        ProviderScrollMethod.down_scroll(self)
                else:
                    raise TimeoutException(f"{locator_name} 못찾아서 케이스 종료")

            if "찾을때까지_위로_스크롤" in arg:
                locator = ProviderLocator(self.driver)
                locator_name = arg["찾을때까지_위로_스크롤"]
                locator_method = getattr(ProviderLocator, locator_name)
                max_scrolls = 35
                scroll_count = 0
                while scroll_count < max_scrolls:
                    try:
                        locator.is_enabled_quick(locator_method)
                        break
                    except TimeoutException:
                        scroll_count += 1
                        ProviderScrollMethod.up_scroll(self)
                else:
                    raise TimeoutException(f"{locator_name} 못찾아서 케이스 종료")

            if "찾을때까지_위로_조금_스크롤" in arg:
                locator = ProviderLocator(self.driver)
                locator_name = arg["찾을때까지_위로_조금_스크롤"]
                locator_method = getattr(ProviderLocator, locator_name)
                max_scrolls = 35
                scroll_count = 0
                while scroll_count < max_scrolls:
                    try:
                        locator.is_enabled_quick(locator_method)
                        break
                    except TimeoutException:
                        scroll_count += 1
                        ProviderScrollMethod.up_scroll2(self)
                else:
                    raise TimeoutException(f"{locator_name} 못찾아서 케이스 종료")

            if "찾을때까지_오른쪽_스와이프" in arg:
                locator = ProviderLocator(self.driver)
                locator_name = arg["찾을때까지_오른쪽_스와이프"]
                locator_method = getattr(ProviderLocator,locator_name)
                max_scrolls = 25
                scroll_count = 0
                while scroll_count < max_scrolls:
                    try:
                        locator.is_enabled_quick(locator_method)
                        break
                    except TimeoutException:
                        scroll_count += 1
                        if scroll_count == 24:
                            raise TimeoutException(f"{locator_name} 못찾아서 케이스 종료")
                        else:
                            ProviderScrollMethod.to_right_swipe(self)
                            pass

            if "찾을때까지_y기준_오른쪽_스와이프" in arg:
                locator = ProviderLocator(self.driver)
                arg_list = arg["찾을때까지_y기준_오른쪽_스와이프"].split(',')
                find_locator = getattr(ProviderLocator, arg_list[0]) # 찾아야하는 요소
                y_guide_locator = getattr(ProviderLocator, arg_list[1]) # y 좌표 위치 참조하는 요소
                y_guide_xy = locator.get_location_xy(y_guide_locator)
                added_y = int(arg_list[2])

                width = self.driver.get_window_size()['width'] # x 좌표는 화면 기준으로 구함
                start_x = int(width * 0.2)
                end_x = int(width * 0.8)

                max_scrolls = 30
                scroll_count = 0
                while scroll_count < max_scrolls:
                    try:
                        locator.is_enabled_quick(find_locator)
                        break
                    except TimeoutException:
                        scroll_count += 1
                        if scroll_count == 30:
                            raise TimeoutException(f"{arg_list[0]} 못찾아서 케이스 종료")
                        else:
                            ProviderScrollMethod.xy_swipe(self, start_x, y_guide_xy[1]+added_y, end_x, y_guide_xy[1]+added_y)
                            pass

            if "찾을때까지_왼쪽_스와이프" in arg:
                locator = ProviderLocator(self.driver)
                locator_name = arg["찾을때까지_왼쪽_스와이프"]
                locator_method = getattr(ProviderLocator,locator_name)
                max_scrolls = 25
                scroll_count = 0
                while scroll_count < max_scrolls:
                    try:
                        locator.is_enabled_quick(locator_method)
                        break
                    except TimeoutException:
                        scroll_count += 1
                        if scroll_count == 24:
                            raise TimeoutException(f"{locator_name} 못찾아서 케이스 종료")
                        else:
                            ProviderScrollMethod.to_left_swipe(self)
                            pass

            if "찾을때까지_y기준_왼쪽_스와이프" in arg:
                locator = ProviderLocator(self.driver)
                arg_list = arg["찾을때까지_y기준_왼쪽_스와이프"].split(',')
                find_locator = getattr(ProviderLocator, arg_list[0]) # 찾아야하는 요소
                y_guide_locator = getattr(ProviderLocator, arg_list[1]) # y 좌표 위치 참조하는 요소
                y_guide_xy = locator.get_location_xy(y_guide_locator)
                added_y = int(arg_list[2])

                width = self.driver.get_window_size()['width'] # x 좌표는 화면 기준으로 구함
                start_x = int(width * 0.8)
                end_x = int(width * 0.2)

                max_scrolls = 30
                scroll_count = 0
                while scroll_count < max_scrolls:
                    try:
                        locator.is_enabled_quick(find_locator)
                        break
                    except TimeoutException:
                        scroll_count += 1
                        if scroll_count == 30:
                            raise TimeoutException(f"{arg_list[0]} 못찾아서 케이스 종료")
                        else:
                            ProviderScrollMethod.xy_swipe(self, start_x, y_guide_xy[1]+added_y, end_x, y_guide_xy[1]+added_y)
                            pass

            # 조건에 맞다면, 좌표 스크롤 수행
            if "if_좌표_스크롤" in arg:
                locator = ProviderLocator(self.driver)
                xy_str = arg["if_좌표_스크롤"]
                xy_list = xy_str.split(',')

                x_locator = int(xy_list[1])
                y_locator = int(xy_list[2])
                x_end_locator = int(xy_list[3])
                y_end_locator = int(xy_list[4])
                
                max_scrolls = 10
                scroll_count = 0
                locator_method = getattr(ProviderLocator, xy_list[0])

                while scroll_count < max_scrolls:
                    try:
                        if locator.is_enabled_quick(locator_method):
                            scroll_count += 1
                            time.sleep(0.5)
                            ProviderScrollMethod.xy_swipe(self, x_locator, y_locator, x_end_locator, y_end_locator)
                    except TimeoutException:
                        break

            # A요소의 Top이 B요소의(기준) Bottom 에 N오차 내에 들어갈 때 까지 스크롤
            # arg : "A_locator,B_locator,N,x_start,y_start,x_end,y_end"
            # 사용 예 : 광고 타이틀 요소가 검색 탭 요소의 bottom +- 100 내 들어갈 때 까지 스크롤 (광고 컬렉션을 최상위에 위치)
            if "if_y기준_좌표_스크롤" in arg:
                locator = ProviderLocator(self.driver)
                arg_str = arg["if_y기준_좌표_스크롤"]
                arg_list = arg_str.split(',')

                moving_locator = arg_list[0]
                fixed_locator = arg_list[1]
                threshold = int(arg_list[2])
                x_start, y_start, x_end, y_end = int(arg_list[3]), int(arg_list[4]), int(arg_list[5]), int(arg_list[6])

                moving_locator_method = getattr(ProviderLocator, moving_locator)
                fixed_locator_method = getattr(ProviderLocator, fixed_locator)
                # 얘를 못찾을경우 디버깅이 어려워짐. 핸들러 추가.
                fixed_bounds = timeout_handler(lambda: locator.get_bounds(fixed_locator_method), fixed_locator)
                print(f'고정 로케이터 bounds 정보 : {fixed_bounds}')

                max_scrolls = 10
                scroll_count = 0

                while scroll_count < max_scrolls:
                    try:
                        moving_locator_location = locator.get_location_xy(moving_locator_method)
                        if fixed_bounds[3] + threshold >= moving_locator_location[1] >= fixed_bounds[3] - threshold:
                            break
                        else:
                            scroll_count += 1
                            time.sleep(0.5)
                            ProviderScrollMethod.xy_swipe(self, x_start, y_start, x_end, y_end)
                    except TimeoutException:
                        break
                else:
                    raise TimeoutException(f"{moving_locator}를 못찾아서 케이스종료")
                    
            #
            # if "찾을때까지_오른쪽_스와이프_좌표" in arg:
            #     locator = ProviderLocator(self.driver)
            #     locator_name = arg["찾을때까지_오른쪽_스와이프_좌표"]
            #     locator_method = getattr(ProviderLocator,locator_name)
            #     max_scrolls = 25
            #     scroll_count = 0
            #     while scroll_count < max_scrolls:
            #         try:
            #             locator.is_enabled_quick(locator_method)
            #             break
            #         except TimeoutException:
            #             scroll_count += 1
            #             if scroll_count == 24:
            #                 raise TimeoutException(f"{locator_name} 못찾아서 케이스 종료")
            #             else:
            #                 ProviderScrollMethod.to_right_swipe(self)
            #                 pass

            if "찾을때까지_조금씩_스크롤" in arg:
                locator = ProviderLocator(self.driver)
                locator_name = arg["찾을때까지_조금씩_스크롤"]
                locator_method = getattr(ProviderLocator,locator_name)
                max_scrolls = 35
                scroll_count = 0
                while scroll_count < max_scrolls:
                    try:
                        locator.is_enabled_quick(locator_method)
                        break
                    except TimeoutException:
                        scroll_count += 1
                        ProviderScrollMethod.down_scroll2(self)
                else:
                    raise TimeoutException(f"{locator_name} 못찾아서 케이스 종료")

            #요소가 노출될때까지 기다렸다가 클릭. 최대 60초
            if "노출_기다리고_클릭" in arg:
                locator = ProviderLocator(self.driver)
                locator_name = arg["노출_기다리고_클릭"]
                locator_method = getattr(ProviderLocator,locator_name)

                MAX_WAIT_TIME = 60
                start_time = time.time()
                while time.time() < start_time + MAX_WAIT_TIME:
                    try:
                        locator = ProviderLocator(self.driver)
                        locator_method = getattr(ProviderLocator, arg["노출_기다리고_클릭"])
                        locator.click_quick(locator_method)
                        break
                    except TimeoutException:
                        time.sleep(0.5)
                        continue
                else:
                    raise TimeoutException("60초 대기동안 요소를 찾지못해 fail처리")

            # 요소가 없어야 pass. 요소가 없어야 할때 사용합니다.
            if "요소미노출" in arg:
                locator_method = getattr(ProviderLocator, arg["요소미노출"])
                locator = ProviderLocator(self.driver)
                try:
                    time.sleep(0.5)
                    locator.is_enabled_quick(locator_method)
                    raise TimeoutException(f'요소가 존재해서 fail처리 : {arg["요소미노출"]}')
                except TimeoutException:
                    pass

            if "뒤로가기" in arg:
                try:
                    count = int(arg["뒤로가기"].replace("회", ""))
                    for _ in range(count):
                        time.sleep(0.5)
                        ProviderScrollMethod.back_key(self)
                except ValueError:
                    ProviderScrollMethod.back_key(self)

            if "새로고침" in arg:
                ProviderScrollMethod.pull_to_refresh(self)

            if "앱_재시작" in arg:
                if platform == "aos":
                    AppStart.android_ohou_restart(self, "precondition")
                else:
                    AppStart.ios_ohou_restart(self)

            if "쉬고" in arg:
                time.sleep(int(arg["쉬고"].replace("초", "")))

            if "활성화" in arg:
                enabled_str = arg["활성화"]
                enabled_list = enabled_str.split(',')
                for enabled_result in enabled_list:
                    print(enabled_result, enabled_list)
                    locator_method = getattr(ProviderLocator, enabled_result)
                    time.sleep(0.5)
                    timeout_handler(lambda: locator.is_enabled(locator_method), enabled_result)

            if "광고_제거_클릭" in arg:
                try:
                    time.sleep(2)
                    locator = ProviderLocator(self.driver)
                    locator_method = getattr(ProviderLocator, arg["광고_제거_클릭"])
                    locator.click(locator_method)

                except TimeoutException:
                    print(f"광고 예외처리")

            if "만약" in arg:
                try:
                    locator = ProviderLocator(self.driver)
                    locator_1 = getattr(ProviderLocator, arg["만약"]["활성화"])
                    timeout_handler(lambda: locator.is_enabled_quick(locator_1), arg["만약"]["활성화"])
                    try:
                        locator_2 = getattr(ProviderLocator, arg["만약"]["클릭1"])
                        locator.click(locator_2)
                    except TimeoutException:
                        print("조건 예외처리")
                    except KeyError:
                        pass

                    try:
                        locator_3 = getattr(ProviderLocator, arg["만약"]["클릭2"])
                        locator.click(locator_3)
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

                except TimeoutException:
                    print("조건 예외처리")

            # 클릭 전후로 요소의 이름을 비교하는 키워드 갈을경우 익셉션 발생시킴 => 같으면 이 키워드를 쓸 이유가 없기때문에, 액션에따라 요소이름이 변경될때 활용
            if "클릭_요소_이름_비교" in arg:
                locator_method = getattr(ProviderLocator, arg["클릭_요소_이름_비교"])
                element = arg["클릭_요소_이름_비교"]
                time.sleep(0.5)
                result1 = timeout_handler(lambda: locator.get_name(locator_method), element)
                print(f'클릭_요소_이름_비교 : {result1}')
                time.sleep(0.5)
                timeout_handler(lambda: locator.click(locator_method), element)
                time.sleep(0.5)
                locator_method2 = getattr(ProviderLocator, arg["클릭_요소_이름_비교"])
                result2 = timeout_handler(lambda: locator.get_name(locator_method2), element)
                print(f'클릭_요소_이름_비교 : {result2}')
                if result1 == result2:
                    raise TimeoutException(f'{arg["클릭_요소_이름_비교"]}요소의 {result1}과{result2}의 이름이 같음')
                else:
                    pass
                    # return True

            if "클릭_요소_텍스트_비교" in arg:
                locator_method = getattr(ProviderLocator, arg["클릭_요소_텍스트_비교"])
                element = arg["클릭_요소_텍스트_비교"]

                time.sleep(0.5)
                result1 = timeout_handler(lambda: locator.get_text(locator_method), element)
                print(f'클릭_요소_텍스트_비교 : {result1}')

                time.sleep(0.5)
                timeout_handler(lambda: locator.click(locator_method), element)
                time.sleep(0.5)
                locator_method2 = getattr(ProviderLocator, arg["클릭_요소_텍스트_비교"])

                result2 = timeout_handler(lambda: locator.get_text(locator_method2), element)
                print(f'클릭_요소_텍스트_비교 : {result2}')
                print(result1,result2)
                if result1 == result2:
                    raise TimeoutException(f'{arg["클릭_요소_텍스트_비교"]}요소의 {result1}과{result2}의 텍스트값이 같음')
                else:
                    pass
                    # return True

            if "홈화면_검색" in arg:
                locator = ProviderLocator(self.driver)
                placeholder_text = PlaceholderApi().is_placeholder_text()
                placeholder = ProviderLocator.search_btn(placeholder_text) if re_text == "aos" else ProviderLocator.search_btn

                timeout_handler(lambda: locator.click(placeholder), "search_btn")
                search_text_box = ProviderLocator.search_text_box
                # timeout_handler(lambda: locator.click(search_text_box), "search_text_box")
                time.sleep(1)
                timeout_handler(lambda: locator.send_key(search_text_box,arg["홈화면_검색"]), arg["홈화면_검색"])
                search_vk_btn = ProviderLocator.search_vk_btn
                timeout_handler(lambda: locator.click(search_vk_btn), "search_vk_btn")


            if "쇼핑홈_검색" in arg:
                locator = ProviderLocator(self.driver)
                gnb_shopping_btn = ProviderLocator.gnb_shopping_btn
                timeout_handler(lambda: locator.click(gnb_shopping_btn), "gnb_shopping_btn")
                time.sleep(1)
                placeholder_text = PlaceholderApi().is_placeholder_text_shop_home()
                placeholder = ProviderLocator.search_btn(placeholder_text) if re_text == "aos" else ProviderLocator.shopping_home_search_btn

                timeout_handler(lambda: locator.click(placeholder), "shopping_home_search_btn")
                
                search_text_box = ProviderLocator.search_text_box
                timeout_handler(lambda: locator.click(search_text_box), "search_text_box")
                time.sleep(1)
                timeout_handler(lambda: locator.send_key(search_text_box,arg["쇼핑홈_검색"]), arg["쇼핑홈_검색"])
                search_vk_btn = ProviderLocator.search_vk_btn
                timeout_handler(lambda: locator.click(search_vk_btn), "search_vk_btn")

    def actual_result(self, *args,re_text=None):
        results = []
        for arg in args:
            if "aos" in re_text:
                ProviderLocator = ProviderLocatorAndroid
                binary_result = ResultAndroid()
            else:
                ProviderLocator = ProviderLocatorIos
                binary_result = Result()

            locator = ProviderLocator(self.driver)
            if "미실행" in arg:
                pass

            if "텍스트확인" in arg:
                locator_method = getattr(ProviderLocator, arg["텍스트확인"])
                time.sleep(0.5)
                result = timeout_handler(lambda: locator.get_text(locator_method), arg["텍스트확인"])
                results.append(result)

            if "이름확인" in arg:
                locator_method = getattr(ProviderLocator, arg["이름확인"])
                time.sleep(0.5)
                result = timeout_handler(lambda: locator.get_name(locator_method), arg["이름확인"])
                print(result)
                results.append(result)

            # 리뷰작성 사용한 뒤에 체크하는 용도의 키워드. "금액,플랫폼","+포인트_결과_조회" 형식으로 사용. 포인트가 추가되었을때만 해당 키워드를 사용한다.
            if "+포인트_결과_조회" in arg:
                point_str = arg["+포인트_결과_조회"]
                point_str_list = point_str.split(',')
                point = int(point_str_list[0])
                platform = point_str_list[1]
                if platform == "iOS":
                    id = AccountInfo.ios_account_email2
                    pw = AccountInfo.ios_account_pw
                else:
                    id = AccountInfo.aos_account_email2
                    pw = AccountInfo.aos_account_pw

                code = SignInApi().get_user_id(id,pw)[0]
                if code == 200:
                    result = SignInApi().is_sign_in(id, pw)
                    token = result[0]
                    cookie = result[1]
                    user_id = result[2]
                else:
                    raise TimeoutException ("get_user_id api 200안떨어짐. api 확인필요")
                after_point = PointAPI().get_point(user_id, cookie, token)
                before_point = int(binary_result.read_result_slack(f"{platform}_point"))
                print(f"이전포인트:{before_point},이후포인트:{after_point}")
                results.append(True) if before_point+point == after_point else results.append(False)

            # 바이너리에 저장된 이름을 비교한다. 형식 : "요소명A,요소명B","이름_저장_비교" 같으면 True, 다르면 False // 텍스트_저장 키워드에도 사용가도
            if "이름_저장_비교" in arg:
                time.sleep(1)
                locator = ProviderLocator(self.driver)
                compare_name_str = arg["이름_저장_비교"]
                compare_name_list = compare_name_str.split(',')
                before_name = compare_name_list[0]
                after_name = compare_name_list[1]
                print(f'이름_저장_비교 : {binary_result.read_result_slack(before_name),binary_result.read_result_slack(after_name) }')
                results.append(True) if binary_result.read_result_slack(before_name) == binary_result.read_result_slack(after_name) else results.append(False)

            # 1번요소가 2번요소보다 x좌표가 크다면 True, 작다면 False
            if "x_좌표_비교" in arg:
                time.sleep(1)
                locator = ProviderLocator(self.driver)
                compare_name_str = arg["x_좌표_비교"]
                compare_name_list = compare_name_str.split(',')
                first_location = compare_name_list[0]

                sec_location = compare_name_list[1]
                x_1 = first_location.get
                print(f'이름_저장_비교 : {binary_result.read_result_slack(before_name),binary_result.read_result_slack(after_name) }')
                results.append(True) if binary_result.read_result_slack(before_name) == binary_result.read_result_slack(after_name) else results.append(False)


            if "순서대로_이름_저장_비교" in arg:
                time.sleep(1)
                locator = ProviderLocator(self.driver)
                compare_name_str = arg["순서대로_이름_저장_비교"]
                compare_name_list = compare_name_str.split(',')

                # read_result_slack 값 리스트
                resolved_values = [binary_result.read_result_slack(name) for name in compare_name_list]
                print(f'순서대로_이름_저장_비교 : {resolved_values}')

                # 하나라도 같은 값이 있으면 True
                has_match = any(
                    resolved_values[i] == resolved_values[j]
                    for i in range(len(resolved_values))
                    for j in range(i + 1, len(resolved_values))
                )

                results.append(has_match)

            # checkd True면 True, 아니면 False
            if "체크_활성화" in arg:
                checked_str = arg["체크_활성화"]
                checked_list = checked_str.split(',')

                for checked_result in checked_list:
                    locator_method = getattr(ProviderLocator, checked_result)
                    time.sleep(0.5)
                    result = timeout_handler(lambda: locator.is_checked(locator_method), checked_result)
                    print(checked_result,result)
                    results.append(result)
                return str(all(results))
            
            # selected True면 True, 아니면 False
            if "선택_활성화" in arg:
                selected_str = arg["선택_활성화"]
                selected_list = selected_str.split(',')

                for selected_result in selected_list:
                    locator_method = getattr(ProviderLocator, selected_result)
                    time.sleep(0.5)
                    result = timeout_handler(lambda: locator.is_selected(locator_method), selected_result)
                    print(selected_result,result)
                    results.append(result)
                return str(all(results))
            
            if "노출_활성화" in arg:
                displayed_str = arg["노출_활성화"]
                displayed_list = displayed_str.split(',')

                for displayed_result in displayed_list:
                    locator_method = getattr(ProviderLocator, displayed_result)
                    time.sleep(0.5)
                    result = timeout_handler(lambda: locator.is_displayed(locator_method), displayed_result)
                    print(displayed_result,result)
                    results.append(result)
                return str(all(results))

            if "활성화" in arg:
                enabled_str = arg["활성화"]
                enabled_list = enabled_str.split(',')

                for enabled_result in enabled_list:
                    print(enabled_result,enabled_list)
                    locator_method = getattr(ProviderLocator, enabled_result)
                    time.sleep(0.5)
                    result = timeout_handler(lambda: locator.is_enabled(locator_method), enabled_result)
                    results.append(result)
                return str(all(results))

            # A요소와 B요소의 Y축 위치를 비교한다. A요소가 B보다 위에있다면 True, 밑에있다면 False. 형식은 "A요소,B요소","요소_위치_비교"
            if "요소_위치_비교" in arg:
                locator = ProviderLocator(self.driver)
                xy_str = arg["요소_위치_비교"]
                xy_list = xy_str.split(',')

                a_locator = getattr(ProviderLocator, xy_list[0])
                b_locator = getattr(ProviderLocator, xy_list[0])
                xy1 = locator.get_location_xy(a_locator)
                xy2 = locator.get_location_xy(b_locator)
                y_locator1 = int(xy1[1])
                y_locator2 = int(xy2[1])
                results.append(True) if y_locator1 < y_locator2 else results.append(False)

            # A요소와 B요소의 X축 위치를 비교한다. A요소가 B보다 왼쪽에 있다면 True, 오른쪽에 있다면 False. 형식은 "A요소,B요소","x_요소_위치_비교"
            if "x_요소_위치_비교" in arg:
                locator = ProviderLocator(self.driver)
                xy_str = arg["x_요소_위치_비교"]
                xy_list = xy_str.split(',')

                a_locator = getattr(ProviderLocator, xy_list[0])
                b_locator = getattr(ProviderLocator, xy_list[1])
                xy1 = locator.get_location_xy(a_locator)
                xy2 = locator.get_location_xy(b_locator)
                x_locator1 = int(xy1[0])
                x_locator2 = int(xy2[0])
                results.append(True) if x_locator1 < x_locator2 else results.append(False)

            if "요소_이미지_비교" in arg:
                enabled_str = arg["요소_이미지_비교"]
                enabled_list = enabled_str.split(',')

                compare_img_1 = f'{enabled_list[0]}.png'
                compare_img_2 = f'{enabled_list[1]}.png'

                result = CaptureClass.compare_and_delete_screenshots(self, compare_img_1, compare_img_2)
                #같으면 True, 다르면 False
                results.append(result)

            if "순서대로_요소_이미지_비교" in arg:
                enabled_str = arg["순서대로_요소_이미지_비교"]
                enabled_list = enabled_str.split(',')

                compare_img_1 = f'{enabled_list[0]}.png'
                compare_img_2 = f'{enabled_list[1]}.png'
                compare_img_3 = f'{enabled_list[2]}.png'
                compare_img_4 = f'{enabled_list[3]}.png'
                compare_img_5 = f'{enabled_list[4]}.png'

                result = CaptureClass.multi_compare_and_delete_screenshots(self, compare_img_1, compare_img_2, compare_img_3, compare_img_4, compare_img_5)
                #같으면 True, 다르면 False
                results.append(result)

            if "요소미노출" in arg:
                locator_method = getattr(ProviderLocator, arg["요소미노출"])
                try:
                    time.sleep(0.5)
                    locator.is_enabled_quick(locator_method)
                    results.append(False)
                except TimeoutException:
                    results.append(True)

            if "요소찾기" in arg:
                results.append(ProviderCommonMethod.find_xml_text(self,arg["요소찾기"]))

            # 동적_입력 케이스를 확인하기위한 키워드
            if "동적_요소찾기" in arg:
                results.append(ProviderCommonMethod.find_xml_text(self,arg["동적_요소찾기"]+datetime.today().strftime("%Y-%m-%d")))
            
            if "쉬고" in arg:
                time.sleep(int(arg["쉬고"].replace("초", "")))

            if "순서대로_활성화" in arg:
                locator = ProviderLocator(self.driver)
                enabled_str = arg["순서대로_활성화"]
                enabled_list = enabled_str.split(',')

                # enabled_list = [item.strip() for item in enabled_str.split(',')]

                for enabled_result in enabled_list:
                    print(enabled_result, enabled_list)
                    locator_method = getattr(ProviderLocator, enabled_result)
                    max_scrolls = 10
                    scroll_count = 0

                    while scroll_count < max_scrolls:
                        try:
                            locator.is_enabled_quick(locator_method)
                            result = timeout_handler(lambda: locator.is_enabled(locator_method), enabled_result)
                            # print(f"✅ 활성화됨: {enabled_result}")
                            results.append(result)
                            break
                        except TimeoutException:
                            scroll_count += 1
                            # print(f"⬇️ 스크롤 시도 {scroll_count} / {max_scrolls} - {enabled_result}")
                            time.sleep(0.5)
                            ProviderScrollMethod.down_scroll(self)  
                    else:
                        raise TimeoutException(f"{enabled_result} 못찾아서 케이스 종료")
                    
                # print (f'결과 체크 ✅✅✅✅✅✅✅✅ {results}')
                return str(all(results))

        if len(results) == 1:
            return str(results[0])
        return str(results)

    def verify(self, type, expected, *actual_args,re_text=None):
        actual = Keywords.actual_result(self,*actual_args,re_text=re_text)
        if type == "equal":
            ProviderCommonMethod.assert_equal(self,expected,actual)
        if type == "in":
            ProviderCommonMethod.assert_in(self,expected,actual)
        if type == "list_in":
            ProviderCommonMethod.assert_in_list(self,expected,actual)