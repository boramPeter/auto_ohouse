@common
Feature: common Prod

    @Prod
    Scenario: common00001 로그인 페이지 진입 확인
        Given "ohouse_main" 링크로 "진입"
        When "login_menu" 요소 "클릭" 동작
        Then "login_text" 요소 "노출확인"

    @Prod
    Scenario: common00002 고객센터 진입 확인
        When "l_cs_menu" 요소 "클릭" 동작
        Then "cs_text" 요소 "노출확인"

