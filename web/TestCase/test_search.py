from web.ObjectSetting.common_object import *
from web.ObjectSetting.search import *
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.web_result_binary import ResultWeb
from web.BasicSetting.exception_func import *
qa_home = 'https://qa-web.dailyhou.se/'
card_url = 'https://contents.qa-web.dailyhou.se/cards/6396119?affect_type=CardSearch&affect_id=0&query=%EC%A7%91%EB%93%A4%EC%9D%B4&is_video=false'
housewarming_url = 'https://contents.qa-web.dailyhou.se/cards/5898563?affect_type=CardSearch&affect_id=0&query=%EC%A7%91%EB%93%A4%EC%9D%B4%20%EC%BD%98%ED%85%90%EC%B8%A0&is_video=false'
video_url = 'https://contents.qa-web.dailyhou.se/contents/card_collections/1000003829?affect_type=CardSearch&affect_id=0&query=%EB%8F%99%EC%98%81%EC%83%81%20%EB%93%B1%EB%A1%9D%20%ED%85%8C%EC%8A%A4%ED%8A%B8&is_video=true'
search_video_url = 'https://contents.qa-web.dailyhou.se/contents/card_collections/1000003829'
search_housewarming_url = 'https://contents.qa-web.dailyhou.se/cards/5898563'
search_card_url = 'https://contents.qa-web.dailyhou.se/cards/7988524'
advices_url = 'https://qa-web.dailyhou.se/advices/10526'
housewarming_projects_url = 'https://contents.qa-web.dailyhou.se/projects/47885'
card_collections_url = 'https://contents.qa-web.dailyhou.se/contents/card_collections/6692319'
exhibitions_url = 'https://store.qa-web.dailyhou.se/today_deals?affect_type=Home&affect_id=0'
category_url = 'https://qa-web.dailyhou.se/productions/feed?query=%EC%BB%B4%ED%93%A8%ED%84%B0&category_id=10040008'

@pytest.mark.smoke
def test_search_00246(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: SearchAutoComplete(page).search_autocomplete("긍", "긍정 포스터"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["사진"]),
                           check=True)

@pytest.mark.smoke
def test_search_00014(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("테이블"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["쇼핑", "사진"]),
                           check=True)
    
@pytest.mark.smoke
def test_search_00271(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ContentsSearchProcedure(page).search_contents_home("집들이"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["쇼핑", "사진"]),
                           check=True)

@pytest.mark.smoke
def test_search_00157(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchRelatedKeyword(page).search_related_keyword("테이블"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["쇼핑", "사진"]),
                           check=True)

@pytest.mark.smoke
def test_search_00032(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("그릇"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["사진"]))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_card_enter())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_card_check(),
                           check=True)
    
@pytest.mark.smoke
def test_search_00038(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).search_card_tab("그릇"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).card_enter())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_card_check(),
                           check=True)

@pytest.mark.smoke
def test_search_00041(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("스타일링"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["집들이 콘텐츠"]))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_project_enter())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_longform_check(),
                           check=True)

@pytest.mark.skip
def test_search_00048(page):
    try:
        test_search_00041(page)
        print("\ntest_search_00048 : 집들이 탭 검색 > 집들이 상세 진입", end='')
        search_tab = page.locator("nav").filter(has_text="통합")
        search_tab.get_by_text("집들이").click()
        page.wait_for_timeout(1000)
        scrap_count = page.get_by_label("스크랩").count()
        assert scrap_count >= 3, "scrap_count ="+str(scrap_count)
        expect(page.get_by_placeholder("통합검색")).to_have_attribute("value", "스타일링")
        page.locator("article").get_by_role("link").first.click()
        expect(page.get_by_role("button", name="팔로우").first).to_be_visible()
    except AssertionError as e:
        print(" - Fail", end='')
        print(f"\nCaught an AssertionError: {e}")

@pytest.mark.smoke
def test_search_00051(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("소품"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["노하우 콘텐츠"]))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_advice_enter())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_longform_check(),
                           check=True)
    
@pytest.mark.smoke
def test_search_00220(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ContentsSearchProcedure(page).search_contents_tab("오하우스"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ContentsSearchProcedure(page).contents_enter())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_card_check(),
                           check=True)

@pytest.mark.skip
def test_search_00058(page):
    try:
        test_search_00051(page)
        print("\ntest_search_00058 : 노하우 탭 검색 > 노하우 상세 진입", end='')
        search_tab = page.locator("nav").filter(has_text="통합")
        search_tab.get_by_text("노하우").click()
        page.wait_for_timeout(1000)
        scrap_count = page.get_by_label("스크랩").count()
        assert scrap_count >= 3, "scrap_count ="+str(scrap_count)
        expect(page.get_by_placeholder("통합검색")).to_have_attribute("value", "소품")
        page.locator("article").get_by_role("link").first.click()
        expect(page.get_by_role("button", name="팔로우").first).to_be_visible()
    except AssertionError as e:
        print(" - Fail", end='')
        print(f"\nCaught an AssertionError: {e}")

@pytest.mark.smoke
def test_search_00062(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("이불세트"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["쇼핑"]))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_product_enter())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_product_check(),
                           check=True)

@pytest.mark.smoke
def test_search_00069(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    url = web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).search_shop_tab("이불세트"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).re_search_shop_tab("방석커버"),
                           prev_page=url)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).product_enter())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_product_check(),
                           check=True)

@pytest.mark.smoke
def test_search_00315(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).search_shop_home("매트리스"),
                           prev_page=qa_home)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).check_shop_tab(),
                           check=True)

@pytest.mark.smoke
def test_search_00075(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).search_shop_home("소파"),
                           prev_page=qa_home)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).check_shop_tab())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).apply_price_filter())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).check_price_filter(),
                           check=True)

@pytest.mark.smoke
def test_search_00076(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).search_shop_home("가구"),
                           prev_page=qa_home)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).check_shop_tab())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).change_sort_check("판매순", "낮은가격순"),
                           check=True,
                           opt_check=lambda: ShopSearchProcedure(page).check_shop_tab())

@pytest.mark.smoke
def test_search_00077(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("한샘 인테리어"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["시공업체"]))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_experts_enter())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_experts_check(),
                           check=True)

@pytest.mark.smoke
def test_search_00083(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: O2OSearchProcedure(page).search_o2o_tab("한샘 인테리어"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: O2OSearchProcedure(page).re_search_o2o_tab("디자인"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: O2OSearchProcedure(page).experts_enter())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_experts_check(),
                           check=True)

@pytest.mark.smoke
def test_search_00316(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: O2OSearchProcedure(page).search_o2o_home("인테리어"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: O2OSearchProcedure(page).check_o2o_tab("인테리어"),
                           check=True)

@pytest.mark.smoke
def test_search_00167(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("테이블"),
                           prev_page=qa_home)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).re_integrated_search("거실 테이블"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["쇼핑"]),
                           check=True)

@pytest.mark.smoke
def test_search_00088(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("초코"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: UserSearchProcedure(page).check_invisible_collection())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: UserSearchProcedure(page).click_user_tab())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_input_keyword("초코"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: UserSearchProcedure(page).user_enter_and_check(),
                           check=True)
    
@pytest.mark.smoke
def test_search_00500(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("러그"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["새로운 취향을 발견해보세요"], more_btn=False))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_undiscovered_enter())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchDetail(page).integrated_product_check(),
                           check=True)
    
@pytest.mark.smoke
def test_search_00597(page,login_out):
    current_function_name = ProviderFunctionName().get_current_function_name() 

    web_exceptions_handler(page, current_function_name, 
                           step=lambda: SearchAutoComplete(page).search_autocomplete ("냉장고", "쇼핑 검색"), check=True)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: SearchProcedure(page).check_url_contains_productions_shopping, check=True)
    
@pytest.mark.regression
def test_search_00021(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #가구 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("가구"))
    #통검에서 쇼핑 컬렉션 있나 확인하는 코드?
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["쇼핑"]))
    #쇼핑탭 (탭 클릭,해당 함수에 check하는 함수도 호출)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).search_shop_tab("가구"))
    #사진탭 (탭 클릭,해당 함수에 check하는 함수도 호출)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).click_card_tab())
    #콘텐츠탭 (탭 클릭,해당 함수에 check하는 함수도 호출)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ContentsSearchProcedure(page).click_contents_tab())
    #시공업체 (탭 클릭,해당 함수에 check하는 함수도 호출)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: O2OSearchProcedure(page).click_o2o_tab())
    #유저탭 (탭 클릭,해당 함수에 check하는 함수도 호출)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: UserSearchProcedure(page).click_user_tab(),check=True)   

@pytest.mark.regression
def test_search_00010(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 최근 검색어 검색하기 (없으면 검색 기록 추가)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchRetrieveLatest(page).search_retrieve_latest("러그"),check=True)

@pytest.mark.regression
def test_search_00255(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 2순위 인기 검색어 검색하기
    web_exceptions_handler(page, current_function_name,
                          step=lambda: SearchRankingKeyword(page).search_ranking_Keyword(2),check=True)
    
@pytest.mark.regression
def test_search_00458(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).hash_tag("오하우스"),check=True)
    
@pytest.mark.regression
def test_search_00023(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #강제전환 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("이캐아"))
    #원질의 선택 및 확인하는 코드
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_original_keyword_search("이캐아"),check=True)

@pytest.mark.regression
def test_search_00025(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #교정할 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("오이리"))
    #제안키워드 선택 및 확인하는 코드
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_similar_keyword_search("오일"),check=True)

@pytest.mark.regression
def test_search_00091(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #제작형 컨텐츠 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("의자"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_produced_contents("의자", "", "", "", exhibitions_url,category_url),check=True)

@pytest.mark.skip
def test_search_00456(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #제작형 컨텐츠 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("차박"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_produced_contents("차박", advices_url, housewarming_projects_url, card_collections_url, "",""),check=True)

@pytest.mark.regression
def test_search_00457(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #제작형 컨텐츠 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("가구 추천"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_produced_contents("가구 추천", "", "", "", "", ""),check=True) 
        
@pytest.mark.regression
def test_search_00092(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #브랜드명 존재하는 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("이케아"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).brand_home_btn("이케아"),check=True)

@pytest.mark.regression
def test_search_00531(page,login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #동영상 사진 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("동영상 등록 테스트"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_contents_detail("동영상",search_video_url),check=True)
    
@pytest.mark.regression
def test_search_00462(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #카드 상세 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("가구"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["사진"]))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_contents_detail("이 사진을 포함한 사진묶음 보기",search_card_url),check=True)

@pytest.mark.regression
def test_search_00463(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #집들이 상세 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("집들이 콘텐츠"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["사진"]))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_contents_detail("이 사진을 포함한 집들이 보기",search_housewarming_url),check=True)

@pytest.mark.regression
def test_search_00034(page):
    current_function_name = ProviderFunctionName().get_current_function_name()

    #주방 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("주방"))
    #사진 더보기 > 사진 검색 탭 랜딩 확인
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).click_more_btn(["사진"],"주방"),check=True)

@pytest.mark.regression
def test_search_00506(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 사진탭 검색 
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).search_card_tab("오늘의집"))
    # 필터 모달창 췤
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).search_filter_modal())
    # 필터 옵션칩, 결과 확인
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).search_filter_check("공간", "드레스룸"),check=True)
@pytest.mark.regression
def test_search_00521(page,login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    # 사진탭 검색 > 동영상 콘텐츠 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).search_card_tab("동영상 등록 테스트"))
    # 사진탭 > 동영상 필터 선택
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).search_filter_check("동영상", "동영상"))
    # 사진 탭 > 피드 선택 시 동영상 상세로 이동 (하드코딩 url 비교..)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).contents_detail("동영상",video_url),check=True)

@pytest.mark.regression
def test_search_00466(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    # 사진탭 검색 > 카드(사진) 콘텐츠 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).search_card_tab("집들이"))
    # 사진 탭 > 피드 선택 시 카드 상세로 이동 (하드코딩 url 비교..)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).contents_detail("이 사진을 포함한 사진묶음 보기",card_url),check=True)
    
@pytest.mark.regression
def test_search_00468(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    # 사진탭 검색 > 집들이 콘텐츠 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).search_card_tab("집들이 콘텐츠"))
    # 사진 탭 > 피드 선택 시 카드 상세로 이동 (하드코딩 url 비교..)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).contents_detail("이 사진을 포함한 집들이 보기",housewarming_url),check=True)

@pytest.mark.regression
def test_search_00097(page):
    current_function_name = ProviderFunctionName().get_current_function_name()

    # 사진탭 검색 > 의자 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).search_card_tab("의자"))
    # 연관 검색어 노출 및 재검색 동작 확인
    web_exceptions_handler(page, current_function_name,
                           step=lambda: CardSearchProcedure(page).card_related_keyword(),check=True)

@pytest.mark.regression
def test_search_00221(page):
    current_function_name = ProviderFunctionName().get_current_function_name()

    #원룸 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("원룸"))
    #집들이 콘텐츠 더보기 > 콘텐츠 검색 탭 랜딩 확인
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).click_more_btn(["집들이 콘텐츠"],"원룸"),check=True)

@pytest.mark.regression
def test_search_00222(page):
    current_function_name = ProviderFunctionName().get_current_function_name()

    #오늘의집 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("오늘의집"))
    #노하우 콘텐츠 더보기 > 콘텐츠 검색 탭 랜딩 확인
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).click_more_btn(["노하우 콘텐츠"],"오늘의집"),check=True)

@pytest.mark.regression
def test_search_00452(page):
    current_function_name = ProviderFunctionName().get_current_function_name()

    #수납 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("수납"))
    #콘텐츠탭 (탭 클릭,해당 함수에 check하는 함수도 호출)
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ContentsSearchProcedure(page).click_contents_tab())
    #콘텐츠탭 종류 필터 > 집들이 선택
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ContentsSearchProcedure(page).type_filter("집들이"))
    #콘텐츠탭 종류 필터 > 노하우 선택
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ContentsSearchProcedure(page).type_filter("노하우"),check=True)

@pytest.mark.regression
def test_search_00061(page,login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("가구"))
    #로그인을해야 쿠폰값이 정확하게 노출되며, 쇼핑 컬렉션 카드 정보를 로그에 저장시킴
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_collection_info(["쇼핑"]),check=True)

@pytest.mark.regression
def test_search_00065(page):
    current_function_name = ProviderFunctionName().get_current_function_name()

    #거울 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("거울"))
    #쇼핑 더보기 > 쇼핑 검색 탭 랜딩 확인
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).click_more_btn(["쇼핑"],"거울"),check=True)
    
@pytest.mark.regression
def test_search_00072(page):
    current_function_name = ProviderFunctionName().get_current_function_name()

    # 쇼핑 검색 > 의자 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).search_shop_home("의자"))
    # 연관 검색어 노출 및 재검색 동작 확인
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).shop_related_keyword(),check=True)

@pytest.mark.regression
def test_search_00073(page):
    current_function_name = ProviderFunctionName().get_current_function_name()

    # 쇼핑 검색 > 브랜드명 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).search_shop_home("삼성전자"))
    # 브랜드홈 바로가기
    web_exceptions_handler(page, current_function_name,
                           step=lambda: ShopSearchProcedure(page).brand_home_click("삼성전자"),check=True)

@pytest.mark.regression
def test_search_00185(page):
    current_function_name = ProviderFunctionName().get_current_function_name()

    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("잠실"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_apt_info())
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_apt_click(),check=True)

@pytest.mark.regression
def test_search_00079(page):
    current_function_name = ProviderFunctionName().get_current_function_name()

    #마루 키워드 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("마루"))
    #시공업체 더보기 > 시공업체 검색 탭 랜딩 확인
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).click_more_btn(["시공업체"],"마루"),check=True)
    
#00247 통합검색 자동완성에서 쇼핑 검색 랜딩 키워드로 변경되어 주석처리 
@pytest.mark.skip
def test_search_00247(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #홈에서 'ㄱ' 입력 후 카테고리 자동완성 클릭 
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: SearchAutoComplete(page).search_autocomplete("ㄱ", "가구"))
    #가구 카테고리 PLP 확인 
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchAutoComplete(page).check_category_plp("가구"),check=True)
    
@pytest.mark.regression
def test_search_00151(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # '화장대' 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("화장대"))
    # 사진 컬렉션 ib chip 클릭 & 클릭한 chip 수가 1개인지 확인
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchIBChip(page).click_ib_chip("card", 0),check=True)

@pytest.mark.regression
def test_search_00133(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # '화장대' 검색
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("화장대"))
    # 쇼핑 컬렉션 ib chip 클릭 & 클릭한 chip 수 확인
    web_exceptions_handler(page, current_function_name,
                           step=lambda: IntegratedSearchIBChip(page).click_ib_chip("shopping", 0),check=True)
    
@pytest.mark.regression
def test_search_00090(page,login_out):
    current_function_name = ProviderFunctionName().get_current_function_name() 
    #유저 키워드 검색 ('선선선선GGGGG')
    web_exceptions_handler(page, current_function_name,
                           step=lambda:SearchProcedure(page).search_keyword("선선선선GGGGG"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda:UserSearchProcedure(page).click_user_tab(),check=True)
    #유저 팔로우 클릭 > '팔로잉'으로 버튼 변경 확인 
    web_exceptions_handler(page, current_function_name,
                           step=lambda:UserSearchProcedure(page).check_user_follow_btn(),check=True)
    web_exceptions_handler(page, current_function_name,
                           step=lambda:UserSearchProcedure(page).click_user_follow_btn(),check=True)
    web_exceptions_handler(page, current_function_name,
                           step=lambda:UserSearchProcedure(page).check_user_following_btn(),check=True)
    #유저 팔로잉 클릭 > '팔로우'로 버튼 변경 확인 
    web_exceptions_handler(page, current_function_name,
                           step=lambda:UserSearchProcedure(page).click_user_following_btn(),check=True)
    web_exceptions_handler(page, current_function_name,
                           step=lambda:UserSearchProcedure(page).check_user_follow_btn(),check=True)

@pytest.mark.regression
def test_search_00426(page,login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #2개 이상 키워드로 검색 후, 최근에 검색한 키워드가 자동완성 첫번째 옵션으로 노출되는지 확인 
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("커피머신"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("커텐"))
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).check_integrated_search(["쇼핑"]),
                           check=True)   

@pytest.mark.regression
def test_search_00302(page,login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    #통합검색 SRP 이동 
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).search_keyword("가구"))
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: SearchProcedure(page).check_url_contains_productions_integrated, check=True)
    #통합검색 > 쇼핑컬렉션 우측 Circle 더보기 버튼 클릭 
    web_exceptions_handler(page, current_function_name,
                           step=lambda: SearchProcedure(page).scroller_ui_right_click(), check=True)
    #쇼핑탭 랜딩 확인 
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: SearchProcedure(page).check_url_contains_productions_shopping, check=True)   
