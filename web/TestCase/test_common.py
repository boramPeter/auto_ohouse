from web.ObjectSetting.comm_service import *
from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.common_object import *
from web.ObjectSetting.gmail import *
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.web_result_binary import ResultWeb
from web.BasicSetting.exception_func import *

def checkout(page):
    CommonElements.login_func(page)
    page.wait_for_timeout(2000)
    CommPlatformElements.checkout_func(page)
    page.wait_for_timeout(2000)

'''
# 캡챠이슈
def test_common_00005(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    try:
        print("test_common_005 : 카카오톡 회원가입 확인", end='')
        PageElements.qaweb_main_url(page)
        page.get_by_role("link", name="회원가입").click()
        with page.expect_popup() as page1_info:
            page.get_by_role("link", name="카카오톡으로 가입하기").click()
        page1 = page1_info.value
        expect(page.get_by_label("프로필 메뉴"), '프로필 메뉴 요소 미노출').to_be_visible()
        print(" - Pass")
        ResultWeb().write_result(current_function_name, f'*Pass*')
    except AssertionError as e:
        print(" - Fail", end='')
        print(f"\nCaught an AssertionError: {e}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
    except TimeoutError as e1:
        print(" - Fail", end='')
        print(f"\nCaught an TimeoutError: {e1}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
    except Exception as e2:
        print(" - Fail", end='')
        print(f"\nCaught an unknown error: {e2}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')

def test_common_00006(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    try:
        print("test_common_006 : 카카오계정 로그아웃 확인", end='')
        PageElements.qaweb_main_url(page)
        CommonElements.logout_func(page)
        page.get_by_role("link", name="로그인").click()
        page.locator("section").filter(has_text="SNS계정으로 간편 로그인/회원가입").get_by_role("link").nth(2).click()
        expect(page.get_by_label("프로필 메뉴"), '프로필 메뉴 요소 미노출').to_be_visible()
        print(" - Pass")
        ResultWeb().write_result(current_function_name, f'*Pass*')
    except AssertionError as e:
        print(" - Fail", end='')
        print(f"\nCaught an AssertionError: {e}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
    except TimeoutError as e1:
        print(" - Fail", end='')
        print(f"\nCaught an TimeoutError: {e1}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
    except Exception as e2:
        print(" - Fail", end='')
        print(f"\nCaught an unknown error: {e2}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')

def test_common_00007(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    try:
        print("test_common_007 : 카톡 로그인 확인", end='')
        PageElements.qaweb_main_url(page)
        CommonElements.logout_func(page)
        expect(page.get_by_label("프로필 메뉴"), '프로필 메뉴 요소 미노출').to_be_visible()
        print(" - Pass")
        ResultWeb().write_result(current_function_name, f'*Pass*')
    except AssertionError as e:
        print(" - Fail", end='')
        print(f"\nCaught an AssertionError: {e}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
    except TimeoutError as e1:
        print(" - Fail", end='')
        print(f"\nCaught an TimeoutError: {e1}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
    except Exception as e2:
        print(" - Fail", end='')
        print(f"\nCaught an unknown error: {e2}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')

def test_common_00008(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    try:
        print("test_common_008 : 카카오톡 탈퇴 확인", end='')
        PageElements.qaweb_main_url(page)
        CommonElements.logout_func(page)
        expect(page.get_by_label("프로필 메뉴"), '프로필 메뉴 요소 미노출').to_be_visible()
        print(" - Pass")
        ResultWeb().write_result(current_function_name, f'*Pass*')
    except AssertionError as e:
        print(" - Fail", end='')
        print(f"\nCaught an AssertionError: {e}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
    except TimeoutError as e1:
        print(" - Fail", end='')
        print(f"\nCaught an TimeoutError: {e1}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
    except Exception as e2:
        print(" - Fail", end='')
        print(f"\nCaught an unknown error: {e2}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')
'''

@pytest.mark.smoke
def test_common_00012(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_common_012 : 네이버 로그아웃 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.confirm_naver_logout(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_common_00013(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_common_013 : 네이버 로그인 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.confirm_naver_logout(page),
                           check=True)
    print(" - Pass")

@pytest.mark.skip
def test_common_00016(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_common_016 : 페이스북 로그아웃 확인", end='')
    PageElements.qaweb_main_url(page)
    CommonElements.confirm_cookie_delete(page)
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.logout_facebook_func(page),
                           check=True)
    print(" - Pass")

@pytest.mark.skip
def test_common_00017(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_common_017 : 페이스북 로그인 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.login_facebook_func(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_common_00034(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_common_030 : 이메일 로그아웃 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.logout_func(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_common_00035(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_common_031 : 이메일 로그인 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.login_func(page),
                           check=True)
    print(" - Pass")


# @pytest.mark.skip
# # 캡챠로 인한 케이스 제외
# def test_common_00032(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_common_032 : 이메일 탈퇴 확인", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func_2(page)
#         page.get_by_label("프로필 메뉴").click()
#         page.get_by_role("link", name="마이페이지").click()
#         page.locator("li").filter(has_text="설정").get_by_role("link").click()
#         page.get_by_role("button", name="탈퇴하기").click()
#         page.get_by_label("위 내용을 모두 확인하였습니다. 필수").check()
#         page.get_by_label("기타").check()
#         page.get_by_role("button", name="탈퇴신청").click()
#         # 회원가입 (원복)
#         page.get_by_role("link", name="회원가입").click()
#         page.get_by_placeholder("이메일").click()
#         page.get_by_placeholder("이메일").fill("")
#         page.get_by_placeholder("이메일").press("CapsLock")
#         page.get_by_placeholder("이메일").fill("ohouseqaqa")
#         page.get_by_label("선택해주세요naver.comhanmail.netdaum.netgmail.comnate.comhotmail.comoutlook.comicloud.com직접입력이메일 도메인 선택하기").select_option("gmail.com")
#         page.locator("section").click()
#         page.get_by_role("button", name="이메일 인증하기").click()
#         # Gmail 인증
#         auth_number = GmailWebManager().get_gmail_auth_number()
#         page.get_by_placeholder("인증코드 6자리").click()
#         page.get_by_placeholder("인증코드 6자리").fill(auth_number)
#         page.get_by_role("button", name="확인").click()
#         page.wait_for_timeout(2000)
#         page.get_by_placeholder("비밀번호", exact=True).click()
#         page.get_by_placeholder("비밀번호", exact=True).fill("Wkehdghk12!@")
#         page.get_by_placeholder("비밀번호 확인").click()
#         page.get_by_placeholder("비밀번호 확인").fill("Wkehdghk12!@")
#         page.get_by_placeholder("별명 (2~20자)").click()
#         page.get_by_placeholder("별명 (2~20자)").fill("webqa2")
#         page.get_by_label("전체동의 선택항목에 대한 동의 포함").check()
#         expect(page.get_by_label("프로필 메뉴"), '프로필 메뉴 요소 미노출').to_be_visible()
#         print(" - Pass")
#         CommonElements.logout_func(page)
#         ResultWeb().write_result(current_function_name, f'*Pass*')
#     except AssertionError as e:
#         print(" - Fail", end='')
#         print(f"\nCaught an AssertionError: {e}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
#     except TimeoutError as e1:
#         print(" - Fail", end='')
#         print(f"\nCaught an TimeoutError: {e1}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
#     except Exception as e2:
#         print(" - Fail", end='')
#         print(f"\nCaught an unknown error: {e2}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')

@pytest.mark.skip
def test_common_00042(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_common _042 : 비회원 주문 조회하기 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.confirm_guest_order(page),
                           check=True)

@pytest.mark.skip
def test_common_00047(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_common _045 : 3D 인테리어 피드 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.confirm_3d_interior(page),
                           check=True)
    print(" - Pass")
    
@pytest.mark.regression
def test_common_00050(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_common _050 : 이벤트 상세 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.confirm_event_detail(page),
                           check=True)


@pytest.mark.smoke
def test_common_00168(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_common_168 : 마이페이지 - 사진/동영상 올리기 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.change_profile(page),
                           check=True)
    print(" - Pass")

# @pytest.mark.test
# def test_common_00062(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try: 
#         print("\ntest_common_062 : 마이페이지 - 사진/동영상 올리기 확인", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 마이페이지 > 사진올리기
#         page.get_by_label("프로필 메뉴").click()
#         page.get_by_role("link", name="마이페이지").click()
#         page.wait_for_timeout(3000)
#         # page.locator("div").filter(has_text=re.compile(r"^설정.*")).get_by_role("link").click()
#         page.locator("li").filter(has_text="설정").get_by_role("link").click()
#         # page.get_by_role("img", name="프로필 이미지").click()
#         page.wait_for_timeout(3000)
#         file_input = page.locator('input[type="file"]')
#         file_path = './test_file/testlogo.png'
#         page.wait_for_timeout(3000)
#         file_input.set_input_files(file_path)
#         page.wait_for_timeout(3000)
#         print(" - Pass")
#         page.wait_for_timeout(3000)
#         CommonElements.logout_func(page)
#         ResultWeb().write_result(current_function_name, f'*Pass*')
#     except AssertionError as e:
#         print(" - Fail", end='')
#         print(f"\nCaught an AssertionError: {e}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
#     except TimeoutError as e1:
#         print(" - Fail", end='')
#         print(f"\nCaught an TimeoutError: {e1}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
#     except Exception as e2:
#         print(" - Fail", end='')
#         print(f"\nCaught an unknown error: {e2}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')

@pytest.mark.smoke
def test_common_00079(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_common_079 : 마이페이지 - 코드 입력형 쿠폰 등록 확인", end='')
    PageElements.qaweb_product_url_2(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.confirm_code_coupon(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_common_00190(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_common_190 : 마이페이지 - 포인트 상세 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.confirm_point_detail(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_common_00220(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_common_220 : 마이페이지 - 로그아웃 동작 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.confirm_mypage_logout(page),
                           check=True)
    print(" - Pass")
    


@pytest.mark.regression
def test_common_00120(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    try:
        print("test_common_120 : 알림 페이지 이동 동작 확인", end='')
        PageElements.qaweb_main_url(page)
        CommonElements.login_func(page)
        # 알리 페이지 이동
        page.get_by_label("내소식 페이지 링크 버튼").click()
        expect(page.get_by_role("heading", name="내 소식"), '알림 페이지 미노출').to_be_visible()
        expect(page.locator(".css-1s9ngpy").first, '알림 목록 아이콘 미노출').to_be_visible()
        print(" - Pass")
        ResultWeb().write_result(current_function_name, f'*Pass*')
    except AssertionError as e:
        print(" - Fail", end='')
        print(f"\nCaught an AssertionError: {e}")
        capture_screenshot(page, current_function_name)
        ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
    except TimeoutError as e1:
        print(" - Fail", end='')
        print(f"\nCaught an TimeoutError: {e1}")
        capture_screenshot(page, current_function_name)
        ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
    except Exception as e2:
        print(" - Fail", end='')
        print(f"\nCaught an unknown error: {e2}")
        capture_screenshot(page, current_function_name)
        ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')


@pytest.mark.smoke
def test_common_00300(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_main_url(page)
    # 로그인 
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.login_func(page))
    # 마이페이지 > 설정 진입
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.into_mypage_option(page))
    # 이메일 변경하기 + Gmail 인증
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.change_email(page, account="change"))
    # 로그아웃
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.logout_func(page))
    # 변경한 메일로 로그인 
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.login_func_2(page))
    # 마이페이지 > 설정 진입
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.into_mypage_option(page))
    # # 변경한 메일 다시 default 로 복구
    # web_exceptions_handler(page, current_function_name,
    #                        step=lambda: CommonElements.change_email(page, account="default"),
    #                        opt_check=lambda: CommonElements.logout_func(page),
    #                        check=True)
    
    # 변경한 메일 다시 default 로 복구
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.change_email(page, account="default"),
                           check=True)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.change_email_check(page),
                           check=True)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.logout_func(page),
                           check=True)
    


@pytest.mark.skip
def test_common_00999(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_main_url(page)
    # 로그인 
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.login_func(page))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.change_email_check(page),
                           check=True)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.logout_func(page))





@pytest.mark.regression
def test_common_00303(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    try: 
        print("\ntest_common_182 : 마이페이지 - 설정 페이지 확인", end='')
        PageElements.qaweb_main_url(page)
        CommonElements.login_func(page)
        # 마이페이지 > 설정 진입 및 확인
        CommonElements.into_mypage_option(page)
        # 생년월일 영역 이동 및 값 변경 진행
        print("\ntest_common_182 : 생년월일 값 변경 동작 확인", end='')
        page.get_by_text("생년월일").scroll_into_view_if_needed()
        # 돌아가게는 만들었으나 정상적인 흐름은 아니고 if/else로 to have_value 처럼 필드안의 값을 체크하고 일치여부에 따라 분기처리 할 수 있도록 개선이 필요함.
        try: 
            expect(page.get_by_placeholder("생년월일을 선택해주세요."), "생년월일 기존값 확인 불가.").to_have_value("1990-01-01")
            page.get_by_placeholder("생년월일을 선택해주세요.").click()
            page.get_by_label("1월 2일").click()
            expect(page.get_by_placeholder("생년월일을 선택해주세요."),"생년월일 내용 확인 불가 1월 1일").to_have_value("1990-01-02")
            page.get_by_role("button", name="탈퇴하기").scroll_into_view_if_needed()
            page.get_by_role("button", name="완료").click()
            page.wait_for_timeout(2000)
            print(" - Pass")
        except Exception as e:
            page.get_by_placeholder("생년월일을 선택해주세요.").click()
            page.get_by_label("1월 1일").click()
            expect(page.get_by_placeholder("생년월일을 선택해주세요."),"생년원일 내용 확인 불가 1월2일").to_have_value("1990-01-01")
            page.get_by_role("button", name="탈퇴하기").scroll_into_view_if_needed()
            page.get_by_role("button", name="완료").click()
            page.wait_for_timeout(2000)
            print(" - Pass")
            
        ResultWeb().write_result(current_function_name, f'*Pass*')
    except AssertionError as e:
        print(" - Fail", end='')
        print(f"\nCaught an AssertionError: {e}")
        capture_screenshot(page, current_function_name)
        ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
    except TimeoutError as e1:
        print(" - Fail", end='')
        print(f"\nCaught an TimeoutError: {e1}")
        capture_screenshot(page, current_function_name)
        ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
    except Exception as e2:
        print(" - Fail", end='')
        print(f"\nCaught an unknown error: {e2}")
        capture_screenshot(page, current_function_name)
        ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')

@pytest.mark.regression
def test_common_00304(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    try: 
        print("\ntest_common_304 : 마이페이지 - 설정 페이지 확인", end='')
        PageElements.qaweb_main_url(page)
        CommonElements.login_func(page)
        # 마이페이지 > 설정 진입 및 확인
        CommonElements.into_mypage_option(page)
        # 성별 영역 이동 및 남성으로  값 변경 진행
        print("\ntest_common_304 : 성별 초기값 확인", end='')
        page.get_by_text("성별").scroll_into_view_if_needed()
        expect(page.locator("label").filter(has_text="선택하지 않음"), '초기값(선택하지않음) 미선택됨').to_be_checked()
        expect(page.locator("label").filter(has_text="남성"), '초기값(선택하지않음) 남성이 선택됨').not_to_be_checked()
        expect(page.locator("label").filter(has_text="여성"), '초기값(선택하지않음) 여성이 선택됨').not_to_be_checked()
        print(" - Pass")
        
        print("\ntest_common_304 : 성별 변경 동작 확인| 선택하지 않음 > 남성", end='')
        page.locator("label").filter(has_text="남성").click()
        expect(page.locator("label").filter(has_text="선택하지 않음"), '남성을 체크 했으나 값 변경 되지 않음').not_to_be_checked()
        expect(page.locator("label").filter(has_text="남성"), '남성이 선택되지 않음').to_be_checked()
        expect(page.locator("label").filter(has_text="여성"), '남성을 체크 했으나 여성이 선택됨').not_to_be_checked()
        page.get_by_role("button", name="탈퇴하기").scroll_into_view_if_needed()
        page.get_by_role("button", name="완료").click()
        page.wait_for_timeout(1000)
        CommonElements.into_mypage_option(page)
        # 성별 영역 이동 및 여성으로  값 변경 진행
        print("\ntest_common_304 : 성별 초기값 확인", end='')
        page.get_by_text("성별").scroll_into_view_if_needed()
        expect(page.locator("label").filter(has_text="선택하지 않음"), '초기값(선택하지않음) 으로 값이 되돌아감').not_to_be_checked()
        expect(page.locator("label").filter(has_text="남성"), '남성으로 값 미변경됨').to_be_checked()
        expect(page.locator("label").filter(has_text="여성"), '여성으로 값 잘못 변경됨').not_to_be_checked()
        print(" - Pass")
        
        print("\ntest_common_304 : 성별 변경 동작 확인| 남성>여성", end='')
        page.locator("label").filter(has_text="여성").click()
        expect(page.locator("label").filter(has_text="선택하지 않음"), '여성을 체크 했으나 선택하지 않음이 선택됨').not_to_be_checked()
        expect(page.locator("label").filter(has_text="남성"), '여성을 선택했으니 남성이 선택됨').not_to_be_checked()
        expect(page.locator("label").filter(has_text="여성"), '여성을 선택했으나 적용 되지 않음').to_be_checked()
        page.get_by_role("button", name="탈퇴하기").scroll_into_view_if_needed()
        page.get_by_role("button", name="완료").click()
        page.wait_for_timeout(1000)
        CommonElements.into_mypage_option(page)
        # 성별 영역 이동 및 선택하지 않음으로  값 변경 진행
        print("\ntest_common_304 : 성별 초기값 확인", end='')
        page.get_by_text("성별").scroll_into_view_if_needed()
        expect(page.locator("label").filter(has_text="선택하지 않음"), '이전값(남성) 으로 값이 되돌아감').not_to_be_checked()
        expect(page.locator("label").filter(has_text="남성"), '선택하지 않음 값 미변경되고 남성으로 변경됨').not_to_be_checked()
        expect(page.locator("label").filter(has_text="여성"), '이전값(여성) 으로 값이 되돌아감').to_be_checked()
        print(" - Pass")
        
        print("\ntest_common_304 : 성별 변경 동작 확인| 여성 > 선택하지 않음", end='')
        page.locator("label").filter(has_text="선택하지 않음").click()
        expect(page.locator("label").filter(has_text="선택하지 않음"), '선택하지 않음을 선택 했으나 적용되지 않음').to_be_checked()
        expect(page.locator("label").filter(has_text="남성"), '선택하지않음을 선택했으니 남성이 선택됨').not_to_be_checked()
        expect(page.locator("label").filter(has_text="여성"), '선택하지 않음을 선택했으나 적용 되지 않음').not_to_be_checked()
        page.get_by_role("button", name="탈퇴하기").scroll_into_view_if_needed()
        page.get_by_role("button", name="완료").click()
        page.wait_for_timeout(1000)
        CommonElements.into_mypage_option(page)
        # 성별 영역 이동 변경값 확인
        print("\ntest_common_304 : 성별 초기값 확인", end='')
        page.get_by_text("성별").scroll_into_view_if_needed()
        expect(page.locator("label").filter(has_text="선택하지 않음"), '초기값(선택하지않음) 미선택됨').to_be_checked()
        expect(page.locator("label").filter(has_text="남성"), '초기값(선택하지않음) 남성이 선택됨').not_to_be_checked()
        expect(page.locator("label").filter(has_text="여성"), '초기값(선택하지않음) 여성이 선택됨').not_to_be_checked()
        print(" - Pass")

        ResultWeb().write_result(current_function_name, f'*Pass*')
    except AssertionError as e:
        print(" - Fail", end='')
        print(f"\nCaught an AssertionError: {e}")
        capture_screenshot(page, current_function_name)
        ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
    except TimeoutError as e1:
        print(" - Fail", end='')
        print(f"\nCaught an TimeoutError: {e1}")
        capture_screenshot(page, current_function_name)
        ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
    except Exception as e2:
        print(" - Fail", end='')
        print(f"\nCaught an unknown error: {e2}")
        capture_screenshot(page, current_function_name)
        ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')
