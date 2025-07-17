from web.BasicSetting.conftest import *
from web.ObjectSetting.comm_orders import *




#배송 정보
def delivery_info(page):
    page.get_by_test_id("deliveryInfo.deliveryCompany").click()
    page.get_by_text("CJ대한통운 국제특송").click()
    page.wait_for_timeout(2000)
    page.get_by_test_id("deliveryInfo.deliveryInvoice").click()
    page.get_by_test_id("deliveryInfo.deliveryInvoice").fill("1234567890")
    page.wait_for_timeout(2000)



#오로라 - 주문 배송 메뉴
class OrderDeliveryElements():

    #주문건 주문 확인 처리 
    def order_confirm(page,order_id):
        page.goto('https://orora.qa-web.dailyhou.se/orders',timeout=0)
        page.wait_for_timeout(2000)

        page.get_by_test_id("textSearchValue").click()
        page.get_by_test_id("textSearchValue").fill(f"{order_id}")
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="검색", exact=True).click(timeout=90000)    
        page.wait_for_timeout(2000)

        page.get_by_role("row", name=" 주문옵션번호 주문상태 주문번호 주문상품번호 주문자 주문자 연락처 수취인 수취인 연락처 상품명 옵션명 판매가 수량 판매가*수량 배송방법 배송지 배송메모 조립신청 오늘출발 배송정보 배송추적 주문결제완료일 출고예정일 배송예정일 희망배송일").get_by_label("").check()
        page.get_by_role("button", name="주문 확인").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="확인", exact=True).click()
        expect(page.get_by_test_id("snackbar-item"),"오로라 처리 토스트 미노출").to_be_visible(timeout=90000)
        page.wait_for_timeout(3000)
    
    #취소 요청건 승인 처리
    def cancel_approved(page,order_id):

        page.get_by_text("취소/반품/교환").click()
        page.get_by_role("link", name="취소 관리").click()
        page.wait_for_timeout(2000)
        
        page.get_by_test_id("textSearchType").click()
        page.get_by_role("menuitem", name="주문번호").locator("span").click()
        page.wait_for_timeout(2000)
        page.get_by_test_id("textSearchValue").click()
        page.get_by_test_id("textSearchValue").fill(f"{order_id}")
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="검색", exact=True).click()
        page.wait_for_timeout(2000)

        page.get_by_role("row", name=" 구분 요청자 취소번호 취소상태 귀책 구분 취소사유 주문번호 주문상품번호 주문옵션번호 주문자 연락처 상품명 옵션명 수량 판매가*수량 결제일 취소요청일 취소완료일").get_by_label("").check()
        page.get_by_role("button", name="취소승인(환불)").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="취소승인(환불)").nth(1).click()
        page.wait_for_timeout(2000)

 
    #배송중 처리 (invoice_option - 송장이 필요한 일반/화물 상품의 경우 송장 받을 옵션값 입력)
    def order_shipping(page,order_id,invoice_option=None):
        #주문배송진입
        page.goto('https://orora.qa-web.dailyhou.se/orders',timeout=0)
        page.wait_for_timeout(2000)
        #검색
        page.get_by_test_id("textSearchValue").click()
        page.get_by_test_id("textSearchValue").fill(f"{order_id}")
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="검색", exact=True).click(timeout=90000)    
        page.wait_for_timeout(2000)
        #주문 확인 (결제완료 > 배송준비중 변경)
        page.get_by_role("row", name=" 주문옵션번호 주문상태 주문번호 주문상품번호 주문자 주문자 연락처 수취인 수취인 연락처 상품명 옵션명 판매가 수량 판매가*수량 배송방법 배송지 배송메모 조립신청 오늘출발 배송정보 배송추적 주문결제완료일 출고예정일 배송예정일 희망배송일").get_by_label("").check()
        page.get_by_role("button", name="주문 확인").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="확인", exact=True).click()
        expect(page.get_by_test_id("snackbar-item"),"오로라 처리 토스트 미노출").to_be_visible(timeout=90000)
        page.wait_for_timeout(3000)

        #배송준비중 > 배송중 변경 
        retries = 0
        if invoice_option: 
            while retries < invoice_option:
                try:
                    page.get_by_role("button", name="송장 등록").first.click()
                    page.wait_for_timeout(2000)
                except TimeoutException:
                    page.get_by_role("button", name="송장 등록").click()
                    page.wait_for_timeout(2000)

                page.get_by_test_id("deliveryCompanyCode").click()
                page.get_by_text("CJ대한통운 국제특송").click()
                page.wait_for_timeout(2000)
                page.get_by_test_id("deliveryId").click()
                page.get_by_test_id("deliveryId").fill("1234567890")
                page.wait_for_timeout(2000)        
                page.get_by_role("button", name="저장").click(timeout=90000)
                expect(page.get_by_text("송장이 저장되었습니다."),"송장 저장 입력 에러").to_be_visible(timeout=90000)            
                page.wait_for_timeout(2000)
                retries += 1  
        else:
            page.get_by_role("row", name=" 주문옵션번호 주문상태 주문번호 주문상품번호 주문자 주문자 연락처 수취인 수취인 연락처 상품명 옵션명 판매가 수량 판매가*수량 배송방법 배송지 배송메모 조립신청 오늘출발 배송정보 배송추적 주문결제완료일 출고예정일 배송예정일 희망배송일").get_by_label("").check()
            page.wait_for_timeout(3000)
            page.get_by_role("button", name="배송중").click()
            page.wait_for_timeout(2000)
            page.get_by_role("button", name="확인", exact=True).click()
            expect(page.get_by_test_id("snackbar-item"),"오로라 처리 토스트 미노출").to_be_visible(timeout=90000)
            page.wait_for_timeout(3000)

    

            

    #주문 배송 현황
    def order_delivery_page(page):
        page.goto('https://orora.qa-web.dailyhou.se/orders',timeout=0)
        page.wait_for_timeout(2000)


    #배송 - 검색 필터 
    def searchfilter(page,order_id):
        page.get_by_test_id("textSearchValue").click()
        page.get_by_test_id("textSearchValue").fill(f"{order_id}")
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="검색", exact=True).click(timeout=90000)    
        page.wait_for_timeout(2000)

 
    #배송 - 주문 확인
    def order_confirm_2(page):
        page.get_by_role("row", name=" 주문옵션번호 주문상태 주문번호 주문상품번호 주문자 주문자 연락처 수취인 수취인 연락처 상품명 옵션명 판매가 수량 판매가*수량 배송방법 배송지 배송메모 조립신청 오늘출발 배송정보 배송추적 주문결제완료일 출고예정일 배송예정일 희망배송일").get_by_label("").check()
        page.get_by_role("button", name="주문 확인").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="확인", exact=True).click()
        expect(page.get_by_test_id("snackbar-item"),"오로라 처리 토스트 미노출").to_be_visible(timeout=90000)
        page.wait_for_timeout(3000)



    #배송 - 배송완료 (일반, 화물 케이스는 option 입력하여 송장 받기)
    def delivery_completed(page,order_id,invoice_option=None):
        #주문배송진입
        page.goto('https://orora.qa-web.dailyhou.se/orders',timeout=0)
        page.wait_for_timeout(2000)
        #검색
        page.get_by_test_id("textSearchValue").click()
        page.get_by_test_id("textSearchValue").fill(f"{order_id}")
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="검색", exact=True).click(timeout=90000)    
        page.wait_for_timeout(2000)
        #주문 확인 (결제완료 > 배송준비중 변경)
        page.get_by_role("row", name=" 주문옵션번호 주문상태 주문번호 주문상품번호 주문자 주문자 연락처 수취인 수취인 연락처 상품명 옵션명 판매가 수량 판매가*수량 배송방법 배송지 배송메모 조립신청 오늘출발 배송정보 배송추적 주문결제완료일 출고예정일 배송예정일 희망배송일").get_by_label("").check()
        page.get_by_role("button", name="주문 확인").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="확인", exact=True).click()
        expect(page.get_by_test_id("snackbar-item"),"오로라 처리 토스트 미노출").to_be_visible(timeout=90000)
        page.wait_for_timeout(3000)

        #배송준비중 > 배송중 변경 
        retries = 0
        if invoice_option: 
            while retries < invoice_option:
                try:
                    page.get_by_role("button", name="송장 등록").first.click()
                    page.wait_for_timeout(2000)
                except TimeoutException:
                    page.get_by_role("button", name="송장 등록").click()
                    page.wait_for_timeout(2000)

                page.get_by_test_id("deliveryCompanyCode").click()
                page.get_by_text("CJ대한통운 국제특송").click()
                page.wait_for_timeout(2000)
                page.get_by_test_id("deliveryId").click()
                page.get_by_test_id("deliveryId").fill("1234567890")
                page.wait_for_timeout(2000)        
                page.get_by_role("button", name="저장").click(timeout=90000)
                expect(page.get_by_text("송장이 저장되었습니다."),"송장 저장 입력 에러").to_be_visible(timeout=90000)            
                page.wait_for_timeout(2000)
                retries += 1  
        else:
            page.get_by_role("row", name=" 주문옵션번호 주문상태 주문번호 주문상품번호 주문자 주문자 연락처 수취인 수취인 연락처 상품명 옵션명 판매가 수량 판매가*수량 배송방법 배송지 배송메모 조립신청 오늘출발 배송정보 배송추적 주문결제완료일 출고예정일 배송예정일 희망배송일").get_by_label("").check()
            page.wait_for_timeout(3000)
            page.get_by_role("button", name="배송중").click()
            page.wait_for_timeout(2000)
            page.get_by_role("button", name="확인", exact=True).click()
            expect(page.get_by_test_id("snackbar-item"),"오로라 처리 토스트 미노출").to_be_visible(timeout=90000)
            page.wait_for_timeout(3000)

        #배송중 > 배송완료
        page.get_by_role("row", name=" 주문옵션번호 주문상태 주문번호 주문상품번호 주문자 주문자 연락처 수취인 수취인 연락처 상품명 옵션명 판매가 수량 판매가*수량 배송방법 배송지 배송메모 조립신청 오늘출발 배송정보 배송추적 주문결제완료일 출고예정일 배송예정일 희망배송일").get_by_label("").check()
        page.get_by_role("button", name="배송 완료").click()
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="확인", exact=True).click()
        expect(page.get_by_test_id("snackbar-item"),"오로라 처리 토스트 미노출").to_be_visible(timeout=90000)
        page.wait_for_timeout(3000)
    
 



class ClaimElements():

    #구매확정 후 취소 페이지 
    def complete_page(page):
        page.goto('https://orora.qa-web.dailyhou.se/order-delivery/complete',timeout=0)
        page.wait_for_timeout(2000)          


    #취소 관리 페이지 
    def cancel_page(page):
        page.get_by_text("취소/반품/교환").click()
        page.get_by_role("link", name="취소 관리").click()
        page.wait_for_timeout(2000)
    
    #반품 관리 메뉴
    def refund_page(page):
        page.goto('https://orora.qa-web.dailyhou.se/claims/return',timeout=0)
        page.wait_for_timeout(2000)        
    
                
    #교환 페이지
    def exchange_page(page,order_id):
        page.goto('https://orora.qa-web.dailyhou.se/claims/exchange',timeout=0)
        page.wait_for_timeout(2000)
        page.get_by_test_id("textSearchType").click()
        page.get_by_role("menuitem", name="주문번호").locator("span").click()
        page.wait_for_timeout(2000)
        page.get_by_test_id("textSearchValue").click()
        page.get_by_test_id("textSearchValue").fill(f"{order_id}")
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="검색", exact=True).click()
        page.wait_for_timeout(2000)

    

    #취소 관리 페이지 > 취소 요청 건 승인 처리 
    def cancel_approved_btn(page):
        page.get_by_role("row", name=" 구분 요청자 취소번호 취소상태 귀책 구분 취소사유 주문번호 주문상품번호 주문옵션번호 주문자 연락처 상품명 옵션명 수량 판매가*수량 결제일 취소요청일 취소완료일").get_by_label("").check()
        page.get_by_role("button", name="취소승인(환불)").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="취소승인(환불)").nth(1).click()
        page.wait_for_timeout(2000)
    
    #반품 관리 페이지 > 반품 승인
    def refund_approved(page):
        page.get_by_label("", exact=True).check()
        page.get_by_role("button", name="반품승인(환불)").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="반품승인(환불)").nth(1).click()
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)
        expect(page.get_by_text("반품승인(환불) 처리가 완료되었습니다."),"반품 승인 에러").to_be_visible()
        page.wait_for_timeout(2000)      




    #수거 송장 등록 (교환,반품,교환 재배송)
    def claim_invoice(page,option=None,redelivery=False):       
        
        if redelivery:
            delivery_info(page)
            page.get_by_role("button", name="교환재배송").nth(1).click()
            page.get_by_role("button", name="확인").click()
            page.wait_for_timeout(2000)
            expect(page.get_by_text("교환재배송 처리가 완료되었습니다."),"송장 저장 입력 에러").to_be_visible(timeout=90000)            
        else:
            retries = 0        
            while retries < option:
                try:     
                    page.get_by_role("button", name="수거 송장 등록").first.click()
                except TimeoutException:
                    page.get_by_role("button", name="수거 송장 등록").click()
                page.wait_for_timeout(2000)

                delivery_info(page)          
                page.get_by_role("button", name="저장").click()
                page.get_by_role("button", name="확인").click()
                expect(page.get_by_text("송장 등록 처리가 완료되었습니다."),"송장 저장 입력 에러").to_be_visible(timeout=90000)            
                retries += 1
                page.wait_for_timeout(2000)     



    #교환 - 수거 완료 
    def invoice_complete_btn(page):
        page.get_by_label("", exact=True).check()
        page.get_by_role("button", name="수거완료").click()
        page.wait_for_timeout(2000)
        page.get_by_role("row", name=" 구분 교환상태 상품명 옵션명 수량 판매가*수량 요청자").get_by_label("").check()
        page.get_by_role("button", name="수거완료").nth(1).click()
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)



    #교환 재배송 버튼
    def exchange_redelivery_btn(page):
        page.get_by_label("", exact=True).check()
        page.get_by_role("button", name="교환재배송").click()
        page.wait_for_timeout(2000)
        page.get_by_role("row", name=" 구분 교환상태 상품명 옵션명 수량 판매가*수량 요청자").get_by_label("").check()
        page.wait_for_timeout(2000)


    
    #교환 완료
    def exchange_completed_btn(page):
        page.get_by_label("", exact=True).check()
        page.get_by_role("button", name="교환완료").click()
        page.wait_for_timeout(2000)
        page.get_by_role("row", name=" 구분 교환상태 상품명 옵션명 수량 판매가*수량 요청자").get_by_label("").check()
        page.get_by_role("button", name="직접교환 완료").click()
        page.get_by_role("button", name="확인").click()
        expect(page.get_by_text("직접교환 완료 처리가 완료되었습니다."),"교환 완료 에러").to_be_visible(timeout=90000)            
        page.wait_for_timeout(2000)

    #구매확정 후 취소
    def complete_cancel(page):
        page.get_by_label("", exact=True).check()
        page.get_by_role("button", name="구매확정주문 취소").click()
        page.wait_for_timeout(2000)
        page.get_by_role("row", name=" 주문옵션번호 상품명 옵션명 수량 판매가*수량").get_by_label("").check()
        page.get_by_test_id("reason.reasonType").click()
        page.wait_for_timeout(2000)
        page.get_by_text("상품이 필요하지 않아요").click()
        page.wait_for_timeout(2000)
        page.get_by_test_id("acceptTerms").check()
        page.get_by_role("button", name="취소승인").click()
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)
