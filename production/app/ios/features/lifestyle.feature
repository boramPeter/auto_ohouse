Feature: lifestyle Prod

  Scenario: lifestyle00002 둘러보기에서 추천해시태그 노출 확인
    When 홈화면에서 "gnb_life_style_btn"를 "클릭"한 뒤에 둘러보기 페이지 진입
    Then "any_hash_tag"가 "활성화" 된지 확인 후 "True"와 비교해서 둘러보기에서 임의의 해시태그가 정상노출 된지 확인. 그 후 "gnb_home_btn"을 "클릭"하여 홈화면 복귀

  Scenario: lifestyle00003 둘러보기 집들이 탭에서 집들이 상세페이지 진입확인
    When 홈화면에서 "gnb_life_style_btn","houses_tab","houses_tab_img_btn" 를 순서대로 "클릭" 해서 집들이 상세페이지 진입
    Then "follow_btn"이 "활성화" 된지 확인 후 "True"와 비교해서 집들이의 CDP 정상노출 된지 확인. 그 후 "back_btn", "awesome_find_tab", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀


  Scenario: lifestyle00004 둘러보기 집사진 탭에서 집사진 상세페이지 진입확인
    When 홈화면에서 "gnb_life_style_btn", "house_pic_tab"를 "클릭"하고 "[120,300]"를 "좌표_클릭" 한 뒤에 집사진 상세 페이지 진입
    Then "follow_txt_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 집사진의 CDP가 정상노출 된지 확인. 그 후 "back_btn", "awesome_find_tab", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  Scenario: lifestyle00005 둘러보기 살림수납 탭에서 살림수납 정상노출 확인
#    When 홈화면에서 "gnb_life_style_btn", "household_storage_tab"를 순서대로 "클릭" 해서 살림수납 탭 진입 후 "1초" "쉬고" "life_style_bottom_sheet_close_btn"를 "광고_제거_클릭" 해서 광고를 제거함.
    When 홈화면에서 "gnb_life_style_btn", "bottom_sheet_expand_btn","household_storage_tab_modal"를 순서대로 "클릭" 해서 살림수납 탭 진입 후 "1초" "쉬고" "life_style_bottom_sheet_close_btn"를 "광고_제거_클릭" 해서 광고를 제거함.
    Then "household_storage_tab_img_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 살림수납 페이지가 정상노출 된지 확인. 그 후 "bottom_sheet_expand_btn","life_style_channel_tab_modal", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  Scenario: lifestyle00006 둘러보기 콜렉터블 탭에서 콜렉터블 페이지 정상노출 확인
#    When 홈화면에서 "gnb_life_style_btn", "collectable_tab"를 순서대로 "클릭" 해서 콜렉터블 탭 진입
    When 홈화면에서 "gnb_life_style_btn", "bottom_sheet_expand_btn","collectable_tab_modal"를 순서대로 "클릭" 해서 콜렉터블 탭 진입
    Then "collectable_tab_img_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 콜렉터블 페이지가 정상노출 된지 확인. 그 후 "bottom_sheet_expand_btn","life_style_channel_tab_modal", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  Scenario: lifestyle00007 둘러보기 홈스토랑 탭에서 홈스토랑 페이지 정상노출 확인
#    When 홈화면에서 "gnb_life_style_btn" 다음 "[300,120,40,120]" 만큼 "스와이프" 하고 "homestaurant_tab"를 순서대로 "클릭" 해서 홈스토랑 탭 진입
    When 홈화면에서 "gnb_life_style_btn", "bottom_sheet_expand_btn","homestaurant_tab_modal"를 순서대로 "클릭" 해서 홈스토랑 탭 진입
    Then "homestaurant_tab_img_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 홈스토랑 페이지가 정상노출 된지 확인. 그 후 "bottom_sheet_expand_btn","life_style_channel_tab_modal", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  Scenario: lifestyle00008 둘러보기 핫플레이스 탭에서 핫플레이스 페이지 정상노출 확인
#    When 홈화면에서 "gnb_life_style_btn" 다음 "[300,120,40,120]" 만큼 "스와이프" 하고 "hot_place_tab"를 순서대로 "클릭" 해서 핫플레이스 탭 진입
    When 홈화면에서 "gnb_life_style_btn", "bottom_sheet_expand_btn","hot_place_tab_modal"를 순서대로 "클릭" 해서 핫플레이스 탭 진입
    Then "hot_place_tab_img_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 핫플레이스 페이지가 정상노출 된지 확인. 그 후 "bottom_sheet_expand_btn","life_style_channel_tab_modal", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  Scenario: lifestyle00009 둘러보기 육아 탭에서 육아 페이지 정상노출 확인
#    When 홈화면에서 "gnb_life_style_btn" 다음 "[300,120,40,120]" 만큼 "스와이프"를 두번 하고 "parenting_tab"를 순서대로 "클릭" 해서 육아 탭 진입
    When 홈화면에서 "gnb_life_style_btn", "bottom_sheet_expand_btn","parenting_tab_modal"를 순서대로 "클릭" 해서 육아 탭 진입
    Then "parenting_tab_img_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 육아 페이지가 정상노출 된지 확인. 그 후 "bottom_sheet_expand_btn","life_style_channel_tab_modal", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  Scenario: lifestyle00010 둘러보기 플랜테리어 탭에서 플랜테리어 페이지 정상노출 확인
#    When 홈화면에서 "gnb_life_style_btn" 다음 "[300,120,40,120]" 만큼 "스와이프"를 두번 하고 "planterior_tab"를 순서대로 "클릭" 해서 플랜테리어 탭 진입
    When 홈화면에서 "gnb_life_style_btn", "bottom_sheet_expand_btn","planterior_tab_modal"를 순서대로 "클릭" 해서 플랜테리어 탭 진입
    Then "planterior_tab_img_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 플랜테리어 페이지가 정상노출 된지 확인. 그 후 "bottom_sheet_expand_btn","life_style_channel_tab_modal", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀


  Scenario: lifestyle00011 둘러보기 반려동물 탭에서 반려동물 페이지 정상노출 확인
#    When 홈화면에서 "gnb_life_style_btn" 다음 "[300,120,40,120]" 만큼 "스와이프"를 두번 하고 "pet_tab"를 순서대로 "클릭" 해서 반려동물 탭 진입
    When 홈화면에서 "gnb_life_style_btn", "bottom_sheet_expand_btn","pet_tab_modal"를 순서대로 "클릭" 해서 반려동물 탭 진입
    Then "pet_tab_img_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 반려동물 페이지가 정상노출 된지 확인. 그 후 "bottom_sheet_expand_btn","life_style_channel_tab_modal", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  Scenario: lifestyle00012 둘러보기 캠핑 탭에서 캠핑 페이지 정상노출 확인
#    When 홈화면에서 "gnb_life_style_btn" 다음 "[300,120,40,120]" 만큼 "스와이프"를 세번 하고 "camping_tab"를 순서대로 "클릭" 해서 캠핑 탭 진입
    When 홈화면에서 "gnb_life_style_btn", "bottom_sheet_expand_btn","camping_tab_modal"를 순서대로 "클릭" 해서 캠핑 탭 진입
    Then "camping_tab_img_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 캠핑 페이지가 정상노출 된지 확인. 그 후 "bottom_sheet_expand_btn","life_style_channel_tab_modal", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  Scenario: lifestyle00013 둘러보기 취미 탭에서 취미 페이지 정상노출 확인
#    When 홈화면에서 "gnb_life_style_btn" 다음 "[300,120,40,120]" 만큼 "스와이프"를 세번 하고 "hobby_tab"를 순서대로 "클릭" 해서 취미 탭 진입
    When 홈화면에서 "gnb_life_style_btn", "bottom_sheet_expand_btn","hobby_tab_modal"를 순서대로 "클릭" 해서 취미 탭 진입
    Then "hobby_tab_img_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 취미 페이지가 정상노출 된지 확인. 그 후 "bottom_sheet_expand_btn","life_style_channel_tab_modal", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀


  Scenario: lifestyle00014 둘러보기 바텀시트에서 집들이 탭 진입확인
    When "gnb_life_style_btn","bottom_sheet_expand_btn","houses_tab_sheet" 를 순서대로 "클릭" 해서 바텀시트를 통해 집들이탭 진입
    Then "houses_tab_img_btn"이 "활성화" 된지 확인 후 "True"와 비교해서 집들이탭의 페이지가 정상노출 된지 확인. 그 후 "life_style_channel_tab", "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: lifestyle00015 꿀템발견 탭에서 칩 정상노출 확인 및 CDP 정상진입 확인
    Given "gnb_life_style_btn,awesome_find_tab","순서대로_클릭","awesome_find_favorite_chip","활성화","awesome_find_review_chip","활성화","awesome_find_should_buy_chip","활성화","community_category_all_chip","활성화","community_category_chip_review_text","클릭" 페이지 진입 및 확인
    Then "community_category_chip_page_follow"가"활성화","True" 확인 후 "back_btn,gnb_home_btn"를"순서대로_클릭"해서 홈화면 복귀

  @Prod
  Scenario: lifestyle00016 집꾸미기 탭에서 칩 정상노출 확인 및 CDP 정상진입 확인
    Given "gnb_life_style_btn,home_styling_tab","순서대로_클릭","awesome_find_favorite_chip","활성화","home_styling_tab_chip","활성화","home_styling_tab_remodeling_chip","활성화","community_category_all_chip","활성화","home_styling_tab_chip,community_category_chip_review_text","순서대로_클릭" 페이지 진입 및 확인
    Then "community_category_chip_page_follow"가"활성화","True" 확인 후 "back_btn,awesome_find_tab,gnb_home_btn"를"순서대로_클릭"해서 홈화면 복귀
