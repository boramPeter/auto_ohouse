from web.ObjectSetting.comm_service import *
from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.common_object import *
from web.ObjectSetting.o2o import *
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.exception_func import *
from web.BasicSetting.web_result_binary import ResultWeb


def checkout(page):
    CommonElements.login_func(page)
    page.wait_for_timeout(2000)
    CommPlatformElements.checkout_func(page)
    page.wait_for_timeout(2000)

@pytest.mark.regression
def test_o2o_00002(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_002 : 스크랩북&장바구니 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_scrap(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_o2o_00006(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_006 : 주거공간 시공 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.into_remodeling_page(page),
                           check=True)
    print(" - Pass")


@pytest.mark.skip
def test_o2o_00012(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_012 : 상업공간 시공 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.into_simple_councel(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_o2o_00025(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_025 : 신청내역 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_counsel_list(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_o2o_00026(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_026 : 신청내역 상세 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_counsel_list_detail(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_o2o_00028(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_028 : 채팅목록 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_chat_list(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_o2o_00029(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_029 : 채팅 상세 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_chat_list_detail(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_o2o_00030(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_030 : 주거시공 카테고리 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_remodeling_category(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_o2o_00050(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_050 : 우리동네 플러스 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_myvilage_plus(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_o2o_00070(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_070 : 시공업체 포트폴리오 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_portpolio(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_o2o_00072(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_072 : 시공업체 직접 상담 확인", end='')
    PageElements.o2o_partner_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_councel_remodeling(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_o2o_00181(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_181 : 추천 받으러 가기 상담 확인", end='')
    PageElements.o2o_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_direct_councle(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_o2o_00185(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_185 : 주거공간 시공 > 간편상담 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_simple_councle_flow(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_o2o_00188(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_188 : 부분 시공 확인", end='')
    PageElements.o2o_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_parts_remodeling(page),
                           check=True)
    print(" - Pass")
    
@pytest.mark.regression
def test_o2o_00522(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_522 : 집보기 체크리스트 진입 확인", end='')
    PageElements.o2o_partner_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_house_checklist(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_o2o_00530(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_530 : 집보기 체크리스트 상세 진입 확인", end='')
    PageElements.o2o_partner_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_house_checklist_detail(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_o2o_00535(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_535 : 아파트 시공사례 체크리스트 상세 진입 확인", end='')
    PageElements.o2o_partner_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_remodiling_reference(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_o2o_00536(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_536 : 아파트 시공사례 지역변경 확인", end='')
    PageElements.o2o_partner_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_remodiling_reference_change(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_o2o_00537(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_537 : 아파트 시공사례 상세페이지 확인", end='')
    PageElements.o2o_partner_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_remodiling_reference_detail(page),
                           check=True)
    print(" - Pass")

@pytest.mark.regression
def test_o2o_00607(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_607 : 이 컨셉 시공상담 확인", end='')
    PageElements.o2o_partner_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_concept_remodeling(page),
                           check=True)
    print(" - Pass")


@pytest.mark.smoke
def test_o2o_00608(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_608 : 부분시공 숏컷 노출 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.into_parts_shortcut(page),
                           check=True)
    print(" - Pass")

# 전체 서비스 메뉴 삭제로 케이스 수정예정
@pytest.mark.skip
def test_o2o_00609(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_609 : 부분시공 페이지 진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.into_parts_services(page),
                           check=True)
    print(" - Pass")

@pytest.mark.smoke
def test_o2o_00610(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_610 : 부분시공 LNB진입 확인", end='')
    PageElements.qaweb_main_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.into_parts_gnb(page),
                           check=True)
    print(" - Pass")


@pytest.mark.skip
def test_o2o_00611(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    print("\ntest_o2o_607 : 이 컨셉 시공상담 확인", end='')
    PageElements.o2o_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oElements.check_partnercenter_home(page),
                           check=True)
    print(" - Pass")



