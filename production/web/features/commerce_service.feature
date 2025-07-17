@comm_s
Feature: comm_service Prod

    @Prod
    Scenario: commerce_service00001 쇼핑홈 진입 확인
        Given "shop_home" 링크로 "진입"
        When "store_menu" 요소 "클릭" 동작
        Then "store_text" 요소 "노출확인"

    @Prod
    Scenario: commerce_service00012 카테고리 진입 확인
        When "category_menu" 요소 "클릭" 동작
        Then "category_text" 요소 "노출확인"
