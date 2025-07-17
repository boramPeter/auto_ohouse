from web.BasicSetting.conftest import *
from playwright.sync_api import expect
from web.ObjectSetting.comm_service import *
from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.common_object import *


class AffiliateElements():
    
    # 1-1. 마이페이지 진입 후 활동 대시보드 진입 - 활동 대시보드 버튼
    def enter_activity_dashboard_from_mypage_button1(page):
        """
        마이페이지 진입 후 활동 대시보드 진입
        """
        page.get_by_label("프로필 메뉴").click()
        page.get_by_text("마이페이지").click()
        page.get_by_text("활동 대시보드").click()
        page.wait_for_timeout(2000)
        expect(page).to_have_url("https://contents.qa-web.dailyhou.se/creator-active")

    # 1-2. 마이페이지 진입 후 활동 대시보드 진입 - 오감지수 버튼 
    def enter_activity_dashboard_from_mypage_button2(page):
        """
        마이페이지 진입 후 활동 대시보드 진입
        """
        page.get_by_label("프로필 메뉴").click()
        page.get_by_text("마이페이지").click()
        page.get_by_text("오감지수").click()
        page.wait_for_timeout(2000)
        expect(page).to_have_url("https://contents.qa-web.dailyhou.se/creator-active")

    # 2. 활동 대시보드의 활동탭에 노출되는 UI 요소 확인
    def check_activity_dashboard_elements(page):
        """
        활동 대시보드의 활동탭에 노출되는 UI 요소 확인
        """
        expect(page.get_by_role("heading", name="오감지수"), '오감지수 요소 미노출').to_be_visible()
        expect(page.get_by_role("heading", name="최근 30일 인사이트"), '최근 30일 인사이트 요소 미노출').to_be_visible()
        expect(page.get_by_role("heading", name="최근 인기 콘텐츠"), '최근 인기 콘텐츠 요소 미노출').to_be_visible()

    # 3. 첫 기록 시작하기 페이지에 노출되는 UI 요소 확인
    def check_first_record_page_elements(page):
        """
        첫 기록 시작하기 페이지에 노출되는 UI 요소 확인
        """
        expect(page.get_by_role("heading", name="첫 사진을 공유하고\n크리에이터 활동을 시작해보세요"), '첫 사진을 공유하고... heading 미노출').to_be_visible()
        expect(page.get_by_role("heading", name="크리에이터 활동 시작하기"), '크리에이터 활동 시작하기 heading 미노출').to_be_visible()
        expect(page.get_by_role("heading", name="오감지수 별 다양한 혜택 받기"), '오감지수 별 다양한 혜택 받기 heading 미노출').to_be_visible()
        expect(page.get_by_role("heading", name="내 콘텐츠 활동 분석 보기"), '내 콘텐츠 활동 분석 보기 heading 미노출').to_be_visible()
        expect(page.get_by_text("첫 기록 시작하기"), '첫 기록 시작하기 버튼 미노출').to_be_visible()
    
    # 4. 첫 기록 시작하기 페이지 기능 확인 
    def check_first_record_page_function(page):
        """
        [첫 기록 시작하기] 버튼 클릭 시 콘텐츠 업로드 페이지 노출 
        """
        page.get_by_text("첫 기록 시작하기").click()
        page.wait_for_timeout(2000)
        expect(page).to_have_url("https://qa-web.dailyhou.se/contents/card_collections/new?media=photo")       


class AffiliateCommonFunctions():
    # 1. 로그아웃
    def logout(page):
        """
        로그아웃
        """
        page.get_by_label("프로필 메뉴").click()
        page.get_by_text("로그아웃").click()
        page.wait_for_timeout(2000)

    # 2. 신규 계정으로 로그인
    def login_new_account(page, custom_email="ogam2@qqqq.qqqq", custom_password="qwer1234"):
        """
        콘텐츠 생산 이력이 없는 계정 정보로 로그인
        """
        # 신규 계정으로 로그인
        CommonElements.login_payment_func(page, custom_email, custom_password)