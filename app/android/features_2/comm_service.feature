Feature: comm_service ST,RT
  @개별
  Scenario: 00000 커머스서비스 개별실행 사전조건
    Given 2번 계정으로 로그인한 상태 (로그아웃 상태가 아니라면 로그아웃 케이스 적용)

  @ST
  Scenario: 00221 칩 캐러셀 정상노출 확인
#    Given 저장권한 허용
    Given 151986 상품 pdp 진입한 상태
    When https://store-mobile.qa.dailyhou.se/v1/shopping-home api로 칩 캐러셀 리스트 파싱
    Then 칩 정상적으로 노출되는지 확인


  Scenario: comm_service00400 PDP에서 패키지담기 버튼 노출 확인
    Given "home_scrap_btn,home_scrap_folder_tab","순서대로_클릭","home_scrap_folder_00083","찾을때까지_스크롤","home_scrap_folder_00083,home_scrap_folder_item,pdp_glinda_btn","순서대로_클릭" 페이지 진입 및 확인
    Then "pdp_glinda_option_layer,pdp_glinda_coupon_layer,pdp_glinda_put_cart_text_layer,pdp_glinda_put_package_btn_layer"가"활성화","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

