Feature: comm_service ST,RT
#  @개별
#  Scenario: 00000 커머스서비스 개별실행 사전조건
#    Given "qabucketaos3"로 로그인

# 상품 셋팅 : service00195 : 6240759(3번),611308(2번)
# 상품 셋팅 : service00130 : 401328
# 상품 셋팅 : service00264 : 245672
  @개별
  Scenario: 00000 커머스서비스 개별실행 사전조건
    Given "qabucketaos3@gmail.com,qwertyu1"로 로그인

  @RT
  Scenario: comm_service00032 쇼핑홈 카테고리에서 하단 다수 스크롤 후 페이지 정상동작 확인
    Given "qabucketios3@gmail.com,qwertyu1,service00264,2,624075","스크랩_폴더_확인후_상품_스크랩" 페이지 진입 및 확인
    Given "gnb_shopping_btn","클릭","shopping_home_category_btn","찾을때까지_조금씩_스크롤","shopping_home_category_btn","클릭","40회","아래로_스크롤","shopping_home_scrap_btn","찾을때까지_스크롤" 페이지 진입 및 확인
    Then "shopping_home_scrap_btn"가"활성화","True" 확인 후 "gnb_shopping_btn,gnb_home_btn"를"순서대로_클릭"해서 홈화면 복귀


  @RT
  Scenario: comm_service00033 쇼핑홈 카테고리 디테일 페이지에서 탑버튼 동작 확인
    Given "gnb_shopping_btn","클릭","shopping_home_category_btn","찾을때까지_스크롤","shopping_home_category_btn","클릭","shopping_home_category_detail_page_top_btn","찾을때까지_스크롤","shopping_home_category_detail_page_top_btn","클릭" 페이지 진입 및 확인
    Then "shopping_home_category_detail_page_name_btn"가"활성화","True" 확인 후 "back_homeIcon_btn,gnb_home_btn"를"순서대로_클릭"해서 홈화면 복귀


  @RT
  Scenario: comm_service00056 쇼핑홈 하단 다수 스크롤 후 페이지 정상동작 확인
    Given "gnb_shopping_btn","클릭","40회","아래로_스크롤","shopping_home_scrap_btn","찾을때까지_스크롤" 페이지 진입 및 확인
    Then "shopping_home_scrap_btn"가"활성화","True" 확인 후 "gnb_shopping_btn,gnb_home_btn"를"순서대로_클릭"해서 홈화면 복귀


  @RT
  Scenario: comm_service00058 쇼핑홈 칩캐러셀 아이템리스트 PDP 확인
    Given "gnb_shopping_btn","클릭","shopping_home_review_badge","찾을때까지_스크롤","shopping_home_review_badge","클릭","3초","쉬고","500,600","좌표_클릭","pdp_buy_btn","활성화" 페이지 진입 및 확인
    Then "pdp_buy_btn"가"활성화","True" 확인 후 "back_homeIcon_btn,gnb_shopping_btn,gnb_home_btn"를"순서대로_클릭"해서 홈화면 복귀


  @RT
  Scenario: comm_service00264 신 브랜드홈 진입확인
    Given "home_scrap_btn,home_scrap_folder_tab","순서대로_클릭","1회","아래로_스크롤","home_scrap_folder_00264,home_scrap_folder_item2,pdp_brand_btn","순서대로_클릭","brand_home_title","활성화" 페이지 진입 및 확인
    Then "brand_home_title"가"활성화","True" 확인 후 "back_homeIcon_brand_page_btn"를"클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00265 신 브랜드홈 상세화면 확인
    Given "home_scrap_btn,home_scrap_folder_tab","순서대로_클릭","1회","아래로_스크롤","home_scrap_folder_00264,home_scrap_folder_item2,pdp_brand_btn","순서대로_클릭","2초","쉬고","brand_home_thumbnail_img","찾을때까지_스크롤","10회","위로_스크롤" 페이지 진입 및 확인
    Then "brand_home_scrap_text,brand_home_styling_text,brand_home_brand_subtitle,brand_home_total_category"가"활성화","True" 확인 후 "back_homeIcon_brand_page_btn"를"클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00098 상품상세에서 리뷰더보기를 통해 리뷰 리스트 노출확인
    Given "home_scrap_btn,home_scrap_folder_tab","순서대로_클릭","1회","아래로_스크롤","home_scrap_folder_00264,home_scrap_folder_item2,pdp_rating_bar","순서대로_클릭","1초","쉬고","review_more_img","활성화" 페이지 진입 및 확인
    Then "review_more_img"가"활성화","True" 확인 후 "back_review_close_home_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00228 pdp IIF 요소 정상노출 확인
    Given "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00195,home_scrap_folder_item3","순서대로_클릭","1초","쉬고","pdp_together_view_tab","찾을때까지_스크롤","pdp_together_view_tab","클릭" 페이지 진입 및 확인
    Then "pdp_iif_img,pdp_iif_brand,pdp_iif_name,pdp_iif_sale_percent,pdp_iif_status,pdp_iif_badge"가"활성화","True" 확인 후 "pdp_top_btn,back_homeIcon_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00229 pdp IIF의 pdp진입 확인
    Given "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00195,home_scrap_folder_item3","순서대로_클릭","1초","쉬고","pdp_together_view_tab","찾을때까지_스크롤","pdp_together_view_tab,pdp_iif_img","순서대로_클릭" 페이지 진입 및 확인
    Then "pdp_buy_btn"가"활성화","True" 확인 후 "back_homeIcon_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00233 pdp IIF 상품 스크랩 확인
    Given "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00195,home_scrap_folder_item3","순서대로_클릭","1초","쉬고","pdp_together_view_tab","찾을때까지_스크롤","pdp_together_view_tab,shopping_home_scrap_btn","순서대로_클릭" 페이지 진입 및 확인
    Then "shopping_home_scrap_txt"가"활성화","True" 확인 후 "shopping_home_scrap_btn,pdp_top_btn,back_homeIcon_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00130 모음전 재료상품 옵션선택 레이어 확인
    Given "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00130,home_scrap_folder_item","순서대로_클릭","3초","쉬고","collection_pdp_option_btn","찾을때까지_스크롤","1회","아래로_스크롤","collection_pdp_option_btn","클릭","collection_pdp_option_menu_text","활성화" 페이지 진입 및 확인
    Then "collection_pdp_option_menu_text"가"활성화","True" 확인 후 "vk_fold_btn,pdp_top_btn,back_homeIcon_btn"를"순서대로_클릭"해서 홈화면 복귀


  @RT
  Scenario: comm_service00133 모음전 프로모션 배너를 통해 페이지이동 확인
    Given "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00130,home_scrap_folder_item","순서대로_클릭","2초","쉬고","pdp_promotion_banner","찾을때까지_스크롤","pdp_promotion_banner","클릭","pdp_promotion_banner_page_webview","활성화" 페이지 진입 및 확인
    Then "pdp_promotion_banner_page_webview"가"활성화","True" 확인 후 "back_home_btn_origin"를"클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00139 실시간베스트의 pdp 진입 확인
    Given "gnb_shopping_btn","클릭","shopping_home_best_btn","찾을때까지_스크롤","shopping_home_best_btn,shopping_home_best_real_best_tab,shopping_home_best_real_best_thumbnail","순서대로_클릭","2초","쉬고","pdp_buy_btn","활성화" 페이지 진입 및 확인
    Then "pdp_buy_btn"가"활성화","True" 확인 후 "back_homeIcon_btn,gnb_shopping_btn,gnb_home_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00151 기획전상세페이지에서 상품보기로 pdp 진입확인
    Given "gnb_shopping_btn","클릭","shopping_home_exhibition_detail_btn","찾을때까지_스크롤","shopping_home_exhibition_detail_btn","클릭","2초","쉬고","exhibition_product_view_btn,exhibition_product_view_thumbnail","순서대로_클릭","3초","쉬고","pdp_buy_btn","활성화" 페이지 진입 및 확인
    Then "pdp_buy_btn"가"활성화","True" 확인 후 "back_homeIcon_btn,gnb_shopping_btn,gnb_home_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00188 스타일링샷 게시물 신고 후 숨김처리 확인
#    Given "23020836","신고_삭제" 페이지 진입 및 확인
    Given "home_scrap_btn,home_scrap_folder_tab","순서대로_클릭","1회","아래로_스크롤","home_scrap_folder_00264,home_scrap_folder_item2","순서대로_클릭","pdp_styling_title_btn","찾을때까지_스크롤","pdp_styling_title_btn","클릭","pdp_styling_detail_img_1,cdp_more_btn2,report_btn,report_menu_1,bottom_sheet_report_btn","순서대로_클릭","brand_styling_report_complete_text","활성화","home_report_complete_page_btn","클릭" 페이지 진입 및 확인
    When "home_scrap_btn,home_scrap_folder_tab","순서대로_클릭","1회","아래로_스크롤","home_scrap_folder_00264,home_scrap_folder_item2","순서대로_클릭","pdp_styling_title_btn","찾을때까지_스크롤","pdp_styling_title_btn","클릭" 페이지 진입 및 확인
    Then "pdp_styling_detail_report_text_1"가"활성화","True" 확인 후 "back_btn,vk_fold_btn,vk_fold_btn,vk_fold_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00189 스타일링샷 게시물을 통해 유저홈 진입해서 유저 신고 후 숨김처리 확인
    Given "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00130,home_scrap_folder_item","순서대로_클릭","pdp_styling_title_btn","찾을때까지_스크롤","pdp_styling_title_btn","클릭","pdp_styling_detail_img_2,cdp_user_img_2,cdp_user_more_btn,cdp_user_more_report_btn,cdp_user_more_report_yes_btn,user_report_menu_1","순서대로_클릭","user_report_complete_text","활성화" 페이지 진입 및 확인
    When 앱 재시작
    When "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00130,home_scrap_folder_item","순서대로_클릭","pdp_styling_title_btn","찾을때까지_스크롤","pdp_styling_title_btn","클릭","pdp_styling_detail_report_text_1","활성화","pdp_styling_detail_report_text_1","클릭" 페이지 진입 및 확인
    Then "pdp_styling_detail_report_text_1"가"활성화","True" 확인 후 "back_btn,vk_fold_btn,vk_fold_btn,vk_fold_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00190 리뷰 신고 후 숨김처리 확인
    Given "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00130,home_scrap_folder_item,pdp_rating_bar,pdp_review_list_expand_btn,pdp_review_list_item_btn2,review_report_btn,report_menu_1,bottom_sheet_report_btn","순서대로_클릭" 페이지 진입 및 확인
    Then "report_complete_text"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00191 리뷰를 통해 유저홈 진입해서 유저 신고 후 숨김처리 확인
    Given "home_scrap_btn,home_scrap_folder_tab","순서대로_클릭","1회","아래로_스크롤","home_scrap_folder_00264,home_scrap_folder_item2,pdp_rating_bar","순서대로_클릭","review_user_img,review_user_more_btn,review_user_report_btn,review_user_report_confirm_btn,review_user_report_menu_1","순서대로_클릭","2초","쉬고","review_user_report_complete_text","활성화" 페이지 진입 및 확인
    When 앱 재시작
    When "home_scrap_btn,home_scrap_folder_tab","순서대로_클릭","1회","아래로_스크롤","home_scrap_folder_00264,home_scrap_folder_item2,pdp_rating_bar","순서대로_클릭","report_complete_text","활성화","report_complete_text","클릭" 페이지 진입 및 확인
    Then "report_complete_text"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00192 문의를 신고 후 숨김처리 확인
    Given "home_scrap_btn,home_scrap_folder_tab","순서대로_클릭","1회","아래로_스크롤","home_scrap_folder_00264,home_scrap_folder_item2","순서대로_클릭","pdp_question_btn","찾을때까지_스크롤","pdp_question_btn","클릭","pdp_question_report_btn","찾을때까지_스크롤","pdp_question_report_btn,report_menu_1,bottom_sheet_report_btn","순서대로_클릭","report_complete_text","활성화" 페이지 진입 및 확인
    Then "report_complete_text"가"활성화","True" 확인 후 "back_btn,vk_fold_btn,vk_fold_btn,vk_fold_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00194 브랜드홈 스타일링샷 신고 후 숨김처리 확인
    Given "home_scrap_btn,home_scrap_folder_tab","순서대로_클릭","1회","아래로_스크롤","home_scrap_folder_00264,home_scrap_folder_item2,pdp_brand_btn","순서대로_클릭","2초","쉬고","brand_home_styling_text,brand_home_styling_img,cdp_more_btn2,cdp_user_more_report_btn2,report_menu_1,bottom_sheet_report_btn,back_cdp_img_btn_report","순서대로_클릭","brand_report_complete_text","활성화" 페이지 진입 및 확인
    Then "brand_home_styling_img"가"활성화","True" 확인 후 "backIcon_btn,back_homeIcon_brand_page_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00195 브랜드홈 스타일링샷 유저 신고 후 숨김처리 확인
    Given "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00195,home_scrap_folder_item2,pdp_brand_btn","순서대로_클릭","2초","쉬고","brand_home_styling_text,brand_home_styling_img,cdp_user_img_2,cdp_user_more_btn,cdp_user_more_report_btn,cdp_user_more_report_yes_btn,user_report_menu_1,user_report_complete_text","순서대로_클릭" 페이지 진입 및 확인
    When 앱 재시작
    When "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00195,home_scrap_folder_item2,pdp_brand_btn","순서대로_클릭","2초","쉬고","brand_home_styling_text,brand_report_complete_text","순서대로_클릭" 페이지 진입 및 확인
    Then "brand_report_complete_text"가"활성화","True" 확인 후 "backIcon_btn,back_homeIcon_brand_page_btn"를"순서대로_클릭"해서 홈화면 복귀


  @RT
  Scenario: comm_service00344 쇼핑홈 바이너리샵 피쳐드브랜드 모듈 노출 및 페이지랜딩 확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","4초","쉬고","1회","아래로_조금_스크롤","3초","쉬고","binary_shop_brand_title","찾을때까지_조금씩_스크롤","binary_shop_brand_logo","찾을때까지_조금씩_스크롤","2초","쉬고","binary_shop_brand_logo","클릭","binary_shop_page_brand_title","활성화" 페이지 진입 및 확인
    Then "binary_shop_page_brand_title"가"활성화","True" 확인 후 "back_homeIcon_brand_page_btn,gnb_shopping_btn,binary_shop_shopping_tab,gnb_home_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00345 쇼핑홈 바이너리샵 피쳐드브랜드 모듈 상품리스트 노출 및 상품상세 진입 확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","4초","쉬고","binary_shop_brand_item_img","찾을때까지_조금씩_스크롤","binary_shop_brand_item_img","클릭","pdp_buy_btn","활성화" 페이지 진입 및 확인
    Then "pdp_buy_btn"가"활성화","True" 확인 후 "back_home_btn,gnb_shopping_btn,binary_shop_shopping_tab,gnb_home_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00328 쇼핑홈 바이너리샵 브랜드모듈에 스크랩버튼 노출확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","4초","쉬고","shopping_home_scrap_btn","찾을때까지_조금씩_스크롤","shopping_home_scrap_btn","활성화" 페이지 진입 및 확인
    Then "shopping_home_scrap_btn"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀


  @RT
  Scenario: comm_service00346 큐레이팅모듈 노출 확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","binary_curator_chip_carousel","찾을때까지_조금씩_스크롤","binary_curator_chip_carousel","활성화" 페이지 진입 및 확인
    Then "binary_curator_chip_carousel"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00348 큐레이팅모듈의 상품 선택 후 pdp 진입 확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","binary_curator_chip_carousel_item","찾을때까지_조금씩_스크롤","binary_curator_chip_carousel_item","클릭" 페이지 진입 및 확인
    Then "pdp_buy_btn"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00350 바이너리샵 카테고리 노출 및 진입 확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","binary_category_title","찾을때까지_스크롤","binary_category_menu_1","찾을때까지_조금씩_스크롤","binary_category_menu_1","클릭","binary_category_page_title","활성화" 페이지 진입 및 확인
    Then "binary_category_page_img"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00351 바이너리샵 바이너리픽 모듈의 상품상세 진입확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","binary_binary_pick_title","찾을때까지_스크롤","binary_binary_pick_brand_name","찾을때까지_조금씩_스크롤","binary_binary_pick_brand_name","클릭","pdp_buy_btn","활성화" 페이지 진입 및 확인
    Then "pdp_buy_btn"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00353 바이너리샵 매거진 모듈 노출 및 상세페이지 진입확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","binary_magazine_title","찾을때까지_스크롤","binary_magazine_img","찾을때까지_조금씩_스크롤","binary_magazine_img","클릭","pdp_buy_btn","활성화" 페이지 진입 및 확인
    Then "pdp_buy_btn"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀
  @RT
  Scenario: comm_service00354 바이너리샵 라인업 모듈 노출 및 상세페이지 진입확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","binary_lineup_title","찾을때까지_스크롤","binary_lineup_img","찾을때까지_조금씩_스크롤","binary_lineup_img","클릭","binary_shop_page_brand_title","활성화" 페이지 진입 및 확인
    Then "binary_shop_page_brand_title"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00355 바이너리샵 라인업 모듈 더보기 페이지 확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","binary_lineup_title","찾을때까지_스크롤","binary_lineup_more_btn","클릭","binary_lineup_more_page_title","활성화" 페이지 진입 및 확인
    Then "binary_lineup_more_page_list"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00359 바이너리샵 트렌딩 노출 확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","binary_trending_sub_title","찾을때까지_스크롤" 페이지 진입 및 확인
    Then "binary_trending_title"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00360 바이너리샵 트렌딩 상품 노출 확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","binary_trending_view_all_btn","찾을때까지_스크롤" 페이지 진입 및 확인
    Then "binary_shop_brand_item_img"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00365 바이너리샵 트렌딩 PLP 진입 후 상품노출 확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","binary_trending_view_all_btn","찾을때까지_스크롤","binary_trending_view_all_btn","클릭","binary_trending_plp_filter_btn","활성화" 페이지 진입 및 확인
    Then "binary_trending_plp_img,binary_trending_percent_text"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00366 바이너리샵 트렌딩 PLP 진입 필터동작 확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","binary_trending_view_all_btn","찾을때까지_스크롤","binary_trending_view_all_btn,binary_trending_all_tab_btn,binary_trending_plp_filter_2,binary_trending_plp_filter_2_1,close_btn","순서대로_클릭","binary_trending_plp_filter_2_1_product_name","활성화","binary_trending_plp_filter_btn","클릭" 페이지 진입 및 확인
    Then "binary_trending_plp_filter_1,binary_trending_plp_filter_2,binary_trending_plp_filter_3,binary_trending_plp_filter_4,binary_trending_plp_filter_5"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀


  @RT
  Scenario: comm_service00334 유저페이지의 스크랩탭 진입 후 브랜드로고 확인
    Given "큐에이버킷아이폰2"검색어로 srp 진입 후 "srp_user_tab,srp_user_list_name,user_scrap_tab_btn","순서대로_클릭" 스텝 진행
    Then "home_brand_scrap_logo,home_brand_scrap_text_logo"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00335 유저페이지의 스크랩탭 진입 후 브랜드 선택해서 브랜드홈 진입확인
    Given "큐에이버킷아이폰2"검색어로 srp 진입 후 "srp_user_tab,srp_user_list_name,user_scrap_tab_btn,home_brand_scrap_text_logo","순서대로_클릭","brand_home_brand_subtitle","활성화" 스텝 진행
    Then "brand_home_scrap"가"활성화","True" 확인 후 "back_homeIcon_brand_page_btn"를"클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00337 유저페이지의 스크랩탭 진입 후 스크랩폴더에서 브랜드 로고 확인
    Given "큐에이버킷아이폰2"검색어로 srp 진입 후 "srp_user_tab,srp_user_list_name,user_scrap_tab_btn,user_scrap_btn,all_scrap_tab_btn","순서대로_클릭","home_scrap_title","활성화" 스텝 진행
    Then "home_brand_scrap_logo,home_brand_scrap_text_logo"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @RT
  Scenario: comm_service00323 PDP ATF에서 브랜드 스크랩 동작확인
    Given "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00195,home_scrap_folder_item3","순서대로_클릭","pdp_atf_brand_logo","찾을때까지_스크롤","pdp_atf_brand_scrap","클릭","shopping_home_scrap_txt","활성화" 페이지 진입 및 확인
    Then "pdp_atf_brand_scrap"가"활성화","True" 확인 후 "pdp_atf_brand_scrap"를"클릭","5회"를"위로_스크롤","back_homeIcon_btn"를"클릭"해서 홈화면 복귀


  @RT
  Scenario: comm_service00325 PDP ATF에서 브랜드 홈 진입 후 스크랩 동작 확인
    Given "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00195,home_scrap_folder_item3,pdp_brand_btn,brand_home_scrap,brand_home_scrap_view_btn","순서대로_클릭","brand_scrap_tab","활성화" 페이지 진입 및 확인
    Then "brand_scrap_title"가"활성화","True" 확인 후 "brand_scrap_btn,back_imageview_btn,back_homeIcon_brand_page_btn"를"순서대로_클릭"해서 홈화면 복귀


  @RT
  Scenario: comm_service00408 pdp/ddp 포토/영상 전체보기 페이지 및 리뷰뷰어 페이지 노출 확인
    Given "home_scrap_btn,home_scrap_folder_tab,home_scrap_folder_00130,home_scrap_folder_item","순서대로_클릭","3초","쉬고","pdp_rating_bar,review_more_img","순서대로_클릭","review_photo_page_title","활성화","review_photo_video_img","클릭","review_photo_video_review_user_icon","활성화","미실행","앱_재시작" 페이지 진입 및 확인
    When "home_scrap_btn,home_scrap_folder_tab","순서대로_클릭","1회","아래로_스크롤","home_scrap_folder_00264,home_scrap_folder_item2,pdp_rating_bar,review_more_img","순서대로_클릭","review_photo_page_title","활성화","review_photo_video_img","클릭" 페이지 진입 및 확인
    Then "review_photo_video_review_user_icon,review_photo_video_review_more_btn"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀


