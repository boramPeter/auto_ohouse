from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.comm_orders import *
from web.ObjectSetting.common_object import *
from web.ObjectSetting.comm_orora import *
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.web_result_binary import ResultWeb
from web.ObjectSetting.comm_claim import *
from web.BasicSetting.conftest import *
from web.BasicSetting.exception_func import *
from API.admin.orora.orora_orders import call_change_order_status
from API.admin.orora.orora_orders import call_claims_refund_approve
from API.admin.orora.orora_orders import call_claims_refund_reject
from API.admin.orora.orora_settlement  import get_sales_summary
from API.admin.orora.orora_settlement import call_get_search_sales
from API.commplatform.payment import post_virtual_account
from API.admin.orora.orora_settlement import call_settlement_sales_data
import asyncio



#testcase별 orderid check
def orderid(url):
    global order_id
    order_id = CommOrdersElements.order_id(page,url)
    return order_id

    

@pytest.mark.skip
def test_settlement_00001(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_settlement_00001 :  옵션조정, 쿠폰 데이터 생성", end='')
    
    
    def order_checkout(page):
        web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100035319))
        web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",3,"B",8,None,None))
    
    try:
        order_checkout(page)
        orderid(page.url)    
        CommOrdersElements.settlement_cart_coupon(page)    

    except CouponNotFoundError:
    
        web_exceptions_handler(page, current_function_name, step=lambda:PageElements.admin_url(page))
        web_exceptions_handler(page, current_function_name, step=lambda:CommonElements.login_admin_func(page))
        web_exceptions_handler(page, current_function_name, step=lambda:BenefitListElements.publish_admin_coupon(page,1011975,23021450,5))
        order_checkout(page)
        orderid(page.url)    
        web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.settlement_cart_coupon(page))
    
    web_exceptions_handler(page, current_function_name, step=lambda: CommOrdersElements.point(page,10000))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.virtual_account_payment(page))
    asyncio.ensure_future(post_virtual_account(order_id)) 
    page.wait_for_timeout(3000)
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=3))
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.purchase_confirm_func(page,order_id,2),check=True)         
    #asyncio.ensure_future(get_sales_summary())


@pytest.mark.skip
def test_settlement_00002(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_settlement_00002: 조립비, 배송비, 옵션조정, 쿠폰, 포인트 생성", end='')
    
    
    def order_checkout(page):
        web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100035317))
        web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_assembly_checkbox(page))
        web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",6,"B",4,None,None))
    
    try:
        order_checkout(page)
        orderid(page.url)    
        CommOrdersElements.settlement_cart_coupon(page)
        web_exceptions_handler(page, current_function_name, step=lambda: CommOrdersElements.point(page,10000))

    except CouponNotFoundError:
    
        web_exceptions_handler(page, current_function_name, step=lambda:PageElements.admin_url(page))
        web_exceptions_handler(page, current_function_name, step=lambda:CommonElements.login_admin_func(page))
        web_exceptions_handler(page, current_function_name, step=lambda:BenefitListElements.publish_admin_coupon(page,1011975,23021450,5))
        order_checkout(page)
        orderid(page.url)    
        web_exceptions_handler(page, current_function_name, step=lambda:CommOrdersElements.settlement_cart_coupon(page))
        web_exceptions_handler(page, current_function_name, step=lambda: CommOrdersElements.point(page,10000))

    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.virtual_account_payment(page))
    asyncio.ensure_future(post_virtual_account(order_id))

    asyncio.ensure_future(call_change_order_status(order_id,retry_count=2))
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.purchase_confirm_func(page,order_id,2),check=True)         
    #asyncio.ensure_future(get_sales_summary())


@pytest.mark.skip
def test_settlement_00003(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("정산상세, 정산 내역 상세 데이터 정합성 체크 ", end='') 
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100035317))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",2,"B",2,"A",3))   
    orderid(page.url)    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.virtual_account_payment(page))
    asyncio.ensure_future(call_settlement_sales_data(order_id))

    #asyncio.ensure_future(call_settlement_sales_data(order_id,"2025-07-11"))
