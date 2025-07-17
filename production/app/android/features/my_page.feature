Feature: my_page Prod

  @Prod
  Scenario: my_page00001 마이페이지 확인
    When 홈화면에서 "gnb_my_page_btn"를 "클릭"한 뒤에 마이페이지 진입
    Then "prof_img_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 마이페이지 정상노출 된지 확인. 그 후 "gnb_home_btn"을 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: my_page00002 마이페이지에서 쇼핑페이지 확인
    When 홈화면에서 "gnb_my_page_btn" 다음 "my_shopping_btn"를 순서대로 "클릭" 해서 마이페이지의 쇼핑탭 미노출 예외처리를 위한 "앱_재시작"
    When 홈화면에서 "gnb_my_page_btn" 다음 "my_shopping_btn"를 순서대로 "클릭" 해서 마이페이지의 쇼핑탭 진입
    Then "order_txt"가 "활성화" 된지 확인 후 "True"와 비교해서 마이페이지의 쇼핑탭이 정상노출 된지 확인. 그 후 "prof_tab_btn", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: my_page00003 마이페이지 쇼핑탭에서 나의리뷰 페이지 확인
    When 홈화면에서 "gnb_my_page_btn", "my_shopping_btn", "my_review_btn"를 순서대로 "클릭" 해서 나의리뷰 페이지 진입
    Then "write_my_review_text"가 "활성화" 된지 확인 후 "True"와 비교해서 쇼핑탭의 나의리뷰페이지가 정상노출 된지 확인. 그 후 "back_xpath_btn", "prof_tab_btn", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: my_page00004 마이페이지 설정-> 내정보수정 페이지 확인
    When 홈화면에서 "gnb_my_page_btn", "my_set_btn", "my_prof_edit_btn" 를 순서대로 "클릭" 해서 "3초" "쉬고" 내정보수정 페이지 진입 "my_prof_img_del_btn","활성화"
    Then "my_info_title"과 "my_prof_img_del_btn"가 "활성화" 된지 확인 후 "[True, True]"와 비교해서 내정보수정 페이지가 정상노출 된지 확인. 그 후 "back_xpath_btn_o2o","my_prof_set_back_btn","gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: my_page00005 마이페이지 설정 -> 알림설정 페이지 확인
    When 홈화면에서 "gnb_my_page_btn", "my_set_btn", "my_alarm_edit_btn" 를 순서대로 "클릭" 해서 알림설정 페이지 진입
    Then "my_alarm_edit_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 알림설정 페이지가 정상노출 된지 확인. 그 후 "back_homeIcon_btn", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: my_page00008 마이페이지 설정 -> 비밀번호변경 페이지 확인
    When 홈화면에서 "gnb_my_page_btn", "my_set_btn", "my_change_pw_btn" 를 순서대로 "클릭" 해서 비밀번호변경 페이지 진입
    Then "my_change_pw_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 비밀번호변경 페이지가 정상노출 된지 확인. 그 후 "back_imageview_btn", "my_prof_set_back_btn", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: my_page00011 마이페이지 쇼핑탭 -> 스크랩북 페이지 확인
    When 홈화면에서 "gnb_my_page_btn", "my_shopping_btn", "my_shopping_product_scrap_book" 를 순서대로 "클릭" 해서 상품 스크랩북 페이지 진입
    Then "home_top_scrap_page_title"가 "활성화" 된지 확인 후 "True"와 비교해서 상품 스크랩북 페이지가 정상노출 된지 확인. 그 후 "back_imageview_btn", "prof_tab_btn", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: my_page00012 마이페이지 쇼핑탭 -> 나의 문의내역 페이지 확인
    When 홈화면에서 "gnb_my_page_btn", "my_shopping_btn", "my_shopping_question_list" 를 순서대로 "클릭" 해서 나의 문의내역 페이지 진입 "1회","아래로_조금_스크롤"
    Then "non_question_text"가 "활성화" 된지 확인 후 "True"와 비교해서 나의 문의내역 페이지가 정상노출 된지 확인. 그 후 "backIcon_btn", "prof_tab_btn", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: my_page00015 마이페이지 쇼핑탭 -> 고객센터 페이지 확인
    When 홈화면에서 "gnb_my_page_btn", "my_shopping_btn", "my_shopping_customer_center" 를 순서대로 "클릭" 해서 고객센터 페이지 진입 후 "3초","쉬고","1회","아래로_스크롤","help_title","활성화"
    Then "help_title"가 "활성화" 된지 확인 후 "True"와 비교해서 고객센터 페이지가 정상노출 된지 확인. 그 후 "앱_재시작" 해서 홈 화면 복귀
