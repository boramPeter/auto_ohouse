from web.ObjectSetting.comm_service import *
from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.common_object import *
from web.ObjectSetting.lifestyle import *
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.web_result_binary import ResultWeb
from web.BasicSetting.exception_func import *
qa_home = 'https://qa-web.dailyhou.se/'
qa_recommend = 'https://contents.qa-web.dailyhou.se/topics/recommend'


# lifestyle 40
@pytest.mark.smoke
def test_content_00001(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 추천 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_recommend_tab())
    # 하단 스크롤
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.infinite_scroll(page),
                           check=True)
    
# lifestyle 41
@pytest.mark.smoke
def test_content_00002(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 추천 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_recommend_tab())
    # 콘텐츠 그리드 구성요소 확인
    web_exceptions_handler(page, current_function_name,
                        #    step=lambda: expect(page.get_by_text("테스트자동화용"), '추천 페이지 미노출').to_be_visible(),
                           step=lambda: expect(page.get_by_text("Featured Carousel Module"), '추천 페이지 미노출').to_be_visible(),
                           check=True)


# lifestyle 929
@pytest.mark.regression
def test_content_00003(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 추천 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_recommend_tab())
    # 좋아요 on/off 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_cdp_like(page),
                           check=True)
    
# lifestyle 42
@pytest.mark.smoke
def test_content_00004(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 추천 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_recommend_tab())
    # 스크랩 on, off
    web_exceptions_handler(page, current_function_name,
                           step=lambda: LifestyleElements.check_recommend_scrap(page, True),
                           opt_check=lambda: LifestyleElements.check_recommend_scrap(page, False),
                           check=True)
    
# lifestyle 51
@pytest.mark.smoke
def test_content_00009(page, login_out):
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

# lifestyle 44
@pytest.mark.smoke
def test_content_00012(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 추천 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_recommend_tab())
    # 콘텐츠 클릭
    web_exceptions_handler(page, current_function_name,
                           step=lambda: page.locator("span").filter(has_text=re.compile(r"멋지다*")).get_by_role("link").first.click())
    # 콘텐츠 상세 확인
    web_exceptions_handler(page, current_function_name,
                           step=lambda: LifestyleElements.check_cdp(page),
                           check=True)


# lifestyle 43
@pytest.mark.smoke
def test_content_00013(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 추천 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_recommend_tab())
    # 콘텐츠 클릭 & 뒤로가기
    web_exceptions_handler(page, current_function_name,
                        #    step=lambda: page.locator("span").filter(has_text=re.compile(r"테스트자동화용 자동화용 콘텐츠.*")).get_by_role("link").first.click())
                           step=lambda: page.locator("span").filter(has_text=re.compile(r"멋지다*")).get_by_role("link").first.click())    
    page.wait_for_timeout(3000) # 없으면 fail 남
    page.go_back()
    # 피드 내 테스트용 콘텐츠 재확인
    web_exceptions_handler(page, current_function_name,
                        #    step=lambda: expect(page.locator("span").filter(has_text=re.compile(r"테스트자동화용 자동화용 콘텐츠로.*")).get_by_role("link").first, '상세 페이지 미노출').to_be_visible(),
                           step=lambda: expect(page.locator("span").filter(has_text=re.compile(r"멋지다*")).get_by_role("link").first, '상세 페이지 미노출').to_be_visible(),

                           check=True)

# lifestyle 151
@pytest.mark.regression
def test_content_00024(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집사진
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
 
    # maroo_0704 추가
    # 콘텐츠 클릭 & 뒤로가기
    web_exceptions_handler(page, current_function_name,
                           step=lambda: page.locator("#card-collection-item-1000015496").get_by_role("link").first.click())    
    page.wait_for_timeout(3000) # 없으면 fail 남김

    # 집사진 V1 (버티컬 뷰 + 무한스크롤) - maroo_0704 수정
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_cdp(page),
                           check=True)

# lifestyle 152   
@pytest.mark.regression
def test_content_00025(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집사진
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 집사진 V1 (버티컬 뷰 + 무한스크롤)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_house_v1_detail(page),
                           check=True)

# lifestyle 1071   
@pytest.mark.regression
def test_content_00027(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 사진 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 해시태그
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_comment(page),
                           check=True)


# lifestyle 157
@pytest.mark.smoke
def test_content_00036(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집시잔 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_card_tab())
    # 동영상 노출 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.enter_clp_video(page),
                           check=True)

# lifestyle 251
@pytest.mark.smoke
def test_content_00055(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 채널 탭 > 해시태그 페이지 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.enter_hashtag_page(page),
                           check=True)


# lifestyle 252
@pytest.mark.smoke
def test_content_00057(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 채널 탭 > 해시태그 페이지 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.enter_hashtag_page(page))
    # 해시태그 CLP 요소 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_hashtag_page(page),
                           check=True)


# lifestyle 257
@pytest.mark.smoke
def test_content_00058(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 채널 탭 > 해시태그 페이지 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.enter_hashtag_page(page))
    # 채널 참여
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.sign_up_hashtag_page(page))
    # 채널 참여 해제
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.withdraw_hashtag_page(page),
                           check=True)


# lifestyle 319
@pytest.mark.regression
def test_content_00059(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 해시태그
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_hashtag_filter(page),
                           check=True)
    

# lifestyle 268
@pytest.mark.smoke
def test_content_00060(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 채널 탭 > 해시태그 페이지 > 임의의 컨텐츠 선택
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.enter_hashtag_cdp(page),
                           check=True)
    # CDP 확인
    # web_exceptions_handler(page, current_function_name, 
    #                        step=lambda: expect(page.get_by_test_id("CardCollection-scrap-button"), 'CDP 상세페이지 미노출').to_be_visible(),
    #                        check=True)


# lifestyle 489
@pytest.mark.regression
def test_content_00064(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집들이 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_project_tab())
    # 상세 하단 스크롤
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_project_scroll(page),
                           check=True)
    
# lifestyle 491
@pytest.mark.regression
def test_content_00065(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집들이 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_project_tab())
    # 상세 해시태그 
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_project_hashtag(page),
                           check=True)


# lifestyle 492
@pytest.mark.regression
def test_content_00066(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집들이 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_project_tab())
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_project_thumbnail(page),
                           check=True)


# lifestyle 519
@pytest.mark.regression
def test_content_00068(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집들이 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_project_tab())
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_project_ProductGroup(page),
                           check=True)
    

# lifestyle 1165
@pytest.mark.regression
def test_content_00069(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집들이 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_project_tab())
    # 상세 해시태그 
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_project_concept_view(page),
                           check=True)

# lifestyle 507
@pytest.mark.regression
def test_content_00073(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 집들이 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_project_tab())
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_project_comment(page),
                           check=True)


# lifestyle 537
@pytest.mark.regression
def test_content_00079(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_knowhow_cdp(page),
                           check=True)

# lifestyle 554
@pytest.mark.regression
def test_content_00086(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_knowhow_comment(page),
                           check=True)

# lifestyle 562
@pytest.mark.regression
def test_content_00091(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 3D인테리어
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_3d_tab())
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_3d_interior_feed(page),
                           check=True)


# lifestyle 791
@pytest.mark.regression
def test_content_00125(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 업로드 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.enter_upload(page))
    # 업로드 해시태그 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_upload_hashtag(page),
                           check=True)
    

# lifestyle 758
@pytest.mark.smoke
def test_content_00128(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 사진 올리기
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleUpload(page).all_upload_photo(),
                           check=True)


# lifestyle 793
@pytest.mark.regression
def test_content_00129(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 업로드 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleUpload(page).all_upload_photo_undelete())
    # 업로드 해시태그 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_upload_edit(page),
                           check=True)
    
# lifestyle 793
@pytest.mark.regression
def test_content_00130(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 업로드 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleUpload(page).all_upload_photo(),
                           check=True)
       

# lifestyle 760
@pytest.mark.smoke
def test_content_00137(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 동영상 올리기
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleUpload(page).all_upload_video(),
                           check=True)
    

# lifestyle 1376
@pytest.mark.regression
def test_content_00139(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 업로드 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleUpload(page).all_upload_video_undelete())
    # 업로드 해시태그 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_upload_video_edit(page),
                           check=True)
       
# lifestyle 732
@pytest.mark.regression
def test_content_00160(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 사진 CDP 신고
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_report_content(page),
                           check=True)

# lifestyle 733
@pytest.mark.regression
def test_content_00161(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 사진 CDP 유저프로필 신고
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_report_user(page),
                           check=True)

# lifestyle 734
@pytest.mark.regression
def test_content_00162(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 사진 CDP 댓글 신고
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_report_comment(page),
                           check=True)

# lifestyle 735
@pytest.mark.regression
def test_content_00163(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 사진 CDP 대댓글 신고
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_report_recomment(page),
                           check=True)

@pytest.mark.regression
def test_content_00164(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 동영상 CDP 신고
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_report_video_content(page),
                           check=True)

@pytest.mark.regression
def test_content_00165(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 동영상 CDP 유저프로필 신고
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_report_video_user(page),
                           check=True)

# lifestyle 740
@pytest.mark.regression
def test_content_00166(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 동영상 CDP 신고
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_report_house(page),
                           check=True)

# lifestyle 741
@pytest.mark.regression
def test_content_00167(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 동영상 CDP 유저프로필 신고
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_report_house_user(page),
                           check=True)




