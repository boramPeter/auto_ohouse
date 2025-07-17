Feature: o2o Prod

  Scenario Outline: 00001 o2o에서 주거공간 시공 페이지 정상노출 확인
    Given 홈화면에서 "<locator1>"을 "<action1>"하고 "<locator2>"를 "<action2>"하고 "<locator3>"를 "<action3>"해서 o2o 페이지 진입 (func_name : "<func_id_step>")
    When "o2o_ad_popup_close"가 보이면 "광고_제거_클릭" 해서 주거공간 시공페이지의 광고를 제거
    Then "<locator_expected1>" 이 "<action_expected>"된지 확인하고 "<locator_expected2>"가 "<action_expected2>" "<action_expected>" 된지 확인. 그리고 두개가 "<expected>" 인지 확인. 그 후 "<back_locator1>", "<back_locator2>" "<back_locator3>"를 순서대로 "<action4>"하여 홈화면 복귀 (func_name : "<func_id_check>")

  Examples:
    | locator1   | action1 | locator2                      |action2| locator3|action3| locator_expected1                 | locator_expected2 | action_expected| action_expected2 |expected| back_locator1| back_locator2 | back_locator3 | action4 | func_id_step            |func_id_check         |
    |gnb_o2o_btn|클릭       |o2o_house_construction_menu_btn|클릭   | 미실행    |미실행    |o2o_house_construction_menu_ad_txt|    미실행            |활성화            | 미실행            |True    | backIcon_btn  | gnb_home_btn | 미실행          | 클릭     | prod_o2o00001_aos_step |prod_o2o00001_aos_check|


  @Prod
  Scenario: o2o00001 o2o에서 주거공간 시공 페이지 정상노출 확인
    Given "3초" "쉬고" 홈화면에서 "gnb_o2o_btn","o2o_house_construction_menu_btn"를 "클릭"해서 주거공간 시공페이지 진입 확인
    When "3초" "쉬고" "o2o_ad_popup_close"가 보이면 "광고_제거_클릭" 해서 주거공간 시공페이지의 광고를 제거
    Then "o2o_house_construction_menu_ad_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 주거시공 페이지가 정상노출된지 체크. 그 후 "o2o_back_btn"를 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: o2o00004 o2o에서 자재랭킹 페이지 정상노출 확인
    Given "3초","쉬고","gnb_o2o_btn","클릭","2초","쉬고","2회","아래로_스크롤","2초","쉬고","920,940","좌표_클릭" o2o 자재랭킹 페이지 진입 확인
    When "o2o_material_ranking_menu_btn","클릭" o2o 자재랭킹 페이지 진입 확인
    Then "o2o_my_material_list" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 자재랭킹 페이지가 정상노출된지 체크. 그 후 "back_xpath_btn_o2o", "o2o_back_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: o2o00005 o2o에서 계약서진단 페이지 정상노출 확인
    Given "gnb_o2o_btn","클릭","5초","쉬고","2회","아래로_스크롤","2초","쉬고","920,940","좌표_클릭","o2o_contract_diagnosis_menu_btn","활성화","o2o_contract_diagnosis_menu_btn","클릭","o2o_contract_diagnosis_page_txt","활성화" 페이지 진입 및 확인
#    When "o2o_contract_diagnosis_menu_btn","클릭" o2o 계약서진단 페이지 진입 확인
    Then "o2o_contract_diagnosis_page_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 계약서진단 페이지가 정상노출된지 체크. 그 후 "o2o_back_btn", "o2o_back_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: o2o00006 o2o에서 견적계산기 페이지 정상노출 확인
    Given "gnb_o2o_btn","클릭","2초","쉬고","2회","아래로_스크롤","2초","쉬고","920,940","좌표_클릭" o2o 견적계산기 페이지 진입 확인
    When "o2o_quote_calculator_menu_btn","클릭" o2o 견적계산기 페이지 진입 확인
    Then "o2o_quote_calculator_page_title" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 견적계산기 페이지가 정상노출된지 체크. 그 후 "backIcon_btn", "o2o_back_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: o2o00007 o2o에서 이사 페이지 정상노출 확인
    Given "gnb_o2o_btn","클릭","5초","쉬고","2회","아래로_스크롤","2초","쉬고","920,940","좌표_클릭","o2o_move_menu_btn","활성화","o2o_move_menu_btn","클릭","3초","쉬고","o2o_move_page_btn_txt","활성화" 페이지 진입 및 확인
#    When "o2o_move_menu_btn","클릭" o2o 이사 페이지 진입 확인
    Then "o2o_move_page_btn_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 이사 페이지가 정상노출된지 체크. 그 후 "back_imageview_btn", "o2o_back_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: o2o00008 o2o에서 입주청소 페이지 정상노출 확인
    Given "gnb_o2o_btn","클릭","2초","쉬고","o2o_move_in_clean_menu_btn","찾을때까지_스크롤","2초","쉬고","o2o_move_in_clean_menu_btn","클릭" o2o 입주청소 페이지 진입 확인 "o2o_move_in_clean_menu_page_btn","활성화"
#    When "o2o_move_in_clean_menu_btn","활성화" o2o 입주청소 페이지 진입 확인
    Then "o2o_move_in_clean_menu_page_btn" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 입주청소 페이지가 정상노출된지 체크. 그 후 "back_imageview_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: o2o00009 o2o에서 제품설치 페이지 정상노출 확인
    Given "gnb_o2o_btn","클릭","2초","쉬고","2회","아래로_스크롤","2초","쉬고","920,940","좌표_클릭" o2o 제품설치 페이지 진입 확인
    When "o2o_product_installation_menu_btn","클릭" o2o 제품설치 페이지 진입 확인
    Then "o2o_product_installation_page_btn" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 제품설치 페이지가 정상노출된지 체크. 그 후 "o2o_back_btn", "o2o_back_btn"를 순서대로 "클릭"하여 홈화면 복귀

  
  Scenario: o2o00010 o2o에서 집보기 체크리스트 페이지 정상노출 확인
    Given "gnb_o2o_btn","클릭","2초","쉬고","2회","아래로_스크롤","2초","쉬고","920,940","좌표_클릭" o2o 집보기 체크리스트 페이지 진입 확인
    When "1회"만큼 "아래로_스크롤"해서 집보기 체크리스트 노출 확인
    When "o2o_home_viewing_checklist_btn"를 "클릭" 해서 집보기 체크리스트 페이지 진입 확인
    When "o2o_ad_popup_close"가 보이면 "광고_제거_클릭" 해서 집보기 체크리스트 바텀시트를 제거
    Then "o2o_home_viewing_checklist_bottom_btn" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 집보기 체크리스트 페이지가 정상노출된지 체크. 그 후 "back_xpath_btn_o2o", "o2o_back_btn"를 순서대로 "클릭"하여 홈화면 복귀

  
  Scenario: o2o00011 o2o에서 아파트 시공사례 페이지 정상노출 확인
    Given "3초","쉬고","gnb_o2o_btn","클릭","2초","쉬고","3회","위로_스크롤","2회","아래로_스크롤","2초","쉬고","920,940","좌표_클릭" o2o 집보기 체크리스트 11케이스 페이지 진입 확인
    When "1회"만큼 "아래로_스크롤"해서 아파트 시공사례 노출 확인
    When "o2o_apt_construction_example_btn"를 "클릭" 해서 아파트 시공사례 페이지 진입 확인, "3초","쉬고"
    Then "o2o_nearby_apt_list_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 아파트 시공사례 페이지가 정상노출된지 체크. 그 후 "o2o_back_btn", "o2o_back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: o2o00012 o2o에서 주거공간 시공 페이지의 시공업체탭 정상노출 확인
    Given "3초" "쉬고" 홈화면에서 "gnb_o2o_btn","o2o_house_construction_menu_btn"를 "클릭"해서 주거공간 시공페이지 진입 확인
    When "3초" "쉬고" "o2o_ad_popup_close"가 보이면 "광고_제거_클릭" 해서 주거공간 시공페이지의 광고를 제거
    Then "o2o_house_construction_menu_ad_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 주거시공 페이지의 시공업체탭이 정상노출된지 체크. 그 후 "o2o_back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: o2o00013 o2o에서 주거공간 시공 페이지의 시공사례탭 정상노출 확인
    Given "3초" "쉬고" 홈화면에서 "gnb_o2o_btn","o2o_house_construction_menu_btn"를 "클릭"해서 주거공간 시공페이지 진입 확인
    When "1초" "쉬고" "o2o_ad_popup_close"가 보이면 "광고_제거_클릭" 해서 주거공간 시공페이지의 광고를 제거
    When "2초" "쉬고" "o2o_construction_example_tab"를 "클릭" 해서 시공사례 탭 진입
    Then "o2o_construction_example_tab_page_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 주거시공 페이지의 시공사례탭이 정상노출된지 체크. 그 후 "back_xpath_btn_o2o"를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: o2o00014 o2o에서 주거공간 시공 페이지의 간편매칭탭 정상노출 확인
    Given "3초" "쉬고" 홈화면에서 "gnb_o2o_btn","o2o_house_construction_menu_btn"를 "클릭"해서 주거공간 시공페이지 진입 확인
    When "o2o_easy_matching_tab"를 "클릭" 해서 간편매칭 탭 진입
    Then "o2o_easy_matching_tab_page_btn" 이 "활성화"된지 확인하고 "True" 된지 확인하여 주거시공 페이지의 간편매칭탭이 정상노출된지 체크. 그 후 "back_xpath_btn_o2o"를 순서대로 "클릭"하여 홈화면 복귀
