Feature: o2o Prod

  @Prod
  Scenario: o2o00001 o2o에서 주거공간 시공 페이지 정상노출 확인
    Given "gnb_o2o_btn","클릭","3초","쉬고","o2o_house_construction_menu_btn","클릭","3초","쉬고","o2o_house_construction_menu_ad_txt","활성화" 페이지 진입 및 확인
#    Given 홈화면에서 "gnb_o2o_btn","클릭","o2o_house_construction_menu_btn"를 "클릭"해서 주거공간 시공페이지 진입 확인 "[344,197]","좌표_클릭","3초","쉬고","o2o_house_construction_menu_ad_txt","활성화"
    Then "o2o_house_construction_menu_ad_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 주거시공 페이지가 정상노출된지 체크. 그 후 "back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: o2o00004 o2o에서 자재랭킹 페이지 정상노출 확인
    Given 홈화면에서 "gnb_o2o_btn","클릭","2회","아래로_스크롤","o2o_all_menu_btn","클릭"해서 o2o 자재랭킹 페이지 진입 확인
    When "o2o_material_ranking_menu_btn","클릭"해서 o2o 자재랭킹 페이지 진입 확인
    Then "o2o_my_material_list" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 자재랭킹 페이지가 정상노출된지 체크. 그 후 "o2o_back_home_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: o2o00005 o2o에서 계약서진단 페이지 정상노출 확인
    Given 홈화면에서 "gnb_o2o_btn","클릭","3초","쉬고","o2o_all_menu_btn","찾을때까지_스크롤","o2o_all_menu_btn","클릭"해서 o2o 계약서진단 페이지 진입 확인
    When "o2o_contract_diagnosis_menu_btn","클릭"해서 o2o 계약서진단 페이지 진입 확인
    Then "o2o_contract_diagnosis_page_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 계약서진단 페이지가 정상노출된지 체크. 그 후 "back_btn","gnb_o2o_btn","gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  
  Scenario: o2o00006 o2o에서 견적계산기 페이지 정상노출 확인
    Given 홈화면에서 "gnb_o2o_btn","클릭","3초","쉬고","o2o_all_menu_btn","찾을때까지_스크롤","o2o_all_menu_btn","클릭"해서 o2o 견적계산기 페이지 진입 확인
    When "o2o_quote_calculator_menu_btn","클릭"해서 o2o 견적계산기 페이지 진입 확인
    Then "o2o_quote_calculator_page_title" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 견적계산기 페이지가 정상노출된지 체크. 그 후 "back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  
  Scenario: o2o00007 o2o에서 이사 페이지 정상노출 확인
    When 홈화면에서 "gnb_o2o_btn","o2o_move_menu_btn"를 "클릭"해서 o2o 이사 페이지 진입 확인
    Then "o2o_move_page_btn_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 이사 페이지가 정상노출된지 체크. 그 후 "back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  
  Scenario: o2o00008 o2o에서 입주청소 페이지 정상노출 확인
    When 홈화면에서 "gnb_o2o_btn","o2o_move_in_clean_menu_btn"를 "클릭"해서 o2o 입주청소 페이지 진입 확인
    Then "o2o_move_in_clean_menu_page_btn" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 입주청소 페이지가 정상노출된지 체크. 그 후 "back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  
  Scenario: o2o00009 o2o에서 제품설치 페이지 정상노출 확인
    When 홈화면에서 "gnb_o2o_btn","o2o_product_installation_menu_btn"를 "클릭"해서 o2o 제품설치 페이지 진입 확인
    Then "o2o_product_installation_page_btn" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 제품설치 페이지가 정상노출된지 체크. 그 후 "back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  
  Scenario: o2o00010 o2o에서 집보기 체크리스트 페이지 정상노출 확인
    When 홈화면에서 "gnb_o2o_btn"를 "클릭"해서 o2o 전체서비스 페이지 진입 확인
    When "o2o_all_menu_btn"를 "클릭" 해서 전체서비스 페이지 진입 확인
    When "1회"만큼 "아래로_스크롤"해서 집보기 체크리스트 노출 확인
    When "o2o_home_viewing_checklist_btn"를 "클릭" 해서 집보기 체크리스트 페이지 진입 확인
    When "o2o_ad_popup_close"가 보이면 "광고_제거_클릭" 해서 집보기 체크리스트 바텀시트를 제거
    Then "o2o_home_viewing_checklist_bottom_btn" 이 "활성화"된지 확인하고 "True" 된지 확인하여 o2o 집보기 체크리스트 페이지가 정상노출된지 체크. 그 후 "o2o_back_home_btn"를 "클릭"하여 홈화면 복귀

  
  Scenario: o2o00011 o2o에서 아파트 시공사례 페이지 정상노출 확인
    When 홈화면에서 "gnb_o2o_btn"를 "클릭"해서 o2o 페이지 진입 확인(아파트 시공사례)
    When "o2o_all_menu_btn"를 "클릭"해서 전체서비스 페이지 진입 확인(아파트 시공사례)
    When "1회"만큼 "아래로_스크롤"해서 아파트 시공사례 노출 확인
    When "o2o_apt_construction_example_btn"를 "클릭"해서 아파트 시공사례 페이지 진입 확인
    Then "o2o_nearby_apt_list_txt"이 "활성화"된지 확인하고 "True"된지 확인하여 o2o 아파트 시공사례 페이지가 정상노출된지 체크. 그 후 "o2o_back_home_btn"를 "클릭"하여 홈화면 복귀

  
  Scenario: o2o00012 o2o에서 주거공간 시공 페이지의 시공업체탭 정상노출 확인
    Given 홈화면에서 "gnb_o2o_btn","o2o_house_construction_menu_btn"를 "클릭"해서 주거공간 시공페이지 진입 확인
    When "o2o_ad_popup_close"가 보이면 "광고_제거_클릭" 해서 주거공간 시공페이지의 광고를 제거 후 "2초"를 "쉬고" 마무리
    Then "o2o_house_construction_menu_ad_txt"이 "활성화"된지 확인하고 "True"된지 확인하여 주거시공 페이지의 시공업체탭이 정상노출된지 체크. 그 후 "back_btn","gnb_home_btn"를 순서대로 "클릭"하여 홈화면 복귀

  
  Scenario: o2o00013 o2o에서 주거공간 시공 페이지의 시공사례탭 정상노출 확인
    Given 홈화면에서 "gnb_o2o_btn","o2o_house_construction_menu_btn"를 "클릭"해서 주거공간 시공페이지 진입 확인
    When "[145,120]"를 "좌표_클릭" 해서 시공사례 탭 진입
    Then "o2o_construction_example_tab_page_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 주거시공 페이지의 시공사례탭이 정상노출된지 체크. 그 후 "back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  
  Scenario: o2o00014 o2o에서 주거공간 시공 페이지의 간편매칭탭 정상노출 확인
    Given 홈화면에서 "gnb_o2o_btn","o2o_house_construction_menu_btn"를 "클릭"해서 주거공간 시공페이지 진입 확인
    When "[320,120]"를 "좌표_클릭" 해서 간편매칭 탭 진입
    Then "o2o_easy_matching_tab_page_btn" 이 "활성화"된지 확인하고 "True" 된지 확인하여 주거시공 페이지의 간편매칭탭이 정상노출된지 체크. 그 후 "back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

 
  Scenario: o2o00015 o2o에서 주거공간 시공 페이지의 부분시공탭 정상노출 확인
    Given 홈화면에서 "gnb_o2o_btn","o2o_house_partial_menu_btn"를 "클릭"해서 주거공간 시공페이지 진입 확인
    Then "o2o_partial_construction_tab_page_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 주거시공 페이지의 부분시공탭이 정상노출된지 체크. 그 후 "back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

  # 15 케이스 백업
#  Scenario: o2o00015 o2o에서 주거공간 시공 페이지의 부분시공탭 정상노출 확인
#    Given 홈화면에서 "gnb_o2o_btn","o2o_house_construction_menu_btn"를 "클릭"해서 주거공간 시공페이지 진입 확인
#    When "[330,120]"를 "좌표_클릭" 해서 부분시공 탭 진입
#    Then "o2o_partial_construction_tab_page_txt" 이 "활성화"된지 확인하고 "True" 된지 확인하여 주거시공 페이지의 부분시공탭이 정상노출된지 체크. 그 후 "back_btn", "gnb_home_btn" 를 순서대로 "클릭"하여 홈화면 복귀

