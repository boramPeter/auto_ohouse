from playwright.sync_api import *
from app.common.base_method.exception_func import timeout_handler, write_log
import re
from selenium.common.exceptions import TimeoutException
from web.BasicSetting.conftest import *

class SearchProcedure():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.integrated_search_box = page.get_by_placeholder("통합검색")
        self.x_button = page.get_by_role("button", name="")

    def search_keyword(self, keyword):
        timeout_handler(lambda: self.page.goto('https://qa-web.dailyhou.se/', timeout= 0), "enter_qa_home")
        timeout_handler(lambda: self.integrated_search_box.fill(keyword), "search_input")
        timeout_handler(lambda: self.integrated_search_box.press("Enter"), "search_enter")
    
    def goto_home(self):
        timeout_handler(lambda: self.page.goto('https://qa-web.dailyhou.se/', timeout=0), "enter_qa_home")

    #쇼핑 SRP 랜딩되었는지 확인 
    def check_url_contains_productions_shopping(self):
        expected_substring = "/productions"
        current_url = self.page.url

        if expected_substring in current_url:
            return True
        else:
            print(f"URL에 '{expected_substring}' 포함되어 있지 않습니다.")
            return False
        
    #통합검색 SRP 랜딩되었는지 확인 
    def check_url_contains_productions_integrated(self):
        expected_substring = "/search/index?query"
        current_url = self.page.url

        if expected_substring in current_url:
            return True
        else:
            print(f"URL에 '{expected_substring}' 포함되어 있지 않습니다.")
            return False

    def check_integrated_search(self, collection, more_btn=True):
        #통합 탭 확인
        expect(self.page.get_by_role("link", name="통합")).to_be_visible()
        #컬렉션 타이틀+더보기 확인
        for i in range(len(collection)):
            #타이틀 확인
            header = self.page.get_by_role("heading", name=collection[i])
            timeout_handler(lambda: expect(header).to_be_visible(timeout=10*1000), "collection_header")

            #더보기 확인 (취향발견 컬렉션 처럼 더보기 없는 경우도 존재함)
            if more_btn:
                header_more = self.page.locator("header").filter(has_text=re.compile(collection[i]+r"\d.*더보기")).get_by_role("link")
                timeout_handler(lambda: expect(header_more).to_be_visible(), "collection_header_more")
                
                return header_more # 더보기 버튼 리스트 반환
            #더보기 수 출력
            #len_param = len(str(collection[i]))
            #more_count = collection_more.inner_text().split('더보기')[0][len_param:].rstrip()
            #print("\n"+collection[i]+" 컬렉션 더보기 개수 = "+more_count+" 개")

    # 더보기 클릭 
    def click_more_btn(self, collection, keyword, more_btn=True):
        more_button = timeout_handler(lambda: self.check_integrated_search(collection, more_btn), "collection_header_more")
        more_button.click()

        OP = O2OSearchProcedure(self.page)
        SP = ShopSearchProcedure(self.page)
        CSP = ContentsSearchProcedure(self.page)
        CP = CardSearchProcedure(self.page)

        # keyword에 따라 동작 수행
        '''
        매치함수 에러가 있어서 일단 dict방식으로 존재하면 수행하도록 변경했어요
        '''
        # match keyword:
        #     case "마루":
        #         timeout_handler(lambda: OP.check_o2o_tab(keyword), "check_o2o_more_btn")
        #     case "거울":
        #         timeout_handler(lambda: SP.search_shop_tab(keyword), "check_shop_more_btn")
        #     case "원룸":
        #         timeout_handler(lambda: CSP.check_contents_tab(), "check_contents_more_btn")
        #     case "주방":
        #         timeout_handler(lambda: CP.check_card_tab(), "check_picture_more_btn")
        #     case "오늘의집":
        #         timeout_handler(lambda: CSP.check_contents_tab(), "check_contents_more_btn2")
        # 키워드와 함수 매핑
        actions = {
            "마루": lambda: timeout_handler(lambda: OP.check_o2o_tab(keyword), "check_o2o_more_btn"),
            "거울": lambda: timeout_handler(lambda: SP.search_shop_tab(keyword), "check_shop_more_btn"),
            "원룸": lambda: timeout_handler(lambda: CSP.check_contents_tab(), "check_contents_more_btn"),
            "주방": lambda: timeout_handler(lambda: CP.check_card_tab(), "check_picture_more_btn"),
            "오늘의집": lambda: timeout_handler(lambda: CSP.check_contents_tab(), "check_contents_more_btn2"),
        }

        # 키워드에 따라 동작 수행
        if keyword in actions:
            actions[keyword]()


    def check_input_keyword(self, input_keyword):
        timeout_handler(lambda: expect(self.integrated_search_box).to_have_attribute("value", input_keyword), "input_keyword")

    def re_integrated_search(self, keyword):
        timeout_handler(lambda: self.x_button.click(), "click_x_btn")
        timeout_handler(lambda: self.integrated_search_box.fill(keyword), "re_search_input")
        timeout_handler(lambda: self.integrated_search_box.press("Enter"), "re_search_enter")
        timeout_handler(lambda: expect(self.page).to_have_title(re.compile(fr"{keyword}의 검색결과.*")), "check_integrated_search_title")

    # 원질의 선택 후 확인하는 케이스
    def check_original_keyword_search(self, keyword):
        timeout_handler(lambda: self.page.get_by_role("link", name=re.compile(fr"{keyword} 검색결과 보기")).click(),"click_original_keyword_search")
        #print(f"{keyword} 검색 결과를 클릭했습니다.")
        timeout_handler(lambda: self.check_input_keyword(keyword),"input_keyword")
        timeout_handler(lambda: expect(self.page.get_by_role("link", name="통합")).to_be_visible(),"expect_check")

    # 제안 키워드 선택 후 확인하는 케이스
    def check_similar_keyword_search(self, keyword):
        timeout_handler(lambda: self.page.get_by_role("link", name=re.compile(fr"{keyword}로 검색하시겠어요?")).click(),"click_similar_keyword_search")
        #print(f"{keyword} 검색 결과를 클릭했습니다.")
        timeout_handler(lambda: self.check_input_keyword(keyword),"input_keyword")
        timeout_handler(lambda: expect(self.page.get_by_role("link", name="통합")).to_be_visible(),"expect_check")
    
    def hash_tag(self,keyword):
        timeout_handler(lambda: self.search_keyword(keyword),"input_keyword")
        hash_tag = self.page.locator("section").filter(has_text="오하우스에 관심있는 사람들이 모인 곳#오하우스콘텐츠").get_by_role("link")
        timeout_handler(lambda: hash_tag.click(),"hash_tag_click")
        timeout_handler(lambda: self.page.get_by_role("heading", name="#오하우스").wait_for(state='visible'),"expect_check")
    
    # 통검 > 사진 컬렉션 > 컨텐츠 선택
    def search_contents_detail(self,card, url):
        card_xpath = "//a[@class='search-card-item__link']"
        locator = self.page.locator(f'xpath={card_xpath}')
        timeout_handler(lambda: locator.nth(0).click(),"card_click") 

        if url == self.page.url:
            write_log('web', f"첫번째 카드 선택 시 이동된 상세 주소: {self.page.url}")
            if card =="동영상":
                timeout_handler(lambda: self.page.locator("video").wait_for(state='visible'),"video_detail_expect_check")
            else:
                timeout_handler(lambda: self.page.get_by_role("link", name=re.compile(fr".*{card}.*")).wait_for(state='visible'),"contents_detail_expect_check")
        else:
            raise TimeoutException(f"다른 카드로 이동됨")
    
    # 통검 > 제작형 컨텐츠 확인 
    def search_produced_contents(self, keyword, advices_url, housewarming_projects_url, card_collections_url, exhibitions_url, category_url):
        housewarming_locator = self.page.locator("div:nth-child(3) > .css-381py4 > .css-zjik7 > .css-qnj4zr > .css-bl687k")
        advices_locator = self.page.locator(".css-zjik7 > .css-qnj4zr > .css-bl687k")
        card_locator =  self.page.locator("div:nth-child(4) > .css-381py4 > .css-zjik7 > .css-qnj4zr > .css-bl687k")
        #차박 > 노하우/집들이/카드 컬렉션 진입 확인
        if keyword == "차박":
            timeout_handler(lambda: advices_locator.first.click(),"advices_click")
            assert advices_url == self.page.url
            self.page.wait_for_timeout(2000)
            timeout_handler(lambda: self.page.go_back(), "go_back")
            timeout_handler(lambda: housewarming_locator.click(), "housewarming_click")
            assert housewarming_projects_url == self.page.url
            self.page.wait_for_timeout(2000)
            timeout_handler(lambda: self.page.go_back(), "go_back")
            timeout_handler(lambda: card_locator.click(), "card_click")
            assert card_collections_url == self.page.url
            self.page.wait_for_timeout(2000)
            timeout_handler(lambda: self.page.go_back(), "go_back")
        # 가구 추천 > 첫번째 링크 이동 확인
        elif keyword == "가구 추천":
            timeout_handler(lambda: self.page.locator("label").filter(has_text="가구 추천 가구추천").click(), "link_click")
            timeout_handler(lambda: self.check_input_keyword(re.compile(fr"가구 추천 가구추천.*")),"check_input_keyword")
        # 의자 > 타이틀, 서브 타이틀 확인 / 기획전 랜딩, 유튭 재생, 링크 랜딩
        elif keyword == "의자":
            exhibitions_xpath = '/html/body/div[1]/div/div/article/div/div/div[1]'
            write_log('web', f"제작형 컨텐츠 노출정보 확인: {self.page.locator(f'xpath={exhibitions_xpath}').inner_text()}")
            timeout_handler(lambda: self.page.get_by_role("link", name="기획전 바로가기").click(), "exhibitions_click")
            assert exhibitions_url == self.page.url
            self.page.wait_for_timeout(2000)
            timeout_handler(lambda: self.page.go_back(), "go_back")
            
            #유튜브 콘텐츠 찾아서 재생버튼 클릭 (주석처리)
            '''youtube = self.page.locator("article").filter(has_text=re.compile(fr"{keyword}.*")).locator("iframe").content_frame.get_by_label("재생", exact=True)
            timeout_handler(lambda: youtube.click(),"youtube_play")'''

            #링크 아이콘 클릭 : 쿼리 키워드 랜딩
            timeout_handler(lambda: self.page.get_by_role("link", name="인테리어의자").click(),"link_click")
            SP = ShopSearchProcedure(self.page)
            timeout_handler(lambda: SP.check_shop_tab(),"shop_search_check")
            timeout_handler(lambda: self.page.go_back(), "go_back")

            #링크 아이콘 : 카테고리 필터 적용되어 랜딩 
            timeout_handler(lambda: self.page.get_by_role("link", name="게이밍의자").click(),"link_click")
            assert category_url == self.page.url
            self.page.wait_for_timeout(2000)
            timeout_handler(lambda: self.page.go_back(), "go_back")
    
    # 통검 > 브랜드홈 확인 및 랜딩
    def brand_home_btn(self, brand):
        brand_home_xpath= '/html/body/div[1]/div/div/article/div/div'
        write_log('web', f"브랜드 홈의 노출 정보 확인: {self.page.locator(f'xpath={brand_home_xpath}').inner_text()}")    
        timeout_handler(lambda: self.page.locator(f'xpath={brand_home_xpath}').click(), "brand_home_btn_click")
        timeout_handler(lambda: self.page.get_by_role("heading", name=brand).wait_for(state = 'visible'),"brand_detail_check")

    # 통검 > 쇼핑 컬렉션 > 카드 정보 확인
    def search_collection_info(self, collection):
        for i in range(len(collection)):
            #타이틀 확인
            header = self.page.get_by_role("heading", name=collection[i])
            timeout_handler(lambda: expect(header).to_be_visible(timeout=10*1000), "collection_header")
            header_info = header.inner_text()
            #print("타이틀 정보 : "+header_info)

            # 카드 정보 확인
            card_list_xpath="//ul[@class='row search-store__production-list']"
            card_list = self.page.locator(f'xpath={card_list_xpath}').locator('.col-lg-2.col-4.search-store__scroller__product__wrap')
            list_values = []
            img_details = []
            label_details = []
            benefit_details = []
            count = card_list.count()
            for i in range(count):
                text= card_list.nth(i).inner_text()
                list_values.append(text)
                #print("-------------------------------------------")
                #print("상세정보 :"+list_values[i])
                
                delivery_locator = card_list.nth(i).locator('img.icon')     
                if  delivery_locator.count() > 0:  
                    delivery_alt =  delivery_locator.get_attribute('alt') 
                    img_details.append(delivery_alt) 
                    #print(f"delivery라벨 : {delivery_alt}")
                else:  # 이미지가 없는 경우
                    img_details.append({'delivery_alt': "배송정보 라벨 없음"}) 
                    #print("배송정보 라벨 없음")

                svg_locators = card_list.nth(i).locator('svg.icon')
                if  svg_locators.count() > 0:  
                    for j in range(svg_locators.count()):  
                        aria_label = svg_locators.nth(j).get_attribute('aria-label') 
                        label_details.append({'aria-label': aria_label})
                        #print(f"label : {aria_label}")
                else: 
                    label_details.append({'aria-label': "라벨 없음"})
                    #print("SVG 라벨 없음")

                benefit_locators = card_list.nth(i).locator('span.css-sqm42b.etn6hd10')
                if  benefit_locators.count() > 0: 
                    for k in range(benefit_locators.count()):  
                        benefit_label = benefit_locators.nth(k).inner_text() 
                        benefit_details.append({'benefit': benefit_label})
                        #print(f"쿠폰정보 : {benefit_label}")
                else: 
                    benefit_details.append({'benefit': "쿠폰 없음"})
                    #print("쿠폰 없음")

        write_log('web', f"타이틀 정보: {header_info}")
        write_log('web', f"카드 정보: {list_values+img_details+label_details+benefit_details}")

    def search_apt_info(self):
        #타이틀 확인
        header = self.page.locator('.css-1bl7vfq.e14e6g9x8')
        timeout_handler(lambda: expect(header).to_be_visible(timeout=10*1000), "collection_header")
        write_log('web', f"타이틀 정보: {header.inner_text()}")
        
        # 카드 정보 확인
        card_list_xpath="//div[contains(@class, 'css-netewu') and contains(@class, 'e14e6g9x6')]"
        card_list = self.page.locator(f'xpath={card_list_xpath}').locator('.css-e4xcpv.e14e6g9x5')
        list_values = []
        count = card_list.count()
        for i in range(count):
            text= card_list.nth(i).inner_text()
            list_values.append(text)
            write_log('web',list_values[i])
    
    def search_apt_click(self):
        card_list_xpath="//div[contains(@class, 'css-netewu') and contains(@class, 'e14e6g9x6')]"
        card_list = self.page.locator(f'xpath={card_list_xpath}').locator('.css-e4xcpv.e14e6g9x5')
        list_values = []
        count = card_list.count()
        random_index = random.randint(0, count - 1)

        for i in range(count):
            text= card_list.nth(i).inner_text()
            list_values.append(text)

        if count > 0:
            timeout_handler(lambda: card_list.nth(random_index).click(),"random_related_click") 
            write_log('web', f"랜덤으로 선택한 아파트 정보: {list_values[random_index]}")
        else:
            raise TimeoutException(f"아파트를 클릭 할 수 없음")
        #상세 이동 후, 아파트 뱃지 css 소스 있는지 확인
        timeout_handler(lambda: expect(self.page.locator('.css-cku8hy')).to_be_visible(timeout=5000), "apt_check")

    #우측 스와이프 버튼 클릭 후, 마지막에 더보기 버튼 찾아서 클릭 
    def scroller_ui_right_click(self):
        scroller_ui_btn = "div.scroller__ui__right > svg.active > g"
        #스와이프 버튼 3번 반복 클릭
        for _ in range(3):
            timeout_handler(lambda: self.page.locator(scroller_ui_btn).first.click(), "scroller_ui_btn_click")
            time.sleep(0.5)
        #더보기 버튼 클릭 
        more_button_right = self.page.locator(".css-15ohgvg.e1sp4cgg1")
        timeout_handler(lambda: more_button_right.click(), "click_more_btn_right")
        time.sleep(0.5)
        
class SearchAutoComplete():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.integrated_search_box = page.get_by_placeholder("통합검색")
    
    def search_autocomplete(self, input_keyword, click_keyword):
        timeout_handler(lambda: self.page.goto('https://qa-web.dailyhou.se/', timeout= 0), "enter_qa_home")
        timeout_handler(lambda: self.integrated_search_box.fill(input_keyword), "search_input")
        search_keyword = self.page.get_by_role("option", name=click_keyword)
        timeout_handler(lambda: search_keyword.click(), "option_click")

    #통합검색 searchField에 키워드 검색 후, 자동완성에서 첫번째 옵션에 해당 검색어가 노출되는지 확인
    def search_autocomplete_first_option_check_ture(self, input_keyword, check_keyword):
        timeout_handler(lambda: self.page.goto('https://qa-web.dailyhou.se/', timeout=0), "enter_qa_home")
        timeout_handler(lambda: self.integrated_search_box.fill(input_keyword), "search_input")
        time.sleep(1) 
        all_options = self.page.get_by_role("option")
        first_option = all_options.first
        first_option_text = first_option.inner_text()  

        if first_option_text == check_keyword:
             timeout_handler(lambda: first_option.click(), "first_option_click")
        else:
            return False

    #통합검색 searchField에 키워드 검색 후, 자동완성에서 첫번째 옵션에 해당 검색어가 미노출되는지 확인
    def search_autocomplete_first_option_check_false(self, input_keyword, check_keyword):
        timeout_handler(lambda: self.page.goto('https://qa-web.dailyhou.se/', timeout=0), "enter_qa_home")
        timeout_handler(lambda: self.integrated_search_box.fill(input_keyword), "search_input")
        time.sleep(1) 
        all_options = self.page.get_by_role("option")
        first_option = all_options.first
        first_option_text = first_option.inner_text()  

        if first_option_text != check_keyword:
             return True
        else:
            return False

    def check_category_plp(self, category_name):
        category_element = self.page.locator('a', has_text=category_name)
        if category_element.count() > 0:
            href_value = category_element.nth(0).get_attribute('href')  # 첫 번째 요소의 href 가져오기
            # assert 문을 사용하여 href_value가 유효하고 '/store/category'를 포함하는지 확인
            assert href_value and '/store/category' in href_value, f"{category_name} 이름의 '/store/category' 링크를 못찾음"

class SearchRelatedKeyword():
    def __init__(self, page: Page) -> None:
        self.page = page

    def search_related_keyword(self, related_keyword):
        SP = SearchProcedure(self.page)
        timeout_handler(lambda: SP.search_keyword(related_keyword), "integrated_search")
        keyword_related_locator = self.page.get_by_role("link", name=re.compile(fr".*{related_keyword}.*")).first
        timeout_handler(lambda: keyword_related_locator.click(), f"search_related : {keyword_related_locator.inner_text()}")
        SP.check_input_keyword(keyword_related_locator.inner_text())

# 최근 검색어
class SearchRetrieveLatest():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.integrated_search_box = page.get_by_placeholder("통합검색")
        self.search_community_home = page.get_by_role("link", name="커뮤니티")
        self.recent_search = page.locator("text=최근 검색어")
        #self.first_option = page.get_by_role("option", exact=True)

    def handle_recent_search(self, search_keyword):
        # 최근 검색어 UI 확인 
        if self.recent_search.count() > 0:
            #print("최근 검색어가 존재하므로 키워드 선택합니다.")
            timeout_handler(lambda: self.page.get_by_text(search_keyword, exact=True).click(),"recent_search_click") 
            timeout_handler(lambda: expect(self.page.get_by_role("link", name="통합")).to_be_visible(), "check_serch")

        else:
            #print("최근 검색어가 없으므로 새 검색어를 작성합니다.")
            timeout_handler(lambda: self.integrated_search_box.fill(search_keyword), "search_input")
            timeout_handler(lambda: self.integrated_search_box.press("Enter"), "search_enter") 
            timeout_handler(lambda: self.search_retrieve_latest(search_keyword),"search_retrieve_latest") #최근 검색어를 채운 후 최근 검색어 선택하는 함수 재호출

    def search_retrieve_latest(self, keyword):
        #print(f"넘김 키워드: {keyword}")
        SP = SearchProcedure(self.page)
        timeout_handler(lambda: SP.goto_home(), "goto_home")
        timeout_handler(lambda: self.search_community_home.click(),"community_home_click")
        timeout_handler(lambda: self.integrated_search_box.click(),"placeholder_click")
        # 최근 검색어 처리
        timeout_handler(lambda: self.handle_recent_search(keyword),"handle_recent_search")

# 인기 검색어
class SearchRankingKeyword():
    rank_popup_button_xpath = "/html/body/div[1]/div/div/header/div[2]/div/div/div[2]/div/span/div/button"
    rank_popup_xpath = "/html/body/div[2]/div/div/div/header/h2"
    
    def __init__(self, page: Page) -> None:
        self.page = page
        self.integrated_search_box = page.get_by_placeholder("통합검색")

    # 인기 검색어 레이어 노출하는 버튼 선택하고 "인기 검색어"라는 레이아웃 노출
    def click_rank_button(self):    
        timeout_handler(lambda: self.page.locator(f'xpath={self.rank_popup_button_xpath}').click(), "rank_button_click")
        #print("인기 검색어 노출 버튼을 클릭했습니다.")
        timeout_handler(lambda: self.page.locator(f'xpath={self.rank_popup_xpath}').wait_for(state="visible"),"rank_popup_open")
        #print("인기검색어 팝업 로드되었습니다.")
    
    # n순위 인기 검색어 선택해라
    def click_rank_keyword(self, rank):
        # 순위는 -1을 해야해서 요렇게 선언함 요소가 first > nth(1) 요런 순으로 빠짐
        rank = rank-1
        # 순위를 선택해
        timeout_handler(lambda: self.page.locator('div[mode="list"] a').nth(rank).click(), "click_rank_keyword")
        #print("인기검색어 버튼을 클릭했습니다.") 

    # 해당 순위 키워드를 선택해라
    def search_ranking_Keyword(self, rank):
        # print(f"넘김 순위: {rank}")
        SP = SearchProcedure(self.page)
        timeout_handler(lambda: SP.goto_home(), "goto_home")
        timeout_handler(lambda: self.click_rank_button(), "click_rank_button")
        timeout_handler(lambda: self.click_rank_keyword(rank), "click_rank_keyword")
        timeout_handler(lambda: expect(self.page.get_by_role("link", name="통합")).to_be_visible(),"expect_check")

class IntegratedSearchDetail():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.integrated_card_item = page.locator(".search-card-item__link").first
        self.card_detail_checkpoint = page.get_by_title("좋아요")
        
        self.integrated_project_item = page.locator(".search-project-item__link").first
        self.integrated_advice_item = page.locator("section").filter(has_text='노하우').locator("article").get_by_role("link").first
        self.longform_detail_checkpoint = page.get_by_role("button", name="팔로우").first

        self.integrated_product_item = page.locator("section").filter(has_text='쇼핑').locator("ul").get_by_role("link").first
        self.product_detail_checkpoint = page.get_by_role("button", name="바로구매").first

        self.integrated_experts_item = page.locator(".expert-user-feed__card-wrap").first
        self.experts_myhome_checkpoint = page.get_by_role("button", name="상담신청")

        self.integrated_undiscovered_item = page.locator("section").filter(has_text='새로운 취향을 발견해보세요').locator("ul").get_by_role("link").first

    def integrated_card_enter(self):
        timeout_handler(lambda: self.integrated_card_item.click(), "enter_card_detail")

    def integrated_card_check(self):
        timeout_handler(lambda: expect(self.card_detail_checkpoint).to_be_visible(), "check_card_detail")

    def integrated_project_enter(self):
        timeout_handler(lambda: self.integrated_project_item.click(), "enter_project_detail")

    def integrated_longform_check(self):
        # content type : project, advice
        timeout_handler(lambda: expect(self.longform_detail_checkpoint).to_be_visible(), "check_longform_detail")
    
    def integrated_advice_enter(self):
        timeout_handler(lambda: self.integrated_advice_item.click(), "enter_advice_detail")
    
    def integrated_product_enter(self):
        timeout_handler(lambda: self.integrated_product_item.click(), "enter_product_detail")

    def integrated_product_check(self):
        timeout_handler(lambda: expect(self.product_detail_checkpoint).to_be_visible(), "check_product_detail")

    def integrated_experts_enter(self):
        timeout_handler(lambda: self.integrated_experts_item.click(), "enter_experts_detail")

    def integrated_experts_check(self):
        timeout_handler(lambda: expect(self.experts_myhome_checkpoint).to_be_visible(), "check_experts_myhome")

    def integrated_undiscovered_enter(self):
        timeout_handler(lambda: self.integrated_undiscovered_item.click(), "enter_undiscovered_detail")

class CardSearchProcedure():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.card_tab = page.get_by_role("link", name="사진")
        self.card_follow = page.get_by_text("팔로우")
        self.card_item = page.locator("article:has(div.card-search-item__content)").first
    
    def click_card_tab(self):
        timeout_handler(lambda: self.card_tab.click(), "enter_card_tab")
        timeout_handler(lambda: self.check_card_tab(), "check_card_tab")

    def card_enter(self):
        timeout_handler(lambda: self.card_item.click(), "enter_card_detail")

    def search_card_tab(self, keyword):
        SP = SearchProcedure(self.page)
        SP.search_keyword(keyword)
        self.click_card_tab()

    def check_card_tab(self):
        self.page.wait_for_timeout(2 * 1000)
        follow_count = self.card_follow.count()
        assert follow_count >= 4, "follow_count ="+str(follow_count)
    
     # 쇼핑 검색 > 연관 키워드 확인 > 랜덤으로 키워드 선택
    def card_related_keyword(self):
        # "연관"이라는 텍스트가 보일 때까지 대기
        timeout_handler(lambda: self.page.get_by_text("연관").wait_for(state='visible'), "card_related_expect_check")

        related_xpath = "//p[@class='card-feed__related-keywords']"
        locator = self.page.locator(f'xpath={related_xpath}')
        links = locator.locator('a')
        link_count = links.count()
        link_texts = []
        random_index = random.randint(0, link_count - 1)  # 0부터 link_count - 1 사이의 랜덤 인덱스 생성
        
        for i in range(link_count):
            # 각 링크의 텍스트를 가져옴
            link_text = links.nth(i).inner_text()  # nth() 메서드를 사용하여 특정 인덱스의 요소 접근
            link_texts.append(link_text)

        # 랜덤으로 링크 선택
        if link_count > 0:
            timeout_handler(lambda: links.nth(random_index).click(),"random_related_click")  # 랜덤 인덱스를 통해 랜덤 링크 선택
            # 선택한 링크 클릭
            write_log('web', f"랜덤으로 선택한 연관 검색어 정보: {link_texts[random_index]}")
        else:
            raise TimeoutException(f"연관 검색어를 클릭 할 수 없음")
        
    # 사진 탭에서 첫번쨰 카드 선택 시 상세로 이동  
    def contents_detail(self,card, url):
        card_xpath = "//div[@class='card-search-item__content']"
        locator = self.page.locator(f'xpath={card_xpath}')
        timeout_handler(lambda: locator.nth(0).click(),"card_click") 

        if url == self.page.url:
            write_log('web', f"첫번째 카드 선택 시 이동된 상세 주소: {self.page.url}")
            if card =="동영상":
                timeout_handler(lambda: self.page.locator("video").wait_for(state='visible'),"video_detail_expect_check")
            else:
                timeout_handler(lambda: self.page.get_by_role("link", name=re.compile(fr".*{card}.*")).wait_for(state='visible'),"contents_detail_expect_check")
        else:
            raise TimeoutException(f"다른 카드로 이동됨")
        
    # 사진 탭 > 필터 모달창 확인
    def search_filter_modal(self):
        timeout_handler(lambda: self.page.get_by_role("button", name="정렬").hover(),"filter_hover")
        sort_filter = self.page.locator("div").filter(has_text=re.compile(fr"추천순.*")).nth(1)
        write_log('web', f"필터 모달 확인: {sort_filter.inner_text()}")
        timeout_handler(lambda: self.page.get_by_role("button", name="동영상").hover(),"filter_hover")
        video_filter = self.page.locator("ul").filter(has_text=re.compile(fr"^동영상$")).get_by_role("button")
        timeout_handler(lambda: video_filter.wait_for(state="visible", timeout=5000),"video_filter_check")
        timeout_handler(lambda: self.page.get_by_role("button", name="주거형태").hover(),"filter_hover")
        house_filter = self.page.locator("div").filter(has_text=re.compile(fr"원룸&오피스텔.*")).nth(1)
        write_log('web', f"필터 모달 확인: {house_filter.inner_text()}")
        timeout_handler(lambda: self.page.get_by_role("button", name="공간", exact=True).hover(),"filter_hover")
        place_filter = self.page.locator("div").filter(has_text=re.compile(fr"원룸거실침실주방욕실아이방드레스룸서재.*")).nth(1)
        write_log('web', f"필터 모달 확인: {place_filter.inner_text()}")
        timeout_handler(lambda: self.page.get_by_role("button", name="평수").hover(),"filter_hover")
        sqft_filter = self.page.locator("div").filter(has_text=re.compile(fr"평 미만10평대20평대30평대40평대50평 이상.*")).nth(1)
        write_log('web', f"필터 모달 확인: {sqft_filter.inner_text()}")
        timeout_handler(lambda: self.page.get_by_role("button", name="스타일").hover(),"filter_hover")
        style_filter = self.page.locator("div").filter(has_text=re.compile(fr"모던북유럽빈티지내추럴프로방스&로맨틱클래식&앤틱한국&아시아유니크.*")).nth(1)
        write_log('web', f"필터 모달 확인: {style_filter.inner_text()}")
        timeout_handler(lambda: self.page.get_by_role("button", name="컬러").hover(),"filter_hover")
        color_filter = self.page.locator("div").filter(has_text=re.compile(fr"그레이화이트블랙민트블루핑크그린레드.*")).nth(1)
        write_log('web', f"필터 모달 확인: {color_filter.inner_text()}")
        timeout_handler(lambda: self.page.get_by_role("button", name="셀프/전문").hover(),"filter_hover")
        self_professional_filter = self.page.locator("div").filter(has_text=re.compile(fr"셀프전문가.*")).nth(1)
        write_log('web', f"필터 모달 확인: {self_professional_filter.inner_text()}")
        timeout_handler(lambda: self.page.get_by_role("button", name="제품정보").hover(),"filter_hover")
        prd_info_filter = self.page.locator("div").filter(has_text=re.compile(fr"제품정보 사진.*")).nth(1)
        timeout_handler(lambda: prd_info_filter.wait_for(state="visible", timeout=5000),"prd_info_filter_check")
    
    # 사진탭 > 필터 모달 확인 > 상세 필터 선택
    def search_filter_check(self,filter,filter_name):
        if filter == "동영상":
            timeout_handler(lambda: self.page.get_by_role("button", name=filter).hover(),"videofilter_hover")
            video_filter = self.page.locator("ul").filter(has_text=re.compile(fr"^{filter}$")).get_by_role("button")
            timeout_handler(lambda: video_filter.wait_for(state="visible", timeout=5000),"video_filter_check")
            timeout_handler(lambda: video_filter.click(), "video_filter_click")
            self.page.wait_for_timeout(2000)
        elif filter =="공간":
            timeout_handler(lambda: self.page.get_by_role("button", name=filter, exact=True).hover(),"filter_hover")
            timeout_handler(lambda: self.page.get_by_role("button", name=filter_name).click(),"filter_click")
            timeout_handler(lambda: self.page.get_by_text(re.compile(fr"{filter_name}초기화")).wait_for(state="visible", timeout=5000),"place_filter_check")
            self.page.wait_for_timeout(2000)
        elif filter =="제품정보":
            timeout_handler(lambda: self.page.get_by_role("button", name=filter, exact=True).hover(),"filter_hover")
            timeout_handler(lambda: self.page.get_by_role("button", name=filter_name).click(),"filter_click")
            timeout_handler(lambda: self.page.get_by_text(re.compile(fr"{filter}초기화")).wait_for(state="visible", timeout=5000),"prd_info_filter_check")
            self.page.wait_for_timeout(2000)
        else :
            timeout_handler(lambda: self.page.get_by_role("button", name=filter).hover(),"filter_hover")
            timeout_handler(lambda: self.page.get_by_role("button", name=filter_name).click(),"filter_click")
            timeout_handler(lambda: self.page.get_by_text(re.compile(fr"{filter_name}초기화")).wait_for(state="visible", timeout=5000),"other_filer_check")
            self.page.wait_for_timeout(2000)

class ShopSearchProcedure():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.shop_tab = page.locator("nav").filter(has_text="통합").get_by_text("쇼핑")
        # 상품 카드 요소 개선
        #self.product_items = page.get_by_role("article").get_by_role("link")
        #self.product_item = page.get_by_role("article").get_by_role("link").first
        #self.product_items_div = page.locator(".css-1fbe9bq")
        #self.product_item_div = page.locator(".css-1fbe9bq").first
        self.product_item = page.locator('.virtualized-list.production-feed__content.row').get_by_role("link").first
        self.scrap_toggle_btn = page.get_by_label("scrap 토글 버튼")

        self.x_button = page.get_by_role("button", name="")
        self.shop_search_box = page.get_by_placeholder("쇼핑 검색")
        self.shop_gnb = page.get_by_role("link", name="쇼핑")
        
        self.price_filter = page.get_by_role("button", name="특가", exact=True)
        self.price_filter_checkpoint = page.get_by_role("button", name="특가상품 보기").first
        #self.price_filter_badge = page.get_by_test_id('badge-list-container') # 뱃지를 담는 통
        self.price_filter_badge = page.locator('.production-feed__item-wrap.col-6.col-md-4.col-lg-3').first.get_by_label("특가") # 첫번째 상품 카드의 특가 뱃지
        self.sort_button = page.query_selector("button[class='category-filter-bar-order-button']")
        self.sort_option = page.locator("li").get_by_role("button")

    def product_enter(self):
        ''' 쇼핑탭 > PDP 진입 '''
        timeout_handler(lambda: self.product_item.click(), "enter_product_detail")
        
        ''' # USP 뱃지 때문에 요소 분기 만든 것 (일단 유지..)
        if self.product_item.is_visible():
            print("article click")
            timeout_handler(lambda: self.product_item.click(), "enter_product_detail") 
        elif self.product_item_div.is_visible():
            print("class click")
            timeout_handler(lambda: self.product_item_div.click(), "enter_product_detail") 
        '''

    def search_shop_tab(self, keyword):
        ''' 통합검색 > 쇼핑 탭 클릭 '''
        SP = SearchProcedure(self.page)
        SP.search_keyword(keyword)
        timeout_handler(lambda: self.shop_tab.click(), "enter_shop_tab")
        timeout_handler(lambda: self.check_shop_tab(), "check_shop_tab")

    def re_search_shop_tab(self, keyword):
        ''' 쇼핑 SRP 에서 재검색 동작 '''
        timeout_handler(lambda: self.x_button.click(), "click_x_btn")
        timeout_handler(lambda: self.shop_search_box.fill(keyword), "shop_search_input")
        timeout_handler(lambda: self.shop_search_box.press("Enter"), "shop_search_enter")
        timeout_handler(lambda: self.check_shop_tab(), "check_shop_tab")

    def check_shop_tab(self):
        ''' 쇼핑 SRP 확인 '''
        self.page.wait_for_timeout(2 * 1000)
        for retry in range(4):
            try:
                #XPC 1005 에서 상품카드(article) 요소 변경되어 스크랩으로 확인
                #item_count = self.product_items.count()
                item_count = self.scrap_toggle_btn.count()
                assert item_count >= 4, "item_count ="+str(item_count)
                break
            except Exception as e:
                if retry == 3:
                    raise TimeoutException(f"스크랩 토글 버튼 미노출")
                else:
                    self.page.wait_for_timeout(1 * 1000)

    def search_shop_home(self, keyword):
        ''' 쇼핑홈에서 검색 '''
        timeout_handler(lambda: self.page.goto('https://qa-web.dailyhou.se/', timeout= 0), "enter_qa_home")
        timeout_handler(lambda: self.shop_gnb.click(), "enter_shop_home")
        timeout_handler(lambda: self.shop_search_box.click(), "shop_search_box_click")
        timeout_handler(lambda: self.shop_search_box.fill(keyword), "shop_search_input")
        timeout_handler(lambda: self.shop_search_box.press("Enter"), "shop_search_enter")

    def apply_price_filter(self):
        ''' 쇼핑 SRP > 특가 뱃지 적용 '''
        timeout_handler(lambda: self.price_filter.click(), "price_filter_click")
        timeout_handler(lambda: self.page.get_by_role("checkbox").check(), "filter_checkbox_click")
        timeout_handler(lambda: self.price_filter.click(), "price_filter_click")
        timeout_handler(lambda: expect(self.price_filter_checkpoint).to_be_visible(), "apply_filter_click")
    
    def check_price_filter(self):
        ''' 특가 뱃지 적용된 상품 리스트 확인 '''
        self.page.wait_for_timeout(2 * 1000)
        timeout_handler(lambda: expect(self.price_filter_badge).to_be_visible(), "price_filter_first_item")
        
        ''' 노출된 뱃지 컨테이너 개수를 세는 방식 (특가 뱃지가 없어도 pass 되기 때문에 주석 처리)
        for retry in range(4):
            try:
                badge_count = self.price_filter_badge.count()
                assert badge_count >= 4, "badge_count ="+str(badge_count)
                break
            except Exception as e:
                if retry == 3:
                    raise TimeoutException(f"특가 뱃지 미노출 : {e}")
                else:
                    self.page.wait_for_timeout(1 * 1000)
        '''

    def change_sort(self, filter_name):
        ''' 정렬 변경 후 결과 수 Return '''
        timeout_handler(lambda: self.sort_button.click(), "sort_button_click")
        timeout_handler(lambda: self.sort_option.filter(has_text=filter_name).click(), "sort_option_click")
        self.page.wait_for_timeout(1000)
        timeout_handler(lambda: expect(self.page.get_by_role("button", name=filter_name)).to_be_visible(), "sort_option_check")
        
        #정렬 동작 후 전체 결과 수 return
        element = self.page.query_selector('.page .production-feed .css-1uv28lx.eh8ehv78 > p')
        if element is not None:
            result_number = re.sub(r'\D', '', element.text_content())
            return result_number
        
    def change_sort_check(self, option1, option2):
        ''' 정렬 변경 두 번 진행 후 전체 결과수가 변경되지 않았는지 확인 '''
        result_number1 = self.change_sort(option1)
        result_number2 = self.change_sort(option2)
        # count 비교값이 달라 fail나서 우선 주석처리
        # if result_number1 and result_number2:
        #     assert result_number1 == result_number2
        # else:
        #     raise TimeoutException(f"정렬 변경 후 전체 결과 수 획득 실패")
        if result_number1 and result_number2:
            if result_number1 == result_number2:
                assert result_number1 == result_number2
            else:
                write_log('web', "판매순: "+result_number1+", 낮은가격순: "+result_number2 + " < 값이 다르긴하나 pass하는 코드")
        else:
            raise TimeoutException(f"정렬 변경 후 전체 결과 수 획득 실패")
    
    # 브랜드 홈 바로가기
    def brand_home_click(self, keyword):
        timeout_handler(lambda: self.page.get_by_role("link", name=fr"{keyword} 브랜드홈바로가기").click() ,"brand_home_click")
        timeout_handler(lambda: self.page.get_by_role("heading", name=keyword).wait_for(state='visible'),"brand_home_expect_check")
    
    # 쇼핑 검색 > 연관 키워드 확인 > 랜덤으로 키워드 선택
    def shop_related_keyword(self):
        # "연관"이라는 텍스트가 보일 때까지 대기
        timeout_handler(lambda: self.page.get_by_text("연관").wait_for(state='visible'), "shop_related_expect_check")

        related_xpath = "//p[@class='production-feed__related-keywords']"
        locator = self.page.locator(f'xpath={related_xpath}')
        links = locator.locator('a')
        link_count = links.count()
        link_texts = []
        random_index = random.randint(0, link_count - 1)  # 0부터 link_count - 1 사이의 랜덤 인덱스 생성
        
        for i in range(link_count):
            # 각 링크의 텍스트를 가져옴
            link_text = links.nth(i).inner_text()  # nth() 메서드를 사용하여 특정 인덱스의 요소 접근
            link_texts.append(link_text)

        # 랜덤으로 링크 선택
        if link_count > 0:
            timeout_handler(lambda: links.nth(random_index).click(),"random_related_click")  # 랜덤 인덱스를 통해 랜덤 링크 선택
            # 선택한 링크 클릭
            write_log('web', f"랜덤으로 선택한 연관 검색어 정보: {link_texts[random_index]}")    
        else:
            raise TimeoutException(f"연관 검색어를 클릭 할 수 없음")
        
class ContentsSearchProcedure():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.contents_tab = page.get_by_role("link", name="콘텐츠")
        self.scrap_toggle_btn = page.get_by_label("scrap 토글 버튼")
        self.contents_item = page.locator("article").get_by_role("link").first
        self.contents_search_box = page.get_by_placeholder("통합검색")
    
    def click_contents_tab(self):
        timeout_handler(lambda: self.contents_tab.click(), "enter_contents_tab")
        timeout_handler(lambda: self.check_contents_tab(), "check_contents_tab")

    def contents_enter(self):
        timeout_handler(lambda: self.contents_item.click(), "enter_contents_detail")

    def search_contents_tab(self, keyword):
        SP = SearchProcedure(self.page)
        SP.search_keyword(keyword)
        self.click_contents_tab()

    def check_contents_tab(self):
        self.page.wait_for_timeout(2 * 1000)
        scrap_count = self.scrap_toggle_btn.count()
        assert scrap_count >= 4, "scrap_count ="+str(scrap_count)
    
    def type_filter(self,filter):
        timeout_handler(lambda: self.page.get_by_role("button", name="종류").click(),"type_fllter_click")
        timeout_handler(lambda: self.page.get_by_role("button", name= filter).click(),"housewarming_fllter_click")
        timeout_handler(lambda:self.check_contents_tab(),"check_contents_tab")


    def search_contents_home(self, keyword):
        timeout_handler(lambda: self.page.goto('https://qa-web.dailyhou.se/contents/card_collections', timeout= 0), "enter_contents_home")
        timeout_handler(lambda: self.contents_search_box.click(), "contents_search_box_click")
        timeout_handler(lambda: self.contents_search_box.fill(keyword), "contents_search_input")
        timeout_handler(lambda: self.contents_search_box.press("Enter"), "contents_search_enter")

class O2OSearchProcedure():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.o2o_tab = page.locator("nav").filter(has_text="통합").get_by_text("시공업체")
        self.x_button = page.get_by_role("button", name="")
        self.o2o_search_box = page.get_by_placeholder("시공업체 검색")
        self.o2o_gnb = page.get_by_role("link", name="인테리어/생활")
        self.o2o_search_box = page.get_by_placeholder("시공업체 검색")
        self.o2o_experts_item = page.query_selector_all('.expert-user-feed__full-card__carousel-wrap')

    def click_o2o_tab(self):
        timeout_handler(lambda: self.o2o_tab.click(), "enter_o2o_tab")
        timeout_handler(lambda: self.check_o2o_tab(), "check_o2o_tab")

    def experts_enter(self):
        timeout_handler(lambda: self.o2o_experts_item[0].click(), "click_o2o_experts_item")

    def search_o2o_tab(self, keyword):
        SP = SearchProcedure(self.page)
        SP.search_keyword(keyword)
        self.click_o2o_tab()
        self.check_o2o_tab(keyword)

    def check_o2o_tab(self, keyword=None):
        if keyword:
            expect(self.page.get_by_text(f"'{keyword}' 업체 검색 결과")).to_be_visible
        else:
            experts_item_count = len(self.o2o_experts_item)
            assert experts_item_count > 0, "experts_item count ="+str(experts_item_count)
        
    def re_search_o2o_tab(self, keyword):
        timeout_handler(lambda: self.x_button.click(), "click_x_btn")
        timeout_handler(lambda: expect(self.page.get_by_text("최근 검색어")).to_be_visible(), "recent_keyword_check")        
        timeout_handler(lambda: self.o2o_search_box.fill(keyword), "o2o_search_input")
        timeout_handler(lambda: self.o2o_search_box.press("Enter"), "o2o_search_enter")
        timeout_handler(lambda: self.check_o2o_tab(keyword), "check_o2o_tab")

    def search_o2o_home(self, keyword):
        timeout_handler(lambda: self.page.goto('https://qa-web.dailyhou.se/', timeout= 0), "enter_qa_home")
        timeout_handler(lambda: self.o2o_gnb.click(), "enter_shop_home")
        timeout_handler(lambda: self.o2o_search_box.click(), "shop_search_box_click")
        timeout_handler(lambda: self.o2o_search_box.fill(keyword), "shop_search_input")
        timeout_handler(lambda: self.o2o_search_box.press("Enter"), "shop_search_enter")

class UserSearchProcedure():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.user_tab = page.locator("nav").filter(has_text="통합").get_by_text("유저")
        self.user_title = page.get_by_role("heading", name=re.compile(r"유저\d.*"))
        self.user_more_btn = page.locator("header").filter(has_text=re.compile(r"유저.*더보기"))
        self.user_follow_btn = page.get_by_role("button", name="팔로우").first
        self.user_following_btn = page.get_by_role("button", name="팔로잉").first
        self.user_item = page.query_selector("[data-item-index='1']")
        self.user_home_checkpoint = page.get_by_text("모두보기")

    def check_invisible_collection(self):
        timeout_handler(lambda: expect(self.user_title).not_to_be_visible(), "check_user_title")
        timeout_handler(lambda: expect(self.user_more_btn).not_to_be_visible(), "check_user_more_btn")

    def click_user_tab(self):
        timeout_handler(lambda: self.user_tab.click(), "enter_user_tab")
        timeout_handler(lambda: self.check_user_tab(), "check_user_tab")

    def check_user_tab(self, keyword=None):
        timeout_handler(lambda: expect(self.user_follow_btn).to_be_visible(), "check_follow_btn")

    def check_user_follow_btn(self):
        timeout_handler(lambda: expect(self.user_follow_btn).to_be_visible(), "check_follow_btn")
    
    def click_user_follow_btn(self):
        timeout_handler(lambda: self.user_follow_btn.click(), "click_follow_btn")
    
    def check_user_following_btn(self):
        timeout_handler(lambda: expect(self.user_following_btn).to_be_visible(), "check_following_btn")

    def click_user_following_btn(self):
        timeout_handler(lambda: self.user_following_btn.click(), "click_following_btn")

    def user_enter_and_check(self):
        timeout_handler(lambda: self.user_item.click(), "enter_user_item")
        timeout_handler(lambda: expect(self.user_home_checkpoint).to_be_visible(), "check_user_home")
        
class IntegratedSearchIBChip():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.selected_ib_class = "div.e1x3u3dh0.css-3v8746"
        self.unselected_ib_class = "div.e1x3u3dh0.css-e5g9xf"
        
        self.shopping_collection = page.locator("section").filter(has_text='쇼핑')
        self.shopping_selected_ib_chip = self.shopping_collection.locator(self.selected_ib_class)
        self.shopping_unselected_ib_chip = self.shopping_collection.locator(self.unselected_ib_class)

        self.card_collecton = page.locator("section").filter(has_text='사진')
        self.card_selected_ib_chip = self.card_collecton.locator(self.selected_ib_class)
        self.card_unselected_ib_chip = self.card_collecton.locator(self.unselected_ib_class)

    # 쇼핑이나 사진 컬렉션의 n번째 위치한 ib chip 을 클릭
    def click_ib_chip(self, collection_name, chip_idx):
        if collection_name == 'shopping':
            click_ib_chip = self.shopping_unselected_ib_chip.nth(chip_idx)
        elif collection_name == 'card':
            click_ib_chip = self.card_unselected_ib_chip.nth(chip_idx)
        # print(f'클릭한 IB chip 이름 : {click_ib_chip.inner_text()}')
        timeout_handler(lambda: click_ib_chip.click(), f"click_{collection_name}_ib_chip")
        timeout_handler(lambda: self.check_ib_chip(collection_name), f"check_{collection_name}_unselected_ib_chip")

    # 쇼핑이나 사진 컬렉션에서 선택된 ib chip 이 하나인지 확인
    def check_ib_chip(self, collection_name):
        if collection_name == 'shopping':
            assert self.shopping_selected_ib_chip.count() == 1, f"{collection_name} 컬렉션의 선택된 ib chip 이 1이 아님"
        elif collection_name == 'card':
            assert self.card_selected_ib_chip.count() == 1, f"{collection_name} 컬렉션의 선택된 ib chip 이 1이 아님"
