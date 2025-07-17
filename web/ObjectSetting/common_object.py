from web.BasicSetting.conftest import *
import ssl
from web.ObjectSetting.gmail import *
from playwright.sync_api import *
from app.common.base_method.exception_func import timeout_handler
from web.ObjectSetting.comm_platform import *

class PageElements():

    def qaweb_product_url(page):
        page.goto('https://qa-web.dailyhou.se/productions/563973/selling', timeout= 0)

    def qaweb_product_url_2(page):
        page.goto('https://qa-web.dailyhou.se/productions/100008379/selling', timeout= 0)

    def qaweb_product_url_3(page, product_id):
        page.goto(f'https://qa-web.dailyhou.se/productions/{product_id}/selling', timeout= 0)

    def qaweb_main_url(page):
        page.goto('https://qa-web.dailyhou.se/', timeout= 0)

    def qaweb_o2o_partners_url(page):
        page.goto('https://partner-house.qa-web.dailyhou.se/signin?redirectUrl=https://o2o-partner.qa-web.dailyhou.se', timeout= 0)

    def qaweb_stylingshot_url(page):
        page.goto('https://qa-web.dailyhou.se/productions/594835/selling', timeout= 0)   

    def qaweb_recommend_url(page):
        page.goto('https://contents.qa-web.dailyhou.se/topics/recommend', timeout= 0)
    
    def orora_url(page):
        page.goto('https://orora.qa-web.dailyhou.se/signin', timeout= 0)

    def admin_url(page):
        page.goto('https://admin-portal.qa.dailyhou.se/', timeout=0)

    def o2o_url(page):
        page.goto('https://qa-web.dailyhou.se/experts', timeout=0) 

    def o2o_partner_url(page):
        page.goto('https://qa-web.dailyhou.se/experts/myhome/12454528', timeout=0) 

    def lifestyle_curator(page):
        page.goto('https://qa-web.dailyhou.se/curator/intro', timeout=0) 

    def qaweb_glinda_url(page):
        page.goto('https://store.qa-web.dailyhou.se/packages', timeout= 0)
        page.wait_for_timeout(2000)
        elements_visible = page.get_by_role("button", name="나만의 패키지 만들기").is_visible()
        if elements_visible:
            page.get_by_role("button", name="나만의 패키지 만들기").click()



class CommonElements():
    # 로그인 하기
    def login_func(page):
        # 로그인 상태인지 체크하여 로그인/로그아웃 진행
        elements_visible = page.get_by_role("link", name="로그인").is_visible()
        if elements_visible:
            # 로그인
            page.get_by_role("link", name="로그인").click()
            page.get_by_placeholder("이메일").click()
            page.get_by_placeholder("이메일").fill("ohouseqa@gmail.com")
            page.get_by_placeholder("비밀번호").click()
            page.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
            page.get_by_role("button", name="로그인").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
        expect(page.get_by_label("프로필 메뉴"), '프로필 메뉴 요소 미노출').to_be_visible()
        # API Response check
        # api_url = 'https://qa-web.dailyhou.se/'
        # response = send_api_get(api_url)
        # assert response.status_code == 200

    def login_func_2(page):
        # common 032 탈퇴 케이스용 계정
        # 로그인 상태인지 체크하여 로그인/로그아웃 진행
        elements_visible = page.get_by_role("link", name="로그인").is_visible()
        if elements_visible:
            # 로그인
            page.get_by_role("link", name="로그인").click()
            page.get_by_placeholder("이메일").click()
            page.get_by_placeholder("이메일").fill("ohouseqaqa@gmail.com")
            page.get_by_placeholder("비밀번호").click()
            page.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
            page.get_by_role("button", name="로그인").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
        expect(page.get_by_label("프로필 메뉴"), '프로필 메뉴 요소 미노출').to_be_visible()
        

    def login_naver_func(page):
        # 네이버 로그인 계정
        # 로그인 상태인지 체크하여 로그인/로그아웃 진행
        page.get_by_role("link", name="로그인").click()
        # 네이버 SNS 클릭
        page.locator("section").filter(has_text="SNS계정으로 간편 로그인/회원가입").get_by_role("link").nth(2).click()
        elements_visible = page.get_by_label("아이디 또는 전화번호")
        if elements_visible:
            # 로그인
            page.get_by_label("아이디 또는 전화번호").click()
            page.get_by_label("아이디 또는 전화번호").fill("gswebqa")
            page.get_by_label("비밀번호").click()
            page.get_by_label("비밀번호").fill("qaqaqa1!")
            page.get_by_role("button", name="로그인", exact=True).click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
        expect(page.get_by_label("프로필 메뉴"), '프로필 메뉴 요소 미노출').to_be_visible()
        # expect(page.get_by_role("link", name="추천"), 'GNB 메뉴 요소 미노출').to_be_visible()
        # API Response check
        # api_url = 'https://qa-web.dailyhou.se/'
        # response = send_api_get(api_url)
        # assert response.status_code == 200

    def login_facebook_func(page):
        # 페이스북 로그인 계정
        # 로그인 상태인지 체크하여 로그인/로그아웃 진행
        page.get_by_role("link", name="로그인").click()
        page.locator("section").filter(has_text="SNS계정으로 간편 로그인/회원가입").get_by_role("link").first.click()
        page.wait_for_timeout(2000)
        elements_visible = page.get_by_placeholder("이메일 또는 전화번호").is_visible()
        if elements_visible:
            # 로그인
            page.get_by_placeholder("이메일 또는 전화번호").click()
            page.get_by_placeholder("이메일 또는 전화번호").fill("qabucketfacebook@gmail.com")
            page.get_by_placeholder("비밀번호").click()
            page.get_by_placeholder("비밀번호").fill("Qjznlt12!@")
            page.get_by_role("button", name="로그인").click()
            page.wait_for_timeout(5000)
            page.get_by_label("집님으로 계속").click()
            page.wait_for_timeout(2000)
        else:
            page.get_by_label("집님으로 계속").click()
            page.wait_for_timeout(1000)
        expect(page.get_by_label("프로필 메뉴"), '프로필 메뉴 요소 미노출').to_be_visible()
        expect(page.get_by_role("link", name="추천"), 'GNB 메뉴 요소 미노출').to_be_visible()
        # API Response check
        # api_url = 'https://qa-web.dailyhou.se/'
        # response = send_api_get(api_url)
        # assert response.status_code == 200

    def logout_facebook_func(page):
        # 페이스북 로그인 계정
        # 로그인 상태인지 체크하여 로그인/로그아웃 진행
        page.get_by_role("link", name="로그인").click()
        page.locator("section").filter(has_text="SNS계정으로 간편 로그인/회원가입").get_by_role("link").first.click()
        page.wait_for_timeout(2000)
        elements_visible = page.get_by_placeholder("이메일 또는 전화번호").is_visible()
        if elements_visible:
            # 로그인
            page.get_by_placeholder("이메일 또는 전화번호").click()
            page.get_by_placeholder("이메일 또는 전화번호").fill("qabucketfacebook@gmail.com")
            page.get_by_placeholder("비밀번호").click()
            page.get_by_placeholder("비밀번호").fill("Qjznlt12!@")
            page.get_by_role("button", name="로그인").click()
            page.wait_for_timeout(5000)
            page.get_by_label("집님으로 계속").click()
            page.wait_for_timeout(5000)
        else:
            page.get_by_label("집님으로 계속").click()
            page.wait_for_timeout(5000)
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click()
        expect(page.get_by_role("link", name="로그인"), '로그인 메뉴 요소 미노출').to_be_visible()


    def login_payment_func(page,id,pw):
        # payment 전용 로그인 계정
        # 로그인 상태인지 체크하여 로그인/로그아웃 진행
        elements_visible = page.get_by_role("link", name="로그인").is_visible()
        if elements_visible:
            # 로그인
            page.get_by_role("link", name="로그인").click()
            page.get_by_placeholder("이메일").click()
            page.get_by_placeholder("이메일").fill(f"{id}")
            page.get_by_placeholder("비밀번호").click()
            page.get_by_placeholder("비밀번호").fill(f"{pw}")
            page.get_by_role("button", name="로그인").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(2000)


    def logout_func(page):
        # 로그인 상태인지 체크하여 로그인/로그아웃 진행
        page.get_by_label("오늘의집 로고").click()
        page.wait_for_timeout(1000)
        elements_visible = page.get_by_role("link", name="로그인").is_visible()
        if elements_visible:
            page.wait_for_timeout(1000)
        else:
            # 로그아웃
            page.get_by_label("프로필 메뉴").click()
            page.wait_for_timeout(2000)
            page.get_by_role("button", name="로그아웃").click()
            page.wait_for_timeout(1000)
        expect(page.get_by_role("link", name="로그인"), '프로필 메뉴 요소 미노출').to_be_visible()
        page.wait_for_timeout(2000)


    def login_orora_func(page):
        #오로라 전용 로그인   
        page.get_by_test_id("email").click()
        page.get_by_test_id("email").fill("test01@test.com")
        page.get_by_test_id("password").click()
        page.get_by_test_id("password").fill("qwer1234!")
        page.wait_for_timeout(2000)
        page.get_by_label("로그인 버튼").click(timeout=90000)
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="인증하기").click()
        page.get_by_test_id("verificationCode").click()
        page.get_by_test_id("verificationCode").fill("123456")
        page.get_by_role("button", name="인증하기").click()
        page.wait_for_timeout(2000)
    


    def login_admin_func(page):
        page.get_by_label("LogIn ID").click()
        page.get_by_label("LogIn ID").fill("qa1")
        page.wait_for_timeout(1000)
        page.get_by_label("Password").click()
        #변경된 비번 업데이트 
        page.get_by_label("Password").fill("12qwaszx!@")
        page.get_by_role("button", name="Log In").click()
        page.wait_for_timeout(1000)


    def into_mypage_option(page):
        # 마이페이지 > 설정 화면 진입
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("link", name="마이페이지").click()
        page.locator("li").filter(has_text="설정").get_by_role("link").click()
        expect(page.get_by_role("link", name="회원정보수정"), '회원정보수정화면 비노출').to_be_visible()
        page.wait_for_timeout(2000)

    def change_email(page, account="change"):
        # 마이페이지 > 설정 화면 진입한 상태로 시작
        # 이메일 변경하기
        email_addr = "ohouseqaqa@gmail.com" if account == "change" else "ohouseqa@gmail.com"
        page.get_by_role("button", name="이메일 변경하기").click()
        page.get_by_placeholder("이메일을 입력해 주세요.").click()
        page.get_by_placeholder("이메일을 입력해 주세요.").fill(email_addr)
        page.get_by_role("button", name="이메일 인증하기").click()
        page.wait_for_timeout(5000)
        # Gmail 인증
        auth_number = GmailWebManager(account).get_gmail_auth_number()
        page.get_by_placeholder("인증코드 6자리").click()
        page.get_by_placeholder("인증코드 6자리").fill(auth_number)
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)
        # 완료 버튼 선택 
        page.get_by_role("button", name="탈퇴하기").scroll_into_view_if_needed()
        page.get_by_role("button", name="완료").click()

    def change_email_check(page):
        # 마이페이지 > 설정 화면 진입
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("link", name="마이페이지").click()
        page.locator("li").filter(has_text="설정").get_by_role("link").click()
        page.wait_for_timeout(2000)

        # 텍스트를 추출할 요소 선택 (CSS Selector 또는 XPath)
        element = page.locator("div").filter(has_text=re.compile(r"^이메일$")).locator("div").first
        text_content = element.text_content()
        print(f"추출된 텍스트: {text_content}")


    def change_profile(page, account="change"):
         # 마이페이지 > 사진올리기
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("link", name="마이페이지").click()
        # page.get_by_role("link", name="사진", exact=True).click()
        page.locator("li").filter(has_text="설정").get_by_role("link").click()

        page.wait_for_timeout(3000)
        file_input = page.locator('input[type="file"]')
        file_path = './test_file/testlogo.png'
        file_input.set_input_files(file_path)

        page.wait_for_timeout(3000)

    def confirm_naver_logout(page):
        # 네이버 로그아웃 확인
        # 네이버 로그인 시도
        page.get_by_role("link", name="로그인").click()
        # 네이버 SNS 클릭
        page.locator("section").filter(has_text="SNS계정으로 간편 로그인/회원가입").get_by_role("link").nth(2).click()
        elements_visible = page.get_by_label("아이디 또는 전화번호")
        page.wait_for_timeout(2000)
        if elements_visible:
            # 로그인
            page.get_by_label("아이디 또는 전화번호").click()
            page.get_by_label("아이디 또는 전화번호").fill("gswebqa")
            page.get_by_label("비밀번호").click()
            page.get_by_label("비밀번호").fill("qaqaqa1!")
            page.get_by_role("button", name="로그인", exact=True).click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click()
        expect(page.get_by_role("link", name="로그인"), '로그인 메뉴 요소 미노출').to_be_visible()

    def confirm_3d_interior(page):
        # 3D 인테리어 확인
        page.get_by_role("link", name="3D인테리어").click()
        expect(page.get_by_role("button", name="3D 인테리어 하러가기"), '3D 인테리어 버튼 요소 미노출').to_be_visible()

    def confirm_code_coupon(page):
        # 마이페이지 > 코드입력형 쿠폰 등록 확인
        CommPlatformElements.checkout_2_func(page)
        page.wait_for_timeout(2000)
        # 테스트 코드형 쿠폰 등록하기
        page.get_by_role("button", name="쿠폰코드가 있으신가요? ").click()
        page.wait_for_timeout(2000)
        # expect(page.locator("section").filter(has_text=re.compile("장바구니 쿠폰.*")), '쿠폰  미노출').to_be_visible()
        page.locator("section").filter(has_text=re.compile("장바구니 쿠폰.*")).get_by_role("textbox").click()
        page.wait_for_timeout(1000)
        page.locator("section").filter(has_text=re.compile("장바구니 쿠폰.*")).get_by_role("textbox").fill("qwer1234")
        page.wait_for_timeout(1000)
        # page.locator("section").filter(has_text="장바구니 쿠폰50,000원 할인장바구니 쿠폰 조건 테스트 21만원 이상 구매시41일 남음1장30,000원 할인[JWT 확인용] 정액 30000원").get_by_role("textbox").fill("qwer1234")
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(1000)
        expect(page.get_by_text("장바구니 쿠폰-500원", exact=True), '쿠폰 적용 금액 미노출').to_be_visible()
        
    def confirm_point_detail(page):
        # 마이페이지 > 포인트 상세 확인
        # 마이페이지 - 포인트 조회
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("link", name="마이페이지").click()
        page.get_by_role("link", name="나의 쇼핑").click()
        page.get_by_role("link", name="포인트", exact=True).click()
        expect(page.get_by_role("heading", name="사용 가능한 포인트"), '사용가능한 포인트 요소 미노출').to_be_visible()
        # 로그아웃 시도 (초기화)
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click()
        expect(page.get_by_role("link", name="로그인"), '로그인 페이지 미노출').to_be_visible()

    def confirm_point_detail(page):
        # 마이페이지 > 로그아웃 동작 확인
        # 로그아웃 시도
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click()
        page.wait_for_timeout(2000)
        expect(page.get_by_role("link", name="로그인"), '로그인 페이지 미노출').to_be_visible()

    def confirm_mypage_logout(page):
        # 마이페이지 > 설정 화면 진입
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click()
        page.wait_for_timeout(2000)
        expect(page.get_by_role("link", name="로그인"), '프로필 메뉴 요소 미노출').to_be_visible()

    def confirm_cookie_delete(page):
        page.goto("https://facebook.com")
        cookies = page.context.cookies()
        # 쿠키 삭제
        page.context.clear_cookies()
        # 로컬 스토리지와 세션 스토리지 삭제
        page.evaluate("window.localStorage.clear();")
        page.evaluate("window.sessionStorage.clear();")

        cookies_after_deletion = page.context.cookies()
        # 쿠키삭제 확인
        assert len(cookies_after_deletion) == 0, "Failed to delete all facebook.com cookies"

    def confirm_guest_order(page):
        page.get_by_role("link", name="로그인", exact=True).click()
        page.get_by_role("button", name="비회원 주문 조회하기").click()
        page.get_by_placeholder("주문번호").click()
        page.get_by_placeholder("주문번호").fill("50024432")
        page.locator("form").filter(has_text="주문조회").get_by_placeholder("이메일").click()
        page.locator("form").filter(has_text="주문조회").get_by_placeholder("이메일").fill("ohouseqa@gmail.com")
        page.get_by_role("button", name="주문조회").click()
        page.wait_for_timeout(1000)
        
        #주문상세정보 확인
        print("상품명 확인", end='')
        expect(page.get_by_role("link", name="[코튼리빙] 40수 코마사 호텔수건 200g 10장"), "메인상품옵션 누락되었습니다.").to_be_visible
        print(" - Pass2")
        print("메인상품 누락 체크", end='')
        expect(page.get_by_text("화이트 10장"), "메인상품옵션 누락되었습니다.").to_be_visible()
        print(" - Pass")
        print("추가 상품 누락 체크 ", end='')
        expect(page.get_by_text("추가상품 - 1매케이스"), "추가 상품 옵션 누락 되었습니다.").to_be_visible()
        print(" - Pass")
        print("조립비 누락 체크", end='')
        expect(page.get_by_text("- 조립/설치신청 5,000원"), "조립비 누락되었습니다.").to_be_visible()
        print(" - Pass")

        #배송지 정보 확인
        page.get_by_text("배송지 정보").scroll_into_view_if_needed()
        print("배송지 정보 누락 체크", end='')
        expect(page.get_by_text("배송지 정보"), "배송지 정보 없습니다.").to_be_visible()
        print(" - Pass")
        print("받는사람 누락 체크", end='')
        expect(page.get_by_text("받는 사람q****o"), "받는사람 항목 비노출").to_be_visible()
        print(" - Pass")
        print("받는사람 연락처 누락 체크", end='')
        expect(page.get_by_text("연락처010-****-9186").first, "연락치 항목 비노출").to_be_visible()
        print(" - Pass")
        print("주소 누락 체크", end='')
        expect(page.get_by_text("주소(06620) 서울특별시 서초구 서초대로74길 ******"), "주소 항목 비노출").to_be_visible()
        print(" - Pass")
        print("배송메모 연락처 누락 체크", end='')
        expect(page.get_by_text("배송메모"), "배송메모 항목 비노출").to_be_visible()
        print(" - Pass")

        expect(page.get_by_text("부재시 문앞에 놓아주세요"), "배송메모 정보 비노출 혹은 잘못 노출 ").to_be_visible()

        #가상계좌정보 확인(무통장입금 형태)
        page.get_by_text("가상계좌정보").scroll_into_view_if_needed()
        print("가상계좌정보 구좌 누락 체크", end='')
        expect(page.get_by_text("가상계좌정보"), "가상계좌정보 없습니다.").to_be_visible()
        print(" - Pass")
        # print("은행명 누락 체크", end='')
        # expect(page.get_by_text("은행명기업은행"), "은행명 항목 비노출").to_be_visible()
        # print(" - Pass")
        # print("계좌번호 누락 체크", end='')
        # expect(page.get_by_text("계좌번호X8011953697104"), "계좌번호 항목 비노출").to_be_visible()
        # print(" - Pass")
        # print("예금주 누락 체크", end='')
        # expect(page.get_by_text("예금주주식회사 버킷플레이스"), "예금주 항목 비노출").to_be_visible()
        # print(" - Pass")
        # print("입금금액 누락 체크", end='')
        # expect(page.get_by_text("입금금액33,750원"), "입금금액 항목 비노출").to_be_visible()
        # print(" - Pass")
        # print("기간 누락 체크", end='')
        # expect(page.get_by_text("기간2024-03-22 23:59 까지"), "기간 항목 비노출").to_be_visible()
        # print(" - Pass")

        #결제정보 확인(무통장입금 형태)
        page.get_by_text("결제정보").scroll_into_view_if_needed()
        print("결제정보 구좌 노출 체크", end='')
        expect(page.get_by_text("결제정보"), "결제정보 정보 없습니다.").to_be_visible()
        print(" - Pass")
        print("상품금액 항목 체크", end='')
        expect(page.get_by_text("상품금액0원"), "상품금액 항목 비노출").to_be_visible()
        print(" - Pass")
        print("주문자 항목 체크", end='')
        expect(page.get_by_text("주문자q****o"), "주문자 항목 비노출").to_be_visible()
        print(" - Pass")
        print("선불배송비 항목 체크", end='')
        expect(page.get_by_text("선불배송비(+) 0원"), "선불배송비 항목 비노출").to_be_visible()
        print(" - Pass")
        print("연락처 항목 체크", end='')
        expect(page.get_by_text("연락처010-****-9186").nth(1), "연락처 항목 비노출").to_be_visible()
        print(" - Pass")
        print("사용 포인트 항목 체크", end='')
        expect(page.get_by_text("사용 포인트(-) 0원"), "사용 포인트 항목 비노출").to_be_visible()
        print(" - Pass")
        print("이메일 항목 체크", end='')
        expect(page.get_by_text("이메일oho*****@*****.***"), "이메일 항목 비노출").to_be_visible()
        print(" - Pass")
        print("쿠폰 할인가 항목 체크", end='')
        expect(page.get_by_text("쿠폰 할인가(-) 0원"), "쿠폰 할인가 항목 비노출").to_be_visible()
        print(" - Pass")
        print("결제금액 항목 체크", end='')
        expect(page.get_by_text("결제금액0원"), "결제금액 항목 비노출").to_be_visible()
        print(" - Pass")
        print("결제방법 항목 체크", end='')
        expect(page.get_by_text("결제방법가상계좌"), "결제방법 항목 비노출").to_be_visible()

    def confirm_event_detail(page):
        # 탑바의 알림 탭 진입 > 진입 확인
        page.get_by_label("내소식 페이지 링크 버튼").click()

        page.wait_for_timeout(1000)
        print("내소식 구좌 노출 확인", end='')
        expect(page.get_by_role("heading", name="내 소식"), "첫번째 알림 내용 비노출 됩니다.").to_be_visible()
        print(" - Pass")
        print("내 소식 첫번째 아이콘 확인", end='')
        expect(page.locator(".css-1s9ngpy").first, "첫번째 알림 아이콘 비노출 됩니다.").to_be_visible
        print(" - Pass")

        # 이벤트 탭 진입 > 진입 확인
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("link", name="이벤트").click()

        page.wait_for_timeout(1000)
        print("이벤트 탭 진입 확인", end='')
        # expect(page.get_by_role("link", name="24/02/22~24/04/30 진행중"), "이벤트 탭 진입 확인이 되지 않습니다.").to_be_visible()

        # API Response check
        api_url = 'https://qa-web.dailyhou.se/competitions/feed'
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200


class AccountInfo:      
    #id
    payment_id = "platformqa_03@naver.com"        
    #pw 
    payment_pw = "qqqq1111"


