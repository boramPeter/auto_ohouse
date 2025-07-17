from web.BasicSetting.conftest import *
from selenium.common.exceptions import TimeoutException
from web.ObjectSetting.comm_admin import *
from web.ObjectSetting.common_object import *

import re


class CommOrdersElements():  

    #주문서에서 사용되는 공통 기능 정의
    def local_shippingcosts(page):
        #지역별 배송비
        page.get_by_role("button", name="변경", exact=True).click()
        page.get_by_role("button", name="선택").nth(1).click()
        page.wait_for_timeout(1000) 
        page.get_by_test_id("bds-dim").get_by_role("button", name="확인").click()
        page.wait_for_timeout(1000) 

    #개인통관번호
    def customer_number(page):
        # 현재 배송지명 텍스트 확인
        user_name = page.text_content('.css-su9qbs.e1j5k3ko4')
        input_box = page.get_by_placeholder("P부터 13자리를 모두 입력해주세요.")
        input_value = input_box.input_value()
        ##tds-mobile-portal-container > div > div > div.tds-mobile-bottom-cta--a__content.css-9o43oi > div > button > div.css-ez4mp1

        def check():
            page.get_by_label("수집한 개인통관고유부호는 원활한 통관 진행 및 계속 사용을 위해 회원님의 정보로 안전하게 저장하여 관리합니다.").check()
            page.wait_for_timeout(2000)

        def fill_customs_number():
            input_box.click()
            input_box.fill("P882143142944")
            page.wait_for_timeout(2000)

        #이름 있으면, 입력 + 체크 
        if user_name == "현지연":
            #if input_value:
            fill_customs_number()
            check()
            #else:
            #    fill_customs_number()
            #    check()

        else:
            #제주도면, 통관 배송지로 변경
            page.get_by_test_id("bds-dim").get_by_role("button", name="확인").click()
            page.wait_for_timeout(2000)
            page.get_by_role("button", name="변경", exact=True).click()
            page.get_by_role("button", name="선택").first.click()
            page.wait_for_timeout(3000)

            #통관 번호 있으면 체크
            if input_value:
                check()
            else:
                fill_customs_number()
                check()



    #쿠폰 전체 제거 (상품, 장바구니 - product_count:상품 개수)
    def product_coupon_remove(page,product_count):

        page.wait_for_timeout(3000)
        locator_visible = page.get_by_role("button", name="쿠폰 변경").is_visible()
        if locator_visible:
            page.get_by_role("button", name="쿠폰 변경").click() 
            page.wait_for_timeout(2000)  

            if product_count==1:          
                page.get_by_label("적용 안함").check()
                page.wait_for_timeout(2000)
                page.get_by_role("button", name="변경 완료").click()
                page.wait_for_timeout(2000)
            else:
                count_plus=1
                while count_plus <= product_count:
                    page.get_by_text("적용 안함").nth(f"{count_plus}").click()
                    page.wait_for_timeout(2000)                                           
                    count_plus+=1
                page.get_by_role("button", name="변경 완료").click()
                page.wait_for_timeout(2000)                                          
   



    #장바구니 쿠폰 - 정률 
    def cartcoupon_fixed_rate(page):         
        coupon_visible = page.get_by_text("자동화용 변경 금지 시디즈 10% 쿠폰").is_visible()

        if  coupon_visible:
            page.get_by_text("자동화용 변경 금지 시디즈 10% 쿠폰").click()
            page.wait_for_timeout(2000)
        else:
            if page.get_by_text("적용 안함").is_visible():
                retry =0
                while retry<3:
                    page.get_by_text("적용 안함").click()                
                    page.wait_for_timeout(2000)
                    retry+=1
            else:
                pass


 

    #장바구니 쿠폰 - 정액  
    def settlement_cart_coupon(page):

        coupon =page.get_by_text("정산전용 오집 삼십프로부담 10% 쿠폰")
        coupon_count = coupon.count()
        print(f"쿠폰은 {coupon_count} 개 입니다.")
        

        if coupon_count ==0: 
            print("쿠폰이 없습니다.")
            raise CouponNotFoundError
        
        elif coupon_count ==1 :
            print("쿠폰이 1개 입니다.")
            coupon.click()
        
        elif coupon_count >=2 :       
            coupon.first.click()

    
        page.wait_for_timeout(2000)
            
            

            

        


    #상품 쿠폰 사용
    def product_coupon_use(page,name,product_count):
        #name에 쿠폰명 ex) [자동화]상품쿠폰 6,500원 쿠폰
        page.wait_for_timeout(2000)
        check = 1

        expect(page.get_by_role("button", name="쿠폰 변경"), "쿠폰 변경 버튼 미노출").to_be_visible()
        page.get_by_role("button", name="쿠폰 변경").click() 
        page.wait_for_timeout(1000)

        expect(page.get_by_text(str(name)).first, "상품쿠폰 미노출").to_be_visible()
        page.get_by_text(str(name)).first.click()
        page.wait_for_timeout(1000)

        while check < product_count:
            page.get_by_text(str(name)).nth(f"{check}").click()
            check += 1

        if page.get_by_role("button", name="변경 완료").is_enabled():
            page.get_by_role("button", name="변경 완료").click()
        #이미 선택된 경우
        else:
            page.get_by_role("button", name="취소").click()
        page.wait_for_timeout(1000)


    #장바구니 쿠폰 사용
    def cart_coupon_use(page,name):
        #name에 쿠폰명 ex) [자동화]장바구니쿠폰 8,500원 쿠폰
        page.wait_for_timeout(2000)

        expect(page.get_by_text(str(name)).first, "장바구니쿠폰 미노출").to_be_visible()
        page.get_by_text(str(name)).first.click()
        page.wait_for_timeout(1000)


    #장바구니 쿠폰 - 적용 안함
    def cart_coupon_remove(page):  
        page.wait_for_timeout(3000)
        if page.get_by_text("적용 안함").is_visible():
            page.get_by_text("적용 안함").click()
        else:
            pass
            page.wait_for_timeout(2000)


    #포인트 - 부분 포인트 사용
    def point(page,point):
        if page.locator("li").filter(has_text="무통장입금").is_visible()                                       :
            page.locator("li").filter(has_text="무통장입금").click()                                       
        else:
            page.get_by_role('button').get_by_text('무통장').click(timeout=90000)
        try:
            page.get_by_placeholder("0").click()
            page.get_by_placeholder("0").fill(f"{point}")
            page.wait_for_timeout(3000)      
        except TimeoutException:
            pass



    #포인트 전액 결제
    def allpoint_payment(page):        
        for retry in range(3):
            try:
                page.get_by_role("button", name="전액 사용").click()
                page.wait_for_timeout(2000)

                if page.get_by_text("최종 결제 금액0 원").is_visible():
                    page.get_by_role("button", name="결제하기").click(timeout=90000)
                    break
                else:
                    raise AssertionError("결제 실패: 포인트 부족")

            except Exception as e:
                print(f"포인트 전액 예외 : {e}")
                page.wait_for_timeout(2000)

                try:
                    if page.locator("li").filter(has_text="무통장입금").is_visible():
                        page.locator("li").filter(has_text="무통장입금").click()
                    else:
                        page.get_by_role("button", name="무통장").click(timeout=90000)
                except Exception as e2:
                    print(f"포인트 전액 > 무통장 선택 실패: {e2}")

                page.wait_for_timeout(2000)
        else:
            raise AssertionError("포인트 전액 결제 실패")

        # 주문 결과 페이지 생성 확인
        expect(page.get_by_role("button", name="주문현황 보기"), "PG 인증 완료 > 주문 결과 페이지 생성 오류").to_be_visible(timeout=90000)


    #결제 수단 - 토스페이 버튼
    def tosspay_payment(page):

        locator_visible = page.locator("li").filter(has_text="토스페이").is_visible()
        if locator_visible:
           page.locator("li").filter(has_text="토스페이").click()          
        else:
            page.get_by_role('button').get_by_text('토스페이').click(timeout=90000)
        page.wait_for_timeout(2000)
        page.get_by_role('button').get_by_text('결제하기').click(timeout=90000)
        page.wait_for_timeout(3000)


    #결제 수단 - 네이버 페이 
    def naverpay_payment(page):
        locator_visible = page.locator("li").filter(has_text="네이버페이").is_visible()
        if locator_visible:
            page.locator("li").filter(has_text="네이버페이").click()
        else:   
            page.get_by_role('button').get_by_text('네이버페이').click(timeout=90000)
        page.wait_for_timeout(2000)
     
        with page.expect_popup() as page1_info:
            page.get_by_role('button').get_by_text('결제하기').click(timeout=90000)
        page1 = page1_info.value
    
        page1.get_by_label("아이디 또는 전화번호").click()        
        page1.get_by_label("아이디 또는 전화번호").fill("autotest_01")
        page1.wait_for_timeout(2000) 
        page1.get_by_label("비밀번호").click()        
        page1.get_by_label("비밀번호").fill("qqqq1111")
        page1.wait_for_timeout(2000)                      

        page1.locator("#submit_btn").click()
        #"로그인"텍스트 실제 코드에 존재하지 않아, locator 진행
        page1.wait_for_timeout(2000)       
        page1.get_by_role("button", name="등록", exact=True).click()                
        with page1.expect_popup() as page2_info:
            page1.locator("a.button:has-text('결제하기')").click()
        page2 = page2_info.value
        page2.wait_for_timeout(2000) 
        #page2.get_by_role("heading", name="비밀번호 입력").click()
        


    def kakaopay_payment(page,order_id):
        locator_visible = page.locator("li").filter(has_text="카카오페이").is_visible()
        
        if locator_visible:
            page.locator("li").filter(has_text="카카오페이").click()
        else:
            page.get_by_role('button').get_by_text('카카오페이').click(timeout=90000)
        page.wait_for_timeout(2000)     
        page.get_by_role('button').get_by_text('결제하기').click(timeout=90000)
        page.wait_for_timeout(3000)
    


    #페이코
    def payco_payment(page):
        locator_visible =  page.locator("li").filter(has_text="페이코").is_visible()           

        if locator_visible:
            page.locator("li").filter(has_text="페이코").click()
        else:           
            page.get_by_role('button').get_by_text('페이코').click(timeout=90000)
        page.wait_for_timeout(2000)   
     
        page.get_by_role('button').get_by_text('결제하기').click(timeout=90000)
        page.wait_for_timeout(3000)



    #휴대폰 결제
    def phone_payment(page):
        #결제 수단 선택
        try:
            if page.locator("li").filter(has_text="핸드폰").is_visible():
                page.locator("li").filter(has_text="핸드폰").click()                
            else:
                page.get_by_role("button").get_by_text("핸드폰").click(timeout=90000)
        except Exception as e:
            print(f"휴대폰 결제 버튼 선택 실패: {e}")
            assert False            

        page.wait_for_timeout(2000) 
        page.get_by_role('button').get_by_text('결제하기').click(timeout=90000)
        page.wait_for_timeout(3000)

        #UI 변경전 화면 
        phonepay_pw = [1,0,2,9,0,6]
        iframe = CommOrdersElements.iframe_index(page)
        frame = page.frame_locator(f"iframe >> nth={iframe}").frame_locator("iframe")
        
        #휴대폰 결제 iframe
        try: 
            frame.get_by_text("휴대폰 결제 항목 모두 동의 (필수)").click()
            page.wait_for_timeout(2000)          
            frame.get_by_role("tab", name="휴대폰 간편결제").click()
            page.wait_for_timeout(2000)  
            frame.get_by_role("textbox", name="휴대폰번호").click()
            page.wait_for_timeout(2000)  
            frame.get_by_role("textbox", name="휴대폰번호").fill("010-6690-2069")
            frame.locator("div").filter(has_text="다 음").nth(3).click()
            page.wait_for_timeout(2000)  
            
            #비밀번호 변경 뜨는 경우
            locator_visible = frame.get_by_role("button", name="3개월 후 다시보기").is_visible()
            if locator_visible:
                frame.get_by_role("button", name="3개월 후 다시보기").click()
                page.wait_for_timeout(2000)

            index =0 
            for num in phonepay_pw:
                frame.get_by_role("link", name=str(num)).click()
                page.wait_for_timeout(1000)  
    
        except Exception as e:
            print(f"휴대폰 결제 Iframe 결제 진행중 실패 :{e} ")

        #주문 결과 생성 체크 
        expect(page.get_by_role("button", name="주문현황 보기"),"PG 인증 완료 > 주문 결과 페이지 생성 오류").to_be_visible(timeout=90000)
        page.get_by_role("button", name="주문현황 보기").click()
        page.wait_for_timeout(2000)



    #무통장 입금 결제     
    def virtual_account_payment(page):

        #무통장 버튼 클릭
        try:
            locator = page.locator("li").filter(has_text="무통장입금")
            if locator.is_visible():        
                locator.click()
            else:
                page.get_by_role('button').get_by_text('무통장').click(timeout=90000)
        except Exception as e:
            print(f"무통장 입급 버튼 선택 실패 :{e}")
        page.wait_for_timeout(2000) 
     
        #결제 하기
        page.get_by_role('button').get_by_text('결제하기').click(timeout=90000)    
        page.wait_for_timeout(2000)
        
        iframe = CommOrdersElements.iframe_index(page)
        frame = page.frame_locator(f"iframe >> nth={iframe}").frame_locator("iframe[name='nice_frame']")
        frame_second = page.frame_locator(f"iframe >> nth={iframe}")

        try:  
            frame.get_by_role("checkbox", name="이용약관 전체동의 이용약관 전체동의, 더보기").click()
            frame.get_by_role("button", name="모두 동의 후 진행").click()
            page.wait_for_timeout(2000)                
            frame.get_by_role("button", name="우리은행로고 우리은행").click()
            frame.get_by_role("button", name="다음", exact=True).click()
            page.wait_for_timeout(2000)                
            frame.get_by_text("결제 정보를 모두 확인했습니다.").click()
            frame.get_by_role("button").get_by_text("결제").click()
        except:
            frame_second.get_by_role("link", name="국민").click()
            page.wait_for_timeout(2000)
            frame_second.get_by_placeholder("휴대폰번호를 입력해주세요.").click()
            frame_second.get_by_placeholder("휴대폰번호를 입력해주세요.").fill("01066902069")
            page.wait_for_timeout(2000)
            frame_second.get_by_label("[필수] 서비스 이용 약관, 개인정보 처리 동의").check()
            frame_second.get_by_label("확인-국민 결제").click()
            page.wait_for_timeout(2000)
        #주문 결과 생성 체크 
        expect(page.get_by_role("button", name="주문현황 보기"),"PG 인증 완료 > 주문 결과 페이지 생성 오류").to_be_visible(timeout=90000)
        page.get_by_role("button", name="주문현황 보기").click()
        page.wait_for_timeout(2000)

    


    #토스 퀵 페이
    def tosspay_quick_payment(page):
        try:
            # 1. 결제 수단 선택
            if page.locator("li").filter(has_text="퀵계좌이체").is_visible():
                page.locator("li").filter(has_text="퀵계좌이체").click()
            else:
                page.get_by_role("button", name="퀵계좌이체 퀵계좌이체 결제 아이콘").click()
        except Exception as e:
            print(f"토스 퀵 페이 결제 버튼 선택 실패: {e}")
            assert False     

        page.wait_for_timeout(2000)       
        page.get_by_role('button').get_by_text('결제하기').click(timeout=90000)
        page.wait_for_timeout(3000)

        #토스 퀵 계좌 PG        
        password = [2,0,2,4,2,0]
        iframe = CommOrdersElements.iframe_index(page)
        frame = page.frame_locator(f"iframe >> nth={iframe}")        
        page.wait_for_timeout(2000)

        try: 
            if frame.get_by_role("button", name="다음").is_visible():
               page.wait_for_timeout(2000)  
               frame.get_by_role("button", name="다음").click()
               page.wait_for_timeout(2000)  
            else:
                raise AssertionError("토스 퀵 계좌 다음 버튼 없음")
        except Exception as e:
            print(f"토스 퀵 계좌 다음 버튼 인식 실패 : {e}") 
        
        for num in password:
            frame.get_by_label(str(num)).click()
            page.wait_for_timeout(1000)  

        frame.get_by_role("button", name="동의하고 결제하기").click()
        frame.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)


        for num in password:
            frame.get_by_label(str(num)).click()
            page.wait_for_timeout(1000)  

        #주문 결과 생성 체크 
        expect(page.get_by_role("button", name="주문현황 보기"),"PG 인증 완료 > 주문 결과 페이지 생성 오류").to_be_visible(timeout=90000)
        page.get_by_role("button", name="주문현황 보기").click()
        page.wait_for_timeout(2000)
  
    
    #iframe check
    def iframe_index(page):
        iframe_count = page.query_selector_all('iframe') 
        count = len(iframe_count)
        index=str(count-1)    
        return index    
   
   
    #orderid check
    def order_id(page,url):
        order_id=re.sub(r'[^0-9]', '',url)
        return order_id
    

#(정산용 예외) 쿠폰 없을 때, 예외 
class CouponNotFoundError(Exception):
    pass
