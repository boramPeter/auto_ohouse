@comm_p
Feature: comm_platform Prod

    # 6/3까지 XPC 1524 실험중
    Scenario: commerce_platform00001 장바구니 버튼 확인
        Given "shop_goods" 링크로 "진입"
        When "order_cart_btn" 요소 "클릭" 후 "order_cart_btn2" 요소 "클릭" 동작
        Then "cart_order_btn" 요소 "노출확인"

    @Prod
    Scenario: commerce_platform00003 바로구매 버튼 확인
        Given "shop_goods" 링크로 "진입"
        When "order_direct_btn" 요소 "클릭" 동작
        Then "order_text" 요소 "대기 후 노출확인"


#일부만 남기고 제거







