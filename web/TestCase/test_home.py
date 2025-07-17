from web.ObjectSetting.comm_service import *
from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.common_object import *
from web.ObjectSetting.home import *
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.web_result_binary import ResultWeb
from web.BasicSetting.exception_func import *

def checkout(page):
    CommonElements.login_func(page)
    page.wait_for_timeout(2000)
    CommPlatformElements.checkout_func(page)
    page.wait_for_timeout(2000)

# @pytest.mark.skip
# def test_home_00001(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_001 : 로그인 확인", end='')
#         PageElements.qaweb_main_url(page)
#         expect(page.get_by_label("오늘의집 로고"), '"오늘의집 로고" 요소 미노출').to_be_visible()
#         print(" - Pass")
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

# @pytest.mark.skip
# def test_home_00002(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_002 : 전체 메뉴 노출 확인", end='')
#         PageElements.qaweb_main_url(page)
#         # CommonElements.login_func(page)
#         # 홈 탭 확인
#         expect(page.get_by_role("link", name="홈", exact=True), '홈 요소 미노출').to_be_visible()
#         # 추천 탭 확인
#         expect(page.get_by_role("link", name="추천"), '추천 요소 미노출').to_be_visible()
#         # #채널 탭 확인
#         expect(page.get_by_role("link", name="#채널"), '#채널 요소 미노출').to_be_visible()
#         # 집들이 탭 확인
#         # expect(page.get_by_role("link", name="집들이"), '집들이 요소 미노출').to_be_visible()
#         # 집사진 탭 확인
#         expect(page.get_by_role("link", name="집사진"), '집사진 요소 미노출').to_be_visible()
#         # 3D인테리어 탭 확인
#         expect(page.get_by_role("link", name="3D인테리어"), '3D인테리어 요소 미노출').to_be_visible()
#         # 살림수납 탭 확인
#         expect(page.get_by_role("link", name="살림수납"), '살림수납 요소 미노출').to_be_visible()
#         # 콜렉터블 탭 확인
#         expect(page.get_by_role("link", name="콜렉터블"), '콜렉터블 요소 미노출').to_be_visible()
#         # 홈스토랑 탭 확인
#         expect(page.get_by_role("link", name="홈스토랑"), '홈스토랑 요소 미노출').to_be_visible()
#         # page.wait_for_timeout(1000)
#         print(" - Pass")
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

# @pytest.mark.skip
# def test_home_00017(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_017 : 배너 상세보기 확인", end='')
#         PageElements.qaweb_main_url(page)
#         # CommonElements.login_func(page)
#         # 최상단 우측 배너 클릭
#         expect(page.locator("div").filter(has_text=re.compile(r"^1/1*")).locator("span").nth(4), '스와이프배너 미노출').to_be_visible()
#         page.get_by_role("button", name="").click()
#         expect(page.locator("div").filter(has_text=re.compile(r"^2/1*")).locator("span").nth(4), '스와이프배너 미노출').to_be_visible()
#         page.wait_for_timeout(2000)
#         print(" - Pass")
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

# @pytest.mark.skip
# def test_home_00018(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_018 : 배너 상세보기 확인", end='')
#         PageElements.qaweb_main_url(page)
#         # CommonElements.login_func(page)
#         with page.expect_popup() as page1_info:
#             page.get_by_label(re.compile(r"1 of 1*")).get_by_role("link").click()
#         page1 = page1_info.value
#         page.wait_for_timeout(2000)
#         expect(page1.get_by_role("link", name="이벤트 홈으로 돌아가기"), '이벤트 상세페이지 미노출').to_be_visible()
#         print(" - Pass")
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

# @pytest.mark.skip
# def test_home_00019(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_019 : 배너 상세보기 확인", end='')
#         PageElements.qaweb_main_url(page)
#         # CommonElements.login_func(page)
#         # 우상단 배너 '+' 클릭
#         # page.locator("div").filter(has_text=re.compile(r"^1/15$")).locator("span").nth(4).click()
#         page.locator("div").filter(has_text=re.compile(r"^1/1*")).locator("span").nth(4).click()
#         # API Response check
#         api_url = 'https://qa-web.dailyhou.se/competitions/feed'
#         response = send_api_get(api_url)
#         assert response.status_code == 200
#         print(" - Pass")
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

# @pytest.mark.skip
# def test_home_00020(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_020 : 임의의 숏컷 확인", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 배너 하단 숏컷 클릭
#         page.get_by_role("link", name="쇼핑").click()
#         expect(page.get_by_role("link", name="쇼핑홈"), '숏컷 컨텐츠 미노출').to_be_visible()
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

# @pytest.mark.skip
# def test_home_00023(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_023 : 스크랩 동작 확인", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 오늘의 스토리 모듈의 스크랩 클릭
#         page.locator("article").nth(0).get_by_role("button").click()
#         expect(page.get_by_text("스크랩했습니다."), '스크랩 on 미동작').to_be_visible()
#         page.wait_for_timeout(1000)
#         # 스크랩 초기화
#         page.locator("article").nth(0).get_by_role("button").click()
#         expect(page.get_by_text("스크랩북에서 삭제했습니다."), '스크랩 off 미동작').to_be_visible()
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


# def test_home_00024(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 오늘의 스토리 첫번째 모듀의 더보기 > 집들이 페이지 노출화인(필터로 체크)
#         print("test_home_024 : 첫번째 모듈 노출 % 더보기 동작 확인", end='')
#         page.locator("div").filter(has_text=re.compile(r"^맞춤 정보 없는 유저 1$")).first.scroll_into_view_if_needed()
#         page.locator("div").filter(has_text=re.compile(r"^맞춤 정보 없는 유저 1더보기$")).get_by_role("button").click()
#         expect(page.get_by_role("button", name="정렬 "), '정렬 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="주거형태 "), '주거형태 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="평수 "), '평수 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="예산 "), '예산 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="가족형태 "), '가족형태 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="스타일 "), '스타일 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="컬러 "), '컬러 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="세부공사 "), '세부공사 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="분야 "), '분야 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="작업자 "), '작업자 필터 비노출됨').to_be_visible()
#         PageElements.qaweb_main_url(page)
#         page.wait_for_timeout(1000)
#         print(" - Pass")

#         # 오늘의 스토리 두번째 모둘의 더보기 > 집들이 페이지 노출화인(필터로 체크)
#         print("test_home_024 : 두번째 모듈 노출 % 더보기 동작 확인", end='')
#         page.locator("div").filter(has_text=re.compile(r"^모두 노출 1$")).first.scroll_into_view_if_needed()
#         page.locator("div").filter(has_text=re.compile(r"^모두 노출 1더보기$")).get_by_role("button").click()
#         expect(page.get_by_role("button", name="정렬 "), '정렬 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="주거형태 "), '주거형태 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="평수 "), '평수 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="예산 "), '예산 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="가족형태 "), '가족형태 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="스타일 "), '스타일 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="컬러 "), '컬러 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="세부공사 "), '세부공사 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="분야 "), '분야 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="작업자 "), '작업자 필터 비노출됨').to_be_visible()
#         PageElements.qaweb_main_url(page)
#         page.wait_for_timeout(1000)
#         print(" - Pass")

#         # 오늘의 스토리 세번째 모둘의 더보기 > 집들이 페이지 노출화인(필터로 체크)
#         print("test_home_024 : 세번째 모듈 노출 % 더보기 동작 확인", end='')
#         page.locator("div").filter(has_text=re.compile(r"^모두 노출 2$")).first.scroll_into_view_if_needed()
#         page.locator("div").filter(has_text=re.compile(r"^모두 노출 2더보기$")).get_by_role("button").click()
#         expect(page.get_by_role("button", name="정렬 "), '정렬 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="주거형태 "), '주거형태 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="평수 "), '평수 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="예산 "), '예산 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="가족형태 "), '가족형태 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="스타일 "), '스타일 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="컬러 "), '컬러 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="세부공사 "), '세부공사 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="분야 "), '분야 필터 비노출됨').to_be_visible()
#         expect(page.get_by_role("button", name="작업자 "), '작업자 필터 비노출됨').to_be_visible()
#         PageElements.qaweb_main_url(page)
#         page.wait_for_timeout(1000)
#         print(" - Pass")

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

# @pytest.mark.skip
# def test_home_00024(page, login_out):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     print("test_home_024 : 첫번째 모듈 노출 % 더보기 동작 확인", end='')
#     PageElements.qaweb_main_url(page)
#     web_exceptions_handler(page, current_function_name, 
#                            step=lambda: HomeElements.check_moreview_module(page),
#                            check=True)



# def test_home_00035(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("\ntest_home_035 : 오늘의 스토리 스크랩 클릭", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 오늘의 스토리 스크랩 클릭 > 스크랩 On 확인
#         page.get_by_text("맞춤 정보 없는 유저 1").scroll_into_view_if_needed()
#         page.locator("div").filter(has_text=re.compile(r"^맞춤 정보 없는 유저 1더보기231무채색에 진심! 싱글 5\.5평 원룸 인테리어!ttw전문가유저 반셀프일반유저 셀프TEST$")).get_by_label("scrap 토글 버튼").first.click()
#         expect(page.locator("div").filter(has_text=re.compile(r"^맞춤 정보 없는 유저 1더보기231무채색에 진심! 싱글 5\.5평 원룸 인테리어!ttw전문가유저 반셀프일반유저 셀프TEST$"))).to_be_enabled()
        
#         # 폴더에 담기 > 새로운 폴더 추가 > 폴더명 1 > 완료
#         page.get_by_role("button", name="폴더에 담기").click()
#         page.get_by_role("button", name=" 새로운 폴더 추가하기").click()
#         page.get_by_placeholder("폴더명을 입력하세요").click()
#         page.get_by_placeholder("폴더명을 입력하세요").fill("1")
#         page.get_by_role("button", name="완료").click()
#         page.once("dialog", lambda dialog: dialog.accept())
#         expect(page.get_by_text("'1'폴더로 이동했습니다."))

                
#         # 스크랩북 보기> 스크랩한 콘텐츠 상세 진입 > 제목 확인
#         page.wait_for_timeout(1000) # 페이지 로딩 속도 때문에 딜레이 넣지 않으면 Fail 뜸
#         page.get_by_role("button", name="스크랩북 보기").click()
#         expect(page.get_by_text("스크랩북1설정공유하기")).to_be_visible()
#         page.get_by_role("link", name="집들이", exact=True).click()
#         page.wait_for_timeout(5000) # 페이지 로딩 속도 때문에 딜레이 넣지 않으면 Fail 뜸
#         expect(page.get_by_text("무채색에 진심! 싱글 5.5평 원룸 인테리어!"), "제목이 일치 하지 않습니다.").to_be_visible()

#         # 홈 이동 > 스크랩 해제한 콘텐츠 스크랩 disable 확인
#         page.get_by_role("link", name="홈", exact=True).click()
#         expect(page.locator("div").filter(has_text=re.compile(r"^맞춤 정보 없는 유저 1더보기231무채색에 진심! 싱글 5\.5평 원룸 인테리어!ttw전문가유저 반셀프일반유저 셀프TEST$"))).to_be_enabled()
#         page.locator("div").filter(has_text=re.compile(r"^맞춤 정보 없는 유저 1더보기231무채색에 진심! 싱글 5\.5평 원룸 인테리어!ttw전문가유저 반셀프일반유저 셀프TEST$")).get_by_label("scrap 토글 버튼").first.click()
#         expect(page.get_by_text("스크랩북에서 삭제했습니다.")).to_be_visible()
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

# @pytest.mark.skip
# def test_home_00035(page, login_out):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     print("\ntest_home_035 : 오늘의 스토리 스크랩 클릭", end='')
#     PageElements.qaweb_main_url(page)
#     web_exceptions_handler(page, current_function_name, 
#                            step=lambda: HomeElements.check_today_scrap(page),
#                            check=True)
    

# @pytest.mark.skip
# def test_home_00041(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_041 : 카테고리별 상품찾기 확인", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 카테고리별 상품찾기 구좌 확인
#         page.get_by_text("카테고리별 상품 찾기").scroll_into_view_if_needed()
#         expect(page.get_by_role("link", name="가구", exact=True), '오늘의 스토리 콘텐츠 미노출').to_be_visible()
#         expect(page.get_by_role("link", name="패브릭"), '오늘의 스토리 콘텐츠 미노출').to_be_visible()
#         expect(page.get_by_role("link", name="장식/소품"), '오늘의 스토리 콘텐츠 미노출').to_be_visible()
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

# @pytest.mark.skip
# def test_home_00042(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_042 : 오늘의딜 구좌 확인", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 오늘의딜 컨텐츠 클릭
#         page.locator("strong").filter(has_text="오늘의딜").scroll_into_view_if_needed()
#         expect(page.get_by_role('article').nth(0), '오늘의 스토리 콘텐츠 미노출').to_be_visible()
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

# @pytest.mark.skip
# def test_home_00049(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_049 : 이런 사진 찾고 있나요 구좌 확인", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 이런 사진 찾고 있나요 컨텐츠 클릭
#         page.get_by_text("이런 사진 찾고 있나요?").scroll_into_view_if_needed()
#         page.get_by_text("이런 사진 찾고 있나요?").click()
#         page.locator("#card-collection-item-6726113").get_by_role("link").first.click()
#         expect(page.get_by_text("조회"), '"이런 사진 찾고있나요" 콘텐츠 미노출').to_be_visible()
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

@pytest.mark.regression
def test_home_00017(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    try:
        print("test_home_053 : 유저들의 인테리어 시공리뷰 확인", end='')
        PageElements.qaweb_main_url(page)
        # CommonElements.login_func(page)
        # 유저들의 인테리어 시공 리뷰 클릭
        page.get_by_text("유저들의 인테리어 시공 리뷰").scroll_into_view_if_needed()
        page.get_by_text("유저들의 인테리어 시공 리뷰").click()
        expect(page.get_by_role("heading", name="오늘 올라온 인테리어 리뷰"), '인테리어 시공리뷰 페이지 미노출').to_be_visible()
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

# @pytest.mark.skip
# def test_home_00054(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_054 : 유저들의 인테리어 시공리뷰 상세확인", end='')
#         PageElements.qaweb_main_url(page)
#         # CommonElements.login_func(page)
#         # 유저들의 인테리어 시공 리뷰 클릭
#         page.get_by_text("유저들의 인테리어 시공 리뷰").scroll_into_view_if_needed()
#         page.get_by_text("유저들의 인테리어 시공 리뷰").click()
#         expect(page.get_by_role("heading", name="오늘 올라온 인테리어 리뷰"), '인테리어 시공리뷰 페이지 미노출').to_be_visible()
#         # 주거공간 시공 클릭
#         page.get_by_role("button", name="HOT 주거시공").click()
#         # 웰컴 팝업 종료
#         page.get_by_role("button", name="분쟁 걱정없이 시공하는 법").click()
#         page.get_by_role("button", name="책임보장 업체 보기").click()
#         page.wait_for_timeout(2000)
#         # 첫번째 리뷰 컨텐츠 클릭
#         page.get_by_role('article').nth(2).click()
#         expect(page.get_by_role("button", name="상담신청"), '인테리어 시공리뷰 상세 페이지 미노출').to_be_visible()
#         page.wait_for_timeout(2000)
#         print(" - Pass")
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

# @pytest.mark.skip
# def test_home_00055(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_055 : 시공리뷰 더보기 동작 확인", end='')
#         PageElements.qaweb_main_url(page)
#         # 유저들의 인테리어 시공 리뷰 클릭
#         page.get_by_text("유저들의 인테리어 시공 리뷰").scroll_into_view_if_needed()
#         page.locator("div").filter(has_text=re.compile(r"^유저들의 인테리어 시공 리뷰더보기$")).get_by_role("button").click()
#         expect(page.get_by_role("heading", name="오늘 올라온 인테리어 리뷰"), '인테리어 시공리뷰 페이지 미노출').to_be_visible()
#         print(" - Pass")
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

# @pytest.mark.skip
# def test_home_00056(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_056 : 오늘의 기획전 상세 확인", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 오늘의 기획전 클릭
#         page.get_by_text("오늘의 기획전").scroll_into_view_if_needed()
#         page.get_by_text("오늘의 기획전").click()
#         # 기획전 노출 확인
#         # expect(page.get_by_role("link", name="상단 상품 테스트"), '오늘의 기획전 페이지 미노출').to_be_visible()
#         # API Response check
#         api_url = 'https://store.qa-web.dailyhou.se/exhibitions'
#         response = send_api_get(api_url)
#         assert response.status_code == 200
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

# @pytest.mark.skip
# def test_home_00057(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_057 : 기획전 피드 이동 확인", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 오늘의 기획전 더보기 클릭
#         page.get_by_text("오늘의 기획전").scroll_into_view_if_needed()
#         page.locator("div").filter(has_text=re.compile(r"^오늘의 기획전더보기$")).get_by_role("button").click()
#         # API Response check
#         api_url = 'https://store.qa-web.dailyhou.se/exhibitions'
#         response = send_api_get(api_url)
#         assert response.status_code == 200
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

# @pytest.mark.skip
# def test_home_00058(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_058 : 베스트 모듈 확인", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 베스트 클릭
#         page.get_by_text("베스트").scroll_into_view_if_needed()
#         page.get_by_text("베스트").click()
#         # 베스트 페이지 노출 확인
#         expect(page.get_by_role("button", name="실시간 베스트"), '베스트 페이지 미노출').to_be_visible()
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

# @pytest.mark.skip
# def test_home_00059(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_home_059 : 베스트 상품상세 진입 확인", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 베스트 클릭
#         page.get_by_text("베스트").scroll_into_view_if_needed()
#         page.get_by_text("베스트").click()
#         page.get_by_role('article').nth(0).click()
#         # 베스트 페이지 노출 확인
#         expect(page.get_by_text("주문금액").first, '상품상세 페이지 미노출').to_be_visible()
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

@pytest.mark.regression
def test_home_00024(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_home_60 : 베스트 탭 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: HomeElements.into_best_module(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_home_00025(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_home_061 : 역대베스트 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: HomeElements.into_bestrank_module(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_home_00029(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_home_086 : 하단푸터 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: HomeElements.into_footer(page),
                           check=True)

@pytest.mark.regression
def test_home_00031(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_home_087 : 이메일문의하기", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: HomeElements.check_email_qna(page),
                           check=True)
    
@pytest.mark.regression
def test_home_00034(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_home_090 : 하단 푸터 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: HomeElements.check_footer(page),
                           check=True)
    



