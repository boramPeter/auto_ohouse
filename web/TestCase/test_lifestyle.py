from web.ObjectSetting.comm_service import *
from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.common_object import *
from web.ObjectSetting.lifestyle import *
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.web_result_binary import ResultWeb
from web.BasicSetting.exception_func import *
qa_home = 'https://qa-web.dailyhou.se/'
qa_recommend = 'https://contents.qa-web.dailyhou.se/topics/recommend'

@pytest.mark.skip
def test_lifestyle_00003(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 추천 탭 진입 > 모달창 노출 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_recommend_tab(modal_check=True),
                           check=True)

@pytest.mark.skip
def test_lifestyle_00013(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 추천 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_recommend_tab())
    # 테스트용 콘텐츠 확인
    web_exceptions_handler(page, current_function_name,
                           step=lambda: expect(page.locator("span").filter(has_text=re.compile(r"테스트자동화용 자동화용 콘텐츠로.*")).get_by_role("link").first, '상세 페이지 미노출').to_be_visible(),
                           check=True)

@pytest.mark.skip
def test_lifestyle_00014(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 추천 페이지 API Response check
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_recommend_tab())
    # #채널 페이지 API Response check
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_channel_tab())
    # 집들이
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_project_tab())
    # 집사진
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 3D인테리어
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_3d_tab())
    # 살림수납
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_topic_tab())
    # 이벤트
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_competitions_tab(),
                           check=True)

@pytest.mark.skip
def test_lifestyle_00020(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 추천 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_recommend_tab())
    # 추천 칩 5개인지 체크
    web_exceptions_handler(page, current_function_name,
                           step=lambda: LifestyleElements.check_recommend_chip(page),
                           check=True)

@pytest.mark.skip
def test_lifestyle_00021(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 추천 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_recommend_tab())
    # 2번째 키워드 칩 선택
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.click_recommend_chip(page),
                           opt_check=lambda: LifestyleElements.click_recommend_chip(page),
                           check=True)




    

@pytest.mark.smoke
def test_lifestyle_00051(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 추천 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_recommend_tab())
    # 동영상 콘텐츠 클릭
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.click_recommend_video(page))
    
    # 동영상 노출 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.enter_recommend_video(page),
                           check=True)

@pytest.mark.regression
def test_lifestyle_00149(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집사진
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 집사진 피드 4grid 노출 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_house_tab_4grid(page),
                           check=True)

@pytest.mark.smoke
def test_lifestyle_00150(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 사진 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 임의의 컨텐츠 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: page.locator(".card-collection-item__content__link").first.click())
    page.go_back()
    page.wait_for_timeout(1000)
    # 뒤로가기 후 집사진 탭 유지확인(정렬버튼 노출여부로 validation)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: expect(page.get_by_role("button", name="정렬"), '정렬 버튼 미노출').to_be_visible(),
                           check=True)


@pytest.mark.skip
def test_lifestyle_00213(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 채널 탭 노출 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: expect(page.get_by_role("link", name="#채널"), '채널 탭 미노출').to_be_visible(),
                           check=True)

@pytest.mark.skip
def test_lifestyle_00214(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 채널 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_channel_tab())
    # 채널 탭 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: expect(page.get_by_text("마음에 드는 채널을 골라보세요"), '채널 탭 미노출').to_be_visible(),
                           check=True)

@pytest.mark.skip
def test_lifestyle_00217(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 채널 탭 진입 > 해시태그 페이지 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.enter_hashtag_page(page))
    # 채널 참여
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.sign_up_hashtag_page(page, out_check=True))
    # 참여한 채널 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.enter_active_hashtag_page(page))
    # 채널 참여 해제
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.withdraw_hashtag_page(page),
                           check=True)

@pytest.mark.skip
def test_lifestyle_00233(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 채널 탭 진입 
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.enter_hashtag_tab(page))
    # '#{텍스트} 노출 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_hashtag_tab(page),
                           check=True)


@pytest.mark.regression
def test_lifestyle_00345(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집사진
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 해시태그
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_hashtag_clp(page),
                           check=True)

@pytest.mark.regression
def test_lifestyle_00346(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집사진
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 해시태그
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_rich_hashtag_clp(page),
                           check=True)

@pytest.mark.regression
def test_lifestyle_00419(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집사진
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 썸네일 좋아요
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_grid_like(page),
                           check=True)

@pytest.mark.regression
def test_lifestyle_00420(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집사진
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 썸네일 좋아요
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_grid_detail_like(page),
                           check=True)

@pytest.mark.smoke
def test_lifestyle_00471(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집들이 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_project_tab())
    # 집들이 피드 3grid 노출 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_project_tab_3grid(page),
                           check=True)

@pytest.mark.smoke
def test_lifestyle_00472(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집들이 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_project_tab())
    # 하단 스크롤
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.infinite_scroll(page),
                           check=True)

    
@pytest.mark.regression
def test_lifestyle_01094(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집사진
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 콘텐츠 수익화 프로그램
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_myreward(page),
                           check=True)

@pytest.mark.regression
def test_lifestyle_01095(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집사진
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 콘텐츠 수익화 프로그램
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_myreward_detail(page),
                           check=True)
    
@pytest.mark.regression
def test_lifestyle_01144(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집사진
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 집사진 필터 설정 후 노출 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_house_filter(page),
                           check=True)

@pytest.mark.regression
def test_lifestyle_01146(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집들이
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_project_tab())
    # 집들이 필터 설정 후 노출 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_project_filter(page),
                           check=True)
    
@pytest.mark.regression
def test_lifestyle_01173(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집들이 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_project_tab())
    # 상세 해시태그 
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_curator(page),
                           check=True)

@pytest.mark.regression
def test_lifestyle_01174(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 큐레이터 링크 진입
    page.goto('https://qa-web.dailyhou.se/curator/intro', timeout=0) 
    # 상세 해시태그 
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_curator_guest(page),
                           check=True)





