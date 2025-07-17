from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.comm_orders import *
from web.ObjectSetting.common_object import *
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.web_result_binary import ResultWeb
from web.BasicSetting.exception_func import *
from web.BasicSetting.conftest import *
from web.ObjectSetting.comm_admin import *

    

@pytest.mark.regression
def test_payment_00001(page,pay_login_out):
    
    current_function_name = ProviderFunctionName().get_current_function_name()
   
    print("test_payment_00001 : 일반 배송/무료 > 무통장 결제", end='')   
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008478)) 
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,"B",1,None,None))          #주문/결제    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.virtual_account_payment(page),check=True)         

    
@pytest.mark.regression
def test_payment_00002(page,pay_login_out):

    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_payment_00002 : 업체희망일 배송/최대/착불/조건부 > 무통장 결제", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008444))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",1,None,None,None,None))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.virtual_account_payment(page),check=True)     



@pytest.mark.skip
def test_payment_00003(page,pay_login_out):

    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_payment_00003 : 화물 배송/무료 > 무통장 결제", end='')    
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008401))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_assembly_checkbox(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",1,None,None,None,None))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.virtual_account_payment(page),check=True) 
    



#업체 희망일 배송 > 무통장 결제
@pytest.mark.regression
def test_payment_00004(page,pay_login_out):
    
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_payment_00004 : 업체 배송 착불/유료 무통장 결제", end='')   
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008514)) 
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",4,None,None,"A",1))
    #주문/결제
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.virtual_account_payment(page),check=True)    





@pytest.mark.regression
def test_payment_00005(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()    
    print("test_payment_00005 : 업체 묶음 배송 최소/선결제/유료+최소/선결제/조건부 > 무통장 결제", end='')        
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.cart_purchase(page,100008327,100008458))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.virtual_account_payment(page),check=True)       


@pytest.mark.skip
def test_payment_00006(page,pay_login_out):

    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_payment_00006 : 업체/무료 > 토스 퀵 계좌이체 결제 (상품 쿠폰Y, 장바구니 쿠폰Y, 포인트 Y) ", end='')    
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008438))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",3,None,None,None,None))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.tosspay_quick_payment(page),check=True) 


@pytest.mark.regression
def test_payment_00007(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_payment_00007 : 업체 희망일 배송/착불/유료 > 토스 퀵 계좌이체 ", end='')    
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008430))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",1,None,None,None,None))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.customer_number(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.tosspay_quick_payment(page),check=True) 
    #web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.phone_payment(page),check=True)               

    

@pytest.mark.regression
def test_payment_00008(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_payment_00008 : 업체+희망일/선결제/조건부+업체/희망일/선결제/유료 > 토스 퀵 (장바구니 쿠폰 Y, 지역별 Y)", end='')        
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.cart_purchase(page,100008400,100008340))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.customer_number(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.point(page,5000))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.tosspay_quick_payment(page),check=True) 
    #web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.phone_payment(page),check=True)               


@pytest.mark.regression
def test_payment_00009(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()    
    print("test_payment_00009 : 업체 희망일 묶음 배송 최소/선결제/조건부+최소/선결제/유료 > 토스 퀵 계좌 이체", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.cart_purchase(page,100008444,100008442))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.point(page,500))
    #web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.tosspay_quick_payment(page),check=True) 
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.phone_payment(page),check=True)               

    


@pytest.mark.skip
def test_payment_00010(page,pay_login_out):

    current_function_name = ProviderFunctionName().get_current_function_name()    
    print("test_payment_00010 : 화물 해외 배송/착불/조건부 > 무통장 결제", end='')    
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008381))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,None,None,None,None))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.customer_number(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.point(page,1000))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.virtual_account_payment(page))


@pytest.mark.skip
def test_payment_00011(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()  

    print("test_payment_00011 : 일반/유료 > 토스 퀵계좌이체(지역별Y, 포인트Y)", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008358))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,None,None,None,None))     
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.local_shippingcosts(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.point(page,3000))    
    #web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.tosspay_quick_payment(page),check=True)          


@pytest.mark.skip
def test_payment_00012(page,pay_login_out):

    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_payment_00012 : 일반 배송/선결제/유료(비례) > 토스 페이 퀵 계좌 이체(상품 쿠폰Y,포인트Y)", end='')
    web_exceptions_handler(page, current_function_name, step=lambda:CommPlatformElements.pdp_url(page,100008372), check=True)
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",4,"B",1,None,None))  
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.point(page,500))    
    #web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.tosspay_quick_payment(page),check=True) 
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.phone_payment(page),check=True)               




@pytest.mark.skip
def test_payment_00013(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_payment_00013 : 업체 희망일 배송 최대/착불/조건부 > 토스 퀵 계좌 결제(장바구니 쿠폰Y, 포인트Y)", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008444))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,"B",1,None,None))      
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.point(page,1500))
    #web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.tosspay_quick_payment(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.phone_payment(page),check=True)               



@pytest.mark.skip
def test_payment_00014(page,pay_login_out):

    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_payment_00014 : 화물 배송/선결제/조건부 > 휴대폰 결제 (지역별Y+장바구니 쿠폰Y)", end='')    
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008404))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",4,"B",1,None,None))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.point(page,100))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.phone_payment(page))
    web_exceptions_handler(page, current_function_name,step=lambda: CommonElements.logout_func(page),check=True)             


@pytest.mark.regression
def test_payment_00015(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_payment_00015 : 일반 배송/최소/무료 > 휴대폰+포인트 결제", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008363))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",6,None,None,None,None))      
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.point(page,500))        
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.phone_payment(page),check=True)                       


@pytest.mark.regression
def test_payment_00016(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_payment_00016 : 업체 희망일 배송/최소/선결제/조건부 > 휴대폰 결제", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008458))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_assembly_checkbox(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_expected_date(page))

    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",4,None,None,"A",1))     
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.local_shippingcosts(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.point(page,4000))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.phone_payment(page),check=True)            
    

@pytest.mark.skip
def test_payment_00017(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    
    print("test_payment_00017: 일반 해외 묶음 배송 최대/선결제/조건부+최대/선결제/조건부 > 휴대폰 결제 (상품 쿠폰Y)", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.cart_purchase(page,100008470,100008469))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.customer_number(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.point(page,5000))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.phone_payment(page),check=True) 



@pytest.mark.skip
def test_payment_00018(page,pay_login_out):

    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_payment_00018 : 업체 해외 선결제/유료 >  휴대폰 결제", end='')    
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008362))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",1,None,None,None,None))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.customer_number(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.phone_payment(page),check=True)               




@pytest.mark.skip
def test_payment_00019(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_payment_00019 : 화물 묶음 배송 최소/선결제/조건부+최소/무료 > 포인트 전액 결제", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.cart_purchase(page,100008346,100008351))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page),check=True) 
     



@pytest.mark.skip
def test_payment_00020(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_payment_00020 : 업체희망일 배송/무료 > 포인트 전액 결제", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008449))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,None,None,"A",1))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page),check=True) 



@pytest.mark.skip
def test_payment_00021(page,pay_login_out):

    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_payment_00021 :  화물 배송/선결제/유료 > 포인트 전액 (지역별Y, 상품쿠폰Y)", end='')    
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements .pdp_url(page,100008405))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_assembly_checkbox(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,None,None,None,None))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.local_shippingcosts(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page),check=True) 
       
      


@pytest.mark.skip
def test_payment_00022(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    
    print("test_payment_00022 : 일반 해외 배송/최소/선결제/조건부 >토스 결제(모달)", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008472))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,"B",1,None,None)) 
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.point(page,1300))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.tosspay_payment(page),check=True) 



@pytest.mark.skip
def test_payment_00023(page,pay_login_out):

    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_payment_00023: 화물/해외 배송+선결제+유료(비례) > 카드 결제 (지역별Y)(모달 체크)", end='')    

    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008383))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",1,None,None,None,None))
    #주문/결제
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.customer_number(page))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.allpoint_payment(page),check=True) 
            

@pytest.mark.skip
def test_payment_00024(page,pay_login_out):

    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_payment_00024: 일반 해외 배송/최소/착불/조건부 > 카카오페이 결제(모달 체크) ", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008474))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",1,None,None,None,None))
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.customer_number(page))    
    web_exceptions_handler(page, current_function_name,step=lambda:CommOrdersElements.kakaopay_payment(page),check=True) 
    
    


@pytest.mark.regression
def test_payment_00025(page,pay_login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()

    print("test_payment_00025 : 일반/최소/착불/조건부 > 포인트 전액", end='')
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_url(page,100008361))
    web_exceptions_handler(page, current_function_name,step=lambda:CommPlatformElements.pdp_selectopt_checkout(page,"A",5,"B",1,None,None))  
    web_exceptions_handler(page, current_function_name,step=lambda: CommOrdersElements.allpoint_payment(page),check=True)  
    
  