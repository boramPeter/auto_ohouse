import pytest
from web.BasicSetting.conftest import *
from web.ObjectSetting.affiliate import AffiliateElements, AffiliateCommonFunctions
from web.ObjectSetting.common_object import PageElements, CommonElements
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.exception_func import *

@pytest.mark.regression
def test_affiliate_00016(page):
    """
    마이페이지 > 활동 대시보드 버튼을 통한 활동 탭 진입 확인
    """
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 오늘의집 QA 웹 페이지 진입
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: PageElements.qaweb_main_url(page))
    # 로그인 체크 
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: CommonElements.login_func(page))
    # 마이페이지 진입 > 활동 대시보드 버튼 탭 > 페이지 진입 
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: AffiliateElements.enter_activity_dashboard_from_mypage_button1(page))
    # 활동 탭 진입 후 활동 페이지 정상 노출 확인 (각 요소값 체크) 
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: AffiliateElements.check_activity_dashboard_elements(page),
                          check=True)
    # 로그아웃
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: AffiliateCommonFunctions.logout(page))

@pytest.mark.regression
def test_affiliate_00015(page):
    """
    마이페이지 > 오감지수 버튼을 통한 활동 탭 진입 확인
    """
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 오늘의집 QA 웹 페이지 진입
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: PageElements.qaweb_main_url(page))
    # 로그인 체크 
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: CommonElements.login_func(page))
    # 마이페이지 진입 > 오감지수 버튼 탭 > 페이지 진입 
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: AffiliateElements.enter_activity_dashboard_from_mypage_button2(page))
    # 활동 탭 진입 후 활동 페이지 정상 노출 확인 (각 요소값 체크) 
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: AffiliateElements.check_activity_dashboard_elements(page),
                          check=True)
    # 로그아웃
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: AffiliateCommonFunctions.logout(page))

@pytest.mark.regression
def test_affiliate_00010(page):
    """
    콘텐츠 생성 이력이 없는 계정 > 활동 대시보드 진입 시 '첫 기록 시작' 페이지 노출 확인 
    """
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 오늘의집 QA 웹 페이지 진입
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: PageElements.qaweb_main_url(page))
    # 신규 계정으로 로그인
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: AffiliateCommonFunctions.login_new_account(page))
    # 마이페이지 진입 > 활동 대시보드 버튼 탭 > 페이지 진입 
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: AffiliateElements.enter_activity_dashboard_from_mypage_button1(page))
    # 첫 기록 시작하기 페이지에 노출되는 UI 요소 확인
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: AffiliateElements.check_first_record_page_elements(page),
                          check=True)
    # 첫 기록 시작하기 버튼 클릭 시 콘텐츠 업로드 페이지 노출 확인
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: AffiliateElements.check_first_record_page_function(page),
                          check=True)
    # 메인 페이지로 돌아가서 로그아웃
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: PageElements.qaweb_main_url(page))
    page.wait_for_timeout(2000)
    web_exceptions_handler(page, current_function_name, 
                          step=lambda: AffiliateCommonFunctions.logout(page))
    