from web.BasicSetting.conftest import *
from playwright.sync_api import *
from app.common.base_method.exception_func import timeout_handler, write_log
from web.ObjectSetting.comm_platform import *

class CommServiceElements():

    # Summary
    def Service_func(page):
        # page = browser.new_page()
        page.goto('https://stage-web.dailyhou.se/')
        element = page.get_by_placeholder("이메일")
        return element
    
    def into_shopping_tap(page):
        # 쇼핑 탭 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        expect(page.get_by_role("link", name="쇼핑홈"), '"쇼핑홈" 요소 미노출').to_be_visible()
        # 카테고리 탭 확인
        page.get_by_role("link", name="카테고리").click()
        expect(page.get_by_role("heading", name="가구", exact=True).get_by_role("link"), '"가구" 요소 미노출').to_be_visible()
        # 베스트 탭 확인
        page.get_by_role("link", name="베스트").click()
        expect(page.get_by_role("button", name="실시간 베스트"), '"실시간 베스트" 요소 미노출').to_be_visible()
        # 오늘의딜 탭 확인
        page.get_by_role("link", name="오늘의딜").click()
        expect(page.get_by_role("button", name="스크랩"), '스크랩버튼 요소 미노출').to_be_visible()
        # 스페셜/피드 탭 확인
        page.get_by_role("link", name="스페셜/피드").click()
        expect(page.get_by_role("button", name="판매상품 목록보기"), '"판매상품 목록보기" 요소 미노출').to_be_visible()
        # 프리미엄 탭 확인
        page.get_by_role("link", name="프리미엄", exact=True).click()
        #expect(page.get_by_role("button", name="브랜드"), '"브랜드" 요소 미노출').to_be_visible()
        # 프리미엄 페이지 API Response check
        api_url = 'https://store.qa-web.dailyhou.se/exhibitions/10294'
        response = send_api_get(api_url)
        assert response.status_code == 200
        # 기획전 탭 확인
        page.get_by_role("link", name="기획전", exact=True).click()
        expect(page.locator('div[data-element="MainWrapper"][data-component="ExhibitionItem"]').nth(0), '"기획전" 요소 미노출').to_be_visible()
        
    def into_quick_menu(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        # 퀵 메뉴 버튼 노출 확인
        for _ in range(3):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="Test BEST").scroll_into_view_if_needed()
        page.wait_for_timeout(3000)
        expect(page.get_by_role("link", name="Test BEST"), '"BEST" 메뉴 미노출').to_be_visible()
        expect(page.get_by_role("link", name="Clik 오늘의딜"), '"오늘의딜" 메뉴 미노출').to_be_visible()
        expect(page.get_by_role("link", name="new 프리미엄"), '"프리미엄" 메뉴 미노출').to_be_visible()
        expect(page.get_by_role("link", name="기획전상세"), '"기획전상세" 메뉴 미노출').to_be_visible()
        page.wait_for_timeout(1000)
       
    def confirm_category(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        # 카테고리 > 가구 & 패브릭 노출 확인
        page.get_by_role("heading", name="카테고리", exact=True).scroll_into_view_if_needed()
        expect(page.get_by_role("link", name="가구", exact=True), '"가구" 메뉴 미노출').to_be_visible()
        page.wait_for_timeout(1000)
        expect(page.get_by_role("link", name="패브릭"), '"패브릭" 메뉴 미노출').to_be_visible()

    def confirm_iif(page):
        # page.get_by_role("link", name="쇼핑", exact=True).click()
        page.goto("https://qa-web.dailyhou.se/productions/412330/selling")
        page.wait_for_timeout(2000)
        for i in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="추천").click()
        expect(page.locator("article").filter(has_text=re.compile(r"소희 브랜드오늘의집 배송 상품.*")).get_by_role("link"), 'IIF 영역 미노출').to_be_visible()

    def confirm_iif_detail(page):
        # page.get_by_role("link", name="쇼핑", exact=True).click()
        page.goto("https://qa-web.dailyhou.se/productions/412330/selling")
        page.wait_for_timeout(2000)
        for i in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="추천").click()
        # page.locator("article").filter(has_text="소희 브랜드오늘의집 배송 상품225% 30,0001리뷰 1최대 5천원 쿠폰최대 30% 결제할인").get_by_role("link").click()
        page.locator("article").filter(has_text=re.compile(r"소희 브랜드오늘의집 배송 상품.*")).get_by_role("link").click()
        expect(page.get_by_text("오늘의집 배송 상품2"), 'IIF 상세페이지 미노출').to_be_visible()

    def confirm_iif_scrap(page):
        # page.get_by_role("link", name="쇼핑", exact=True).click()
        page.goto("https://qa-web.dailyhou.se/productions/412330/selling")
        page.wait_for_timeout(2000)
        for i in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="추천").click()
        # page.locator("article").filter(has_text="소희 브랜드오늘의집 배송 상품225% 30,0001리뷰 1최대 5천원 쿠폰최대 30% 결제할인").get_by_role("link").click()
        page.locator("article").filter(has_text=re.compile(r"소희 브랜드오늘의집 배송 상품.*")).get_by_label("scrap 토글 버튼").click()
        expect(page.get_by_text("스크랩했습니다."), 'IIF 상세페이지 미노출').to_be_visible()
        page.wait_for_timeout(2000)
        page.locator("article").filter(has_text=re.compile(r"소희 브랜드오늘의집 배송 상품.*")).get_by_label("scrap 토글 버튼").click()
        expect(page.get_by_text("스크랩북에서 삭제했습니다."), 'IIF 상세페이지 미노출').to_be_visible()

    def confirm_collection_option(page):
        page.goto("https://qa-web.dailyhou.se/productions/100032009/selling?affect_id=0&affect_type=CategoryMDpicks")
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="상품을 선택하세요.").first.click()
        page.get_by_role("button", name="1 주니 평상형(서랍없음) LED침대 매트제외 3colors SS/Q 20% 199,000").click()
        page.locator(".form-control").first.select_option("0")
        page.locator("div:nth-child(2) > .form-control").first.select_option("0")
        page.wait_for_timeout(2000)
        expect(page.get_by_role("heading", name="사이즈: 슈퍼싱글 / 색상: 화이트").first, '모음전 옵션 미노출').to_be_visible()

    def confirm_collection_banner(page):
        page.goto("https://qa-web.dailyhou.se/productions/100032009/selling?affect_id=0&affect_type=CategoryMDpicks")
        page.wait_for_timeout(2000)
        expect(page.locator(".production-selling-promotion-banner"), '모음전 옵션 미노출').to_be_visible()


    def confirm_today_deal(page):
        # 오늘의딜 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.wait_for_load_state("networkidle")
        
        for i in range(5):            
            page.evaluate("window.scrollTo(0, document.body.scrollHeight);") # 페이지 스크롤 내리기
            page.wait_for_timeout(1 * 1000) # 페이지 로딩 대기

            title_locator = page.locator('h1[data-element="Title"]').filter(has_text='오늘의딜')
            if title_locator.is_visible() :
                write_log('web', f'{i+1}회 스크롤 완료, 요소 보임')
                break
            else:
                write_log('web', f'{i+1}회 스크롤 완료, 요소 없음')
            if i == 4:
                raise TimeoutException(f"오늘의딜 타이틀 못찾음")
        
        expect(page.locator('article.css-e1g59h').first).to_be_visible() # 상품 카드 체크
        write_log('web', '첫번째 상품 이름:' + page.locator('article.css-e1g59h').first.locator('.product-name.css-11e7usa.eo39oc44').inner_text())
        # API Response check
        api_url = 'https://store.qa-web.dailyhou.se/today_deals'
        response = send_api_get(api_url)
        assert response.status_code == 200

    def confirm_plp(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.locator(".css-b2kr9d").filter(has_text='오늘의딜').click() # 칩카루셀 아이템리스트 > 오늘의딜 클릭
        page.wait_for_load_state("networkidle") 
        page.locator('[data-element="Container"][data-component="SubModuleItemList"]').locator('[style="overflow-anchor: none;"]').get_by_role('article').first.click()
        write_log('web',f'클릭한 상품 url : {page.url}')
        expect(page.get_by_text("주문금액").first, '"상품상세" 메뉴 미노출').to_be_visible()

    def confirm_plp2(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.wait_for_load_state("networkidle")
        
        # for i in range(5):            
        #     page.evaluate("window.scrollTo(0, document.body.scrollHeight);") # 페이지 스크롤 내리기
        #     page.wait_for_timeout(1 * 1000) # 페이지 로딩 대기
        for i in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)


            title_locator = page.locator('h1[data-element="Title"]').filter(has_text='오늘의딜')
            if title_locator.is_visible() :
                write_log('web', f'{i+1}회 스크롤 완료, 요소 보임')
                break
            else:
                write_log('web', f'{i+1}회 스크롤 완료, 요소 없음')
            if i == 4:
                raise TimeoutException(f"오늘의딜 타이틀 못찾음")
        page.locator("article").filter(has_text=re.compile(r"298일 남음.*")).get_by_role("link").nth(0).click()
        expect(page.get_by_role("button", name="공유하기"), '"상품상세" 메뉴 미노출').to_be_visible()
    
    def confirm_plp3(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        for i in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.locator("label").filter(has_text="오늘의딜").click()
        page.wait_for_timeout(1000)
        # page.locator("[data-test-id=\"virtuoso-item-list\"] div").filter(has_text=re.compile(r".*리뷰.*")).nth(1).click()
        page.locator("article").filter(has_text=re.compile(r"베베숲시그니처 레드 70매.*")).get_by_role("link").click()
        page.wait_for_timeout(2000)
        expect(page.get_by_text("주문금액").first, '"상품상세" 메뉴 미노출').to_be_visible()


    def confirm_popular_product(page):
        # 몰랐던 취향까지 발견하기 (구 인기상품) 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        # page.get_by_role("heading", name="몰랐던 취향까지 발견하기").scroll_into_view_if_needed()
        expect(page.get_by_role("heading", name="몰랐던 취향까지 발견하기"), '인기상품 메뉴 미노출').to_be_hidden()

    def confirm_item_carousel(page, case='carousel'):
        item_carousel = page.locator('[data-component="HomeModuleChipCarouselItemCarousel"]')
        item_carousel_chip = item_carousel.locator('.sticky-container')
        timeout_handler(lambda: page.goto('https://store.qa-web.dailyhou.se/', timeout= 0), "goto_shop_home")

        if case == 'carousel': # 아이템 카루셀 확인 
            timeout_handler(lambda: expect(item_carousel).to_be_visible(),
                            "check_item_carousel")
            write_log('web','쇼핑홈 칩카루셀_아이템카루셀 확인')

        elif case == 'chip': # 아이템 카루셀 상단 칩 확인
            timeout_handler(lambda: expect(item_carousel_chip.filter(has_text='추천')).to_be_visible(),
                            "check_item_carousel_chip(recommend)")
            timeout_handler(lambda: expect(item_carousel_chip.filter(has_text='최근본상품')).to_be_visible(),
                            "check_item_carousel_chip(recent)")
            write_log('web','쇼핑홈 칩카루셀_아이템카루셀 칩(추천, 최근본상품) 확인')
        
        # elif case == 'product': # 아이템 카루셀 상품 확인
        #     timeout_handler(lambda: page.locator('.css-b2kr9d').filter(has_text='최근본상품').click(),
        #                     "click_item_carousel_chip(recent)")
        #     page.wait_for_load_state("networkidle")
        #     timeout_handler(lambda: expect(item_carousel.locator("article:has(a)").first).to_be_visible(),
        #                     "check_item_carousel_product")
        
        elif case == 'product': # 아이템 카루셀 상품 확인
            timeout_handler(lambda: item_carousel.locator("article:has(a)").first.click(),
                            "click_item_carousel_chip")
            # page.wait_for_load_state("networkidle")
            page.wait_for_timeout(3000)
            timeout_handler(lambda: expect(page.get_by_role("button", name="공유하기"), '"상품상세" 메뉴 미노출').to_be_visible(),
                            "check_pdp")

        elif case == 'enter_product': # 아이템 카루셀 상품 진입
            timeout_handler(lambda: item_carousel.locator("article:has(a)").first.click(),
                            "click_item_carousel_product")
            write_log('web',f'클릭한 상품 url : {page.url}')
            timeout_handler(lambda: expect(page.get_by_text("주문금액").first, '"상품상세" 메뉴 미노출').to_be_visible(),
                            "check_pdp")

    def confirm_item_carousel_scrap(page, case='carousel'):
        item_carousel = page.locator('[data-component="HomeModuleChipCarouselItemCarousel"]')
        item_carousel_chip = item_carousel.locator('.sticky-container')
        timeout_handler(lambda: page.goto('https://store.qa-web.dailyhou.se/', timeout= 0), "goto_shop_home")
        page.wait_for_timeout(3000)
        if case == 'product': # 아이템 카루셀 확인 
            page.locator('[data-component="SubModuleItemList"]').locator("[aria-label='scrap 토글 버튼']").first.click() # 카루셀 아이템 리스트 첫번째 상품의 스크랩 버튼 클릭
            expect(page.get_by_text("스크랩했습니다."), '스크랩 완료 문구 미노출').to_be_visible()
            page.wait_for_timeout(3000)
            page.locator('[data-component="SubModuleItemList"]').locator("[aria-label='scrap 토글 버튼']").first.click() # 스크랩 해제
            expect(page.get_by_text("스크랩북에서 삭제했습니다."), '스크랩 삭제 미노출').to_be_visible()
            page.wait_for_timeout(3000)


        elif case == 'enter_product': # 아이템 카루셀 상품 진입
            timeout_handler(lambda: item_carousel.locator("article:has(a)").first.click(),
                            "click_item_carousel_product")
            write_log('web',f'클릭한 상품 url : {page.url}')
            timeout_handler(lambda: expect(page.get_by_text("주문금액").first, '"상품상세" 메뉴 미노출').to_be_visible(),
                            "check_pdp")

    # 쇼핑홈 제작형 카드 확인
    def confirm_item_list_card(page, case='ui_check'):
        # 쇼핑홈 진입
        timeout_handler(lambda: page.goto('https://store.qa-web.dailyhou.se/', timeout= 0), "goto_shop_home")
        item_list = page.locator('[data-element="Container"][data-component="SubModuleItemList"]')
        item_list_card = item_list.locator('[data-component="CustomizableCard"]').first
        item_list_card_thumbnail = item_list_card.locator('[data-component="CustomizableCardThumbnail"]').first
        item_list_card_info = item_list_card.locator('[data-component="CustomizableCardInfo"]').first

        if case == 'ui_check':
            timeout_handler(lambda: expect(item_list_card).to_be_visible(), 
                            "item_list_card") # 제작형 카드 확인
            timeout_handler(lambda: expect(item_list_card_thumbnail).to_be_visible(), 
                            "item_list_card_thumbnail") # 제작형 카드 - 썸네일 확인
            timeout_handler(lambda: expect(item_list_card_thumbnail.locator('[aria-label="scrap 토글 버튼"]')).to_be_visible(), 
                            "item_list_scrap_btn") # 제작형 카드 - 스크랩 버튼 확인
            
            timeout_handler(lambda: expect(item_list_card_info).to_be_visible(),
                            "item_list_card_info") # 제작형 카드 - 정보 영역 확인
            timeout_handler(lambda: expect(item_list_card_info.locator('figure.e1aub4hd0')).to_be_visible(),
                            "item_list_card_sub_image") # 제작형 카드 - 서브 이미지 확인
            # timeout_handler(lambda: expect(item_list_card_info.locator('h3.css-k8wgmw')).to_be_visible(),
            #                 "item_list_card_sub_title") # 제작형 카드 - 서브타이틀 확인
            # write_log('web', item_list_card_info.locator('h3.css-k8wgmw').inner_text()) # 서브타이틀 로깅
            timeout_handler(lambda: expect(item_list_card_info.locator('[data-element="MainTitle"]')).to_be_visible(),
                            "item_list_card_main_title") # 제작형 카드 - 메인타이틀 확인
            write_log('web', item_list_card_info.locator('[data-element="MainTitle"]').inner_text()) # 메인타이틀 로깅
            timeout_handler(lambda: expect(item_list_card_info.locator('[data-element="Description"]')).to_be_visible(),
                            "item_list_card_description") # 제작형 카드 - 디스크립션 확인
            write_log('web', item_list_card_info.locator('[data-element="Description"]').inner_text()) # 디스크립션 로깅
            timeout_handler(lambda: expect(item_list_card_info.locator('[data-element="ChevronRightIconWrapper"]')).to_be_visible(),
                            "item_list_card_right_icon") # 제작형 카드 - 화살표 버튼
        
        elif case == 'enter_card':
            timeout_handler(lambda: item_list_card.click(), "item_list_card") # 제작형 카드 클릭
            expect(page.get_by_role("button", name="판매상품 목록보기"), '"판매상품 목록보기" 요소 미노출').to_be_visible() # 기획전 상세 확인
        
    def confirm_item_list_card_scrap(page, case='ui_check'):
        # 쇼핑홈 진입
        timeout_handler(lambda: page.goto('https://store.qa-web.dailyhou.se/', timeout= 0), "goto_shop_home")
        item_list = page.locator('[data-element="Container"][data-component="SubModuleItemList"]')
        item_list_card = item_list.locator('[data-component="CustomizableCard"]').first
        item_list_card_thumbnail = item_list_card.locator('[data-component="CustomizableCardThumbnail"]').first
        item_list_card_info = item_list_card.locator('[data-component="CustomizableCardInfo"]').first

        if case == 'ui_check':
            timeout_handler(lambda: expect(item_list_card_thumbnail.locator('[aria-label="scrap 토글 버튼"]')).to_be_visible(), 
                            "item_list_scrap_btn") # 제작형 카드 - 스크랩 버튼 확인
            page.locator('[data-component="SubModuleItemList"]').locator("[aria-label='scrap 토글 버튼']").first.click() # 카루셀 아이템 리스트 첫번째 상품의 스크랩 버튼 클릭
            expect(page.get_by_text("스크랩했습니다."), '스크랩 완료 문구 미노출').to_be_visible()
            page.wait_for_timeout(3000)
            page.locator('[data-component="SubModuleItemList"]').locator("[aria-label='scrap 토글 버튼']").first.click() # 스크랩 해제
            expect(page.get_by_text("스크랩북에서 삭제했습니다."), '스크랩 삭제 미노출').to_be_visible()
            page.wait_for_timeout(3000)

        elif case == 'enter_card':
            timeout_handler(lambda: item_list_card.click(), "item_list_card") # 제작형 카드 클릭
            expect(page.get_by_role("button", name="판매상품 목록보기"), '"판매상품 목록보기" 요소 미노출').to_be_visible() # 기획전 상세 확인
        
    def confirm_review_write(page):
        page.get_by_role("button", name="글쓰기 ").click()
        page.get_by_role("link", name="상품 리뷰 쓰기 상품 리뷰를 작성하고 포인트도 받아 보세요").click()
        page.wait_for_timeout(1000)
        # 리뷰 남기기
        page.locator(".review-my-home__review-list__item__review-btn__button").first.click()
        page.wait_for_timeout(1000)
        # 5점
        # page.locator("li:nth-child(5) > .rating-input__star > .star > path").first.click() 
        page.locator("label:nth-child(5) > .star > .star-fill").click()
        # page.locator("div:nth-child(2) > .review-modal__form__star__value > .rating-input > li:nth-child(5) > .rating-input__star > .star > path").click()
        # page.locator("div:nth-child(3) > .review-modal__form__star__value > .rating-input > li:nth-child(5) > .rating-input__star > .star > path").click()
        # page.locator("div:nth-child(4) > .review-modal__form__star__value > .rating-input > li:nth-child(5) > .rating-input__star > .star > path").click()
        # page.locator(".check").first.click()
        # page.get_by_role("textbox", name="자세하고 솔직한 리뷰는 다른 고객에게 큰 도움이 됩니다. (최소 20자 이상)").click()
        # page.get_by_role("textbox", name="자세하고 솔직한 리뷰는 다른 고객에게 큰 도움이 됩니다. (최소 20자 이상)").fill("test1test2test3test4test5test6test7test8")
        page.get_by_placeholder("다른 분들이 도움을 받을 수 있도록 상품 후기를 솔직하게 공유해주세요 (최소 20자 이상)").click()
        page.get_by_placeholder("다른 분들이 도움을 받을 수 있도록 상품 후기를 솔직하게 공유해주세요 (최소 20자 이상)").fill("test1test2test3test4test5test6test7test8")
        page.get_by_role("button", name="저장하기").click()
        # page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)
        # expect(page.get_by_role("link", name="나의 리뷰 보기"), '"나의리뷰보기" 요소 미노출').to_be_visible()
        expect(page.get_by_role("button", name="확인"), '"확인 팝업" 요소 미노출').to_be_visible()
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)
        # page.wait_for_timeout(3000)
        # page.get_by_text("| 오늘의집 구매").first.click()

    def confirm_brand_home(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        item_carousel = page.locator('[data-component="HomeModuleChipCarouselItemCarousel"]')
        timeout_handler(lambda: item_carousel.locator("article:has(a)").first.click(),
                            "click_item_carousel_product")
        page.wait_for_timeout(2000)
        # 브랜드 홈 진입
        page.locator('xpath=/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div[1]/div[3]/a/div[2]').click()
        expect(page.get_by_text("명이 이 브랜드 상품을 스크랩했어요"), '브랜드홈 페이지 미노출').to_be_visible()
        expect(page.get_by_label("공유하기"), '공유하기 버튼 미노출').to_be_visible()
        # page.wait_for_timeout(2000)

    def confirm_brand_home_detail(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        item_carousel = page.locator('[data-component="HomeModuleChipCarouselItemCarousel"]')
        timeout_handler(lambda: item_carousel.locator("article:has(a)").first.click(),
                            "click_item_carousel_product")
        page.wait_for_timeout(2000)
        # 브랜드 홈 진입
        page.locator('xpath=/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div[1]/div[3]/a/div[2]').click()
        page.wait_for_timeout(2000)
        # expect(page.get_by_role("heading", name="스타일링홈"), '타이틀 미노출').to_be_visible()
        # expect(page.get_by_role("button", name="스타일링샷"), '스타일링샷 페이지 미노출').to_be_visible()
        # expect(page.get_by_role("link", name="패브릭"), '카테고리 미노출').to_be_visible()
        expect(page.get_by_text("명이 이 브랜드 상품을 스크랩했어요"), '브랜드홈 페이지 미노출').to_be_visible()
        # page.wait_for_timeout(2000)

    def confirm_brand_home_scrap(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        item_carousel = page.locator('[data-component="HomeModuleChipCarouselItemCarousel"]')
        timeout_handler(lambda: item_carousel.locator("article:has(a)").first.click(),
                            "click_item_carousel_product")
        page.wait_for_timeout(2000)
        page.locator("button[name=\"스크랩\"]").click()
        expect(page.get_by_text("스크랩했습니다."), '스크랩 완료 문구 미노출').to_be_visible()
        page.wait_for_timeout(3000)
        page.locator("button[name=\"스크랩\"]").click()
        expect(page.get_by_text("스크랩북에서 삭제했습니다."), '스크랩 삭제 미노출').to_be_visible()
        # page.locator("div").filter(has_text=re.compile(r"^스타일링홈.*")).get_by_role("button").nth(3).click()
        
    def confirm_brand_home_detail_scrap(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        item_carousel = page.locator('[data-component="HomeModuleChipCarouselItemCarousel"]')
        timeout_handler(lambda: item_carousel.locator("article:has(a)").first.click(),
                            "click_item_carousel_product")
        page.wait_for_timeout(2000)
        # 브랜드 홈 진입
        page.locator('xpath=/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div[1]/div[3]/a/div[2]').click()
        page.wait_for_timeout(2000)
        # page.locator("div").filter(has_text=re.compile(r"^스타일링홈.*")).get_by_role("button").nth(3).click()
        page.locator('xpath=//*[@id="__next"]/div[1]/div/div[2]/section[1]/section/section/div/div[1]/div[2]/div[2]/button').click()
        # expect(page.get_by_text("스크랩했습니다."), '스크랩 완료 문구 미노출').to_be_visible()
        page.wait_for_timeout(2000)
        # page.locator("div").filter(has_text=re.compile(r"^스타일링홈.*")).get_by_role("button").nth(3).click()
        page.locator('xpath=//*[@id="__next"]/div[1]/div/div[2]/section[1]/section/section/div/div[1]/div[2]/div[2]/button').click()
        # expect(page.get_by_text("스크랩북에서 삭제했습니다."), '스크랩 삭제 미노출').to_be_visible()
        # page.wait_for_timeout(2000)

    def confirm_review_graph(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        item_carousel = page.locator('[data-component="HomeModuleChipCarouselItemCarousel"]')
        timeout_handler(lambda: item_carousel.locator("article:has(a)").first.click(),
                            "click_item_carousel_product")
        page.wait_for_timeout(2000)
        page.get_by_role("link", name=re.compile(r"리뷰.*")).click()
        page.get_by_role("button", name="리뷰쓰기").click()
        expect(page.get_by_text("리뷰 쓰기"), '스크랩 완료 문구 미노출').to_be_visible()
        page.wait_for_timeout(2000)
    
    def confirm_userpage_folder(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.get_by_role("link", name="스크랩북 페이지 링크 버튼").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name=re.compile(r"폴더.*")).click()
        expect(page.get_by_role("button", name="폴더 추가 "), '폴더 페이지 미노출').to_be_visible()
        page.wait_for_timeout(2000)

    def confirm_userpage_brand(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.get_by_role("link", name="스크랩북 페이지 링크 버튼").click()
        page.get_by_role("button", name=re.compile(r"브랜드(.*")).click()
        expect(page.get_by_role("link", name="스타일링홈"), '브랜드 페이지 미노출').to_be_visible()
        page.wait_for_timeout(2000)

    def confirm_category_detail(page):
        # 카테고리 상세 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        # page.get_by_text("카테고리").scroll_into_view_if_needed()
        page.get_by_role("heading", name="카테고리").scroll_into_view_if_needed() # SDUI ver.
        page.get_by_role("link", name="가구", exact=True).click()
        expect(page.get_by_role("link", name="소파/거실가구"), '가구 상세페이지 미노출').to_be_visible()
        page.get_by_label("오늘의집 로고").click()
        page.get_by_text("카테고리별 상품 찾기").scroll_into_view_if_needed()
        page.get_by_role("link", name="패브릭").click()
        expect(page.get_by_role("heading", name="패브릭"), '패브릭 상세페이지 미노출').to_be_visible()

    def confirm_mdpick(page):
        # MD Pick 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.get_by_role("heading", name="카테고리", exact=True).scroll_into_view_if_needed()
        page.get_by_role("link", name="가구", exact=True).click()
        page.wait_for_timeout(1000)
        # md's pick 캐로셀 영역의 첫번째 상품 선택 진입
        mdpick = page.locator('xpath=/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/ul/a[1]')
        elements_visible = mdpick.is_visible()
        if elements_visible:
            mdpick.click()
            page.wait_for_timeout(2000)
        else:
            page.locator('xpath=/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/ul/article[1]').click()
            page.wait_for_timeout(1000)
        # 배송정보 노출영역에 '배송' 텍스트 노출확인
        expect(page.locator("span").filter(has_text=re.compile(r"^배송$")), '"배송" 텍스트 미노출').to_be_visible()

    def confirm_floating_btn(page):
        # Top 플로팅버튼 확인
         # 가구 카테고리 > 하단으로 스크롤 과정에서 특정구좌의 노출여부로 탑 버튼 동작 유무 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.get_by_role("link", name="가구", exact=True).click()
        page.wait_for_timeout(1000)
        expect(page.locator("div").filter(has_text=re.compile(r"^#MD's PICK$")), '"MD Pick"요소 미노출').to_be_visible()
        for _ in range(20):
                        page.evaluate("window.scrollBy(0, window.innerHeight)")
                        page.wait_for_timeout(500)
        page.get_by_role("button", name="").nth(1).click()
        expect(page.locator("div").filter(has_text=re.compile(r"^#MD's PICK$")), '"MD Pick"요소 미노출').to_be_visible()

    def confirm_mdpick_detail(page):
        # MD's pick 상세 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.get_by_role("link", name="가구", exact=True).click()
        page.wait_for_timeout(1000)
        expect(page.get_by_text("#MD's PICK"), '"MD Pick"요소 미노출').to_be_visible()
        # md's pick 캐로셀 영역의 첫번째 상품 선택 진입
        mdpick = page.locator('xpath=/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/ul/a[1]')
        elements_visible = mdpick.is_visible()
        if elements_visible:
            mdpick.click()
            page.wait_for_timeout(2000)
        else:
            page.locator('xpath=/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/ul/article[1]').click()
            page.wait_for_timeout(1000)
        page.wait_for_timeout(1000)
        # 10. 배송정보 노출영역에 '배송' 텍스트 노출확인
        expect(page.locator("div").filter(has_text=re.compile(r"^배송$")).locator("span"), '"배송" 텍스트 미노출').to_be_visible()
        
    def confirm_today_deal_more(page):
        # 오늘의딜 더보기 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        # 오늘의 딜 더보기
        for _ in range(3):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(3000)
        # page.get_by_role("heading", name="오늘의딜", exact=True).scroll_into_view_if_needed()
        page.get_by_role("heading", name="오늘의딜").scroll_into_view_if_needed()
        page.get_by_role("link", name="더보기").click()
        page.wait_for_timeout(3000)
        # 리스트의 첫번재 상품 노출확인
        # expect(page.get_by_role('article').nth(0), '상품 미노출').to_be_visible()
        # today_deal = page.locator('xpath=/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/a/div/div[1]/div')
        # expect(today_deal).to_be_visible()
        # elements_visible = today_deal.is_visible()
        # if elements_visible:
        #     expect(today_deal).to_be_visible()
        #     page.wait_for_timeout(2000)
        # else:
        #     expect(page.locator('xpath=/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/article')).to_be_visible()
        #     page.wait_for_timeout(1000)
        #     # /html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/article/a
        expect(page.get_by_role("button", name="판매상품 목록보기"), '상품보기 버튼 미노출').to_be_visible()

    def confirm_today_deal_detail(page):
        # 오늘의딜 더보기 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.wait_for_timeout(2000)
        # 오늘의 딜 더보기
        for _ in range(3):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("heading", name="오늘의딜").scroll_into_view_if_needed()
        page.get_by_role("link", name="더보기").click()
        page.wait_for_timeout(1000)
        # 리스트의 첫번재 상품 노출확인
        page.get_by_role('article').nth(0).click()
        page.wait_for_timeout(1000)
        # 배송정보 노출영역에 '배송' 텍스트 노출확인
        expect(page.locator("div").filter(has_text=re.compile(r"^배송$")).locator("span"), '배송 텍스트 미노출').to_be_visible()
       
    def confirm_scrap(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.wait_for_load_state("networkidle")
        page.locator('[data-component="SubModuleItemList"]').locator("[aria-label='scrap 토글 버튼']").first.click() # 카루셀 아이템 리스트 첫번째 상품의 스크랩 버튼 클릭
        expect(page.get_by_text("스크랩했습니다."), '스크랩 완료 문구 미노출').to_be_visible()
        page.wait_for_timeout(1000)
        page.locator('[data-component="SubModuleItemList"]').locator("[aria-label='scrap 토글 버튼']").first.click() # 스크랩 해제
        expect(page.get_by_text("스크랩북에서 삭제했습니다."), '스크랩 삭제 미노출').to_be_visible()

    def confirm_coupon_price(page):
        # 쿠폰 적용가 확인
        CommPlatformElements.checkout_2_func(page)
        expect(page.get_by_text(re.compile(r"상품 쿠폰-.*")), '"상품 쿠폰 적용 금액" 요소 미노출').to_be_visible()
    
    def confirm_accept_coupon(page):
        # PDP 들어온 상태로 진행
        page.wait_for_load_state("networkidle")
        # 받은 쿠폰 확인
        elements_visible = page.get_by_role("button", name="쿠폰 받기 ").is_visible()
        if elements_visible:
            page.get_by_role("button", name="쿠폰 받기 ").click()
        else:
            page.get_by_role("button", name="받은 쿠폰 보기 ").click()
        
        try:
            # 받은 쿠폰 모달에 상품 쿠폰과 장바구니 쿠폰 모두 노출 확인
            expect(page.get_by_role("heading", name="상품쿠폰", exact=True), '"상품쿠폰" 영역 미노출').to_be_visible()
            expect(page.get_by_role("heading", name="장바구니쿠폰"), '"장바구니쿠폰" 영역 미노출').to_be_visible()
            page.get_by_role("button", name="").click() # 모달 닫기
        except Exception:
            PageElements.qaweb_product_url_3(page, '100007866')
            write_log('web', "100007866 상품으로 재확인")
            raise TimeoutError("'상품쿠폰' 영역 미노출")

        expect(page.get_by_text("쿠폰적용됨"), '쿠폰적용됨 문구 미노출').to_be_visible()
    
    def confirm_cart_coupon(page):
        # 장바구니 쿠폰 문구 확인
        expect(page.get_by_role("heading", name=re.compile(r"쿠폰가에서 .*")), '쿠폰 적용 문구 미노출').to_be_visible()

    def confirm_scrap_onoff(page):
        # 스크랩 동작 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.wait_for_timeout(3000)
        # 스크롤
        for _ in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.locator("article").nth(7).get_by_label("scrap 토글 버튼").click()
        expect(page.get_by_text("스크랩했습니다."), '스크랩 on 미동작').to_be_visible()
        page.wait_for_timeout(2000)
        # 스크랩 초기화
        page.locator("article").nth(7).get_by_label("scrap 토글 버튼").click()
        expect(page.get_by_text("스크랩북에서 삭제했습니다."), '스크랩 off 미동작').to_be_visible()

    def confirm_styling_shot(page):
        # 스타일링샷 확인
        # page.get_by_role("link", name="쇼핑", exact=True).click()
        # # 인기상품 첫번째 노출되는 상품 (idx=0) 진입
        # page.get_by_role('article').nth(4).click()
        # 유저들의 스타일링샷 노출 확인
        # page.get_by_role("heading", name="유저들의 스타일링샷 8,746", exact=True).scroll_into_view_if_needed()
        page.get_by_text(re.compile("유저들의 스타일링샷.*")).scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        # expect(page.get_by_role("heading", name="유저들의 스타일링샷 8,746"), '유저들의 스타일링샷 미노출').to_be_visible()
        expect(page.get_by_text(re.compile("유저들의 스타일링샷.*")), '유저들의 스타일링샷 미노출').to_be_visible()

    def confirm_review_detail(page):
        # 스타일링샷 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        # 첫번째 노출되는 상품 (idx=0) 진입
        page.get_by_role('article').nth(1).click()
        # page.get_by_role("link", name="리뷰14,461").click()
        page.get_by_role("link", name=re.compile("리뷰.*")).click
        # 리뷰영역에 '도움돼요' 버튼 노출확인
        # expect(page.get_by_role("button", name="도움이 돼요").first, '"도움이 돼요" 버튼 미노출').to_be_visible()
        expect(page.locator("div").filter(has_text=re.compile(r"^도움돼요.*")).nth(0), '"도움돼요" 버튼 미노출').to_be_visible()
        # page.get_by_role("button", name="사진리뷰").click()

    def confirm_collection_product(page):
        # 모음전 진입
        PageElements.qaweb_product_url_3(page, '401328')
        page.wait_for_load_state("networkidle")
        expect(page.locator("div").filter(has_text=re.compile(r"^배송$")).locator("span"), '"배송" 텍스트 미노출').to_be_visible()
        expect(page.locator('.production-select-button__production__blank').filter(has_text='상품을 선택하세요.').first, "상품 선택 UI").to_be_visible()
        
    def confirm_collection_detail(page):
        # 모음전 진입
        PageElements.qaweb_product_url_3(page, '401328')
        page.locator('.deal-production-item__wrapper').first.click() # 모음전 첫번째 상품 자세히보기
        expect(page.locator('.deal-production-modal__content')).to_be_visible() # 모달 확인

    def confirm_realtime_best(page):
        # 실시간 베스트 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        for _ in range(3):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="Test BEST").scroll_into_view_if_needed()
        page.get_by_role("link", name="Test BEST").click()
        # 리스트의 첫번째 상품 노출확인 (idx=0)
        expect(page.get_by_role('article').nth(0), '상품 미노출').to_be_visible()

    def confirm_quick_todaydeal(page):
        # 퀵메뉴 오늘의딜 상세 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        # 퀵메뉴 영역에 '오딜(신)' 메뉴 선택
        for _ in range(3):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="Test BEST").scroll_into_view_if_needed()
        page.get_by_role("link", name="Clik 오늘의딜").click()
        page.wait_for_timeout(3000)
        # 리스트의 첫번째 상품 노출확인 (idx=0)
        # today_deal = page.locator('xpath=/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/a/div/div[1]/div')
        # expect(today_deal).to_be_visible()
        # elements_visible = today_deal.is_visible()
        # if elements_visible:
        #     expect(today_deal).to_be_visible()
        #     page.wait_for_timeout(2000)
        # else:
        #     expect(page.locator('xpath=/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/article')).to_be_visible()
        #     page.wait_for_timeout(1000)
        # expect(page.get_by_role('article').nth(0), '상품 미노출').to_be_visible()
        expect(page.get_by_role("button", name="판매상품 목록보기"), '상품보기 버튼 미노출').to_be_visible()

    def confirm_quick_exhibition(page):
        # 퀵메뉴 기획전 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        for _ in range(3):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="Test BEST").scroll_into_view_if_needed()
        page.get_by_role("link", name="기획전상세").click()
        page.wait_for_timeout(1000)
        # API Response check
        api_url = 'https://image.ohou.se/i/bucketplace-v2-development/uploads/exhibitions/cover_image/170718677717131123.jpg?gif=1&w=1024&h=594&c=c'
        response = send_api_get(api_url)
        assert response.status_code == 200

    def confirm_premium_category(page):
        # 프리미엄 카테고리 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        # 퀵메뉴 구좌의 6번째 메뉴에 "프리미엄" 선택
        for _ in range(3):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="Test BEST").scroll_into_view_if_needed()
        page.get_by_role("link", name="new 프리미엄").click()
        # API Response check
        api_url = 'https://store.qa-web.dailyhou.se/exhibitions/10294'
        response = send_api_get(api_url)
        assert response.status_code == 200

    def confirm_exhibition_feed(page):
        # 기획전 피드 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        # 퀵메뉴 구좌의 8번째 메뉴에 "기획전 피드" 선택
        for _ in range(3):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="Test BEST").scroll_into_view_if_needed()
        page.get_by_role("link", name="HOT 기획전피드").click()
        # API Response check
        api_url = 'https://store.qa-web.dailyhou.se/exhibitions'
        response = send_api_get(api_url)
        assert response.status_code == 200

    def confirm_exhibition_detail(page):
        # 기획전 피드 상세 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        # 퀵메뉴 구좌의 9번째 메뉴에 "기획전 상세" 선택
        for _ in range(3):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="Test BEST").scroll_into_view_if_needed()
        page.get_by_role("link", name="기획전상세").click()
        # API Response check
        api_url = 'https://store.qa-web.dailyhou.se/exhibitions/10196'
        response = send_api_get(api_url)
        assert response.status_code == 200

    def chip_carousel_detail(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.wait_for_timeout(3000)
        # 칩카루셀 영역 임의의 상품 클릭
        # page.locator("article").nth(1).click()
        page.locator(re.compile(r".css.*")).first.click()
        page.wait_for_timeout(2000)
        expect(page.get_by_role("button", name="스크랩"), '"스크랩" 버튼 미노출').to_be_visible()

    def top_floating(page):
        # 가구 카테고리 > 하단으로 스크롤 과정에서 특정구좌의 노출여부로 탑 버튼 동작 유무 확인
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.get_by_role("link", name="가구", exact=True).click()
        page.wait_for_timeout(1000)
        expect(page.locator("div").filter(has_text=re.compile(r"^#MD's PICK$")), '"MD Pick"요소 미노출').to_be_visible()
        for _ in range(20):
                        page.evaluate("window.scrollBy(0, window.innerHeight)")
                        page.wait_for_timeout(500)
        page.get_by_role("button", name="").nth(1).click()
        expect(page.locator("div").filter(has_text=re.compile(r"^#MD's PICK$")), '"MD Pick"요소 미노출').to_be_visible()

    def confirm_infinite_scrolling(page):
         # 스크롤 20회 반복
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.wait_for_timeout(1000)
        for _ in range(20):
                page.evaluate("window.scrollBy(0, window.innerHeight)")
                page.wait_for_timeout(500)

    def infinite_scroll(page):
        # 무한 스크롤 func
        # while True:
        for _ in range(5):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)

    def confirm_product_detail(page):
        # 베스트 > 실시간 베스트 화면 진입
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.get_by_role("link", name="베스트").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="실시간 베스트").click()
        api_url = 'https://store.qa-web.dailyhou.se/ranks?type=recent'
        response = send_api_get(api_url)
        assert response.status_code == 200
        # expect(page.get_by_text("2022.05.11 15:03 기준"), '실시간 베스트 화면 진입 실패').to_be_visible()
        # page.locator(".css-y20lcz").first.click()
        # expect(page.get_by_role("region").first, '상품 상세  진입 실패').to_be_visible()
     
    def confirm_carousel_detail(page):
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.wait_for_timeout(1000)
        for _ in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.locator(".css-1nja1i").click()
        # page.locator(re.compile(r".css.*")).first.click()
        page.wait_for_timeout(1000)
        expect(page.get_by_role("button", name="판매상품 목록보기"), '카루셀 상세 진입 실패').to_be_visible()

    def confirm_best_ranks(page):
        # 베스트 > 역대 베스트 화면 진입
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.get_by_role("link", name="베스트").click()
        page.wait_for_timeout(500)
        page.get_by_role("button", name="역대 베스트").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="테마관"), '역대 베스트 화면 진입 실패').to_be_visible()
        
        # 카테고리 탭별 이동 동작 확인
        page.get_by_role("button", name="테마관").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="테마관 "), '역대 베스트 테마관 진입 실패').to_be_visible()
        page.get_by_role("button", name="가구").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="가구 "), '역대 베스트 가구 진입 실패').to_be_visible()
        page.get_by_role("button", name="패브릭").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="패브릭 "), '역대 베스트 패브릭 진입 실패').to_be_visible()
        page.get_by_role("button", name="조명").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="조명 "), '역대 베스트 조명 진입 실패').to_be_visible()
        page.get_by_role("button", name="가전").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="가전 "), '역대 베스트 가전 진입 실패').to_be_visible()
        page.get_by_role("button", name="주방용품").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="주방용품 "), '역대 베스트 주방용품 진입 실패').to_be_visible()
        page.get_by_role("button", name="장식/소품").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="장식/소품 "), '역대 베스트 장식/소품 진입 실패').to_be_visible()
        page.get_by_role("button", name="수납/정리").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="수납/정리 "), '역대 베스트 수납/정리 진입 실패').to_be_visible()
        page.get_by_role("button", name="생활용품").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="생활용품 "), '역대 베스트 생활용품 진입 실패').to_be_visible()
        page.get_by_role("button", name="생필품").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="생필품 "), '역대 베스트 생필품 진입 실패').to_be_visible()
        page.get_by_role("button", name="공구/DIY").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="공구/DIY "), '역대 베스트 공구/DIY 진입 실패').to_be_visible()
        page.get_by_role("button", name="리모델링·홈케어").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="리모델링·홈케어 "), '역대 베스트 리모델링·홈케어 진입 실패').to_be_visible()
        page.get_by_role("button", name="반려동물").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="반려동물 "), '역대 베스트 반려동물 진입 실패').to_be_visible()
        page.get_by_role("button", name="캠핑용품").click()
        page.wait_for_timeout(500)
        expect(page.get_by_text("검색 결과가 없습니다."), '역대 베스트 캠핑용품 진입 실패').to_be_visible()
        page.get_by_role("button", name="실내운동").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("button", name="실내운동 "), '역대 베스트 실내운동 진입 실패').to_be_visible()

    def confirm_bestranks_detail(page):
            # 베스트 > 역대 베스트 화면 진입
            page.get_by_role("link", name="쇼핑", exact=True).click()
            page.get_by_role("link", name="베스트").click()
            page.wait_for_timeout(500)
            page.get_by_role("button", name="역대 베스트").click()
            page.wait_for_timeout(500)
            expect(page.get_by_role("button", name="테마관"), '역대 베스트 화면 진입 실패').to_be_visible()
            # 리스트의 첫번재 상품 상세 진입 및 진입 동작 확인
            page.locator("article").filter(has_text="1퀵슬립Q4 유로탑 롤팩 매트리스 2sizeddd66% 234,9004.8리뷰 6,536최대 10% 쿠폰").get_by_role("link").click()
            page.wait_for_timeout(500)
            expect(page.locator(".production-selling-cover-image-container"), '상품 상세  진입 실패').to_be_visible()

    def confirm_exhibitions_detail(page):
            page.get_by_role("link", name="쇼핑", exact=True).click()
            for _ in range(3):
                page.evaluate("window.scrollBy(0, window.innerHeight)")
                page.wait_for_timeout(1000)
            page.get_by_role("link", name="Test BEST").scroll_into_view_if_needed()
            page.get_by_role("link", name="기획전상세").click()
            page.wait_for_timeout(1000)
            expect(page.get_by_role("button", name="판매상품 목록보기"), '기획전 상세 진입 실패').to_be_visible()

    def confirm_hotexhibitions_feed(page):
            page.get_by_role("link", name="쇼핑", exact=True).click()
            # 퀵메뉴 구좌의 8번째 메뉴에 "기획전 피드" 선택
            page.get_by_role("link", name="HOT 기획전피드").click()
            # 기획전 피드에서 grace 기획전 노출될대까지 스크롤 후 tttt2 기획전이 피드에서 노출되는지 확인
            page.get_by_role("link", name="grace", exact=True).scroll_into_view_if_needed()
            expect(page.get_by_role("link", name="tttt2"), '기획전 피드 진입 실패').not_to_be_visible








class CommServiceIntopdp:
    def __init__(self, page: Page) -> None:
        self.integrated_shopping_home = page.get_by_role("link", name="쇼핑", exact=True)
        self.integrated_popularproduct = page.get_by_role("heading", name="인기 상품", exact=True)
        self.integrated_popularproduct_filter_popular = page.locator("#store-index").get_by_role("button", name="인기순")
        self.integrated_popularproduct_filter_review = page.get_by_role("button", name="많은 리뷰순")
        self.integrated_popularproduct_firstproduct = page.locator("article").filter(has_text="바이빔 선데이 러그 7size 4colors4% 333,3314.7 리뷰 33,667평일 23:30까지 결제시최대 5천원 쿠폰최대 10% 결제할").get_by_role("link")    

    def auto_pdp_into(self, page: Page):
        print("상품 디테일 진입 확인", end='')
        timeout_handler(lambda: self.integrated_shopping_home.click(),"쇼핑")
        timeout_handler(lambda: self.integrated_popularproduct.scroll_into_view_if_needed(),"인기 상품")
        timeout_handler(lambda: self.integrated_popularproduct_filter_popular.click(),"인기순")
        timeout_handler(lambda: self.integrated_popularproduct_filter_review.click(),"많은 리뷰순")
        timeout_handler(lambda: self.integrated_popularproduct_firstproduct.click(),"PDP 진입")
        page.wait_for_timeout(1000)
        print(" - Pass")


class CommServiceCategory:
    def __init__(self, page: Page) -> None:
        '''
        self.integrated_shopping_home = page.get_by_role("link", name="쇼핑", exact=True)
        self.integrated_popularproduct = page.get_by_role("heading", name="인기 상품", exact=True)
        self.integrated_popularproduct_filter_popular = page.locator("#store-index").get_by_role("button", name="인기순")
        self.integrated_popularproduct_filter_review = page.get_by_role("button", name="많은 리뷰순")
        self.integrated_popularproduct_firstproduct = page.locator("article").filter(has_text="바이빔 선데이 러그 7size 4colors4% 333,3314.7 리뷰 33,667평일 23:30까지 결제시최대 5천원 쿠폰최대 10% 결제할").get_by_role("link")    
        '''
    def auto_category_furniture_filter(self, page: Page):
        # 카테고리 진입 > 필터 구좌 노출 확인
        print("가구 카테고리 필터 선택 및 칩 노출 확인", end='')
        page.get_by_role("link", name="쇼핑", exact=True).click()
        page.get_by_role("link", name="카테고리").click()
        page.get_by_role("button", name="빠른가구배송").scroll_into_view_if_needed()
        page.get_by_role("button", name="빠른가구배송").click()
        page.get_by_role("button", name="사용 인원").click()
        page.get_by_role("button", name="1인").get_by_role("checkbox").check()
        page.get_by_role("button", name="소재").click()
        page.get_by_role("button", name="원목", exact=True).get_by_role("checkbox").check()
        page.get_by_role("button", name="색상").click()
        page.get_by_role("button", name="필터 비주얼 이미지 화이트").get_by_role("checkbox").check()
        page.get_by_role("button", name="브랜드").click()
        page.get_by_role("button", name="한샘").get_by_role("checkbox").check()
        page.get_by_role("button", name="우드톤").click()
        page.get_by_role("button", name="필터 비주얼 이미지 밝은 톤").get_by_role("checkbox").check()
        page.get_by_role("button", name="상품 유형").click()
        page.get_by_role("button", name="해외직구 제외").get_by_role("checkbox").check()
        page.get_by_role("button", name="특가").click()
        page.get_by_role("button", name="특가상품 보기").click()
        page.get_by_role("button", name="인기 BEST").click()
        page.get_by_role("button", name="홈카페용 식탁").get_by_role("checkbox").check()
        page.get_by_role("button", name="원목 수종").click()
        page.get_by_role("button", name="오크(참나무)").get_by_role("checkbox").check()
        page.get_by_role("button", name="자재 등급").click()
        page.get_by_role("button", name="SE0").get_by_role("checkbox").check()
        page.get_by_role("button", name="가격").click()
        page.get_by_role("button", name="50,000원 이하").first.click()
        page.get_by_role("button", name="적용").click()

        expect(page.get_by_role("button", name="빠른가구배송").nth(1), '빠른가구 배송 칩 비노출').to_be_visible()
        expect(page.locator("li").filter(has_text="50,000원 이하").first, '가격 칩 비노출').to_be_visible()
        expect(page.get_by_role("button", name="SE0"), '자재 등급 칩 비노출').to_be_visible()
        expect(page.get_by_role("button", name="오크(참나무)"), '원목 수종 칩 비노출').to_be_visible()
        expect(page.get_by_role("button", name="홈카페용 식탁"), '인가Best 칩 비노출').to_be_visible()
        expect(page.get_by_role("button", name="특가상품 보기"), '특가 칩 비노출').to_be_visible()
        expect(page.get_by_role("button", name="해외직구 제외"), '상품 유형 칩 비노출').to_be_visible()
        expect(page.get_by_role("button", name="밝은 톤"), '우드 톤 칩 비노출').to_be_visible()
        expect(page.get_by_role("button", name="한샘"), '브랜드 칩 비노출').to_be_visible()
        expect(page.get_by_role("button", name="화이트"), '색상 칩 비노출').to_be_visible()
        expect(page.get_by_role("button", name="원목", exact=True), '소재 칩 비노출').to_be_visible()
        expect(page.get_by_role("button", name="1인"), '사용인원 칩 비노출').to_be_visible()
        print(" - Pass")
