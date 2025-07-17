from web.ObjectSetting.comm_service import *
from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.common_object import *
from web.ObjectSetting.comm_service import *
from app.common.base_method.exception_func import *
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.web_result_binary import ResultWeb
from web.BasicSetting.exception_func import *

def checkout(page):
    CommonElements.login_func(page)
    page.wait_for_timeout(2000)
    CommPlatformElements.checkout_func(page)
    page.wait_for_timeout(2000)


@pytest.mark.smoke
def test_comm_service_00001(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\test_comm_service_001 : 쇼핑탭 이동 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.into_shopping_tap(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00014(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\test_comm_service_014 : 퀵메뉴 노출 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.into_quick_menu(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00015(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_015 : 카테고리 리스트 노출 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_category(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00016(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_today_deal(page),
                           check=True)

@pytest.mark.smoke
def test_comm_service_00017(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: PageElements.qaweb_main_url(page))
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_plp3(page),
                           check=True)

@pytest.mark.smoke
def test_comm_service_00019(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_019 : 몰랐던 취향까지 발견하기 (구 인기상품) 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_popular_product(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00022(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_022 : 카테고리 상세영역 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_category_detail(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00026(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_026 : MD's Pick 상품 상세영역 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_mdpick(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_comm_service_00032(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_032 : 무한 스크롤링 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.infinite_scroll(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_comm_service_00033(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_033 : 탑 이동하는 플로팅 버튼 동작 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.top_floating(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00034(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_034 : 하단 리스트의 상품 상세 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_mdpick_detail(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00036(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_036 : 오늘의딜 더보기 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_today_deal_more(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00043(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_043 : 오늘의딜 상세 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_today_deal_detail(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_comm_service_00056(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_056 : 무한스크롤 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_infinite_scrolling(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00057(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: PageElements.qaweb_main_url(page))
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_scrap(page),
                           check=True)

@pytest.mark.regression
def test_comm_service_00058(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_058 : 칩카루셀 상품 디테일 구성 요소 확인")
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: PageElements.qaweb_main_url(page))
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_carousel_detail(page),
                           check=True)


# def test_comm_service_00058(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_comm_service_058 : 상품 디테일 구성 요소 확인 Case 시작")
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)

#         # 쇼핑홈 > 인기상품 구좌까지 스크롤 > 필터 리뷰많은 순 변경 > 첫번째 상품 > 상품제목 확인 및 상품 상세 노출 확인
#             # 상품 디테일 진입반복 케이스
#         web_exceptions_handler(page, current_function_name, step=lambda: CommServiceIntopdp(page).auto_pdp_into(page))

        
#         # 상품상세 진입 확인 후 각 요소 노출 확인
#         # 상단 카테고리 노출 확인 링크 동작 확인 후 되돌아 오기

#         expect(page.get_by_text("패브릭카페트/러그러그"), '상단 카테고리 비노출').to_be_visible()
#         print(" - Pass")
#         print("test_comm_service_058 : 상단 카테고리 노출 확인 후 되돌아 오기", end='')
#         page.get_by_role("link", name="러그", exact=True).click()
#         page.wait_for_timeout(500)
#         expect(page.get_by_role("heading", name="패브릭"), '최상위 카테고리 노출 확인').to_be_visible()
#         expect(page.locator("section").get_by_role("link", name="러그", exact=True), '현재 카테고리 노출 확인').to_be_visible()
#         expect(page.get_by_text("패브릭카페트/러그러그"), '카테고리 경로 확인').to_be_visible()
#         # 상품 디테일 진입반복 케이스
#         web_exceptions_handler(page, current_function_name,step=lambda: CommServiceIntopdp(page).auto_pdp_into(page))


#         #대표이미지 및 좌측 썸네일 노출 확인
#         print("test_comm_service_058 : 대표이미지 및 좌측 썸네일 노출 확인", end='')
#         expect(page.get_by_label("3개 중 1번째 항목"), '대표 이미지 썸네일 노출').to_be_visible()
#         expect(page.get_by_label("1 of 3").get_by_role("img", name="상품의 대표 이미지"), '대표 이미지 노출').to_be_visible()
#         expect(page.get_by_label("3개 중 2번째 항목"), '서브 이미지1 썸네일 노출').to_be_visible()
#         page.get_by_label("3개 중 2번째 항목").click()
#         expect(page.get_by_label("2 of 3").get_by_role("img", name="상품의 서브 이미지"), '서브 이미지1 노출').to_be_visible()
#         expect(page.get_by_label("3개 중 3번째 항목"), '서브 이미지2 썸네일 노출').to_be_visible()
#         page.get_by_label("3개 중 3번째 항목").click()
#         expect(page.get_by_label("3 of 3").get_by_role("img", name="상품의 서브 이미지"), '서브 이미지2 노출').to_be_visible()
#         print(" - Pass")

#         # 우측 상단 - 상단 브랜드 링크 동작 확인 후 되돌아 오기
#         print("test_comm_service_058 : 상단 브랜드 링크 동작 확인 후 되돌아 오기 동작 확인", end='')        
#         page.get_by_role("link", name="바이빔", exact=True).click()
#         expect(page.get_by_role("link", name="바이빔", exact=True), '브랜드홈 노출 확인').to_be_visible()
#         expect(  page.locator("li").filter(has_text="가구").first, '카테고리 가구 노출 확인').to_be_visible()
#         print(" - Pass")
#             # 상품 디테일 진입반복 케이스
#         web_exceptions_handler(page, current_function_name,step=lambda: CommServiceIntopdp(page).auto_pdp_into(page))

#         #우측 상단 리뷰 선택 시 스크롤 점프 동작 후 최상단 재이동
#         print("test_comm_service_058 : 우측 상단 리뷰 선택 시 스크롤 점프 동작 후 최상단 재이동", end='')        
#         page.get_by_role("link", name="별점 4.7점 33,667 개 리뷰").click()
#         expect(page.get_by_text("리뷰 33,667리뷰쓰기"), '우측 상단 리뷰 선택 시 스크롤 점프 동작 안됨').to_be_visible()
#             # 상품 디테일 진입반복 케이스
#         page.get_by_role("button", name="").nth(1).click()
#         expect(page.get_by_text("리뷰 33,667리뷰쓰기"), '최상단 이동 버튼 동작 안됨').to_be_visible()

#         #우측 상단 - 요소 노출 확인 - 상품명 노출 확인
#         print("test_comm_service_058 : 우측 상단 요소 노출 확인 - 상품명 노출 확인", end='')        
#         expect(page.get_by_text("선데이 러그 7size 4colors"), '상품명 노출 되지 않습니다.').to_be_visible()
#         print(" - Pass")

#         #우측 상단 - 스크랩 동작        
#         print("test_comm_service_058 : 우측 상단 스크랩 동작", end='')        
#         page.get_by_role("button", name="스크랩 66,618").click()
#         page.wait_for_timeout(500)
#         expect(page.get_by_text("스크랩했습니다."), '스크랩 되지 않았습니다.').to_be_visible()
#         page.get_by_role("button", name="스크랩 66,619").click()
#         expect(page.get_by_text("스크랩북에서 삭제했습니다."), '스크랩 삭제 되지 않았습니다.').to_be_visible()
#         print(" - Pass")

#         #우측 상단 - 공유하기 동작
#         print("test_comm_service_058 : 우측 상단 공유하기 동작", end='')        
#         page.get_by_role("button", name="공유하기").click()
#         page.get_by_role("button", name="주소 복사").click()
#         page.once("dialog", lambda dialog: dialog.dismiss())
#         with page.expect_popup() as page1_info:
#             page.get_by_role("button", name="카카오톡 공유").click()
#         page1 = page1_info.value
#         page.wait_for_timeout(500)
#         expect(page1.get_by_role("heading", name="Kakao").locator("span").first, '카카오톡 공유 확인 되지 않습니다.').to_be_visible()
#         page1.close()
#         page.get_by_role("button", name="공유하기").click()
#         print(" - Pass")

#         ''' information 버튼을 찾지 못하는 이슈 해결 필요.
#         #우측 상단 - 가격 관련 information 노출 확인 
#         print("test_comm_service_058 : 우측 상단 - 가격 관련 information 노출 확인", end='')        
#         page.locator("span").filter(has_text="4%350,000원333,331원받은 쿠폰 보기").get_by_role("button").first.click()
#         expect(page.get_by_text("상품 등록일을 기준으로 판매자가 제공하는 권장소비자 가격(도서등인 경우 정가) 또는 기타 온라인 채널 판매 가격 등으로, 할인 기준이 되는 가격"), '가격 관련 information 비노출 됨').to_be_visible()
#         page.locator("span").filter(has_text="4%350,000원상품 등록일을 기준으로 판매자가 제공하는 권장소비자 가격(도서등인 경우 정가) 또는 기타 온라인 채널 판매 가격 등으로, 할인").get_by_role("button").first.click()
#         print(" - Pass")
#         '''

#         #우측 상단 - 가격 노출 동작 확인
#         print("test_comm_service_058 : 우측 상단 가격 노출 확인", end='')        
#         expect(page.get_by_text("4%"), '할인비율 비노출').to_be_visible()
#         expect(page.get_by_text("350,000"), '판매가 비출').to_be_visible()
#         expect(page.get_by_role("deletion").get_by_text("원"), '화폐단위 비노출 ').to_be_visible()
#         expect(page.get_by_text("333,331", exact=True), '쿠폰가 비노출').to_be_visible()
#         expect(page.get_by_text("원", exact=True).nth(1), '화폐단위 비노출').to_be_visible()
#         print(" - Pass")

#         #우측상단 - 뱃지 노출 확인(특가, 오늘출발)
#         print("test_comm_service_058 : 우측 상단 뱃지 노출 확인", end='')        
#         expect(page.get_by_label("특가").locator("rect"), '특가 뱃지 비노출').to_be_visible()
#         expect(page.locator("span").filter(has_text="4%350,000원333,331원받은 쿠폰 보기").locator("img"), '오늘출발 뱃지 비노출').to_be_visible() #- 받을 쿠폰이 없는 경우에 한하기 때문에 받을 쿠폰이 있는경우에 대한 분기 처리 필요)
#         print(" - Pass")

#         ''' 
#         #우측상단 - 쿠폰받기 동작 확인 쿠폰받기가 있을때에만 동작하도록 분기 처리 필요
#         page.get_by_text("쿠폰가에서 10% 더 할인돼요!0원 이상 결제시 장바구니 쿠폰 적용 가능").click()
#         page.get_by_role("button", name="쿠폰 받기 ").click()
#         page.get_by_test_id("bds-dim").get_by_text("받은 쿠폰").click()
#         page.get_by_role("button", name="확인").click()        
#         '''

#         # 우측상단 - 받은 쿠폰 보기 동작 확인
#         print("test_comm_service_058 : 받은 쿠폰 보기 동작 확인", end='')        
#         page.get_by_role("button", name="받은 쿠폰 보기 ").click()
#         expect(page.locator("div").filter(has_text=re.compile(r"^받은 쿠폰$")), '받은 쿠폰 목록 비노출').to_be_visible()
#         page.get_by_role("button", name="확인").click()
#         print(" - Pass")

#         # 우측상단 - 쿠폰 할인 안내 문구 노출 확인
#         print("test_comm_service_058 : 쿠폰 할인 안내 문구 노출 확인", end='')
#         expect(page.get_by_text("여기서 10% 더 할인돼요!0원 이상 결제시 장바구니 쿠폰 적용 가능"), '받은 쿠폰 목록 비노출').to_be_visible()
#         print(" - Pass")

#         # 우측상단 - 혜택 구좌  노출 확인
#         print("test_comm_service_058 : 혜택 - 적립액  노출 확인", end='')
#         expect(page.get_by_text("혜택"), '혜택 항목 비노출').to_be_visible()
#         expect(page.get_by_text("334P 적립 (WELCOME 0.1% 적립)"), '혜택내용 비노출').to_be_visible()
#         expect(page.get_by_text("334P 적립 (WELCOME 0.1% 적립)"), '최대 결제 할인율 비노출').to_be_visible()
#         page.get_by_role("button", name="최대 10% 결제할인 (씨티)").click()
#         page.wait_for_timeout(500)
#         expect(page.get_by_text("결제 혜택"), '결제 해택 팝업 비노출').to_be_visible()
#         page.get_by_label("닫기").nth(1).click()
#         expect(page.locator("p").filter(has_text="월 41,666원 (8개월) 무이자할부"), '결제 해택 팝업 비노출').to_be_visible()
#         page.get_by_role("button", name="월 41,666원 (8개월) 무이자할부").click()
#         page.wait_for_timeout(500)
#         expect(page.get_by_text("무이자 할부 안내"), '결제 해택 팝업 비노출').to_be_visible()
#         page.get_by_label("닫기").nth(1).click()
#         print(" - Pass")

#         # 우측상단 - 배송 구좌 노출 확인
#         print("test_comm_service_058 : 배송 구좌 노출 확인", end='')
#         page.locator("div").filter(has_text=re.compile(r"^배송$")).scroll_into_view_if_needed()
#         expect(page.locator("div").filter(has_text=re.compile(r"^배송$")), '받은 쿠폰 목록 비노출').to_be_visible()
#         expect(page.locator("b").filter(has_text="무료배송"), '무료배송 문구 노출').to_be_visible()
#         expect(page.locator("span").filter(has_text="일반택배").first, '배송유형 비노출').to_be_visible()
#         expect(page.locator("span").filter(has_text="제주도/도서산간 지역 6,000원").first, '배송비 비노출').to_be_visible()
#         print(" - Pass")

#         #우측상단 - 브랜드홈 구좌 노출 확인
#         print("test_comm_service_058 : 브랜드홈 구좌 노출 확인", end='')
#         page.get_by_role("link", name="바이빔 브랜드홈").scroll_into_view_if_needed()
#         expect(page.get_by_role("link", name="바이빔 브랜드홈"), '브랜드홈 구좌 비노출').to_be_visible()
#         page.get_by_role("link", name="바이빔 브랜드홈").click()
#         expect(page.get_by_role("link", name="바이빔", exact=True), '브랜드홈 노출 확인').to_be_visible()
#         expect(  page.locator("li").filter(has_text="가구").first, '카테고리 가구 노출 확인').to_be_visible()
#         print(" - Pass")
#             # 상품 디테일 진입반복 케이스
#         web_exceptions_handler(page, current_function_name,step=lambda: CommServiceIntopdp(page).auto_pdp_into(page))

#         #상품 옵션 선택 동작
#         print("test_comm_service_058 : 상품 옵션 선택 동작", end='')
#         page.get_by_role("link", name="바이빔 브랜드홈").scroll_into_view_if_needed()
#         expect(page.get_by_role("link", name="바이빔 브랜드홈"), '브랜드홈 구좌 비노출').to_be_visible()
#         page.locator(".form-control").first.select_option("0")
#         page.locator("div").filter(has_text=re.compile(r"^색상아이보리 \(333,331원\)그레이 \(16,300원\)브라운 \(16,300원\)차콜 \(16,300원\)$")).get_by_role("combobox").select_option("0")
#         page.wait_for_timeout(500)

#         page.get_by_text("주문금액").first.scroll_into_view_if_needed()
#         expect(page.get_by_text("사이즈: [70x200]러너 / 색상: 아이보리1333,331원").first, '선택된 메인상품 비노출').to_be_visible()
#         page.wait_for_timeout(500)
#         expect(page.locator("div").filter(has_text=re.compile(r"^333,331원$")).nth(1), '메인상품 가격 노출').to_be_visible()
#         expect(page.get_by_text("주문금액333,331원").first, '주문금액 총합 비노출').to_be_visible()
#         expect(page.get_by_text("결제할 때 여기서 10% 더 할인돼요").first, '할인 안내 비노출').to_be_visible()
#         page.get_by_label("삭제").nth(1).click()
#         page.once("dialog", lambda dialog: dialog.dismiss())
#         expect(page.get_by_text("주문금액0원").first, '선택 상품 삭제 안됨').to_be_visible()

#         # 상품 없는 상태에서 장바구니, 바로구매 동작 확인
#         page.get_by_role("button", name="장바구니").first.click()
#         page.once("dialog", lambda dialog: dialog.dismiss())
#         page.get_by_role("button", name="바로구매").first.click()
#         page.once("dialog", lambda dialog: dialog.dismiss())


#         # 유저들의 스타일링샷 노출 및 링크 동작 후 되돌아 오기 >  스타일링샷 전체보기 > 되돌아오기
#         print("test_comm_service_058 : 유저들의 스타일링샷 노출 및 링크 동작 후 되돌아 오기 확인", end='')
#         page.locator("header").filter(has_text="유저들의 스타일링샷 24,240").scroll_into_view_if_needed()
#         expect(page.locator("header").filter(has_text="유저들의 스타일링샷 24,240"), '유저들의 스타일링샷 구좌 비노출').to_be_visible()
#         page.locator("header").filter(has_text="유저들의 스타일링샷 24,240").get_by_role("link").click()
#         expect(page.get_by_role("heading", name="선데이 러그 7size 4colors 로 꾸민 유저들의 스타일링샷"), '유저들의 스타일링샹 이동 실패').to_be_visible()
#         print(" - Pass")
#             # 상품 디테일 진입반복 케이스
#         web_exceptions_handler(page, current_function_name,step=lambda: CommServiceIntopdp(page).auto_pdp_into(page))
#         print("test_comm_service_058 : 유저들의 스타일링샷 전체보기 링크 동작 후 되돌아 오기 확인", end='')
#         page.get_by_role("link", name="스타일링샷 전체보기").scroll_into_view_if_needed()
#         page.get_by_role("link", name="스타일링샷 전체보기").click()
#         expect(page.get_by_role("heading", name="선데이 러그 7size 4colors 로 꾸민 유저들의 스타일링샷"), '유저들의 스타일링샹 이동 실패').to_be_visible()
#         print(" - Pass")
#             # 상품 디테일 진입반복 케이스
#         web_exceptions_handler(page, current_function_name,step=lambda: CommServiceIntopdp(page).auto_pdp_into(page))

#         # 상품정보 구좌 노출 확인
#         print("test_comm_service_058 : 유저들의 스타일링샷 노출 및 링크 동작 후 되돌아 오기 확인", end='')
#         page.get_by_role("heading", name="상품정보").scroll_into_view_if_needed()
#         expect(page.locator("center:nth-child(7) > img"), '상품 정보 이미지 노출 확인.').to_be_visible()
#         print(" - Pass")
 
#         # 리뷰 구좌 노출 확인 > 리뷰 쓰기 노출 및 닫기
#         print("test_comm_service_058 : 리뷰 구좌 노출 확인", end='')
#         page.get_by_role("button", name="리뷰쓰기").scroll_into_view_if_needed()
#         expect(page.get_by_text("리뷰 33,667리뷰쓰기"), '리뷰 구좌 노출 확인.').to_be_visible()
#         page.get_by_role("button", name="리뷰쓰기").click()
#         expect(page.get_by_text("리뷰 쓰기"), '리뷰 쓰기 팝업 노출 확인').to_be_visible()
#         page.locator("div").filter(has_text=re.compile(r"^리뷰 쓰기$")).get_by_role("button").click()
#         page.get_by_role("button", name="나가기").click()
#         print(" - Pass")

#         # 문의 구좌 노출 확인 > 문의 쓰기 노출 및 닫기
#         print("test_comm_service_058 : 리뷰 구좌 노출 확인", end='')
#         page.get_by_role("button", name="문의하기").scroll_into_view_if_needed()
#         expect(page.get_by_text("문의 2,411문의하기"), '문의 구좌 노출 확인.').to_be_visible()
#         page.get_by_role("button", name="문의하기").click()
#         expect(page.get_by_text("상품 문의하기"), '상품문의하기 팝업 노출 확인').to_be_visible()
#         page.locator(".product-question__wrap__close").click()
#         page.get_by_role("button", name="나가기").click()
#         print(" - Pass")

#         # 배송 구좌 노출 확인 
#         print("test_comm_service_058 : 배송 구좌 노출 확인", end='')
#         page.locator("header").filter(has_text="배송").scroll_into_view_if_needed()
#         expect(page.get_by_role("cell", name="배송", exact=True), '배송 항목 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="일반택배"), '배송 항목 값 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="배송비", exact=True), '배송비 항목 비노출 ').to_be_visible()
#         expect(page.get_by_role("cell", name="무료배송"), '배송비 값 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="도서산간 추가 배송비"), '도서산간 추가 배송비 항목 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="6,000원"), '도서산간 추가 배송비 값 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="배송불가 지역", exact=True), '배송불가 지역 항목 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="배송불가 지역이 없습니다."), '배송불가 지역 항목 값 비노출').to_be_visible()
#         print(" - Pass")

#         # 교환 환불 안내 구좌 노출 확인
#         print("test_comm_service_058 : 교환 환불 안내 구좌 노출 확인", end='')
#         page.locator("header").filter(has_text="교환/환불").scroll_into_view_if_needed()
#         expect(page.get_by_role("cell", name="반품배송비"), '반품비배송비 항목 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="4,000원 (최초 배송비가 무료인 경우 8,000원 부과)"), '반품배송비 내용 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="교환배송비"), '교환배송비 항목 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="8,000원", exact=True), '교환배송비 내용 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="보내실 곳"), '보내실곳 항목 비노출').to_be_visible()
#         expect(page.locator("header").filter(has_text="교환/환불"), '보내실곳 내용 비노출').to_be_visible()
#         print(" - Pass")

#         # 반품/교환사유에 따른 요청기간 구좌 노출 확인
#         print("test_comm_service_058 : 반품 교환 사유에 따른 요청 기간구좌 노출 확인", end='')
#         page.get_by_role("heading", name="반품/교환 사유에 따른 요청 가능 기간").scroll_into_view_if_needed()
#         expect(page.get_by_text("반품 시 먼저 판매자와 연락하셔서 반품사유, 택배사, 배송비, 반품지 주소 등을 협의하신 후 반품상품을 발송해 주시기 바랍니다."), '안내 미노출').to_be_visible()
#         expect(page.get_by_text("구매자 단순 변심은 상품 수령 후 7일 이내 (구매자 반품배송비 부담)"), '1번 항목 비노출').to_be_visible()
#         expect(page.get_by_text("표시/광고와 상이, 계약내용과 다르게 이행된 경우 상품 수령 후 3개월 이내, 그 사실을 안 날 또는 알 수 있었던 날로부터 30일 이내.둘 중"), '2번 항목 비노출').to_be_visible()
#         print(" - Pass")

#         # 반품/교환 불가능 사유 구좌 노출 확인
#         print("test_comm_service_058 : 반품/교환 불가능 사유 구좌 노출 확인", end='')
#         page.get_by_role("heading", name="반품/교환 불가능 사유").scroll_into_view_if_needed()
#         expect(page.get_by_text("아래와 같은 경우 반품/교환이 불가능합니다."), '반품 불가사유 안내').to_be_visible()
#         expect(page.get_by_text("반품요청기간이 지난 경우"), '반품 불가 1번 항목 비노출').to_be_visible()
#         expect(page.get_by_text("구매자의 책임 있는 사유로 상품 등이 멸실 또는 훼손된 경우 (단, 상품의 내용을 확인하기 위하여 포장 등을 훼손한 경우는 제외)"), '반품 불가 2번 항목 비노출').to_be_visible()
#         expect(page.get_by_text("포장을 개봉하였으나 포장이 훼손되어 상품가치가 현저히 상실된 경우 (예: 식품, 화장품)"), '반품 불가 3번 항목 비노출').to_be_visible()
#         expect(page.get_by_text("구매자의 사용 또는 일부 소비에 의하여 상품의 가치가 현저히 감소한 경우 (라벨이 떨어진 의류 또는 태그가 떨어진 명품관 상품인 경우)"), '반품 불가 4번 항목 비노출').to_be_visible()
#         expect(page.get_by_text("시간의 경과에 의하여 재판매가 곤란할 정도로 상품 등의 가치가 현저히 감소한 경우 (예: 식품, 화장품)"), '반품 불가 5번 항목 비노출').to_be_visible()
#         expect(page.get_by_text("고객주문 확인 후 상품제작에 들어가는 주문제작상품"), '반품 불가 6번 항목 비노출').to_be_visible()
#         expect(page.get_by_text("복제가 가능한 상품 등의 포장을 훼손한 경우 (CD/DVD/GAME/도서의 경우 포장 개봉 시)"), '반품 불가 7번 항목 비노출').to_be_visible()
#         print(" - Pass")

#         # 판매자저옵 구좌 노출 확인
#         print("test_comm_service_058 : 반품/교환 불가능 사유 구좌 노출 확인", end='')
#         page.get_by_role("heading", name="판매자 정보").scroll_into_view_if_needed()
#         expect(page.get_by_role("cell", name="상호"), '상호 항목 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="(A) (퇴점중)주식회사 바이빔"), '상호 항목 내용 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="대표자"), '대표자 항목 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="우민성"), '대표자 항목 내용 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="사업장소재지"), '사업장소재지 항목 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="서울 서초구 서운로 34 5층"), '사업장 소재지 항목 내용 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="고객센터 전화번호"), '고객센터 전화번호 항목 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="000-0000-0000"), '고객센터 전화번호 항목 내용 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="E-mail"), '이메일 항목 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="qa@bucketplace.org"), '이메일 항목 내용 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="사업자 등록번호"), '사업자 등록번호 항목 비노출').to_be_visible()
#         expect(page.get_by_role("cell", name="204-86-10012"), '사업자 등록번호 항목내용 비노출').to_be_visible()
#         print(" - Pass")
#         ResultWeb().write_result(current_function_name, f'*Pass*')
#     except AssertionError as e:
#         print(" - Fail", end='')
#         print(f"\nCaught an AssertionError: {e}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
#     except TimeoutError as e1:
#         print(" - Fail", end='')
#         print(f"\nCaught an TimeoutError: {e1}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
#     except Exception as e2:
#         print(" - Fail", end='')
#         print(f"\nCaught an unknown error: {e2}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')

@pytest.mark.smoke
def test_comm_service_00060(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_060 : 쿠폰 적용가 확인", end='')
    PageElements.qaweb_product_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_coupon_price(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00062(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_product_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_accept_coupon(page),
                           check=True)

@pytest.mark.smoke
def test_comm_service_00065(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_065 : 장바구니 쿠폰정보 확인", end='')
    PageElements.qaweb_product_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_cart_coupon(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00071(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_071 : 스크랩 On/Off 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_scrap_onoff(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_comm_service_00075(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_075 : 리뷰 작성 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_review_write(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00087(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_087 : 유저들의 스타일링샷 확인", end='')
    PageElements.qaweb_stylingshot_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_styling_shot(page),
                           check=True)
    print(" - Pass")


@pytest.mark.smoke
def test_comm_service_00099(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_099 : 리뷰 상세 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_review_detail(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00128(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_128 : 모음전 상품 설명 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_collection_product(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00129(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_129 : 모음전 상품 자세히 보기 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_collection_detail(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_comm_service_00130(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_collection_option(page),
                           check=True)

@pytest.mark.regression
def test_comm_service_00133(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_collection_banner(page),
                           check=True)


@pytest.mark.smoke
def test_comm_service_00138(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_138 : 퀵메뉴 > 실시간 베스트 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_realtime_best(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_comm_service_00139(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_139 : 쇼핑 > 실시간 베스트 > 상품 상세 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_product_detail(page),
                           check=True)
    print(" - Pass")

def test_comm_service_00141(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_141 : 쇼핑 > 역대 베스트 > 탭 이동 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_best_ranks(page),
                           check=True)
    print(" - Pass")

def test_comm_service_00142(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_142 : 쇼핑 > 역대 베스트 > 상품 상세 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_bestranks_detail(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00147(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_147 : 퀵메뉴 > 오늘의딜 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_quick_todaydeal(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00149(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_149 : 퀵메뉴 > 기획전 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_quick_exhibition(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_comm_service_00151(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_151 : 기획전 > 기획전상세 > PDP 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_exhibitions_detail(page),
                           check=True)
    print(" - Pass")


# def test_comm_service_00151(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_comm_service_151 : 기획전 > 기획전상세 > PDP 진입 확인", end='')
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         page.get_by_role("link", name="쇼핑", exact=True).click()
#         page.get_by_role("link", name="기획전상세").click()
#         # API Response check
#         api_url = 'https://image.ohou.se/i/bucketplace-v2-development/uploads/exhibitions/cover_image/170718677717131123.jpg?gif=1&w=1024&h=594&c=c'
#         response = send_api_get(api_url)
#         assert response.status_code == 200
#         # response_data = response.json()
#         # assert 'specific_field' in data
#         # 콘텐츠 영역 좌측 헤더 '기본기능 신기획전' 텍스트 확인
#         # page.get_by_text("기본기능 신기획전").click()
#         # 콘텐츠 영역 우측 부제목 '기본기능 기획전' 텍스트 확인
#         # expect(page.get_by_role("heading", name="기본기능 기획전"), '기획전 미노출').to_be_visible()
#         page.locator("div").filter(has_text=re.compile(r"^선착순할인네이처하이크\[해외\] 키친툴 주방 파우치36% 10,100$")).scroll_into_view_if_needed()
#         page.wait_for_timeout(500)
#         page.locator("article").filter(has_text="선착순할인네이처하이크[해외] 키친툴 주방 파우치36% 10,100").get_by_role("link").click()
#         page.wait_for_timeout(500)
#         expect(page.get_by_text("[해외] 키친툴 주방 파우치"), 'PDP 진입 실패 비노출').not_to_be_visible
#         print(" - Pass")
#         ResultWeb().write_result(current_function_name, f'*Pass*')
#     except AssertionError as e:
#         print(" - Fail", end='')
#         print(f"\nCaught an AssertionError: {e}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
#     except TimeoutError as e1:
#         print(" - Fail", end='')
#         print(f"\nCaught an TimeoutError: {e1}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
#     except Exception as e2:
#         print(" - Fail", end='')
#         print(f"\nCaught an unknown error: {e2}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')

@pytest.mark.smoke
def test_comm_service_00152(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_152 : 프리미엄 > 카테고리 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_premium_category(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00173(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_173 : 기획전 피드 이동 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_exhibition_feed(page),
                           check=True)
    print(" - Pass")

def test_comm_service_00174(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_174 : 기획전 피드 목록 노출 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_exhibition_feed(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_comm_service_00175(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("test_comm_service_175 : 기획전 상세 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_exhibition_detail(page),
                           check=True)
    print(" - Pass")


# def test_comm_service_00187(page):
#     current_function_name = ProviderFunctionName().get_current_function_name()
#     try:
#         print("test_comm_service_187 : 카테고리 필터 동작 확인")
#         PageElements.qaweb_main_url(page)
#         CommonElements.login_func(page)
#         # 카테고리 진입 > 필터 구좌 노출 확인
#         print("test_comm_service_187 : 반품/교환 불가능 사유 구좌 노출 확인")
#         web_exceptions_handler(page, current_function_name,step=lambda: CommServiceCategory(page).auto_category_furniture_filter(page))
#         # 필터 검색 결과 없음을 확인
#         expect(page.get_by_text("필터 검색 결과가 없습니다.다른 필터로 검색해보세요."), '필터 검색 결과 없음 안내 비노출').to_be_visible()
#         #선택된 칩 선택 해제
#         page.get_by_role("button", name="빠른가구배송").nth(1).click()
#         page.get_by_role("button", name="50,000원 이하").first.click()
#         page.get_by_role("button", name="SE0").click()
#         page.get_by_role("button", name="오크(참나무)").click()
#         page.get_by_role("button", name="홈카페용 식탁").click()
#         page.get_by_role("button", name="특가상품 보기").click()
#         page.get_by_role("button", name="해외직구 제외").click()
#         page.get_by_role("button", name="밝은 톤").click()
#         page.get_by_role("button", name="한샘").click()
#         page.get_by_role("button", name="화이트").click()
#         page.get_by_role("button", name="원목", exact=True).click()
#         page.get_by_role("button", name="1인").click()

#         #필터 칩 목록 내 초기화 동작 확인
#         web_exceptions_handler(page, current_function_name,step=lambda: CommServiceCategory(page).auto_category_furniture_filter(page))
#         page.get_by_role("button", name="초기화", exact=True).click()
#         expect(page.get_by_text("필터 검색 결과가 없습니다.다른 필터로 검색해보세요."), '필터 검색 결과 없음 안내 비노출').not_to_be_visible


#         #하단 필터 초기화 동작 확인
#         web_exceptions_handler(page, current_function_name,step=lambda: CommServiceCategory(page).auto_category_furniture_filter(page))
#         page.get_by_role("button", name="필터 초기화").click()
#         expect(page.get_by_text("필터 검색 결과가 없습니다.다른 필터로 검색해보세요."), '필터 검색 결과 없음 안내 비노출').not_to_be_visible

#         print(" - Pass")
#         ResultWeb().write_result(current_function_name, f'*Pass*')
#     except AssertionError as e:
#         print(" - Fail", end='')
#         print(f"\nCaught an AssertionError: {e}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e})')
#     except TimeoutError as e1:
#         print(" - Fail", end='')
#         print(f"\nCaught an TimeoutError: {e1}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e1})')
#     except Exception as e2:
#         print(" - Fail", end='')
#         print(f"\nCaught an unknown error: {e2}")
#         capture_screenshot(page, current_function_name)
#         ResultWeb().write_result(current_function_name, f'*Fail* ({e2})')

@pytest.mark.smoke
def test_comm_service_00220(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_item_carousel(page),
                           check=True)

@pytest.mark.smoke
def test_comm_service_00221(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_item_carousel(page, case='chip'),
                           check=True)

@pytest.mark.smoke
def test_comm_service_00224(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_item_carousel(page, case='product'),
                           check=True)

@pytest.mark.regression
def test_comm_service_00225(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_item_carousel_scrap(page, case='product'),
                           check=True)


@pytest.mark.smoke
def test_comm_service_00226(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_item_carousel(page, case='enter_product'),
                           check=True)

@pytest.mark.regression
def test_comm_service_00228(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_iif(page),
                           check=True)

@pytest.mark.regression
def test_comm_service_00229(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_iif_detail(page),
                           check=True)

@pytest.mark.regression
def test_comm_service_00233(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_iif_scrap(page),
                           check=True)

@pytest.mark.smoke
def test_comm_service_00243(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_item_list_card(page),
                           check=True)

@pytest.mark.regression
def test_comm_service_00244(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_item_list_card_scrap(page),
                           check=True)


@pytest.mark.smoke
def test_comm_service_00245(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_item_list_card(page, case='enter_card'),
                           check=True)

@pytest.mark.regression
def test_comm_service_00264(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_brand_home(page),
                           check=True)

@pytest.mark.regression
def test_comm_service_00265(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_brand_home_detail(page),
                           check=True)

@pytest.mark.regression
def test_comm_service_00323(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_brand_home_scrap(page),
                           check=True)

@pytest.mark.regression
def test_comm_service_00325(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_brand_home_detail_scrap(page),
                           check=True)

@pytest.mark.skip
def test_comm_service_00334(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_userpage_folder(page),
                           check=True)

@pytest.mark.skip
def test_comm_service_00335(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_userpage_brand(page),
                           check=True)

@pytest.mark.regression
def test_comm_service_00337(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommServiceElements.confirm_userpage_folder(page),
                           check=True)

