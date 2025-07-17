Feature: home Prod

  @Prod
  Scenario: home00014 home버튼을 눌러 홈화면 노출 확인
    When "gnb_home_btn"를 "클릭"한뒤에 홈화면 노출 확인
    Then "home_viewer_tab"와 "gnb_home_btn"가 "활성화" 된지 확인 후 "[True, True]"와 비교하여 홈화면이 정상노출되는지 확인

  @Prod
  Scenario: home00015 둘러보기 버튼을 눌러 홈화면 노출 확인
    When "gnb_life_style_btn"를 "클릭"한뒤에 "life_style_next_check_btn"가 노출되면 "광고_제거_클릭"을 하고 둘러보기 진입
    Then "awesome_find_tab"의 "텍스트확인"을 하고 "awesome_find_tab"가 "활성화" 된지 확인 후 "['꿀템발견', True]" 와 비교해서 정상노출되는지 확인. 그 후에 "gnb_home_btn"를 "클릭"하여 홈화면으로 복귀

  @Prod
  Scenario: home00016 쇼핑 버튼을 눌러 홈화면 노출 확인
    Given "gnb_shopping_btn"을 "클릭"한뒤에 "2초" "쉬고" "ad_close_btn"가 노출되면 "광고_제거_클릭"을 하고 쇼핑홈 진입 후 오세페 처리를 위한 "1회" "아래로_스크롤"
    Then "shopping_suggest_chip" 와 "scrap_btn"이 "활성화" 된지 확인 후 "[True, True]"와 비교해서 쇼핑홈이 정상노출되는지 확인. "ad_close_btn"가 노출되면 "광고_제거_클릭"을 한 뒤에 "gnb_home_btn"를 "클릭"하여 홈화면으로 복귀

  @skip
  Scenario: home00017 인테리어/생활 버튼을 눌러 홈화면 노출 확인
    When "gnb_o2o_btn"를 "클릭"한뒤에 o2o화면 노출 확인
    Then "o2o_apply_btn" 와 "o2o_all_menu_btn"이 "활성화" 된지 확인 후 "[True, True]"와 비교해서 o2o홈화면이 정상노출되는지 확인. 그 후 "gnb_home_btn"를 "클릭"하여 홈화면으로 복귀

  @Prod
  Scenario: home00019 스크랩 버튼을 눌러 스크랩북 페이지 확인
    When 홈화면에서 "home_top_scrap_btn"를 "클릭"한뒤에 스크랩화면 노출 확인
    Then "home_top_scrap_page_title"가 "활성화" 된지 확인 후 "True"와 비교해서 스크랩페이지가 정상노출되는지 확인. 그 후 "back_imageview_btn"를 "클릭"하여 홈화면으로 복귀

  @Prod
  Scenario: home00020 홈화면 알림페이지 확인
    When 홈화면에서 "home_noti_icon_btn"를 "클릭"한뒤에 알림페이지 노출 확인
    Then "title","alarm_tab","noti_event_tab"이 "활성화" 된지 확인 후 "[True, True, True]"와 비교해서 알림페이지가 정상노출되는지 확인. 그 후 "backIcon_btn"를 "클릭"하여 홈화면으로 복귀

  @Prod
  Scenario: home00021 마이페이지 - > 유저이미지 정상노출 확인
    When 홈화면에서 "gnb_my_page_btn" 다음 "prof_img_btn" 를 순서대로 "클릭"한뒤에 프로필이미지 확인 준비
    Then "prof_img_detail_view"가 "활성화" 된지 확인 후 "True"와 비교해서 프로필이미지 정상노출되는지 확인. 그 후 "prof_close_btn" 와 "gnb_home_btn"를 순서대로 "클릭"하여 홈화면으로 복귀

  @Prod
  Scenario: home00022 장바구니 - > 장바구니 페이지 확인
    Given 홈화면에서 "home_top_cart_btn"를 "클릭"한 뒤에 "만약" "cart_item_delete_btn"가 "활성화"되어있으면 "cart_item_delete_btn"를 "클릭1" "cart_item_delete_confirm_btn"을 "클릭2"해서 담겨있는 상품 제거 후 "closeIcon_btn"을 "클릭" 하여 홈화면 복귀
    When 홈화면에서 "home_top_cart_btn"를 "클릭"한뒤에 장바구니 진입,"cart_put_item_btn","활성화"
    Then "cart_put_item_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 장바구니페이지가 정상노출되는지 확인. 그 후 "closeIcon_btn"을 "클릭"하여 홈화면으로 복귀

  @Prod
  Scenario: home00026 홈 -> 우하단 플로팅버튼 눌러 메뉴 잘 뜨는지 확인
    When 홈화면에서 "home_floating_btn"를 "클릭"한뒤에 플로팅메뉴 노출시킴
    Then 플로팅메뉴에서 "home_floating_photo_menu","home_floating_video_menu","home_floating_review_menu","home_floating_interior_menu"가 "활성화" 된지 확인 후 "[True, True, True, True]"와 비교해서 플로팅메뉴가 정상노출되는지 확인. 그 후 "closeIcon_btn"을 "클릭"하여 플로팅메뉴 종료

  @Prod
  Scenario: home00043 홈화면 배너영역 노출확인
    When 홈화면에서 "home_main_banner"를 "찾을때까지_스크롤" 후 배너체크 준비
    Then 홈화면에서 "home_main_banner"가 "활성화" 된지 확인 후 "True"와 비교해서 메인배너가 정상노출되는지 확인 후 "gnb_home_btn"을 "클릭" 해서 홈화면 최상단 복귀

  @Prod
  Scenario: home00045 홈 -> 쿠폰 미리받기 선택 후 페이지 확인
    When 홈화면에서 "home_early_bird_btn"를 "클릭"한뒤에 쿠폰 미리받기 페이지 진입
    Then "home_early_bird_btn"가"요소미노출","True" 확인 후 "미실행"를"앱_재시작"해서 홈화면 복귀

  @Prod
  Scenario: home00046 홈 -> 오늘의딜 선택 후 페이지 확인
    When 홈화면에서 "home_today_deal_quick_menu"를 "클릭"한뒤에 오늘의딜 페이지 진입
    Then "home_today_deal_page_txt"가 "활성화" 된지 확인 후 "True"와 비교해서 오늘의딜 페이지 정상노출되는지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀 (페이지가 자주 바뀔수 있어 타이틀 요소로만 체크)


  @Prod
  Scenario: home00047 홈 -> 집들이 선택 후 페이지 확인
    When 홈화면에서 "home_houses_btn"를 "클릭"한뒤에 둘러보기 페이지의 집들이탭 진입
    Then "houses_tab"가 "활성화" 된지 확인 후 "True"와 비교해서 집들이탭 정상진입 확인. 그 후 "gnb_home_btn"다음 "gnb_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: home00048 홈 -> 행운출첵 선택 후 페이지 확인
    When 홈화면에서 "home_lucky_check_btn"를 "클릭"한뒤에 행운출첵 페이지 진입
    Then "home_lucky_check_title"가 "활성화" 된지 확인 후 "True"와 비교해서 행운출첵 페이지 정상노출되는지 확인. 그 후 "뒤로가기"하여 홈화면 복귀

  @Prod
  Scenario: home00049 홈 -> 챌린지참여 선택 후 페이지 확인
    When 홈화면에서 "1초" "쉬고" "[900,450,200,450]" 만큼 "스와이프"한 뒤에 다시 "1초" "쉬고" 그다음 "home_challenge_btn"을 "클릭" 하여 챌린지참여 페이지 진입
    Then "home_challenge_img"가 "활성화" 된지 확인 후 "True"와 비교해서 챌린지참여 페이지 정상노출되는지 확인. 그 후 "뒤로가기"하여 홈화면 복귀 후 "[200,450,900,450]" 만큼 "스와이프"

  Scenario: home00050 홈 -> 크리에이터 선택 후 페이지 확인
    When 홈화면에서 "1초" "쉬고" "[900,450,200,450]" 만큼 "스와이프"한 뒤에 다시 "1초" "쉬고" 그다음 "home_creator_btn"을 "클릭" 하여 크리에이터 페이지 진입
    Then "creator_img"가 "활성화" 된지 확인 후 "True"와 비교해서 크리에이터 페이지 정상노출되는지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀 후 "[200,450,900,450]" 만큼 "스와이프"

  @Prod
  Scenario: home00051 홈 -> 장보기 선택 후 페이지 확인
    When 홈화면에서 "1초" "쉬고" "[900,450,200,450]" 만큼 "스와이프"한 뒤에 다시 "1초" "쉬고" 그다음 "home_grocery_shopping_btn"을 "클릭" 하여 장보기 페이지 진입
    Then "title"가 "활성화" 된지 확인 후 "True"와 비교해서 장보기 페이지 정상노출되는지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀 후 "[200,450,900,450]" 만큼 "스와이프"

  @Prod
  Scenario: home00053 홈 -> 리모델링 선택 후 페이지 확인
    When 홈화면에서 "1초" "쉬고" "[900,450,200,450]" 만큼 "스와이프"한 뒤에 다시 "1초" "쉬고" 그다음 "home_remodeling_btn"을 "클릭" 하여 리모델링 페이지 진입
    Then "remodeling_request_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 리모델링 페이지 정상노출되는지 확인. 그 후 "back_xpath_btn_o2o"을 "클릭"하여 홈화면 복귀 후 "[200,450,900,450]" 만큼 "스와이프","1초",쉬고"

  @Prod
  Scenario: home00054 홈 -> 입주청소 선택 후 페이지 확인
    When 홈화면에서 "1초" "쉬고" "[900,450,200,450]" 만큼 "스와이프"한 뒤에 1번더 반복, 그다음 "home_clean_btn"을 "클릭" 하여 입주청소 페이지 진입 "3초","쉬고"
    Then "clean_moving_btn"가 "활성화" 된지 확인 후 "True"와 비교해서 입주청소 페이지 정상노출되는지 확인. 그 후 "back_imageview_btn"을 "클릭"하여 홈화면 복귀 후 "1초" "쉬고" 그다음 "[200,450,900,450]" 만큼 "스와이프"를 한번더 반복
