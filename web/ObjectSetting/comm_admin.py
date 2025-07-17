from web.BasicSetting.conftest import *
from calendar import monthrange
from datetime import datetime

#어드민 - 상품관리 메뉴
class ProductListElements():

    #어드민 특정 필수옵션 품절 처리
    def set_product_outstock(page,product_id,opt):
        page.goto(f'https://admin-portal.qa.dailyhou.se/commerce/catalog/catalog-goods/{product_id}', timeout= 0)
        page.wait_for_timeout(2000)
        #어드민 로딩 확인
        admin_load = page.frame_locator("iframe[title=\"External Site\"]").get_by_role("heading", name="상품 정보 수정")
        load_check = 0
        while load_check < 3:
            if admin_load.is_hidden():
                page.goto(f'https://admin-portal.qa.dailyhou.se/commerce/catalog/catalog-goods/{product_id}', timeout= 0)
                page.wait_for_timeout(2000)
                load_check += 1
            else:
                load_check = 4
        print(f"retry 횟수 = {load_check}", end='')
        assert load_check == 4

        page.frame_locator("iframe[title=\"External Site\"]").locator('role=button',has_text="필수 구매옵션").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id(f"goodsOptions.{opt}.stockStatus").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_text("품절", exact=True).click()
        page.wait_for_timeout(1000)
        
        page.on("dialog", lambda dialog: dialog.accept())
        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="저장").click()
        page.wait_for_timeout(1000)

    
    #어드민 필수옵션 판매중 처리
    def set_product_instock(page,product_id):
        page.goto(f'https://admin-portal.qa.dailyhou.se/commerce/catalog/catalog-goods/{product_id}', timeout= 0)
        page.wait_for_timeout(2000)
        #어드민 로딩 확인
        admin_load = page.frame_locator("iframe[title=\"External Site\"]").get_by_role("heading", name="상품 정보 수정")
        load_check = 0
        while load_check < 3:
            if admin_load.is_hidden():
                page.goto(f'https://admin-portal.qa.dailyhou.se/commerce/catalog/catalog-goods/{product_id}', timeout= 0)
                page.wait_for_timeout(2000)
                load_check += 1
            else:
                load_check = 4
        print(f"retry 횟수 = {load_check}", end='')
        assert load_check == 4

        page.frame_locator("iframe[title=\"External Site\"]").locator('role=button',has_text="필수 구매옵션").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("goodsOptions.0.stockStatus").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_text("판매중").click()
        page.wait_for_timeout(1000)
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("goodsOptions.1.stockStatus").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("menuitem", name="판매중").locator("span").click()
        page.wait_for_timeout(1000)
        
        page.on("dialog", lambda dialog: dialog.accept())
        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="저장").click()
        page.wait_for_timeout(1000)


#어드민 - 고객혜택관리 메뉴
class BenefitListElements():

    #어드민 쿠폰틀 관리 - 상품 쿠폰틀 생성
    def create_product_mold(page,product_id,name,type,amount):
        #적용할 상품번호 / 쿠폰이름 / 쿠폰타입(다운로드형-1, 어드민발행형-2) / 정액 금액
        #product_id에 텍스트 형태로 추가할 상품들 추가 가능 ex) "1023523,23345234,2334234"

        page.goto('https://admin-portal.qa.dailyhou.se/commerce/benefit/goods_coupon_mold', timeout= 0)
        page.wait_for_timeout(2000)
        #어드민 로딩 확인
        admin_load = page.frame_locator("iframe[title=\"External Site\"]").get_by_role("heading", name="쿠폰틀 조회")
        load_check = 0
        while load_check < 3:
            if admin_load.is_hidden():
                page.goto('https://admin-portal.qa.dailyhou.se/commerce/benefit/goods_coupon_mold', timeout= 0)
                page.wait_for_timeout(2000)
                load_check += 1
            else:
                load_check = 4
        print(f"retry 횟수 = {load_check}", end='')
        assert load_check == 4

        current_data= datetime.today()
        year = current_data.year
        month = current_data.month
        day = current_data.day
        hour = current_data.hour
        hour = f'{hour:02d}'
        #한글로 요일 구하기
        weekday_num = current_data.weekday()
        weekdays_kr = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
        weekday = weekdays_kr[weekday_num]
        next_weekday = weekdays_kr[weekday_num+1]
        #특정 월의 마지막 날 구하기
        last_day_of_month = monthrange(year, month)[1]

        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="상품쿠폰틀 생성").click()
        page.wait_for_timeout(1000)
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("couponNameDetail.promotionName").fill(str(name))

        if type == 2:
            page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("publishType").click()
            page.frame_locator("iframe[title=\"External Site\"]").get_by_text("어드민 발행형").click()

        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("discountAmount").fill(str(amount))
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("minBaseAmount").fill("1")
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("isInfiniteBudget").check()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("chargeRatio").fill("60")
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("isInfinitePublishCnt").check()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_placeholder("발행 시작일 설정").click()
        #오늘일자, 현재시
        page.frame_locator("iframe[title=\"External Site\"]").get_by_label("Choose "+str(year)+"년 "+str(month)+"월 "+str(day)+"일 "+str(weekday)).click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("publishDateDetail.startTime").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_text("("+str(hour)+":00)").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_placeholder("발행 종료일 설정").click()
        #내일일자, 특정시
        if day == last_day_of_month:
            page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="").click()
            page.frame_locator("iframe[title=\"External Site\"]").get_by_label("Choose "+str(year)+"년 "+str(month+1)+"월 1일 "+str(next_weekday)).click()
        else:
            page.frame_locator("iframe[title=\"External Site\"]").get_by_label("Choose "+str(year)+"년 "+str(month)+"월 "+str(day+1)+"일 "+str(next_weekday)).click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("publishDateDetail.endTime").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_text("00:00AM (00:00)").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_label("발행일 기준만료").check()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("expiredInDays").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("listbox").get_by_text("0", exact=True).click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("ownerTeamId").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_text("영업").click()
        page.wait_for_timeout(1000)
        page.frame_locator("iframe[title=\"External Site\"]").get_by_placeholder("쿠폰 책임자 이름 입력").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_text("(영업) Dana / dana.do").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("ids").fill(str(product_id))
        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="상품 등록").click()
        page.wait_for_timeout(1000)
        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="확인").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="쿠폰 등록").click()
        page.wait_for_timeout(1000)
        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="상품쿠폰틀 생성").click()

        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("heading", name="쿠폰틀 조회").is_visible()
        page.wait_for_timeout(3000)


    #어드민 쿠폰틀 관리 - 장바구니 쿠폰틀 생성
    def create_cart_mold(page,product_id,name,type,amount):
        #적용할 상품번호 / 쿠폰이름 / 쿠폰타입(다운로드형-1, 어드민발행형-2) / 정액 금액
        #product_id에 텍스트 형태로 추가할 상품들 추가 가능 ex) "1023523,23345234,2334234"

        page.goto('https://admin-portal.qa.dailyhou.se/commerce/benefit/goods_coupon_mold', timeout= 0)
        page.wait_for_timeout(2000)
        #어드민 로딩 확인
        admin_load = page.frame_locator("iframe[title=\"External Site\"]").get_by_role("heading", name="쿠폰틀 조회")
        load_check = 0
        while load_check < 3:
            if admin_load.is_hidden():
                page.goto('https://admin-portal.qa.dailyhou.se/commerce/benefit/goods_coupon_mold', timeout= 0)
                page.wait_for_timeout(2000)
                load_check += 1
            else:
                load_check = 4
        print(f"retry 횟수 = {load_check}", end='')
        assert load_check == 4

        current_data= datetime.today()
        year = current_data.year
        month = current_data.month
        day = current_data.day
        hour = current_data.hour
        hour = f'{hour:02d}'
        #한글로 요일 구하기
        weekday_num = current_data.weekday()
        weekdays_kr = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
        weekday = weekdays_kr[weekday_num]
        next_weekday = weekdays_kr[weekday_num+1]
        #특정 월의 마지막 날 구하기
        last_day_of_month = monthrange(year, month)[1]

        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="장바구니쿠폰틀 생성").click()
        page.wait_for_timeout(1000)
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("couponNameDetail.promotionName").fill(str(name))

        if type == 2:
            page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("publishType").click()
            page.frame_locator("iframe[title=\"External Site\"]").get_by_text("어드민 발행형").click()
            
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("discountAmount").fill(str(amount))
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("minBaseAmount").fill("1")
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("isInfiniteBudget").check()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("chargeRatio").fill("60")
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("isInfinitePublishCnt").check()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_placeholder("발행 시작일 설정").click()
        #오늘일자, 현재시
        page.frame_locator("iframe[title=\"External Site\"]").get_by_label("Choose "+str(year)+"년 "+str(month)+"월 "+str(day)+"일 "+str(weekday)).click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("publishDateDetail.startTime").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_text("("+str(hour)+":00)").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_placeholder("발행 종료일 설정").click()
        #내일일자, 특정시
        if day == last_day_of_month:
            page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="").click()
            page.frame_locator("iframe[title=\"External Site\"]").get_by_label("Choose "+str(year)+"년 "+str(month+1)+"월 1일 "+str(next_weekday)).click()
        else:
            page.frame_locator("iframe[title=\"External Site\"]").get_by_label("Choose "+str(year)+"년 "+str(month)+"월 "+str(day+1)+"일 "+str(next_weekday)).click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("publishDateDetail.endTime").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_text("00:00AM (00:00)").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_label("발행일 기준만료").check()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("expiredInDays").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("listbox").get_by_text("0", exact=True).click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("ownerTeamId").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_text("영업").click()
        page.wait_for_timeout(1000)
        page.frame_locator("iframe[title=\"External Site\"]").get_by_placeholder("쿠폰 책임자 이름 입력").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_text("(영업) Dana / dana.do").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("ids").fill(str(product_id))
        page.frame_locator("iframe[title=\"External Site\"]").locator("section").filter(has_text="쿠폰 적용 상품").get_by_role("button").click()
        page.wait_for_timeout(1000)
        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="확인").click()
        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="쿠폰 등록").click()
        page.wait_for_timeout(1000)
        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="장바구니쿠폰틀 생성").click()

        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("heading", name="쿠폰틀 조회").is_visible()
        page.wait_for_timeout(3000)


    #어드민 쿠폰 관리 - 어드민발행형쿠폰 발행
    def publish_admin_coupon(page,mold_id,user_id,count):
        #적용할 쿠폰틀아이디 / 유저아이디 / 발행 횟수

        page.goto('https://admin-portal.qa.dailyhou.se/commerce/benefit/goods_coupon', timeout= 0)
        page.wait_for_timeout(2000)
        #어드민 로딩 확인
        admin_load = page.frame_locator("iframe[title=\"External Site\"]").get_by_role("heading", name="쿠폰 조회/수정")
        load_check = 0
        while load_check < 3:
            if admin_load.is_hidden():
                page.goto('https://admin-portal.qa.dailyhou.se/commerce/benefit/goods_coupon', timeout= 0)
                page.wait_for_timeout(2000)
                load_check += 1
            else:
                load_check = 4
        print(f"retry 횟수 = {load_check}", end='')
        assert load_check == 4

        check = 0

        page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="어드민발행형쿠폰 발행").click()
        page.wait_for_timeout(1000)
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("couponMoldId").fill(str(mold_id))
        page.frame_locator("iframe[title=\"External Site\"]").get_by_test_id("userId").fill(str(user_id))

        while check < count:
            page.frame_locator("iframe[title=\"External Site\"]").get_by_role("button", name="쿠폰 발행").click()
            expect(page.frame_locator("iframe[title=\"External Site\"]").get_by_text("쿠폰 발행에 성공했습니다.")).to_be_visible()
            page.frame_locator("iframe[title=\"External Site\"]").get_by_text("쿠폰 발행에 성공했습니다.").click()
            check += 1
            page.wait_for_timeout(2000)

