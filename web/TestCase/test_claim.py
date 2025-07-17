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
from API.admin.orora.orora_orders import call_claims_cancel_approve
from API.commplatform.payment import *
import asyncio




#testcase별 orderid check
def orderid(url):
    global order_id
    order_id = CommOrdersElements.order_id(page,url)


@pytest.mark.smoke
def test_claim_00001(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()    

    print("test_claim_00001 : 입금대기 > 전체 취소 확인", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034378))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",1,None,None,"A",1))

    #주문서 시작
    orderid(page.url)    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.cart_coupon_remove(page))  
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.virtual_account_payment(page))   
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.account_cancel(page,order_id),check=True)
    

#무통장 입금건 api 테스트
@pytest.mark.smoke
def test_claim_00002(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_claim_00002 : 결제 완료 (무통장 입금건) > 전체 취소 확인", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034378))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_coupon_download(page))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",4,None,None,"A",1)) 

    #주문서
    orderid(page.url)
    web_exceptions_handler(page,current_function_name,step=lambda:CommOrdersElements.cartcoupon_fixed_rate(page))      
    web_exceptions_handler(page,current_function_name,step=lambda:CommOrdersElements.virtual_account_payment(page))
    asyncio.ensure_future(post_virtual_account(order_id))
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.order_cancel(page,order_id,"all"),check=True) 
    
    

@pytest.mark.regression
def test_claim_00003(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_claim_00003 : 결제 완료 > 부분 취소 확인 (한 상품 옵션간의 취소)", end='')    
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034360))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_coupon_download(page))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",4,"B",2,None,None))     
    #주문서
    orderid(page.url)   
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.order_cancel(page,order_id,"part"),check=True) 

   


@pytest.mark.skip
def test_claim_00004(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    
    print("test_claim_00004 : 결제 완료 > 부분 취소 (상품간의 취소)", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.cart_purchase(page,100034346,100034351))
    #주문서
    orderid(page.url)
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.local_shippingcosts(page))  
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.cart_coupon_remove(page))  
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.order_cancel(page,order_id,"part"),check=True) 
    




@pytest.mark.skip
def test_claim_00005(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_claim_00005 : 결제 완료 > 전체 취소 확인", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034356))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_coupon_download(page))         
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,"B",2,None,None))     

    #주문서       
    orderid(page.url)
    web_exceptions_handler(page,current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page)) 
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.order_cancel(page,order_id,"all"),check=True) 
       

@pytest.mark.smoke
def test_claim_00006(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    
    print("test_claim_00006 : 배송 준비 > 전체 취소 (판매자 귀책, 비례 배송비 전체 환불)", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034339))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",6,None,None,None,None))     
    orderid(page.url)
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))         
    ##배송 준비중
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=1))
    #주문서       
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.cancel_request(page,order_id),check=True)   
    #취소 요청건 승인 테스트
    asyncio.ensure_future(call_claims_cancel_approve(order_id))
     
    


@pytest.mark.skip
def test_claim_00007(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_claim_00007 : 배송 준비중 (승인 취소)> 전체 옵션 취소 ", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034348))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",7,"B",1,None,None))
    #주문서
    orderid(page.url)
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))
    #배송 상태 변경 (비동기)
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=1))
    #클레임 요청 - 완료 케이스 작성
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.cancel_request(page,order_id,"all"),check=True)   
      



@pytest.mark.regression
def test_claim_00008(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    
    print("test_claim_00008 : 배송 준비중(승인 취소) > 부분 옵션 취소", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034384))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"B",3,None,None,"A",1))     
    #주문서 
    orderid(page.url)       
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))          
        
    #오로라 배송 상태 변경
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=1))

    #클레임 요청 
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.cancel_request(page,order_id,"part"),check=True)   
    



@pytest.mark.skip
def test_claim_00009(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    
    print("test_claim_00009 : 배송 준비중 (승인취 소) > 부분 옵션 취소 + 클레임 승인 ", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034344))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"B",5,None,None,"A",2))     
    
    #주문서 
    orderid(page.url)       
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.cart_coupon_remove(page)) 
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))      
    
    #오로라 배송 상태 변경
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=1))
    #클레임 요청 - 완료 케이스 작성
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.cancel_request(page,order_id,"part"),check=True)   
    asyncio.ensure_future(call_claims_cancel_approve(order_id))





@pytest.mark.smoke
def test_claim_00010(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_claim_00010 : 배송중 > 판매자 귀책 + 전체 반품 + 철회", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034371))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,None,None,"A",1))     

    #주문서 
    orderid(page.url)        
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))    
    
    #오로라 배송 상태 변경 (결제 완료 -> 배송준비 -> 배송중) 
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=3))
    
    #클레임 - 배송중 반품/철회
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.claim_request(page,order_id,"refund"))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.refund_func(page,"all","seller","direct"))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.refund_cancel(page,order_id),check=True)



@pytest.mark.skip
def test_claim_00011(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_claim_00011 : 배송중 > 반품 > 구매자 귀책 + 전체 + 직접수거 + 차감 결제", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034373))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",3,None,None,None,None))     
    
    #주문서 
    orderid(page.url)
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.cart_coupon_remove(page))  
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))
        
    #오로라 배송 상태 변경 (결제 완료 -> 배송준비 -> 배송중)
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=2))

    #클레임 요청
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.claim_request(page,order_id,"refund"))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.refund_func(page,"part","buyer","direct"),check=True)        
    



@pytest.mark.skip
def test_claim_00012(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_claim_00012 : 배송중 > 옵션 부분 반품 (판매자 귀책, 직접 수거)", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034282))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",3,"B",5,None,None))     

    #주문서 
    orderid(page.url)
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))
    
    #오로라 배송 상태 변경 (결제 완료 -> 배송준비 -> 배송중)
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=2))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.claim_request(page,order_id,"refund"))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.refund_func(page,"part","seller","direct"),check=True)        

   


@pytest.mark.skip
def test_claim_00013(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_claim_00013:  업체 직배송 > 배송중 > 옵션 부분 반품 (구매자 귀책, 직접 수거)", end='')
    #해당 상품으로 구매확정 생성하기 (추가 필요)
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034369))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",2,None,None,None,None))     
    #주문서 

    orderid(page.url) 
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.cart_coupon_remove(page))  
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))
    
    #오로라 배송 상태 변경 (결제 완료 -> 배송준비 -> 배송중)
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=2))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.claim_request(page,order_id,"refund"))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.refund_func(page,"part","buyer","direct"),check=True)        

     


@pytest.mark.skip
def test_claim_00014(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_claim_00014: 업체직배송 > 배송중 > 교환 (판매자 귀책 + 직접 수거)", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034367))        
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",2,"B",2,None,None))             

    #주문서 
    orderid(page.url)   
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.cart_coupon_remove(page))  
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))   

    #오로라 배송 상태 변경 (결제 완료 -> 배송준비 -> 배송중)
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=2))    
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.claim_request(page,order_id,"exchange"))
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.exchange_func(page,"all","seller","direct"),check=True)
   



@pytest.mark.skip
def test_claim_00015(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_claim_00015: 업체직배송 > 배송중 > 교환 > 판매자 귀책 + 이미 수거 (유저 송장 입력)", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034371))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",4,"B",3,"A",1))      

    #주문서 
    orderid(page.url)   
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))

    #오로라 배송 상태 변경 (결제 완료 -> 배송준비 -> 배송중)
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=2))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.claim_request(page,order_id,"exchange"))
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.exchange_func(page,"all","seller","direct"),check=True)

    


@pytest.mark.smoke
def test_claim_00016(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_claim_00016: 배송중 > 구매자 귀책 > 클레임 요청 + 거절 처리", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034377))   
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,None,None,"A",1))     
   
    #주문서 
    orderid(page.url)   
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.cart_coupon_remove(page))  
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))

    #오로라 배송 상태 변경 (결제 완료 -> 배송준비 -> 배송중)
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=2))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.claim_request(page,order_id,"refund"))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.refund_func(page,"part","seller","direct"),check=True)     
    asyncio.ensure_future(call_claims_refund_reject(order_id))
   

    
    

@pytest.mark.regression
def test_claim_00017(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_claim_00017: 업체직배송 > 배송 완료 > 묶음 상품 간의 부분 옵션 반품 + 구매자 귀책 + 직접수거 / 구매확정", end='')    
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.cart_purchase(page,100034370,100034367))
    orderid(page.url)   
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.cart_coupon_remove(page))  
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))

    #오로라 배송 상태 변경
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=3))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.claim_request(page,order_id,"refund"))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.refund_func(page,"part","seller","direct"))
    web_exceptions_handler(page, current_function_name,step=lambda:CommClaimElements.purchase_confirm_func(page,order_id,2),check=True)   



@pytest.mark.regression
def test_claim_00018(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    
    print("test_claim_00018: 배송완료 > 판매자 귀책 클레임 요청 > 클레임 승인 처리", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034355))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",8,None,None,None,None))     
    #주문서 
    orderid(page.url)   
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.cart_coupon_remove(page))  
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))
    #오로라 배송 상태 변경 (배송 완료)
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=3))
    #클레임 진행
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.claim_request(page,order_id,"refund"))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.refund_func(page,"part","seller","direct"),check=True)  
    #클레임 승인
    asyncio.ensure_future(call_claims_refund_approve(order_id))
      

    

@pytest.mark.skip
def test_claim_00019(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    
    print("test_claim_00019: 일반 > 배송완료 > 반품 > 구매자 + 직접 수거 + 차감 결제 ", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034344))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,"B",1,None,None))     

    #주문서 
    orderid(page.url)   
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.cart_coupon_remove(page))  
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))
    
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=3))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.claim_request(page,order_id,"refund"))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.refund_func(page,"all","seller","direct"),check=True) 
    
      



@pytest.mark.smoke
def test_claim_00020(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    
    print("test_claim_00020: 일반 배송 > 배송완료 > 반품 > 구매자 + 직접 수거 + 차감 결제+클레임 승인 처리 ", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100034335))
    web_exceptions_handler(page,current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,"B",4,"A",3))     

    #주문서 
    orderid(page.url)   
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.cart_coupon_remove(page))  
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page))
    
    asyncio.ensure_future(call_change_order_status(order_id,retry_count=3))

    #claim 진행
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.claim_request(page,order_id,"refund"))
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.refund_func(page,"part","seller","direct"),check=True)     
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.claim_request(page,order_id,"refund"))   
    web_exceptions_handler(page,current_function_name,step=lambda:CommClaimElements.refund_func(page,"part","seller","direct"),check=True)        
    #클레임 승인 테스트 
    asyncio.ensure_future(call_claims_refund_approve(order_id))
    



