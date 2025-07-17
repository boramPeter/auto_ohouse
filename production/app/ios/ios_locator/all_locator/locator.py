from appium.webdriver.common.appiumby import AppiumBy
from app.common.base_method.appium_method import ProviderCommonMethod


class ProviderLocatorIos(ProviderCommonMethod):
    ############ 팝업 닫기 모음 ############
    alarm_confirm_btn = (AppiumBy.ACCESSIBILITY_ID, '허용')

    alarm_confirm_btn_xpath = (AppiumBy.XPATH, '//XCUIElementTypeAlert[@name="‘오늘의집’이(가) 다른 회사의 앱 및 웹 사이트에 걸친 사용자의 활동을 추적하도록 허용하겠습니까?"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]')

    dont_again_btn = (AppiumBy.ACCESSIBILITY_ID, '다시 보지 않기')

    braze_ad_close_btn = (AppiumBy.ACCESSIBILITY_ID, '닫다')
    # braze_ad_close_btn = (AppiumBy.ACCESSIBILITY_ID, '//XCUIElementTypeOther[@name="오늘의집 앱 전면배너"]/XCUIElementTypeButton')

    later_alarm = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="괜찮아요"]')

    # 쇼핑홈 바텀시트 닫기
    ad_close_btn = (
    AppiumBy.XPATH, '//XCUIElementTypeOther[@name="오늘의집 앱 전면배너"]/XCUIElementTypeOther/XCUIElementTypeButton | //XCUIElementTypeOther[@name="오늘의집 앱 전면배너"]/XCUIElementTypeButton')

    ad_close_btn2 = (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="오늘의집 앱 전면배너"]/XCUIElementTypeButton')

    #라이프스타일에서 노출됨
    next_check_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="다음에 확인하기"]')

    close_btn_dismiss24 = (AppiumBy.ACCESSIBILITY_ID, 'dismiss 24')

    close_btn_checkout = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="주문서"]/XCUIElementTypeButton')

    home_floating_close_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="ic arrow with stick left regul"]')

    ##################### 뒤로가기 모음
    # 뒤로
    back_btn = (AppiumBy.XPATH, '(//XCUIElementTypeOther[@name="배너"]/XCUIElementTypeOther[1] | //XCUIElementTypeButton[@name="뒤로"]) | //XCUIElementTypeButton[@name="home 24"]')

    back_to_email_login_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="이메일로 로그인"]')

    back_home_btn = (AppiumBy.ACCESSIBILITY_ID, 'home 24')

    back_category_btn = (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="가구"])[1]')

    back_my_page_shopping_scrap_btn = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="ohouse.ScrapbookList"]/XCUIElementTypeButton[1]')

    scrap_page_back_btn = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="ohouse.ScrapbookList"]/XCUIElementTypeButton[1]')

    close_20_btn = (AppiumBy.ACCESSIBILITY_ID, 'icClose20')

    ######## 로그인 전까지 ################
    apple_login_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Apple로 계속하기"]')

    kakao_login_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="카카오톡으로 계속하기"]')

    login_question_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="로그인에 문제가 있으신가요?"]')

    # 고객센터
    cs_title = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="고객센터"]')

    # 무엇을 도와드릴까요?
    help_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="무엇을 도와드릴까요?"]')

    # 고객센터 09:00 ~ 18:00
    help_time = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="09:00 ~ 18:00"]')

    email_login_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="이메일로 로그인"]')

    pw_reset_btn = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeButton[3]')

    pw_reset_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="새 비밀번호 만들기"]')

    # 고객센터 09:00 ~ 18:00
    help_txt = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="회원가입 시 입력한 정보가 기억나지 않는다면?"]')

    logout_order_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="둘러보기"]')

    logout_order_btn_confirm = (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="둘러보기"])[2]')

    # title = (AppiumBy.ID, 'net.bucketplace:id/title')
    #
    # order_search_btn = (AppiumBy.XPATH, '//android.widget.Button[@text="주문조회"]')
    #
    # ################# 홈 #########################
    home_viewer_tab = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeButton')
    # 홈화면은 홈 탭때문에 2번 인덱스 -> 홈화면 gnb 버튼으로 대체
    gnb_home_btn_at_home = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="홈"]')

    gnb_home_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="홈"]')

    gnb_life_style_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="커뮤니티"]')

    gnb_shopping_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="쇼핑"]')

    gnb_o2o_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="인테리어/생활"]')

    gnb_my_page_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[contains(@name, "마이페이지") and @visible="true"]')

    home_main_banner = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, " / ")]')

     ################################# 홈 퀵메뉴 시작 #####
    home_early_bird_btn = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeScrollView/XCUIElementTypeCell[1]/XCUIElementTypeImage')

    home_today_deal_quick_menu = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="오늘의딜"]')

    home_today_deal_page_txt = (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="단 하루 특가! 스페셜 오늘의딜 | 오늘의집 쇼핑"]/XCUIElementTypeImage[1] | //XCUIElementTypeStaticText[@name="오늘의딜 | 오늘의집 쇼핑"] | //XCUIElementTypeNavigationBar[@name="오늘의딜"]')

    home_houses_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="커뮤니티"] | //XCUIElementTypeStaticText[@name="인테리어고민"] | //XCUIElementTypeStaticText[@name="집들이"]')

    home_lucky_check_btn = (
    AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "행운출첵") or contains(@name, "혜택미션")]')

    home_lucky_check_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "행운출첵")]')

    home_challenge_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="챌린지참여"]')

    home_creator_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="크리에이터"] | //XCUIElementTypeStaticText[@name="취향의발견"]')

    home_grocery_shopping_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="장보기" or @name="오마트"]')

    home_grocery_shopping_title = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[contains(@name, "오늘의집 쇼핑")]')

    home_remodeling_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="리모델링"]')

    home_clean_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="입주청소"]')

     ########################################## 홈 퀵메뉴 종료 ###

    clean_moving_btn = (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="입주청소도 오늘의집에서"]/XCUIElementTypeLink[1]')

    remodeling_request_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="시공 업체 찾기 복잡하셨죠?"]')

    creator_img = (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="10초"] | //XCUIElementTypeStaticText[@name="#오늘찾은취향"] | //XCUIElementTypeButton[@name="상품 보기"]')

#     toolbarBackButton = (AppiumBy.ID, 'net.bucketplace:id/toolbarBackButton')
#
    home_challenge_img = (
    AppiumBy.XPATH,
    '//android.webkit.WebView[@text="기록 챌린지 모아보기"]/android.view.View/android.view.View/android.view.View/android.widget.TextView[1]' +
    ' | ' +
    '//XCUIElementTypeStaticText[@name="관심 가는 채널에서 일상을 공유해 보세요"]'
)
#
    home_top_scrap_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[contains(@name, "scrap 24") and @visible="true"]')

    home_top_scrap_folder_all_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="모두(1)"]')

    home_scrap_img_btn = (AppiumBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeImage')

    home_scrap_img_btn2 = (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeImage')

    home_top_scrap_page_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="스크랩북"]')

    home_noti_icon_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="notification 24"]')

    home_top_cart_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[contains(@name, "cart 24") and @visible="true"]')

    home_floating_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="글쓰기"]')

    home_floating_photo_menu = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="사진"]')

    home_floating_video_menu = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="동영상"]')

    home_floating_review_menu = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="리뷰"]')

    home_floating_interior_menu = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="인테리어시공 리뷰"]')

    cart_put_item_btn = (AppiumBy.XPATH, '//XCUIElementTypeLink[@name="상품 담으러 가기"]','//XCUIElementTypeImage[@name="장바구니가 비었습니다."] 요소와 같은 그룹에 있으면서, "상품 담으러 가기" name 속성을 가지고 있고, visible 속성이 True인 요소')

    alarm_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="알림"]')

    alarm_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="알림"]')

    noti_event_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="이벤트"]')

    two_tab = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="이사플래너"]',"알림 탭 옆에 있는 요소이며, name값을 가지고있는 XCUIElementTypeStaticText 요소")

    ##### 둘러보기 ########
    life_style_bottom_sheet_close_btn = (AppiumBy.ACCESSIBILITY_ID, 'dismiss 24')

    life_style_challenge_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="챌린지 채널"]')

    life_style_channel_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="#채널"]')

    life_style_channel_tab_modal = (AppiumBy.XPATH,'(//XCUIElementTypeStaticText[@name="#채널"])[position()=count(//XCUIElementTypeStaticText[@name="#채널"])]')


    any_hash_tag = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "#") and string-length(@name) >= 3]')

    awesome_find_tab = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="꿀템발견"]/../..//preceding-sibling::XCUIElementTypeButton[1]')

    home_styling_tab = (
    AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="집꾸미기"]/../..//preceding-sibling::XCUIElementTypeButton[1]')

    awesome_find_favorite_chip = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="인기"]')

    home_styling_tab_chip = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="홈스타일링"]')

    home_styling_tab_remodeling_chip = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="시공/리모델링"]')

    awesome_find_review_chip = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="상품후기"]')

    awesome_find_should_buy_chip = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="살까말까"]')

    community_category_all_chip = (AppiumBy.XPATH,'//XCUIElementTypeButton[@name="전체"]')

    community_category_chip_review_text = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "· 조회 ") and @visible="true"]')

    community_category_chip_page_follow = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="팔로우"]')

    houses_tab = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="집들이"]/../..//preceding-sibling::XCUIElementTypeButton[1]')

    houses_tab_sheet = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="집들이"])[2]')

    houses_tab_img_btn = (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeImage')

    house_pic_tab = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="집사진"]/../..//preceding-sibling::XCUIElementTypeButton[1]')

    house_pic_tab_img_btn = (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[position()=1 or position()=2 or position()=3 or position()=4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther')

    household_storage_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="살림수납"]')

    household_storage_tab_modal = (AppiumBy.XPATH,'(//XCUIElementTypeStaticText[@name="살림수납"])[position()=count(//XCUIElementTypeStaticText[@name="살림수납"])]')

    household_storage_tab_img_btn = (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther')

    collectable_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="콜렉터블"]')

    collectable_tab_modal = (AppiumBy.XPATH,'(//XCUIElementTypeStaticText[@name="콜렉터블"])[position()=count(//XCUIElementTypeStaticText[@name="콜렉터블"])]')

    collectable_tab_img_btn = (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther')

    homestaurant_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="홈스토랑"]')

    homestaurant_tab_modal = (AppiumBy.XPATH,'(//XCUIElementTypeStaticText[@name="홈스토랑"])[position()=count(//XCUIElementTypeStaticText[@name="홈스토랑"])]')

    homestaurant_tab_img_btn = (AppiumBy.XPATH,
                               '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther')

    hot_place_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="핫플레이스"]')

    hot_place_tab_modal = (AppiumBy.XPATH,'(//XCUIElementTypeStaticText[@name="핫플레이스"])[position()=count(//XCUIElementTypeStaticText[@name="핫플레이스"])]')


    hot_place_tab_img_btn = (AppiumBy.XPATH,
                                '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther')

    parenting_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="육아"]')

    parenting_tab_modal = (AppiumBy.XPATH,'(//XCUIElementTypeStaticText[@name="육아"])[position()=count(//XCUIElementTypeStaticText[@name="육아"])]')

    parenting_tab_img_btn = (AppiumBy.XPATH,
                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther')

    planterior_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="플랜테리어"]')

    planterior_tab_modal = (AppiumBy.XPATH,'(//XCUIElementTypeStaticText[@name="플랜테리어"])[position()=count(//XCUIElementTypeStaticText[@name="플랜테리어"])]')

    planterior_tab_img_btn = (AppiumBy.XPATH,
                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther')

    pet_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="반려동물"]')

    pet_tab_modal = (AppiumBy.XPATH,'(//XCUIElementTypeStaticText[@name="반려동물"])[position()=count(//XCUIElementTypeStaticText[@name="반려동물"])]')

    pet_tab_img_btn = (AppiumBy.XPATH,
                             '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther')

    camping_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="캠핑"]')

    camping_tab_modal = (AppiumBy.XPATH,'(//XCUIElementTypeStaticText[@name="캠핑"])[position()=count(//XCUIElementTypeStaticText[@name="캠핑"])]')


    camping_tab_img_btn = (AppiumBy.XPATH,
                       '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther')

    hobby_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="취미"]')

    hobby_tab_modal = (AppiumBy.XPATH,'(//XCUIElementTypeStaticText[@name="취미"])[position()=count(//XCUIElementTypeStaticText[@name="취미"])]')

    hobby_tab_img_btn = (AppiumBy.XPATH,
                           '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther')

    bottom_sheet_expand_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="chevron down 12"]')

    follow_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="팔로우"]')

    follow_txt_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="팔로우"] | //XCUIElementTypeStaticText[@name="팔로우"]')

    ################################### 쇼핑홈 #############################


    shopping_suggest_chip = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="추천"]')

    shopping_today_deal_chip = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="오늘의딜"]')

    shopping_carousel_item_list = (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, '%') and contains(@name, ',')]")

    scrap_btn = (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="ic scrap active off"])[1]')

    shopping_search_btn = (AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField')


    shopping_search_page_txt = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="카테고리"]')

    shopping_banner_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "/2")]')

    shopping_banner_page = (
    AppiumBy.XPATH, '//XCUIElementTypeButton[contains(@name, "상품 보기") or contains(@name, "구매하기")]')

    shopping_category_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="카테고리"]')

    shopping_category_expand_btn = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="전체 펼치기"])[1]')

    shopping_category_1depth_title = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="가구"])[1]')

    shopping_category_3depth_area = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="전체"])[1]')

    shopping_first_category = (
    AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="가구"]')

    shopping_first_category_banner = (
        AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]')

    shopping_category_filter_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="필터로 원하는 상품 찾기"]')

    shopping_category_mds_pick_img = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "무료배송") and @visible="true"]')

    pdp_buy_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="구매하기"]')

    shopping_category_list_pdp_img = (
        AppiumBy.XPATH,
        '(//XCUIElementTypeStaticText[@name="특가"])[1]')

    pdp_option_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="색상"]')

    pdp_detail_option_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="라이트그레이"]')

    pdp_put_cart_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="장바구니"]')#(AppiumBy.XPATH, '//XCUIElementTypeButton[@name="장바구니"]')

    pdp_go_cart_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="바로가기"] | //XCUIElementTypeButton[@name="장바구니 가기"]')

    pdp_direct_buy_btn = (
    AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="바로구매"]')#'//XCUIElementTypeButton[@name="바로구매"]')

    cart_item_delete_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="선택삭제"]')
#
    cart_item_delete_confirm_btn = (AppiumBy.XPATH, '(//android.widget.Button[@text="삭제"])[4]')

    shopping_category_filter_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="필터"]')

    shopping_ad_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="오늘의 추천 상품"]')

    shopping_best_title = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="BEST"]')

    shopping_today_deal_title = (
    AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="오늘의딜"])[2]')

    shopping_more_btn = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="더보기"] | //XCUIElementTypeStaticText[@name="패키지할인"] | //XCUIElementTypeStaticText[@name="BEST"]')




    shopping_today_deal_page_title = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="오늘의딜"]')

    shopping_popular_search_title = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="쇼핑 실시간 인기 검색어"]')

    shopping_category_ad_title = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[contains(@name,"카테고리의 추천 상품")]')

    ####################################### o2o ##########################################
    o2o_apply_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name=" 신청내역"]')

    o2o_back_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="뒤로"]')
    o2o_back_home_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="home 24"]')

    o2o_all_menu_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="전체서비스"]')

    # o2o_house_construction_menu_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="HOT 주거시공"]')
    o2o_house_construction_menu_btn = (AppiumBy.XPATH, '//XCUIElementTypeLink[@name="집 전체 시공 업체 찾기 오늘의집이 시공하자, A/S 보장HOT"]')

    o2o_house_partial_menu_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="부분시공"]')

    o2o_ad_popup_close = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name=""]')

    o2o_house_construction_menu_ad_txt = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="주거공간 시공"]')

    o2o_commercial_construction_menu_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="상업시공"]')

    o2o_commercial_construction_menu_matching_text = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="딱 맞는 업체 매칭"]')

    o2o_qna_menu_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="질문/답변"]')

    o2o_qna_interior_page_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="인테리어 상담소"]')

    o2o_material_ranking_menu_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="시공자재 랭킹"]')

    o2o_my_material_list = (AppiumBy.XPATH, '//XCUIElementTypeLink[@name="내 자재 리스트 "]')

    o2o_contract_diagnosis_menu_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="인테리어 계약서 진단"]')


    o2o_contract_diagnosis_page_txt = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="어려운 인테리어 시공 계약"]')

    o2o_quote_calculator_menu_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="견적계산기"]')

    o2o_quote_calculator_page_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="견적 계산"]')

    o2o_move_menu_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="이사"]')

    o2o_move_page_btn_txt = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="견적 상담 신청하기"]')

    o2o_move_in_clean_menu_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="입주청소"]')

    o2o_move_in_clean_menu_page_btn = (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="입주청소도 오늘의집에서"]/XCUIElementTypeLink[1]')

    o2o_product_installation_menu_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="제품설치"]')

    o2o_product_installation_page_btn = (AppiumBy.XPATH, '//XCUIElementTypeLink[@name="서비스 비용 알아보기"]')

    o2o_home_viewing_checklist_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="집보기 체크리스트"]')

    o2o_home_viewing_checklist_bottom_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="새로운 매물 체크 시작하기"]')

    o2o_apt_construction_example_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="아파트 시공사례"]')

    o2o_nearby_apt_list_txt = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="주변아파트 리스트"]')

    o2o_construction_example_tab = (AppiumBy.XPATH, '//android.view.View[@text="시공사례"]')

    # o2o_construction_example_tab_page_txt = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="인테리어 시공 계획이 있나요?"]')
    o2o_construction_example_tab_page_txt = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="정렬"]')

    o2o_easy_matching_tab = (AppiumBy.XPATH, '//android.view.View[@text="간편매칭"]')

    o2o_easy_matching_tab_page_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="시공 업체 찾기 복잡하셨죠?"]')

#     o2o_partial_construction_tab = (AppiumBy.XPATH, '//android.view.View[@text="부분시공"]')

    o2o_partial_construction_tab_page_txt = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="원하는 시공을 선택해주세요"]')

    o2o_find_store_tab = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="업체찾기"]')

    o2o_find_store_tab_page_area = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="인테리어 시공 계획이 있나요? 주소 입력하고, 맞춤 사례와 업체를 둘러보세요.  사업장 주소  검색하기"]')
    ####################################### 검색 ##########################################
    search_icon = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="ohouse.HomeTab"]/XCUIElementTypeOther')

    search_text_box = (AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField')

    search_vk_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Search"]')

    search_shopping_title = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="쇼핑"])[2]')

    search_more_btn = (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name, '더보기')]")

    search_photo_more_btn = (
        AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name, '더보기') and string-length(@name) = 10]")

    search_houses_more_btn = (
        AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name, '더보기') and string-length(@name) = 7]")

    search_khowhow_more_btn = (
        AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name, '더보기') and string-length(@name) = 7]")

    search_shopping_filter_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="필터"]')

    search_shopping_filter_order_text = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="정렬"]')

    search_photo_title = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="사진"])[2]')

    search_photo_tab_filter = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="주거정보"]')

    search_knowhow_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="노하우 콘텐츠"]')

    search_knowhow_tab_filter = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="노하우" and @value="1"]')

    search_houses_title = (
    AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="집들이 콘텐츠"]')

    search_houses_tab_filter = (
    AppiumBy.XPATH, '//XCUIElementTypeButton[@name="집들이" and @value="1"]')

    search_construction_title = (
        AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="시공업체"])[2]')

    search_construction_tab_selected = (
        AppiumBy.IOS_PREDICATE, 'name == "시공업체" AND label == "시공업체" AND value == "1"')

    search_user_tab = (
        AppiumBy.XPATH, '//XCUIElementTypeButton[@name="유저"]')

    search_user_tab_nickname = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="아이폰자동화계정"]')
    ##### 마이페이지 ########

    prof_img_btn = (AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="오늘의집"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')

    prof_img_detail_view = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="ohouse.UserHomeProfilePinch"]')

    my_shopping_btn = (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="쇼핑"])[1]')

    my_shopping_product_scrap_book = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="상품 스크랩북"]')

    my_shopping_question_list = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="나의 문의내역"]')

    my_shopping_customer_center = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="고객센터"]')

    non_question_text = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="상품문의"]')

    my_set_btn = (AppiumBy.ACCESSIBILITY_ID, 'setting 24')

    order_txt = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="진행중인 주문"]')

    my_review_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="나의 리뷰"]')

     # 작성된 리뷰가 없습니다 텍스트
    write_my_review_text = (
    AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="작성 가능한 리뷰가 없어요"]')

    prof_tab_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="프로필"]')

     #### 마이페이지_설정 페이지 시작 #######
    my_prof_edit_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="내 정보 수정"]')

    my_alarm_edit_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="알림 설정"]')

    my_prof_change_email_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="이메일 변경하기"]')

    my_prof_img_del_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="이미지 삭제"]')

    my_alarm_set_text = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="앱 푸시"]')

    my_change_pw_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="비밀번호 변경"]')

    new_pw_change_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="새 비밀번호"]')

     #### 마이페이지_설정 페이지 종료 #######

    ### 커머스플랫폼 #####

    check_out_title = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="주문서"]')

    # 주문취소 버튼
    check_out_confirm_btn = (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="확인"])[2]')

    order_delivery_list_btn = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="주문배송내역 조회"]')

    order_delivery_list_page_txt = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="아직 주문한 상품이 없어요."]')

    order_delivery_status_btn1 = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="입금 대기"]')

    order_delivery_status_btn2 = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="결제 완료"]')

    order_delivery_status_btn3 = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="배송 준비"]')

    order_delivery_status_btn4 = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="배송중"]')

    order_delivery_status_btn5 = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="배송 완료"]')

    my_page_point_btn = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "포인트")]')

    my_page_point_page_txt = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="포인트 내역"]')

    my_page_coupon_btn = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "쿠폰")]')

    my_page_coupon_page = (
        AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="쿠폰"]')

    my_page_grade_btn = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "등급")]')

    my_page_grade_page_txt = (
        AppiumBy.XPATH, '//XCUIElementTypeOther[@name="아이폰자동화계정2 님의 회원등급"]')
