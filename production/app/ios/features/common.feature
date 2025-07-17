Feature: common Prod

  @Prod
  Scenario: common00001 로그인 페이지 확인
    When 앱 실행 후 "4초" "쉬고" "[200,500]"을 "좌표_클릭" 후 홈화면 진입
    Then "apple_login_btn"가 "활성화" 되었는지,"kakao_login_btn"가 "활성화" 되었는지 확인하여 "[True, True]"를 확인

  @Prod
  Scenario: common00002 로그인에 문제가 있으신가요? 페이지 확인
    When "login_question_btn"를 "클릭"해서 페이지 진입
    Then "cs_title","help_title","help_time"를 "이름확인"하고 "['고객센터', '무엇을 도와드릴까요?', '09:00 ~ 18:00']"와 비교해서 정상노출 확인한 후 "back_btn"을 "클릭"해서 로그인화면으로 복귀

  @Prod
  Scenario: common00004 비밀번호 재설정 페이지 확인
    When "email_login_btn" 다음 "pw_reset_btn"를 "클릭"하여 비밀번호 재설정페이지 진입
    Then "pw_reset_title"가 "활성화"된지 확인하고 "help_txt"를 "이름확인" 하여 "[True, '회원가입 시 입력한 정보가 기억나지 않는다면?']"와 비교해서 정상인지 확인 후, "back_to_email_login_btn", "back_btn"을 순서대로 "클릭" 해서 로그인화면으로 복귀

  @Prod
  Scenario: common00005 둘러보기 페이지 확인 (비회원 주문하기 대체)
    When "logout_order_btn", "logout_order_btn_confirm"을 순서대로 "클릭"해서 둘러보기를 통한 메인 페이지 진입
    When "4초" "쉬고" "[260,480]" "좌표_클릭" 다음 "dont_again_btn","back_btn" "광고_제거_클릭"해서 둘러보기를 통한 홈화면 진입
    Then "gnb_life_style_btn"과 "gnb_home_btn_at_home"가 "활성화" 된지 확인 후 "[True, True]"과 비교해서 둘러보기를 통한 홈화면 진입 체크 그 후 "앱_재시작" 해서 로그인화면 복귀

  @Prod
  Scenario: common00011 이메일로 로그인 기능 체크
    When 로그인 페이지에서 "qabucketios"계정으로 로그인 시도
    When "dont_again_btn"를 "광고_제거_클릭"해서 광고제거 후 홈화면 진입해서 정상동작 체크준비 "later_alarm","광고_제거_클릭"
    Then "home_viewer_tab"과 "gnb_home_btn_at_home"가 "활성화"된지 확인 후 "[True, True]"와 비교해서 로그인 된지 확인
