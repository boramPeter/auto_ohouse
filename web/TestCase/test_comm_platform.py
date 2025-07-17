from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.common_object import *
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.web_result_binary import ResultWeb
from web.BasicSetting.exception_func import *
from web.BasicSetting.conftest import *
from web.ObjectSetting.comm_claim import *
from web.ObjectSetting.comm_platform import *
import report.goole_spread_sheet_func.update_spread_sheet_func as update_sheet
from web.ObjectSetting.comm_admin import *
sheet_id = ResultWeb().read_result_slack('web_spreadsheet')

# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# requests.packages.urllib3.disable_warnings()

# Common
def checkout(page):
    CommonElements.login_func(page)
    page.wait_for_timeout(2000)
    CommPlatformElements.checkout_func(page)
    page.wait_for_timeout(2000)


def func_name(page):
    current_function_name = ProviderFunctionName().get_current_function_name()

'''
def test_comm_platform_00006(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    try:
        print("test_comm_platform_006 : 해외 통관번호 노출 확인", end='')
        # 임의의 해외직구 상품 진입
        page.goto('https://qa-web.dailyhou.se/productions/100008326/selling')
        CommonElements.login_func(page)
        page.get_by_role("combobox").nth(1).select_option("0")
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="바로구매").first.click()
        expect(page.get_by_role("heading", name="개인통관고유부호 (받는 사람)"), '개인통관고유부호 요소 미노출').to_be_visible()
        print(" - Pass")
        ResultWeb().write_result(current_function_name, f'*Pass*')
    except AssertionError as e:
        print(" - Fail", end='')
        print(f"\nCaught an AssertionError: {e}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
    except TimeoutError as e1:
        print(" - Fail", end='')
        print(f"\nCaught an TimeoutError: {e1}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
    except Exception as e2:
        print(" - Fail", end='')
        print(f"\nCaught an unknown error: {e2}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')
'''

@pytest.mark.smoke
def test_comm_platform_00004(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 주문서 생성까지만 확인
    print("test_comm_platform_004 : 비회원 장바구니 진입 후 주문서 생성까지", end='')
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100008327))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.cart(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.guest_cart_purchase(page), check=True)


@pytest.mark.smoke
def test_comm_platform_00005(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 주문서 생성까지만 확인
    print("test_comm_platform_005 : 비회원 바로구매 후 주문서 생성까지", end='')
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100008327))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.guest_pdp_purchase(page), check=True)


@pytest.mark.regression
def test_comm_platform_00007(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_007 : 임의의 상품 장바구니 담아지는지 확인", end='')
    PageElements.qaweb_product_url_2(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommPlatformExceptionElements.check_cart(page),
                           check=True)


@pytest.mark.smoke
def test_comm_platform_00010(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_010 : 빈 장바구니 확인 및 상품 담으러 가기 동작 확인", end='')
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.cart_reset(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.emptycart_goto_shop(page), check=True)


@pytest.mark.smoke
def test_comm_platform_00013(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_013 : 장바구니 상품 주문서 생성 확인", end='')
    PageElements.qaweb_product_url_2(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommPlatformExceptionElements.check_cart_order(page),
                           check=True)

'''
def test_comm_platform_014(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    try:
        print("test_comm_platform_014 : 주문서 상품 쿠폰변경 확인", end='')
        PageElements.qaweb_product_url(page)
        checkout(page)
        page.get_by_role("button", name="쿠폰 변경").click()
        page.wait_for_timeout(2000)
        # 14. 두번째 라디오 버튼 선택
        page.get_by_text("-10,000원", exact=True).click()
        page.wait_for_timeout(2000)
        # 15. [변경 완료] 버튼 선택
        page.get_by_role("button", name="변경 완료").click()
        expect(page.get_by_text("상품 쿠폰-10,000원"), '"상품 쿠폰 적용 금액" 요소 미노출').to_be_visible()
        print(" - Pass")
        ResultWeb().write_result(current_function_name, f'*Pass*')
    except AssertionError as e:
        print(" - Fail", end='')
        print(f"\nCaught an AssertionError: {e2}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
    except TimeoutError as e1:
        print(" - Fail", end='')
        print(f"\nCaught an TimeoutError: {e1}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
    except Exception as e2:
        print(" - Fail", end='')
        print(f"\nCaught an unknown error: {e}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')
'''


@pytest.mark.smoke
def test_comm_platform_00017(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_017 : 주문서 상품 쿠폰적용 확인", end='')
    PageElements.qaweb_product_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommPlatformExceptionElements.check_order_coupon(page),
                           check=True)


@pytest.mark.smoke
def test_comm_platform_00033(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_033 : 주문 배송목록 노출 확인", end='')
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.cart_reset(page))
    PageElements.qaweb_product_url_2(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommPlatformExceptionElements.check_delivery_list(page),
                           check=True)



@pytest.mark.regression
def test_comm_platform_00046(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_046 : 주문상세 페이지 노출 확인", end='')
    PageElements.qaweb_product_url_2(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommPlatformExceptionElements.check_order_detail(page),
                           check=True)

 
 
@pytest.mark.regression
def test_comm_platform_00034(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_00034 : 기간별 배송 필터 확인", end='')
    PageElements.qaweb_product_url_2(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommPlatformExceptionElements.check_period_delivery(page),
                           check=True)


@pytest.mark.regression
def test_comm_platform_00510(page, pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_510 : 상품 쿠폰 발급 및 FE 적용 확인", end='')
    #다른 쿠폰이 있을 경우가 있으니 미리 확인하고 발급
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100034820))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_coupon_download(page))
    #상쿠 발급
    web_exceptions_handler(page, current_function_name, step=lambda:PageElements.admin_url(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommonElements.login_admin_func(page))
    web_exceptions_handler(page, current_function_name, step=lambda:BenefitListElements.create_product_mold(page,100034820,"[자동화]상품쿠폰",1,6500))
    #쿠폰 발급 확인
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100034820))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_coupon_check(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_coupon_download(page))
    #결제 확인
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.checkout_2_func(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.product_coupon_use(page,"[자동화]상품쿠폰 6,500원 쿠폰",1))
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.phone_payment(page), check=True)


@pytest.mark.regression
def test_comm_platform_00511(page, pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_511 : 장바구니 쿠폰 발급 및 FE 적용 확인", end='')
    #다른 쿠폰이 있을 경우가 있으니 미리 확인하고 발급
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100034820))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_coupon_download(page))
    #장쿠 발급
    web_exceptions_handler(page, current_function_name, step=lambda:PageElements.admin_url(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommonElements.login_admin_func(page))
    web_exceptions_handler(page, current_function_name, step=lambda:BenefitListElements.create_cart_mold(page,100034820,"[자동화]장바구니쿠폰",1,8500))
    #쿠폰 발급 확인
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100034820))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_coupon_check(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_coupon_download(page))
    #결제 확인
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.checkout_2_func(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.cart_coupon_use(page,"[자동화]장바구니쿠폰 8,500원 쿠폰"))
    #web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.tosspay_quick_payment(page), check=True)
    #퀵 계좌이체 > 휴대폰 결제 임시 변경
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.phone_payment(page), check=True)


'''
def test_comm_platform_00514(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_514 : 장바구니 품절 상품 뱃지 및 삭제 동작 확인", end='')
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.cart_reset(page), check=True)
    #담기전 품절 체크
    web_exceptions_handler(page, current_function_name, step=lambda:PageElements.admin_url(page), check=True)
    web_exceptions_handler(page, current_function_name, step=lambda:CommonElements.login_admin_func(page), check=True)
    web_exceptions_handler(page, current_function_name, step=lambda:ProductListElements.set_product_instock(page,100034307), check=True)
    #담기
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100034307), check=True)
    web_exceptions_handler(page, current_function_name,
                           step=lambda:CommPlatformElements.pdp_selectopt_cart(page,"A",1,"B",1,"A",1),
                           check=True)
    #첫번째 필수 옵션 품절
    web_exceptions_handler(page, current_function_name, step=lambda:PageElements.admin_url(page), check=True)
    web_exceptions_handler(page, current_function_name, step=lambda:ProductListElements.set_product_outstock(page,100034307,0), check=True)
    #확인 후 품절 모두 삭제(옵션만)
    web_exceptions_handler(page, current_function_name, step=lambda:PageElements.qaweb_main_url(page), check=True)
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.cart_outopt_delete(page), check=True)
    #두번째 필수 옵션 품절
    web_exceptions_handler(page, current_function_name, step=lambda:PageElements.admin_url(page), check=True)
    web_exceptions_handler(page, current_function_name, step=lambda:ProductListElements.set_product_outstock(page,100034307,1), check=True)
    #확인 후 품절 모두 삭제(상품전부)
    web_exceptions_handler(page, current_function_name, step=lambda:PageElements.qaweb_main_url(page), check=True)
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.cart_outstock_delete(page), check=True)
'''


@pytest.mark.regression
def test_comm_platform_00515(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_515 : 장바구니 메모필수 상품 확인", end='')
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.cart_reset(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100034248))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.cart_require_memo(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.delete_memo_order(page), check=True)


@pytest.mark.regression
def test_comm_platform_00516(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_516 : 장바구니 희망배송일 상품 확인", end='')
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.cart_reset(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100034249))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.cart(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.cart_mod_delivery(page), check=True)


@pytest.mark.smoke
def test_comm_platform_00517(page, pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_517 : 패키지할인 토스퀵 결제 확인", end='')
    web_exceptions_handler(page, current_function_name, step=lambda:PageElements.qaweb_glinda_url(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.glinda_goto_cart(page,1))
    #쿠폰 적용 없음
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.product_coupon_remove(page,7))
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.cart_coupon_remove(page))
    #web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.tosspay_quick_payment(page), check=True)
    #퀵 계좌이체 > 포인트 결제 임시 변경
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.allpoint_payment(page), check=True)


@pytest.mark.smoke
def test_comm_platform_00518(page, pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_518 : 패키지할인 포인트 전액 결제 확인", end='')
    #어드민 쿠폰 발행 후 확인
    web_exceptions_handler(page, current_function_name, step=lambda:PageElements.admin_url(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommonElements.login_admin_func(page))
    web_exceptions_handler(page, current_function_name, step=lambda:BenefitListElements.publish_admin_coupon(page,1011473,23021450,8))

    web_exceptions_handler(page, current_function_name, step=lambda:PageElements.qaweb_glinda_url(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.glinda_goto_cart(page,2))
    #상쿠 적용 / 장쿠 없음
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.cart_coupon_remove(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.allpoint_payment(page), check=True)


@pytest.mark.smoke
def test_comm_platform_00519(page, pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_platform_519 : 패키지할인 포인트 + 휴대폰 결제 확인", end='')
    #어드민 쿠폰 발행 후 확인
    web_exceptions_handler(page, current_function_name, step=lambda:PageElements.admin_url(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommonElements.login_admin_func(page))
    web_exceptions_handler(page, current_function_name, step=lambda:BenefitListElements.publish_admin_coupon(page,1011474,23021450,1))

    web_exceptions_handler(page, current_function_name, step=lambda:PageElements.qaweb_glinda_url(page))
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.glinda_goto_cart(page,3))
    #상쿠 없음 / 장쿠 적용
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.product_coupon_remove(page,6))
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.cart_coupon_use(page,"자동화용 정액 1만원 쿠폰"))
    #포인트+토스
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.point(page,15000))
    web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.phone_payment(page), check=True)



'''
# 상품 구매하는 케이스 백업용
def test_comm_platform_00000(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    try:
        print("test_comm_platform_013 : 상품 쿠폰 적용 후 결제 확인", end='')
        PageElements.qaweb_product_url(page)
        CommonElements.login_func(page)
        page.wait_for_timeout(2000)
        CommPlatformElements.checkout_2_func(page)
        page.wait_for_timeout(2000)
        page.get_by_role("checkbox").first.check()
        # page.get_by_role("button", name="무통장입금 무통장입금 결제 아이콘 무통장 입금가능").click()
        page.get_by_role("button", name="0원 결제하기").click()
        page.get_by_role("button", name="주문현황 보기").click()
        # 주문취소하기 (초기화)
        page.get_by_role("button", name="주문취소").first.click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="다음").click()
        page.get_by_label("상품이 필요하지 않아요").check()
        page.get_by_role("button", name="다음").click()
        page.get_by_role("button", name="주문취소").click()
        page.get_by_role("heading", name="주문을 취소했어요").click()
        print(" - Pass")
        ResultWeb().write_result(current_function_name, f'*Pass*')
    except AssertionError as e:
        print(" - Fail", end='')
        print(f"\nCaught an AssertionError: {e}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
    except TimeoutError as e1:
        print(" - Fail", end='')
        print(f"\nCaught an TimeoutError: {e1}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
    except Exception as e2:
        print(" - Fail", end='')
        print(f"\nCaught an unknown error: {e2}")
        ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')
'''






