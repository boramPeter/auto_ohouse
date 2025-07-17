Feature: commerce_platform Prod

  @Prod
  Scenario: commerce_platform00001 pdp에서 상품담은뒤에 장바구니에 정상적으로 담기는지 확인
    Given 홈화면에서 "home_top_cart_btn"를 "클릭"한 뒤에 "만약" "cart_item_delete_btn"가 "활성화"되어있으면 "cart_item_delete_btn"를 "클릭1" "[283,455]"을 "좌표_클릭"해서 담겨있는 상품 제거 후 "back_btn"을 "클릭" 하여 홈화면 복귀
    When 홈화면에서 "home_top_scrap_btn"를 "클릭"한뒤에 스크랩화면 노출 확인
    When 스크랩화면에서 "만약","home_scrap_img_btn2"가 "활성화"되어있다면 "home_scrap_img_btn"를 "클릭1"하고"[30,744]"을 "좌표_클릭"한뒤에 "back_home_btn"을 "클릭2" 하여 홈화면 복귀
    When 스크랩화면 진입 후 "home_scrap_img_btn"을 "클릭"해서 pdp 페이지 진입 "home_top_scrap_folder_all_btn"
    When "home_top_scrap_btn,home_top_scrap_btn,home_scrap_img_btn","if_순서대로_클릭",pdp에서 "pdp_buy_btn" 을 "1초클릭" 하고 "2초" "쉬고" "pdp_option_btn"를 "1초클릭" 하고 "2초" "쉬고" "pdp_detail_option_btn", "pdp_put_cart_btn", "pdp_go_cart_btn"를 순서대로 "1초클릭"해서 장바구니에 담은 뒤 장바구니 진입
    Then "cart_item_delete_btn" 이 "활성화"된지 확인하고 "True" 된지 확인하여 장바구니에 상품이 담긴지 체크. 그 후 "cart_item_delete_btn"을 "클릭" 한뒤에 "[283,455]"을 "좌표_클릭"해서 담겨있는 상품 제거 후 "앱_재시작" 하여 홈화면 복귀

  @Prod
  Scenario: commerce_platform00003 pdp에서 바로구매로 주문서 진입되는지 확인
    When 홈화면에서 앱 간헐적 실패를 막기위한"앱_재시작"후,"home_top_scrap_btn"를 "클릭"한뒤에 스크랩화면 노출 확인
    When 스크랩화면 진입 후 "home_scrap_img_btn"을 "클릭"해서 pdp 페이지 진입 "home_top_scrap_folder_all_btn"
    When "home_top_scrap_btn,home_top_scrap_btn,home_scrap_img_btn","if_순서대로_클릭",pdp에서 "pdp_buy_btn","pdp_option_btn","pdp_detail_option_btn", "pdp_direct_buy_btn" 를 순서대로 "1초클릭"해서 주문서 진입
    Then "check_out_title" 이 "활성화"된지 확인하고 "True" 된지 확인하여 주문서 페이지 정상진입 확인. 그 후 "close_btn_checkout","check_out_confirm_btn", "back_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: commerce_platform00005 pdp에서 장바구니의 바로구매로 주문서 진입되는지 확인
    Given 홈화면에서 "home_top_cart_btn"를 "클릭"한 뒤에 "만약" "cart_item_delete_btn"가 "활성화"되어있으면 "cart_item_delete_btn"를 "클릭1" "[283,455]"을 "좌표_클릭"해서 담겨있는 상품 제거 후 "back_btn"을 "클릭" 하여 홈화면 복귀
    When 홈화면에서 "home_top_scrap_btn"를 "클릭"한뒤에 스크랩화면 노출 확인
    When 스크랩화면 진입 후 "home_scrap_img_btn"을 "클릭"해서 pdp 페이지 진입 "home_top_scrap_folder_all_btn"
    When "home_top_scrap_btn,home_top_scrap_btn,home_scrap_img_btn","if_순서대로_클릭",pdp에서 "pdp_buy_btn" 을 "1초클릭" 하고 "2초" "쉬고" "pdp_option_btn"를 "클릭" 하고 "2초" "쉬고" "pdp_detail_option_btn", "pdp_put_cart_btn", "pdp_go_cart_btn"를 순서대로 "클릭"해서 장바구니에 담은 뒤 장바구니 진입
    When "2초" "쉬고" 장바구니에서 "[250,750]"을 "좌표_클릭"해서 장바구니 -> 주문서 이동
    Then "check_out_title" 이 "활성화"된지 확인하고 "True" 된지 확인하여 장바구니를 통한 주문서 페이지 정상진입 확인. 그 후 "close_btn_checkout","check_out_confirm_btn"를 순서대로 "클릭"하고 "[345,115]" , "[283,455]" 만큼 "좌표_클릭" 실행 후 "앱_재시작"하여 홈화면 복귀 "close_btn_checkout","광고_제거_클릭"

  @Prod
  Scenario: commerce_platform00007 마이페이지 -> 주문배송 목록 페이지 정상노출 확인
    When 홈화면에서 "gnb_my_page_btn" 다음 "my_shopping_btn"를 순서대로 "클릭" 해서 마이페이지의 쇼핑탭 진입
    When "order_delivery_list_btn"을 "클릭" 해서 쇼핑탭의 주문배송 목록 페이지 진입
    Then "order_delivery_list_page_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 주문배송 목록 페이지 정상진입 확인. 그 후 "back_btn","prof_tab_btn", "gnb_home_btn"를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario Outline: commerce_platform00008 마이페이지 -> 주문배송 상태별로 페이지 노출 확인
    Given commerce_platform00008 결과값 확인해서 데이터셋 반복 여부 체크
    When 홈화면에서 "gnb_my_page_btn" 다음 "my_shopping_btn"를 순서대로 "클릭" 해서 마이페이지의 쇼핑탭 진입
    When "<locator1>"을 "<action1>" 해서 주문배송 상태페이지 진입
    Then "<check_locator>" 이 "<action2>"된지 확인하고 주문배송 상태페이지가 "<action_expected>" 인지 확인. 그 후 "<back_locator1>", "<back_locator2>" "<back_locator3>"를 순서대로 "<action1>"하여 홈화면 복귀

  Examples:
    | locator1                 |check_locator                | action1|action2 |action_expected| back_locator1|back_locator2|back_locator3|
    |order_delivery_status_btn1| order_delivery_list_page_txt|클릭    |활성화     |True            | back_btn|prof_tab_btn|gnb_home_btn  |
    |order_delivery_status_btn2| order_delivery_list_page_txt|클릭    |활성화     |True            | back_btn|prof_tab_btn|gnb_home_btn  |
    |order_delivery_status_btn3| order_delivery_list_page_txt|클릭    |활성화     |True            | back_btn|prof_tab_btn|gnb_home_btn  |
    |order_delivery_status_btn4| order_delivery_list_page_txt|클릭    |활성화     |True            | back_btn|prof_tab_btn|gnb_home_btn  |
    |order_delivery_status_btn5| order_delivery_list_page_txt|클릭    |활성화     |True            | back_btn|prof_tab_btn|gnb_home_btn  |

  @Prod
  Scenario: commerce_platform00009 마이페이지 -> 포인트 정상노출 확인
    When 홈화면에서 "gnb_my_page_btn" 다음 "my_shopping_btn"를 순서대로 "클릭" 해서 마이페이지의 쇼핑탭 진입
    When "my_page_point_btn"을 "클릭" 해서 쇼핑탭의 포인트 페이지 진입
    Then "my_page_point_page_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑탭 포인트 페이지 정상진입 확인. 그 후 "back_btn","prof_tab_btn", "gnb_home_btn"를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: commerce_platform00010 마이페이지 -> 쿠폰 정상노출 확인
    When 홈화면에서 "gnb_my_page_btn" 다음 "my_shopping_btn"를 순서대로 "클릭" 해서 마이페이지의 쇼핑탭 진입
    When "my_page_coupon_btn"을 "클릭" 해서 쇼핑탭의 쿠폰 페이지 진입
    Then "my_page_coupon_page" 이 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑탭 쿠폰 페이지 정상진입 확인. 그 후 "back_btn","prof_tab_btn", "gnb_home_btn"를 순서대로 "클릭"하여 홈화면 복귀

@Prod
  Scenario: commerce_platform00011 마이페이지 -> 회원등급 정상노출 확인
    When 홈화면에서 "gnb_my_page_btn" 다음 "my_shopping_btn"를 순서대로 "클릭" 해서 마이페이지의 쇼핑탭 진입
    When "my_page_grade_btn"을 "클릭" 해서 쇼핑탭의 회원등급 페이지 진입
    Then "my_page_grade_page_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 쇼핑탭 회원등급 페이지 정상진입 확인. 그 후 "back_btn","prof_tab_btn", "gnb_home_btn"를 순서대로 "클릭"하여 홈화면 복귀
