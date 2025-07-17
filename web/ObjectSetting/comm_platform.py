from web.BasicSetting.conftest import *
from datetime import datetime
from web.ObjectSetting.comm_orders import *
from playwright.sync_api import *
from web.ObjectSetting.common_object import *
from calendar import monthrange


class CommPlatformElements():

    def checkout_func(page):
        # 필수A 옵션 1개
        page.get_by_role("combobox").nth(1).select_option("0")
        # 필수C 옵션 선택
        # page.get_by_role("combobox").nth(1).select_option("2")
        page.wait_for_timeout(2000)
        # 수량 2개 선택
        page.locator(".e1wjoq3w7 > svg:nth-child(3)").first.click()
        page.wait_for_timeout(1000) 
        # [바로구매] 버튼 선택
        page.get_by_role("button", name="바로구매").first.click()
        page.wait_for_timeout(1000)

    def checkout_2_func(page):
        # 필수A 옵션 선택
        page.get_by_role("combobox").nth(1).select_option("0")
        page.wait_for_timeout(2000)
        # 8. [바로구매] 버튼 선택
        page.get_by_role("button", name="바로구매").first.click()
        page.wait_for_timeout(1000)

    def coupon_modification_modal(page):
        # 12.[쿠폰변경] 버튼 선택
        page.get_by_role("button", name="쿠폰 변경").click()
        # 13.'쿠폰 변경'모달창노출
        expect(page.locator("span").filter(has_text="쿠폰 변경"), '"쿠폰 변경 모달창" 요소 미노출').to_be_visible()
        # result = page.locator("span").filter(has_text="쿠폰 변경")
        # assert result is not None and result.is_visible(), "'쿠폰 변경 모달창' 요소가 보이지 않습니다."
        # 쿠폰변경 모달창 종료
        page.get_by_role("button", name="취소").click()
        page.wait_for_timeout(1000)

    def purchase(page):
        # 13.포인트 영역에[전액사용] 버튼 선택
        page.get_by_role("button", name="전액 사용").click()
        # 14.약관동의 영역에 'ㅁ 아래 내용에 모두 동의합니다. (필수)' 체크박스 선택
        
        page.locator("div").filter(has_text=re.compile(r"^아래 내용에 모두 동의합니다\. \(필수\)$")).get_by_role("checkbox").check()
        page.locator("span").filter(has_text="아래 내용에 모두 동의합니다. (필수)").nth(1).click()
        # selectors.setTestIdAttribute('data-element');
        # await page.getByTestId('AllAgreeLabel').click();
        # 15.[0원결제하기] 버튼 선택
        page.get_by_role("button", name="0원 결제하기").click()
        # 16.주문결과 페이지 이동 '주문결제가 완료되었습니다.' 문구 확인
        page.get_by_role("cell", name="[OHS Full TC] 기본기능 테스트 (장바구니 / 상품쿠폰 적용 / 수정금지)🐳😳").click()
        page.get_by_role("cell", name="0원").click()
        # selectors.setTestIdAttribute('data-element');
        # await expect(page.getByTestId('HeaderImage')).toHaveCount(1);
        expect(page.get_by_role("cell", name="0원"), '"0원" 요소 미노출').to_be_visible()
        # result = page.get_by_role("cell", name="0원")
        # assert result is not None and result.is_visible(), "'쿠폰 변경 모달창' 요소가 보이지 않습니다."
        page.wait_for_timeout(1000)

    def remove_coupon(page):
        # 15. '적용 안함' 라디오 버튼 선택
        page.get_by_role("button", name="쿠폰 변경").click()
        page.locator("label").filter(has_text="적용 안함").click()
        # selectors.setTestIdAttribute('data-element');
        # await page.getByTestId('NoUseRadio').getByTestId('Radio').click();
        # 16. [변경 완료] 버튼 선택
        page.get_by_role("button", name="변경 완료").click()
        # const okButton = page.getByRole('button', { name: '변경 완료' });
        page.wait_for_timeout(1000)


    def cart(page):
        # 필수A 옵션 1개
        page.get_by_role("combobox").nth(1).select_option("0")
        # 필수C 옵션 선택
        # page.get_by_role("combobox").nth(1).select_option("2")
        page.wait_for_timeout(1000)
        # [장바구니]버튼 선택
        page.get_by_role("button", name="장바구니").first.click()
        # 팝업에서[장바구니 가기] 버튼 선택
        page.get_by_role("button", name="장바구니 가기").click()
        page.wait_for_timeout(1000)  

    def cart_2(page):
        # 필수B 옵션
        page.get_by_role("combobox").nth(1).select_option("1")
        # 수량 3개 (3만원 이상 조건 충족)
        page.locator(".e1wjoq3w7 > svg:nth-child(3)").first.click()
        page.wait_for_timeout(1000)
        page.locator(".e1wjoq3w7 > svg:nth-child(3)").first.click()
        page.wait_for_timeout(1000)
        page.locator(".e1wjoq3w7 > svg:nth-child(3)").first.click()
        page.wait_for_timeout(1000)
        # [장바구니]버튼 선택
        page.get_by_role("button", name="장바구니").first.click()
        # 팝업에서[장바구니 가기] 버튼 선택
        page.get_by_role("button", name="장바구니 가기").click()
        page.wait_for_timeout(1000)  

    
    #장바구니 초기화
    def cart_reset(page): 
        page.get_by_label("장바구니 페이지 링크 버튼").click()
        page.wait_for_timeout(2000)

        elements_visible =page.get_by_role("button", name="선택삭제").is_visible()

        if elements_visible:
            page.get_by_role("button", name="선택삭제").click()
            page.get_by_test_id("bds-dim").get_by_role("button", name="삭제").click()
            page.wait_for_timeout(2000)
    
        else:
            page.wait_for_timeout(2000)


    #pdp > 옵션 선택 후 바로구매 (필수,필수,추가)
    def pdp_selectopt_checkout(page,esn,esn_count,esn2,esn2_count,adtn,adtn_count):
        #필수 옵션 선택 - A ~ D option Index (0,1,2,3) / 필수,필수옵션 수,추가,추가옵션 수
        option =["A","B","C","D"]
        
        esn_index= option.index(f"{esn}")      
       #필수옵션 클릭
        page.get_by_role("combobox").nth(1).select_option(f"{esn_index}")
        page.wait_for_timeout(2000)              
        #첫 클릭
        page.locator(".e1wjoq3w7 > svg:nth-child(3)").first.click()
        #나머지 옵션 클릭
        for _ in range(esn_count):
            page.locator(".e1wjoq3w7 > svg:nth-child(3) > path").first.click()
            page.wait_for_timeout(2000)

        #필수 옵션2 있을 경우, 클릭
        if esn2 == None:
            pass
        else:
            esn2_index= option.index(f"{esn2}") 
            page.get_by_role("combobox").nth(1).select_option(f"{esn2_index}")
            page.wait_for_timeout(2000)       
            option_plus=1
            #첫 클릭
            page.locator(".e1wjoq3w7 > svg:nth-child(3)").first.click()
            #나머지 옵션 클릭
            for _ in range(esn2_count): 
                page.locator(".e1wjoq3w7 > svg:nth-child(3) > path").first.click()
                page.wait_for_timeout(2000)

           
            page.wait_for_timeout(2000)

        #추가 옵션 있을 경우, 클릭
        if adtn == None:
            pass
        else:
            adtn_index= option.index(f"{adtn}")       
            page.get_by_role("combobox").nth(2).select_option(f"{adtn_index}")
            page.wait_for_timeout(2000)       
            option_plus=1
            #첫 클릭
            page.locator(".e1wjoq3w7 > svg:nth-child(3)").first.click() 
            # 나머지 옵션 클릭
            for _ in range(adtn_count):  
                page.locator(".e1wjoq3w7 > svg:nth-child(3) > path").first.click()
                page.wait_for_timeout(2000)
            page.wait_for_timeout(2000)

        page.get_by_role("button", name="바로구매").first.click(timeout=90000)
        page.wait_for_timeout(2000)
        

    #pdp > 옵션 선택 후 장바구니 (필수,필수,추가)
    def pdp_selectopt_cart(page,esn,esn_count,esn2,esn2_count,adtn,adtn_count):
        #필수 옵션 선택 - A ~ D option Index (0,1,2,3) / 필수,필수옵션 수,추가,추가옵션 수
        option =["A","B","C","D"]
        esn_index= option.index(f"{esn}")      

        #첫번째 필수 옵션
        page.get_by_role("combobox").nth(1).select_option(f"{esn_index}")
        page.wait_for_timeout(2000)    

        #첫 클릭
        page.locator(".e1wjoq3w7 > svg:nth-child(3)").first.click()
        #나머지 옵션 클릭
        for _ in range(esn_count):
            page.locator(".e1wjoq3w7 > svg:nth-child(3) > path").first.click()
            page.wait_for_timeout(2000)
        

        #필수 옵션2 있을 경우, 클릭
        if esn2 == None:
            pass
        else:
            esn2_index= option.index(f"{esn2}") 
            page.get_by_role("combobox").nth(1).select_option(f"{esn2_index}")
            page.wait_for_timeout(2000)       
            #첫 클릭
            page.locator(".e1wjoq3w7 > svg:nth-child(3)").first.click()
            #나머지 옵션 클릭
            for _ in range(esn2_count):
                page.locator(".e1wjoq3w7 > svg:nth-child(3) > path").first.click()
                page.wait_for_timeout(2000)
            

        #추가 옵션 있을 경우, 클릭
        if adtn == None:
            pass
        else:
            adtn_index= option.index(f"{adtn}")       
            page.get_by_role("combobox").nth(2).select_option(f"{adtn_index}")
            page.wait_for_timeout(2000)       
            #첫 클릭
            page.locator(".e1wjoq3w7 > svg:nth-child(3)").first.click()
            #나머지 옵션 클릭
            for _ in range(adtn_count):
                page.locator(".e1wjoq3w7 > svg:nth-child(3) > path").first.click()
                page.wait_for_timeout(2000)
                
        # [장바구니]버튼 선택
        page.get_by_role("button", name="장바구니").first.click(timeout=90000)
        page.wait_for_timeout(2000)
        # 팝업에서[장바구니 가기] 버튼 선택
        page.get_by_role("button", name="장바구니 가기").click()
        page.wait_for_timeout(1000)


    
    #pdp - 옵션 선택 > 쇼핑 계속하기 (옵션 디폴트)
    def pdp_goto_home(page):
        page.get_by_role("combobox").nth(1).select_option("1")
        page.locator(".e1wjoq3w7 > span:nth-child(3)").first.click()
        page.wait_for_timeout(2000)  
        page.get_by_role("combobox").nth(2).select_option("1")
        page.wait_for_timeout(2000)  
        page.get_by_role("button", name="장바구니").first.click()
        page.get_by_role("button", name="쇼핑 계속하기").click()
        page.wait_for_timeout(2000)  

     #pdp - 옵션선택 > 장바구니 이동 (옵션 디폴트)
    def pdp_goto_cart(page):
        page.get_by_role("combobox").nth(1).select_option("1")
        page.locator(".e1wjoq3w7 > span:nth-child(3)").first.click()        
        page.wait_for_timeout(2000)  
        page.get_by_role("combobox").nth(2).select_option("1")
        page.wait_for_timeout(2000)  
        page.get_by_role("button", name="장바구니").first.click(timeout=90000)
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="장바구니 가기").click()
        page.wait_for_timeout(1000)         
   
        
    #pdp 조립/설치비 체크박스 선택
    def pdp_assembly_checkbox(page):
        page.get_by_text("조립/설치신청").first.click()
        page.wait_for_timeout(1000)


   
    #pdp > 배송 예정일 선택 (희망일 배송)
    def pdp_expected_date(page):
        current_data= datetime.today() 
        month = current_data.month
        day = current_data.day         

        page.get_by_placeholder("희망배송일을 입력해주세요. (선택)").first.click()

        #1일~27일 경우 오늘 기준 "month"/"day+1" 선택
        if day < 28:
            page.get_by_label(str(month)+"월"+"  "+str(day+1)+"일").click()
            page.wait_for_timeout(1000)

        else:
            #28일 ~ 31일 경우
            page.get_by_label("다음 월").click()
            #캘린더 다음월 버튼 클릭하기
            page.get_by_label(str(month+1)+"월"+"  1일").click()
            #오늘 기준 "다음 month"/ 1일 고정 선택
            page.wait_for_timeout(1000)
            

    #PDP - 상품/장바구니 쿠폰 다운로드 
    def pdp_coupon_download(page):
        btn_name_visible=page.get_by_role("button", name="쿠폰 받기 ").is_visible()
        if btn_name_visible:
            page.get_by_role("button", name="쿠폰 받기 ").click()
            page.get_by_role("button", name="확인").click()
            page.wait_for_timeout(2000)
        else: 
            pass


    #PDP - 쿠폰 받기 뜨는지 확인
    def pdp_coupon_check(page):
        expect(page.get_by_role("button", name="쿠폰 받기 "), "쿠폰 받기 버튼 미노출").to_be_visible()
        page.wait_for_timeout(2000)


    #payment,claim - 장바구니 2상품 구매 
    def cart_purchase(page,product_id,product_id2):
        page.get_by_label("장바구니 페이지 링크 버튼").click()
        page.wait_for_timeout(2000)

        elements_visible =page.get_by_role("button", name="선택삭제").is_visible()

        if elements_visible:
            page.get_by_role("button", name="선택삭제").click()
            page.get_by_test_id("bds-dim").get_by_role("button", name="삭제").click()
            page.wait_for_timeout(2000)
    
        else:
            page.wait_for_timeout(2000)

        page.goto(f'https://qa-web.dailyhou.se/productions/{product_id}/selling', timeout= 0)
        page.wait_for_timeout(2000)     

        page.get_by_role("combobox").nth(1).select_option("1")
        page.locator(".e1wjoq3w7 > svg:nth-child(3)").first.click()
        page.wait_for_timeout(2000)
        for _ in range (3):
            page.locator(".e1wjoq3w7 > svg:nth-child(3) > path").first.click()
            page.wait_for_timeout(2000)

        page.get_by_role("button", name="장바구니").first.click()
        page.get_by_role("button", name="").click()
        page.wait_for_timeout(2000)  
        
        page.goto(f'https://qa-web.dailyhou.se/productions/{product_id2}/selling', timeout= 0)
        page.wait_for_timeout(2000)   

        page.get_by_role("combobox").nth(1).select_option("1")
        page.locator(".e1wjoq3w7 > svg:nth-child(3)").first.click()
        page.wait_for_timeout(2000)
        for _ in range (6):
            page.locator(".e1wjoq3w7 > svg:nth-child(3) > path").first.click()
            page.wait_for_timeout(2000)
        
        page.wait_for_timeout(2000)

        page.get_by_role("button", name="장바구니").first.click(timeout=90000)
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="장바구니 가기").click()
        page.wait_for_timeout(1000)         
        
        page.get_by_role("button", name="2개 상품 구매하기").click()
        page.wait_for_timeout(2000)






    #마이페이지 - 쿠폰함(정액쿠폰)
    def couponbox_download(page):
        page.goto('https://qa-web.dailyhou.se/user_shopping_pages/coupons', timeout= 0)
        page.get_by_text("[QA]자동화용 정액 쿠폰5,000원∙ 2026년 05월 31일까지∙ 10원 이상 구매시적용상품 보기 받기받기").click()
        page.locator("div:nth-child(6) > div:nth-child(21) > .coupon-item > button").first.click()
        page.wait_for_timeout(2000)

    #장바구니 - 비회원 구매하기 버튼 클릭 후 주문서 랜딩까지
    def guest_cart_purchase(page):
        with page.expect_popup() as page1_info:
            page.get_by_role("button", name="1개 상품 구매하기").click()
        page1 = page1_info.value
        page.wait_for_timeout(2000)
        page1.get_by_role("button", name="비회원 구매하기").click()
        page.wait_for_timeout(2000)


    #PDP - 비회원 옵션 선택 바로구매 후 주문서 랜딩까지
    def guest_pdp_purchase(page):
        # 필수A 옵션 1개
        page.get_by_role("combobox").nth(1).select_option("0")
        page.wait_for_timeout(1000)
        with page.expect_popup() as page1_info:
            page.get_by_role("button", name="바로구매").first.click(timeout=90000)
        page.wait_for_timeout(2000)
        page1 = page1_info.value
        page.wait_for_timeout(2000)
        page1.get_by_role("button", name="비회원 구매하기").click()
        page.wait_for_timeout(2000)


    #PDP - 메모 필수 상품 선택 후 장바구니
    def cart_require_memo(page):
        # 필수A 옵션 1개
        page.get_by_role("combobox").nth(1).select_option("0")
        page.wait_for_timeout(1000)
        # 메모 입력
        page.get_by_placeholder("주문에 필요한 내용을 적어주세요").first.click()
        page.wait_for_timeout(2000)
        page.get_by_placeholder("주문에 필요한 내용을 적어주세요").first.fill("memo")
        page.wait_for_timeout(2000)
        # [장바구니]버튼 선택
        page.get_by_role("button", name="장바구니").first.click()
        # 팝업에서[장바구니 가기] 버튼 선택
        page.get_by_role("button", name="장바구니 가기").click()
        page.wait_for_timeout(1000)


    #장바구니 메모삭제 후 주문서 생성
    def delete_memo_order(page):
        page.get_by_placeholder("주문메모 입력").click()
        page.get_by_placeholder("주문메모 입력").fill("")
        page.wait_for_timeout(1000)
        page.get_by_placeholder("주문메모 입력").blur()
        page.wait_for_timeout(1000)
        # 경고 문구 확인 후 주문서 생성
        assert page.locator("text=주문메모는 필수 입력입니다.").is_visible()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="1개 상품 구매하기").click()
        page.wait_for_timeout(2000)
        assert page.get_by_test_id("snackbar-item").get_by_text("주문메모는 필수 입력입니다.").is_visible()
        page.wait_for_timeout(1000)


    #장바구니 희망배송일 변경
    def cart_mod_delivery(page):
        current_data= datetime.today()
        year = current_data.year
        month = current_data.month
        day = current_data.day
        #특정 월의 마지막 날 구하기
        last_day_of_month = monthrange(year, month)[1]

        page.get_by_placeholder("희망배송일을 입력해주세요. (선택)").click()
        page.wait_for_timeout(1000)
        #오늘날짜 선택안됨 확인
        assert page.get_by_label(str(month)+"월"+" "+str(day)+"일").is_disabled()
        page.wait_for_timeout(1000)
        #날짜 변경 확인
        if day == last_day_of_month:
            page.get_by_label("다음 월").click()
            page.get_by_label(str(month+1)+"월"+" 1일").click()
            page.wait_for_timeout(1000)
        else:
            page.get_by_label(str(month)+"월"+" "+str(day+1)+"일").click()
            page.wait_for_timeout(1000)
        assert page.get_by_test_id("snackbar-item").get_by_text("저장되었습니다.").is_visible()
        page.wait_for_timeout(1000)


    #빈 장바구니 확인 후 상품 담으러 가기
    def emptycart_goto_shop(page):
        page.get_by_label("장바구니 페이지 링크 버튼").click()
        page.wait_for_timeout(2000)
        #빈 장바구니 확인
        assert page.get_by_role("button", name="상품 담으러 가기").is_visible()
        page.get_by_role("button", name="상품 담으러 가기").click()
        page.wait_for_timeout(2000)
        #쇼핑홈 이동 확인
        assert page.get_by_role("link", name="쇼핑홈").is_visible()
    
            
    #장바구니 옵션 품절 확인 후 품절 모두 삭제
    def cart_outopt_delete(page):
        page.get_by_label("장바구니 페이지 링크 버튼").click()
        page.wait_for_timeout(2000)

        assert page.get_by_text("품절퀸 (Q)").is_visible()
        page.wait_for_timeout(1000)
        assert page.get_by_role("button", name="품절 모두 삭제").is_visible()
        page.get_by_role("button", name="품절 모두 삭제").click()
        page.get_by_test_id("bds-dim").get_by_role("button", name="삭제").click()
        page.wait_for_timeout(2000)
        assert page.get_by_text("품절퀸 (Q)").is_hidden()


    #장바구니 상품 품절 확인 후 품절 모두 삭제 후 빈 장바구니
    def cart_outstock_delete(page):
        page.get_by_label("장바구니 페이지 링크 버튼").click()
        page.wait_for_timeout(2000)

        assert page.get_by_text("품절싱글 (S)").is_visible()
        page.wait_for_timeout(1000)
        assert page.get_by_role("link", name="[벨라][자동화][변경X]품절 상품.. 이미지 품절 [젠티스] [벨라][자동화][변경X]품절 상품.. 배송비 15,000원 업체직접배송").is_visible()
        page.wait_for_timeout(1000)
        assert page.get_by_role("button", name="품절 모두 삭제").is_visible()
        page.get_by_role("button", name="품절 모두 삭제").click()
        page.get_by_test_id("bds-dim").get_by_role("button", name="삭제").click()
        page.wait_for_timeout(2000)
        assert page.get_by_role("button", name="상품 담으러 가기").is_visible()


    #글린다 조합 클릭 후 장바구니
    def glinda_goto_cart(page, combo_id):
        page.get_by_text(f"조합 {combo_id}").click()
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="패키지 구매하기").click()
        page.wait_for_timeout(1000)


    #상품번호로 pdp 바로 랜딩 - 결제 테스트 
    def pdp_url(page,product_id):
        page.goto(f'https://qa-web.dailyhou.se/productions/{product_id}/selling', timeout= 0)
        page.wait_for_timeout(2000)     





' test_CommPlatform Exception 용 함수'''''''''''''''''''''
class CommPlatformExceptionElements():
    def send_api_get(api_url):
        response = requests.get(api_url, verify=False, timeout=10)
        return response

    def check_cart(page):
        CommPlatformElements.cart(page)
        # 장바구니 확인
        expect(page.get_by_role("link", name="[묶음N] 무료, 제주 4500, 반품1700, 교환3400"), '장바구니 상품명 미노출').to_be_visible()
        CommPlatformElements.cart_reset(page)

    def check_cart_order(page):
        CommPlatformElements.cart_reset(page)
        page.goto('https://qa-web.dailyhou.se/productions/100008379/selling', timeout= 0)
        CommPlatformElements.cart_2(page)
        page.wait_for_timeout(2000)
        # 장바구니 진입
        page.get_by_role("button", name="1개 상품 구매하기").click()
        page.wait_for_timeout(5000)
        # 포인트 전액사용 후 결제하기
        page.get_by_role("button", name="전액 사용").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="0원 결제하기").click()
        page.wait_for_timeout(2000)
        expect(page.get_by_role("button", name="주문현황 보기"), '주문현황 보기 버튼 미노출').to_be_visible()
        page.get_by_role("button", name="주문현황 보기").click()

    def check_order_coupon(page):
        CommPlatformElements.checkout_func(page)
        page.wait_for_timeout(2000)
        expect(page.get_by_text(re.compile(r"상품 쿠폰-.*")), '"상품 쿠폰 적용 금액" 요소 미노출').to_be_visible()
        page.get_by_role("button", name="쿠폰 변경").click()
        expect(page.locator("span").filter(has_text="쿠폰 변경"), '쿠폰 변경 팝업 미노출').to_be_visible()
        page.get_by_role("button", name="").click()

    def check_delivery_list(page):
        CommPlatformElements.cart_2(page)
        page.wait_for_timeout(2000)
        # 장바구니 진입
        page.get_by_role("button", name="1개 상품 구매하기").click()
        page.wait_for_timeout(2000)
        # 포인트 전액사용 후 결제하기
        page.get_by_role("button", name="전액 사용").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="0원 결제하기").click()
        page.wait_for_timeout(2000)
        # 나의 쇼핑 진입
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("link", name="나의 쇼핑").click()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name=re.compile(r"입금대기.*")).click()
        page.wait_for_timeout(1000)
        # API Response check
        api_url = 'https://qa-web.dailyhou.se/user_shopping_pages/order_list?status=0'
        # response = send_api_get(api_url)
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200
        page.get_by_role("link", name=re.compile(r"결제완료.*")).click()
        page.wait_for_timeout(1000)

        # API Response check
        api_url = 'https://qa-web.dailyhou.se/user_shopping_pages/order_list?status=2'
        # response = send_api_get(api_url)
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200
        page.get_by_role("link", name=re.compile(r"배송준비.*")).click()
        # API Response check
        api_url = 'https://qa-web.dailyhou.se/user_shopping_pages/order_list?status=3'
        # response = send_api_get(api_url)
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200
        page.get_by_role("link", name=re.compile(r"배송중.*")).click()
        # API Response check
        api_url = 'https://qa-web.dailyhou.se/user_shopping_pages/order_list?status=4'
        # response = send_api_get(api_url)
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200
        page.get_by_role("link", name=re.compile(r"배송완료.*")).click()
        # API Response check
        api_url = 'https://qa-web.dailyhou.se/user_shopping_pages/order_list?status=5'
        # response = send_api_get(api_url)
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200
        page.get_by_role("link", name=re.compile(r"구매확정.*")).click()
        # API Response check
        api_url = 'https://qa-web.dailyhou.se/user_shopping_pages/order_list?status=6'
        # response = send_api_get(api_url)
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200

    def check_order_detail(page):
        CommPlatformElements.cart_reset(page)
        page.goto('https://qa-web.dailyhou.se/productions/100008379/selling', timeout= 0)
        CommPlatformElements.cart_2(page)
        page.wait_for_timeout(2000)
        # 장바구니 진입
        page.get_by_role("button", name="1개 상품 구매하기").click()
        page.wait_for_timeout(5000)
        # 포인트 전액사용 후 결제하기
        page.get_by_role("button", name="전액 사용").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="0원 결제하기").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="주문현황 보기").click()
        page.wait_for_timeout(2000)
        # 나의 쇼핑 진입
        # page.get_by_label("프로필 메뉴").click()
        # page.wait_for_timeout(2000)
        # page.get_by_role("link", name="나의 쇼핑").click()
        # page.wait_for_timeout(2000)
        page.get_by_role("link", name=re.compile(r"결제완료.*")).click()
        page.wait_for_timeout(2000)
        # page.get_by_text("주문상세").click()
        page.locator(".css-iz5zqx").first.click() # 첫번째 상품 주문상세 버튼
        expect(page.get_by_text("주문상세"), '주문상세 페이지 미노출').to_be_visible()

    def check_period_delivery(page):
        page.goto('https://qa-web.dailyhou.se/user_shopping_pages/order_list', timeout= 0)
        expect(page.get_by_role("button", name="3개월 전"),'디폴트 배송필터 체크').to_be_visible()
        page.wait_for_timeout(2000)    

        # 기간 핉터 체크 - api 체크 
        api_url = 'https://qa-web.dailyhou.se/user_shopping_pages/order_list?before=1'
        # response = send_api_get(api_url)
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200
        page.get_by_role("button", name="3개월 전").click()
        page.wait_for_timeout(1000)     
        page.get_by_text("1개월 전").click()
        page.wait_for_timeout(1000)     


        api_url = 'https://qa-web.dailyhou.se/user_shopping_pages/order_list?before=3'
        # response = send_api_get(api_url)
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200
        page.get_by_role("button", name="1개월 전").click()
        page.wait_for_timeout(1000)     
        page.get_by_text("3개월 전").click()
        page.wait_for_timeout(1000)     

        api_url = 'https://qa-web.dailyhou.se/user_shopping_pages/order_list?before=6'
        # response = send_api_get(api_url)
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200
        page.get_by_role("button", name="3개월 전").click()
        page.wait_for_timeout(1000)     
        page.get_by_text("6개월 전").click()
        page.wait_for_timeout(1000)

        api_url = 'https://qa-web.dailyhou.se/user_shopping_pages/order_list?before=12'
        # response = send_api_get(api_url)
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200
        page.get_by_role("button", name="6개월 전").click()
        page.wait_for_timeout(1000)     
        page.get_by_text("1년 전").click()
        page.wait_for_timeout(1000)

        api_url = 'https://qa-web.dailyhou.se/user_shopping_pages/order_list?before=24'
        # response = send_api_get(api_url)
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200
        page.get_by_role("button", name="1년 전").click()
        page.wait_for_timeout(1000)     
        page.get_by_text("2년 전").click()
        page.wait_for_timeout(1000)

        api_url = 'https://qa-web.dailyhou.se/user_shopping_pages/order_list?before=36'
        # response = send_api_get(api_url)
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200
        page.get_by_role("button", name="2년 전").click()
        page.wait_for_timeout(1000)     
        page.get_by_text("3년 전").click()
        page.wait_for_timeout(2000)




