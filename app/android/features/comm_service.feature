Feature: comm_service ST,RT

  @개별
  Scenario: 00000 커머스서비스 개별실행 사전조건
    Given 저장권한 허용
    Given 휴대폰인증 포함 기본정보 셋팅

  @RT
  Scenario: comm_service00362 바이너리샵 트렌딩 상품 스크랩 동작 확인
    Given "gnb_shopping_btn,binary_shop_tab","순서대로_클릭","binary_trending_view_all_btn","찾을때까지_스크롤","binary_trending_tab_2,shopping_home_scrap_btn","순서대로_클릭" 페이지 진입 및 확인
    Then "shopping_home_scrap_btn"가"체크_활성화","True" 확인 후 "shopping_home_scrap_btn,binary_trending_tab_1,gnb_shopping_btn,binary_shop_shopping_tab,gnb_home_btn"를"순서대로_클릭"해서 홈화면 복귀

  @RT
  Scenario: comm_service00415 DDP 옵션셀렉터에 쿠폰받기 노출확인
    Given "https://ozip.qa-web.dailyhou.se/HpVwa5Z?af","삼성브라우저_링크_이동","market_cancel_btn","광고_제거_클릭","[750,1200]","좌표_클릭","3초","쉬고","pdp_buy_btn,ddp_option_expand_btn,ddp_option_coupon_txt","순서대로_클릭" 페이지 진입 및 확인
    Then "ddp_option_coupon_download_btn"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀
