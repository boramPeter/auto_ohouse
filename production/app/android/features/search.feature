Feature: search Prod

  @Prod
  Scenario: search00001 통합검색에서 쇼핑 모듈 정상노출 확인
    Given 홈화면에서 "search_icon"를 "클릭"한다음 "search_text_box 요소에 삼성전자"를 "입력"하고 "search_vk_btn"를 "클릭"하여 SRP 진입
    Then "search_shopping_title"의 "텍스트확인" 하고나서 "쇼핑" 텍스트가 맞는지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: search00002 통합검색에서 쇼핑의 더보기를 눌러 쇼핑탭 진입 확인
    Given 홈화면에서 "search_icon"를 "클릭"한다음 "search_text_box 요소에 삼성전자"를 "입력"하고 "search_vk_btn"를 "클릭"하여 SRP 진입
    When "search_more_btn"만큼 "찾을때까지_조금씩_스크롤"해서 "search_more_btn" 버튼을 "클릭"
    Then "search_shopping_filter_btn"이 "활성화" 된지 확인하고 "True" 가 맞는지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀


  @Prod
  Scenario: search00003 통합검색에서 쇼핑의 더보기를 눌러 쇼핑탭 진입 후 필터뷰 노출 확인
    Given 홈화면에서 "search_icon"를 "클릭"한다음 "search_text_box 요소에 삼성전자"를 "입력"하고 "search_vk_btn"를 "클릭"하여 SRP 진입
    When "search_more_btn"만큼 "찾을때까지_조금씩_스크롤"해서 "search_more_btn" 버튼을 "클릭"
    When "search_shopping_filter_btn"을 "클릭" 해서 필터뷰를 노출시킴
    Then "search_shopping_filter_order_text"이 "활성화" 된지 확인하고 "True" 가 맞는지 확인. 그 후 "close_btn" , "back_home_btn"을 순서대로 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: search00004 통합검색에서 사진 모듈 정상노출 확인
    Given 홈화면에서 "search_icon"를 "클릭"한다음 "search_text_box 요소에 삼성전자"를 "입력"하고 "search_vk_btn"를 "클릭"하여 SRP 진입
    When "2회"만큼 "아래로_조금_스크롤"한 뒤에 "search_photo_title"을 "찾을때까지_스크롤" 해서 사진 타이틀을 찾기 시도
    Then "search_photo_title"의 "텍스트확인" 하고나서 쇼핑 텍스트가 아닌 "사진" 텍스트가 맞는지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: search00005 통합검색에서 사진 모듈의 더보기를 눌러 사진탭 진입 확인
    Given 홈화면에서 "search_icon"를 "클릭"한다음 "search_text_box 요소에 삼성전자"를 "입력"하고 "search_vk_btn"를 "클릭"하여 SRP 진입
    When "2회"만큼 "아래로_조금_스크롤"한 뒤에 "search_photo_title"을 "찾을때까지_스크롤" 해서 사진 타이틀을 찾기 시도
    When "search_more_btn"을 "찾을때까지_조금씩_스크롤" 해서 더보기를 찾은 뒤 "클릭"
    Then "search_photo_tab_img"가 "활성화" 된지 확인하고 "True" 가 맞는지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: search00006 통합검색에서 노하우 컨텐츠 모듈 확인
    Given 홈화면에서 "search_icon"를 "클릭"한다음 "search_text_box 요소에 꿀팁"를 "입력"하고 "search_vk_btn"를 "클릭"하여 SRP 진입
    When "search_knowhow_title"을 "찾을때까지_스크롤" 해서 노하우 컨텐츠 타이틀을 찾기 시도
    Then "search_knowhow_title"가 "활성화" 된지 확인하고 "True" 가 맞는지 확인해서 노하우컨텐츠 타이틀이 노출된지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: search00007 통합검색에서 노하우컨텐츠 모듈의 더보기를 눌러 컨텐츠탭 진입 확인
    Given 홈화면에서 "search_icon"를 "클릭"한다음 "search_text_box 요소에 꿀팁"를 "입력"하고 "search_vk_btn"를 "클릭"하여 SRP 진입
    When "search_knowhow_title"을 "찾을때까지_스크롤" 해서 노하우 컨텐츠 타이틀을 찾기 시도
    When "1회"만큼 "아래로_조금_스크롤"한 뒤에 "search_more_btn"을 "찾을때까지_조금씩_스크롤" 해서 노하우 컨텐츠의 더보기 찾은 뒤 "클릭"
    Then "search_knowhow_tab_filter"가 "활성화" 된지 확인하고 "True" 가 맞는지 확인해서 컨텐츠의 노하우 필터가 정상적인지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: search00008 통합검색에서 집들이 컨텐츠 모듈 확인
    Given 홈화면에서 "search_icon"를 "클릭"한다음 "search_text_box 요소에 삼성전자"를 "입력"하고 "search_vk_btn"를 "클릭"하여 SRP 진입
    When "2회"만큼 "아래로_조금_스크롤"한 뒤에 "search_houses_title"을 "찾을때까지_조금씩_스크롤" 해서 집들이 컨텐츠 타이틀을 찾기 시도
    Then "search_houses_title"가 "활성화" 된지 확인하고 "True" 가 맞는지 확인해서 집들이컨텐츠 타이틀이 노출된지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: search00009 통합검색에서 집들이 컨텐츠 모듈의 더보기를 눌러 컨텐츠탭 진입 확인
    Given 홈화면에서 "search_icon"를 "클릭"한다음 "search_text_box 요소에 삼성전자"를 "입력"하고 "search_vk_btn"를 "클릭"하여 SRP 진입
    When "2회"만큼 "아래로_조금_스크롤"한 뒤에 "search_houses_title"을 "찾을때까지_조금씩_스크롤" 해서 집들이 컨텐츠 타이틀을 찾기 시도
    When "1회"만큼 "아래로_조금_스크롤"한 뒤에 "search_houses_more_btn"을 "찾을때까지_조금씩_스크롤" 해서 집들이 컨텐츠의 더보기 찾은 뒤 "클릭"
    Then "search_houses_tab_filter"가 "활성화" 된지 확인하고 "True" 가 맞는지 확인해서 컨텐츠의 집들이 필터가 정상적인지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: search00010 통합검색에서 시공업체 모듈 확인
    Given 홈화면에서 "search_icon"를 "클릭"한다음 "search_text_box 요소에 시공"를 "입력"하고 "search_vk_btn"를 "클릭"하여 SRP 진입
    When "search_construction_title"을 "찾을때까지_스크롤" 해서 시공업체 타이틀을 찾기 시도
    Then "search_construction_title"가 "활성화" 된지 확인하고 "True" 가 맞는지 확인해서 시공업체 타이틀이 노출된지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: search00011 통합검색에서 시공업체 모듈의 더보기를 눌러 컨텐츠탭 진입 확인
    Given 홈화면에서 "search_icon"를 "클릭"한다음 "search_text_box 요소에 시공"를 "입력"하고 "search_vk_btn"를 "클릭"하여 SRP 진입
    When "search_construction_title"을 "찾을때까지_조금씩_스크롤" 해서 시공업체 타이틀을 찾기 시도
    When "1회"만큼 "아래로_조금_스크롤"한 뒤에 "search_more_btn"을 "찾을때까지_조금씩_스크롤" 해서 시공업체의 더보기 찾은 뒤 "클릭"
    Then "search_construction_page"가 "활성화" 된지 확인하고 "True" 가 맞는지 확인해서 시공업체 페이지가 정상적인지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀

  @Prod
  Scenario: search00012 통합검색에서 시공업체 모듈 확인
    Given 홈화면에서 "search_icon"를 "클릭"한다음 "search_text_box 요소에 안드로이드자동화계정"를 "입력"하고 "search_vk_btn"를 "클릭"하여 SRP 진입
    When "search_user_tab"을 "클릭"해서 유저탭 진입
    Then "search_user_tab_nickname"가 "활성화" 된지 확인하고 "True" 가 맞는지 확인해서 유저탭의 유저가 정상노출 되는지 확인. 그 후 "back_home_btn"을 "클릭"하여 홈화면 복귀