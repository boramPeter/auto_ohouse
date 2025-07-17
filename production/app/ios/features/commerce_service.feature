Feature: commerce_service Prod

  @Prod
  Scenario: commerce_service00001 쇼핑홈에서 검색페이지 정상노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "ad_close_btn"를 "광고_제거_클릭" 하고 "shopping_search_btn"을 "클릭"해서 쇼핑홈 검색페이지 진입
    Then "shopping_search_page_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 검색 페이지가 정상노출된지 체크. 그 후 "back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: commerce_service00002 쇼핑홈에서 배너 선택 후 페이지 정상노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "ad_close_btn"를 "광고_제거_클릭" 하고 "shopping_banner_btn"을 "클릭"해서 쇼핑홈 배너페이지 진입
    Then "shopping_banner_page" 이 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 배너 페이지가 정상노출된지 체크. 그 후 "back_btn" "클릭", "ad_close_btn"를 "광고_제거_클릭" 하고 "gnb_home_btn" 를 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: commerce_service00003 쇼핑홈에서 아이템 캐러셀, 칩 캐러셀 정상노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "1회","아래로_스크롤" 후 다음스텝 진행
    When "shopping_carousel_item_list","찾을때까지_스크롤" 후 다음스텝 진행
    Then "shopping_suggest_chip", "shopping_today_deal_chip", "shopping_carousel_item_list" 이 "활성화"된지 확인하고 "[True, True, True]" 된지 확인하여 쇼핑홈 캐래설이 정상노출된지 체크. 그 후 "gnb_shopping_btn","gnb_home_btn" 을 "클릭"하여 홈화면 복귀


  @Prod
  Scenario: commerce_service00004 쇼핑홈에서 카테고리 진입 후 1~4뎁스 카테고리 노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "ad_close_btn"를 "광고_제거_클릭" 하고 "6회","위로_스크롤", "shopping_category_btn" "찾을때까지_스크롤","shopping_category_btn","shopping_category_expand_btn"을 순서대로 "클릭"해서 쇼핑홈 카테고리페이지 진입
    Then "shopping_category_1depth_title", "shopping_category_3depth_area" 이 "활성화"된지 확인하고 "[True, True]" 된지 확인하여 쇼핑홈 1~4뎁스가 정상노출된지 체크. 그 후 "back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: commerce_service00005 쇼핑홈 가구카테고리 에서 배너 선택 후 페이지 정상노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "shopping_first_category"를 "클릭"한 뒤에 "2초" "쉬고" "[140,140]"을 순서대로 "좌표_클릭"해서 쇼핑홈 배너 진입 "찾을때까지_스크롤"
    Then "shopping_banner_page"이 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 카테고리 배너가 정상노출된지 체크. 그 후 "앱_재시작" 하여 홈화면 복귀

  @Prod
  Scenario: commerce_service00006 쇼핑홈 가구카테고리 에서 md's pick 선택 후 pdp 정상노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "ad_close_btn"를 "광고_제거_클릭" 하고 "shopping_first_category"를 "클릭"한 뒤에 "shopping_category_filter_title"가 "찾을때까지_조금씩_스크롤" 한 뒤에 "shopping_category_mds_pick_img" "클릭"해서 mds pick의 pdp 진입 "찾을때까지_스크롤"
    Then "pdp_buy_btn"이 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 mds pick의 pdp가 정상노출된지 체크. 그 후 "back_home_btn","ad_close_btn"를 "광고_제거_클릭" 하고 "gnb_home_btn" 를 순서대로 "1초클릭"하여 홈화면 복귀

  @Prod
  Scenario: commerce_service00007 쇼핑홈 가구카테고리 에서 필터 선택 후 필터 레이어 정상노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "ad_close_btn"를 "광고_제거_클릭" 하고 "shopping_first_category"를 "클릭"한 뒤에 "shopping_category_filter_btn"가 "찾을때까지_스크롤" 한 뒤에 "1회" "아래로_조금_스크롤" 후 "클릭"해서 카테고리 필터 노출 "찾을때까지_스크롤"
    Then "search_shopping_filter_order_text"이 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 카테고리 필터가 정상노출된지 체크. 그 후 "close_20_btn", "back_btn", "ad_close_btn"를 "광고_제거_클릭", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: commerce_service00008 쇼핑홈 가구카테고리 에서 상품리스트의 pdp 정상노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "ad_close_btn"를 "광고_제거_클릭" 하고 "shopping_first_category"를 "클릭"한 뒤에 "shopping_category_filter_btn"가 "찾을때까지_스크롤" 한 뒤에 "1회" "아래로_스크롤" 후 "shopping_category_list_pdp_img"가 "찾을때까지_조금씩_스크롤" 하고나서 "클릭"해서 카테고리 상품리스트의 pdp 진입 "찾을때까지_스크롤"
    Then "pdp_buy_btn"이 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 카테고리의 상품리스트 pdp가 정상노출된지 체크. 그 후 "back_home_btn" "클릭" 한 뒤에 "광고_제거_클릭" 하고 "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: commerce_service00009 쇼핑홈 아이템리스트에서 pdp 정상진입 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "ad_close_btn"를 "광고_제거_클릭" 하고 "1회","아래로_조금_스크롤", "shopping_carousel_item_list"를 "찾을때까지_스크롤" 한 뒤에 "클릭" 해서 아이템캐러셀 pdp 진입
    Then "pdp_buy_btn"이 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 아이템캐러셀 상품리스트 pdp가 정상노출된지 체크. 그 후"앱_재시작"하여 홈화면 복귀

  Scenario: commerce_service00010 쇼핑홈 아이템리스트에서 오늘의 추천상품 노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "shopping_ad_title"를 "찾을때까지_스크롤" 한 뒤에 아이템캐러셀에서 오늘의 추천상품 타이틀에서 멈춤
    Then "shopping_ad_title"가 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 아이템캐러셀 오늘의 추천상품 광고가 정상노출된지 체크. 그 후 "gnb_shopping_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: commerce_service00011 쇼핑홈 아이템리스트에서 BEST 노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "ad_close_btn"를 "광고_제거_클릭" 하고 "shopping_best_title"를 "찾을때까지_스크롤" 한 뒤에 아이템캐러셀에서 BEST메뉴에서 멈춤
    Then "shopping_best_title"가 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 아이템캐러셀 BEST메뉴가 정상노출된지 체크. 그 후 "gnb_shopping_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: commerce_service00012 쇼핑홈 아이템리스트에서 오늘의딜 메뉴 노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "shopping_today_deal_title"를 "찾을때까지_스크롤" 한 뒤에 아이템캐러셀에서 오늘의딜메뉴에서 멈춤
    Then "shopping_today_deal_title"가 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 아이템캐러셀 오늘의딜메뉴가 정상노출된지 체크. 그 후 "gnb_shopping_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  Scenario: commerce_service00014 쇼핑홈 오늘의딜 더보기 노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "shopping_today_deal_title"를 "찾을때까지_스크롤" 한 뒤에 아이템캐러셀 오늘의딜 타이틀에서 멈춤
    When "shopping_more_btn"를 "찾을때까지_스크롤" 한 뒤에 "클릭"해서 아이템캐러셀에서 오늘의딜메뉴의 더보기 진입
    Then "shopping_today_deal_page_title"가 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 아이템캐러셀 오늘의딜 상세페이지가 정상노출된지 체크. 그 후 "back_btn","ad_close_btn"를 "광고_제거_클릭","gnb_shopping_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  Scenario: commerce_service00017 쇼핑홈 인기검색어 노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "10회"만큼 "아래로_스크롤"해서 쇼핑홈 인기검색어 스크롤 준비
    When "shopping_popular_search_title"를 "찾을때까지_스크롤" 한 뒤에 아이템캐러셀 실시간인기검색어 타이틀에서 멈춤
    Then "shopping_popular_search_title"가 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 아이템캐러셀 실시간인기검색어가 정상노출된지 체크. 그 후 "gnb_shopping_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  Scenario: commerce_service00018 쇼핑홈 광고카테고리1 노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "10회"만큼 "아래로_스크롤"해서 쇼핑홈 광고 카테고리1 스크롤 준비
    When "shopping_category_ad_title"를 "찾을때까지_스크롤" 한 뒤에 아이템캐러셀 광고카테고리1 타이틀에서 멈춤
    Then "shopping_category_ad_title"가 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 아이템캐러셀 광고카테고리1이 정상노출된지 체크. 그 후 "gnb_shopping_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  Scenario: commerce_service00019 쇼핑홈 광고카테고리2 노출 확인
    Given 홈화면에서 "gnb_shopping_btn"을 "클릭"해서 쇼핑홈 페이지 진입 확인
    When "10회"만큼 "아래로_조금씩_스크롤"해서 쇼핑홈 광고 카테고리2 스크롤 준비
    When "shopping_category_ad_title"를 "찾을때까지_스크롤" 한 뒤에 한번더 반복해서 아이템캐러셀 광고카테고리2 타이틀에서 멈춤
    Then "shopping_category_ad_title"가 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑홈 아이템캐러셀 광고카테고리2가 정상노출된지 체크. 그 후 "gnb_shopping_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀
