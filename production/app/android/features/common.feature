Feature: common Prod

  @Prod
  Scenario: common00001 로그인 페이지 확인
    When 앱 실행 후 로그인 페이지 진입후에 "three_sec_btn"를 "클릭"
    Then "three_sec_btn"가 "활성화" 되었는지,"kakao_btn"가 "활성화" 되었는지 확인하여 "[True, True]"를 확인

  @Prod
  Scenario: common00002 로그인에 문제가 있으신가요? 페이지 확인
    When "login_question_btn"를 "클릭"해서 페이지 진입 "3초","쉬고"
    Then "cs_title","help_title","help_time"를 "텍스트확인"하고 "['고객센터', '무엇을 도와드릴까요?', '고객센터 09:00 ~ 18:00']"와 비교해서 정상노출 확인한 후 "back_imageview_btn"을 "클릭"해서 로그인화면으로 복귀

  @Prod
  Scenario: common00004 비밀번호 재설정 페이지 확인
    When "email_login_btn" 다음 "pw_reset_btn"를 "클릭"하여 비밀번호 재설정페이지 진입
    Then "pw_reset_title"가 "활성화"된지 확인하고 "help_txt"를 "텍스트확인" 하여 "[True, '회원가입 시 입력한 정보가 기억나지 않는다면?']"와 비교해서 정상인지 확인 후, "backIcon_btn"를 "클릭" 두번해서 로그인화면으로 복귀

  @Prod
  Scenario: common00005 비회원 주문하기 페이지 확인
    When "logout_order_btn"을 "클릭"해서 비회원주문하기 페이지 진입
    Then "title"과 "order_search_btn"가 "활성화" 된지 확인 후 "[True, True]"과 비교해서 정상인지 체크한 뒤에 "backIcon_btn"을 "클릭"하여 로그인 페이지로 복귀

  @Prod
  Scenario: common00011 이메일로 로그인 기능 체크
    When 로그인 페이지에서 "qabucketaos"계정으로 로그인 시도
    When "2초" "쉬고" "review_later_btn"가 노출되면 "광고_제거_클릭"을 하고 홈화면 진입
    Then "home_viewer_tab"과 "gnb_home_btn"가 "활성화"된지 확인 후 "[True, True]"와 비교해서 로그인 된지 확인
