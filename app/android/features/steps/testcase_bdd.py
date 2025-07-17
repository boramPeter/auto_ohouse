import time
from behave import given, when, then
from app.common.base_method.exception_func import ExceptionHandler
from app.common.base_method.appium_method import ProviderCommonMethod
from app.common.base_method.permission_func import grant_permission
from app.common.app_config.data import PackageName
from app.common.app_config.data import UDID

from app.common.base_method.aos_result_binary import ResultAndroid
from app.android.driver.aos_webdriver import WebDriver
from app.common.base_method.logger_func import *
from selenium.common.exceptions import TimeoutException
from app.common.base_method.screenshot_func import CaptureClass
from app.common.base_method.app_start_func import AppStart
from app.common.base_method.get_function_name_func import ProviderFunctionName
from app.common.app_config.data import AppVersion
from app.common.base_method.mysql_query import UserManager
from app.common.app_config.data import AccountInfo

# api
from app.api.PLP.PLP_in_category import PlpCategoryAPI
from app.api.PLP.index import IndexApi
from app.api.PLP.exhibitions import ExhibitionsAPI
from app.api.home.place_holder import PlaceholderApi


# commservice
from app.android.procedure.comm_service.comm_service_00014 import ShoppingQuickMenuCheck
from app.android.procedure.comm_service.comm_service_00015 import CategoryListCheck
from app.android.procedure.comm_service.comm_service_00016 import TodayDealCheck
from app.android.procedure.comm_service.comm_service_00017 import TodayDealPDPCheck
from app.android.procedure.comm_service.comm_service_00019 import PopularListCheck
from app.android.procedure.comm_service.comm_service_00022 import CategoryPageCheck
from app.android.procedure.comm_service.comm_service_00026 import MdPickProductCheck
from app.android.procedure.comm_service.comm_service_00034 import CategoryProductListCheck
from app.android.procedure.comm_service.comm_service_00036 import TodayDealMoreCheck
from app.android.procedure.comm_service.comm_service_00043 import TodayDealMorePDPCheck
from app.android.procedure.comm_service.comm_service_00057 import PopularProductScrapCheck
from app.android.procedure.comm_service.comm_service_00060 import CouponTextCheck
from app.android.procedure.comm_service.comm_service_00062 import CouponDownloadCheck
from app.android.procedure.comm_service.comm_service_00065 import CartCouponTextCheck
from app.android.procedure.comm_service.comm_service_00071 import PopularPDPScrapCheck
from app.android.procedure.comm_service.comm_service_00087 import UserStylingShotCheck
from app.android.procedure.comm_service.comm_service_00099 import ReviewImageCheck
from app.android.procedure.comm_service.comm_service_00128 import CollectionDetailCheck
from app.android.procedure.comm_service.comm_service_00129 import CollectionDetailPageCheck
from app.android.procedure.comm_service.comm_service_00138 import RealTimeBestCheck
from app.android.procedure.comm_service.comm_service_00147 import QuickTodayDealCheck
from app.android.procedure.comm_service.comm_service_00149 import ExhibitionPageCheck
from app.android.procedure.comm_service.comm_service_00152 import PremiumPageCheck
from app.android.procedure.comm_service.comm_service_00173 import ExhibitionFeedCheck
from app.android.procedure.comm_service.comm_service_00175 import ExhibitionFeedDetailPageCheck

class ServerChange:
    @when("앱 삭제")
    def test_precondtion001_aos_app_del(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler_pre_condition(self, current_function_name,
                                                              step=lambda: AppInstaller.del_app(self,UDID.galaxy_udid_1),
                                                              opt_result_exception="첫번째 디바이스 앱 삭제실패 테스트종료",
                                                              opt_title_exception2="pre-condition",
                                                              opt_result_exception2="fail"
                                                              )

    @when('디플로이게이트 진입 후 버전 찾아서 설치')
    def test_precondtion001_aos_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler_pre_condition(self, current_function_name,
                                                              step=lambda: AppInstaller.do_install(self),
                                                              opt_result_exception="첫번째 디바이스 앱 설치실패 테스트종료",
                                                              opt_title_exception2="pre-condition",
                                                              opt_result_exception2="fail"
                                                              )

    @then('open 버튼 노출확인으로 설치확인')
    def test_precondtion001_aos_result(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler_pre_condition(self,
                                                              current_function_name,
                                                              step=lambda: ProviderCommonMethod.assert_equal(self, "Open",
                                                                                                             AppInstaller.actual_result(
                                                                                                                 self)),
                                                              back_flow=lambda: AppInstaller.back_flow(self),
                                                              opt_result="첫번째 디바이스 앱 설치 완료",
                                                              opt_title2="pre-condition",
                                                              opt_result2="pass",
                                                              opt_result_assert="첫번째 디바이스 앱 설치 완료 (열기 문구는 다름)",
                                                              opt_title_assert2="pre-condition",
                                                              opt_result_assert2="pass",
                                                              opt_result_exception="첫번째 디바이스 앱 설치 실패. 강제종료함",
                                                              opt_title_exception2="pre-condition",
                                                              opt_result_exception2="fail"
                                                              )
    @given("앱 최초설치")
    def test_precondtion002_aos(self):
        pass

    @when('인트로 페이지에서 "3초만에 빠른 회원가입" 롱프레스로 서버를 변경')
    def test_precondtion002_aos_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler_pre_condition(self, current_function_name,
                                               step=lambda: ServerChangeClass.change_qa(self),
                                               opt_result_exception="첫번째 디바이스 QA 서버 전환 실패. 테스트 강제종료함",
                                               opt_title_exception2="pre-condition",
                                               opt_result_exception2="fail"
                                               )

    @then('"카카오톡으로 계속하기", "로그인에 문제가 있으신가요?" 문구 확인')
    def test_precondtion002_aos_result(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler_pre_condition(self,
                                               current_function_name,
                                               step=lambda: ProviderCommonMethod.assert_equal(self, ["카카오톡으로 계속하기", "로그인에 문제가 있으신가요?"], ServerChangeClass.actual_result(self)),
                                               opt_result="첫번째 디바이스 QA 서버 전환 완료",
                                               opt_title2="pre-condition",
                                               opt_result2="pass",
                                               opt_result_assert="QA 서버 전환 완료 (로그인 페이지 문구는 실패함)",
                                               opt_title_assert2="pre-condition",
                                               opt_result_assert2="pass",
                                               opt_result_exception="첫번째 디바이스 QA 서버 전환 실패. 테스트 강제종료함",
                                               opt_title_exception2="pre-condition",
                                               opt_result_exception2="fail"
                                               )


class CommonTestActions:
    '''
    1. 페이지 진입용 함수. 보통 홈에서 페이지 진입의 스텝이 첫 실행 스텝일것이라 given에 첫번째 step으로 고정
    2. 해당 키워드를 한 케이스에서 여러번 재활용이 필요할수 있어, case_no을 붙임. e.g. 페이지 진입_"1", 페이지 진입_"2" 으로 분리해서 사용가능. >> 일단 삭제. 추후 필요시에 추가고려
    3. retry 로직때문에 given을 모으고,가급적 해당 함수에서 step을 처리해야 의미가 생기므로 아래처럼 구현함
    '''

    @given('"{locator1}","{action1}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}","{locator8}","{action8}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}","{locator8}","{action8}","{locator9}","{action9}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}","{locator8}","{action8}","{locator9}","{action9}","{locator10}","{action10}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}","{locator8}","{action8}","{locator9}","{action9}","{locator10}","{action10}","{locator11}","{action11}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}","{locator8}","{action8}","{locator9}","{action9}","{locator10}","{action10}","{locator11}","{action11}","{locator12}","{action12}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}","{locator8}","{action8}","{locator9}","{action9}","{locator10}","{action10}","{locator11}","{action11}","{locator12}","{action12}","{locator13}","{action13}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}","{locator8}","{action8}","{locator9}","{action9}","{locator10}","{action10}","{locator11}","{action11}","{locator12}","{action12}","{locator13}","{action13}","{locator14}","{action14}" 페이지 진입 및 확인')
    @given(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}","{locator8}","{action8}","{locator9}","{action9}","{locator10}","{action10}","{locator11}","{action11}","{locator12}","{action12}","{locator13}","{action13}","{locator14}","{action14}","{locator15}","{action15}" 페이지 진입 및 확인')

    def test_precondition00000_aos_step(self, action1, locator1,locator2=None,locator3=None,locator4=None,locator5=None,locator6=None,locator7=None,locator8=None,locator9=None,locator10=None,locator11=None,locator12=None,locator13=None,locator14=None,locator15=None,action2=None,action3=None,action4=None,action5=None,action6=None,action7=None,action8=None,action9=None,action10=None,action11=None,action12=None,action13=None,action14=None,action15=None):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,st_rt=self.scenario.tags,platform="_aos")
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step","aos",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action4: locator4},
                                                                                            {action5: locator5},
                                                                                            {action6: locator6},
                                                                                            {action7: locator7},
                                                                                            {action8: locator8},
                                                                                            {action9: locator9},
                                                                                            {action10: locator10},
                                                                                            {action11: locator11},
                                                                                            {action12: locator12},
                                                                                            {action13: locator13},
                                                                                            {action14: locator14},
                                                                                            {action15: locator15}
                                                                                            ))


    # 케이스 분리를 위해 when, given각각 분리
    @when('"{locator1}","{action1}" 페이지 진입 및 확인')
    @when(
        '"{locator1}","{action1}","{locator2}","{action2}" 페이지 진입 및 확인')
    @when(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}" 페이지 진입 및 확인')
    @when(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}" 페이지 진입 및 확인')
    @when(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}" 페이지 진입 및 확인')
    @when(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}" 페이지 진입 및 확인')
    @when(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}" 페이지 진입 및 확인')
    @when(
        '"{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}","{locator8}","{action8}" 페이지 진입 및 확인')
    def test_precondition00000_aos_step2(self, action1, locator1, locator2=None, locator3=None, locator4=None,
                                        locator5=None, locator6=None, locator7=None, locator8=None, action2=None,
                                        action3=None, action4=None, action5=None, action6=None, action7=None,
                                        action8=None):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,
                                                                                 st_rt=self.scenario.tags,platform="_aos")
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step","aos",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action4: locator4},
                                                                                            {action5: locator5},
                                                                                            {action6: locator6},
                                                                                            {action7: locator7},
                                                                                            {action8: locator8}
                                                                                            ))
    # 로그인 키워드 (3번 계정 고정)
    @given('"{id}"로 로그인')
    def test_login00000_aos_step_login(self, id):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,st_rt=self.scenario.tags,platform="_aos")
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "login","aos",{"로그인": id}))

    @given('로그아웃 실행')
    def test_logout00000_aos_step_logout(self):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,st_rt=self.scenario.tags,platform="_aos")
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "logout","aos"))


    @when('앱 재시작')
    def test_restart00000_aos_step_restart(self):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,st_rt=self.scenario.tags,platform="_aos")
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "restart","aos",
                                                                                            ))

    # 검색 하이레벨 키워홈 - 이동해서 검색할일은 없기때무네 given에 첫번째 step으로 고정
    @given(
        '"{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}" 스텝 진행')
    @given(
        '"{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}","{locator3}","{action3}" 스텝 진행')
    @given(
        '"{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}" 스텝 진행')
    @given(
        '"{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}" 스텝 진행')
    @given(
        '"{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}" 스텝 진행')
    @given(
        '"{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}" 스텝 진행')
    @given(
        '"{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}","{locator8}","{action8}" 스텝 진행')
    @given(
        '"{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}","{locator8}","{action8}","{locator9}","{action9}" 스텝 진행')
    def test_search00000_aos_step(self, locator1, locator2=None, locator3=None, locator4=None, locator5=None,
                                  locator6=None, locator7=None, locator8=None, locator9=None, action2=None,
                                  action3=None, action4=None, action5=None, action6=None, action7=None, action8=None,
                                  action9=None):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,
                                                                                 st_rt=self.scenario.tags,
                                                                                 platform="_aos")
        # ExceptionHandler.aos_exceptions_handler(self, current_function_name,
        #                                         step=lambda: KeywordMapping.execute_keyword(self, "search","aos",
        #                                                                                     {"홈화면_검색": locator1}
        #                                                                                     ))

        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step", "aos",
                                                                                            {"홈화면_검색": locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action4: locator4},
                                                                                            {action5: locator5},
                                                                                            {action6: locator6},
                                                                                            {action7: locator7},
                                                                                            {action8: locator8},
                                                                                            {action9: locator9}
                                                                                            ))
    # 쇼핑홈 검색 하이레벨 키워홈 - 이동해서 검색할일은 없기때무네 given에 첫번째 step으로 고정
    @given(
        '쇼핑홈에서 "{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}" 스텝 진행')
    @given(
        '쇼핑홈에서 "{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}","{locator3}","{action3}" 스텝 진행')
    @given(
        '쇼핑홈에서 "{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}" 스텝 진행')
    @given(
        '쇼핑홈에서 "{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}" 스텝 진행')
    @given(
        '쇼핑홈에서 "{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}" 스텝 진행')
    @given(
        '쇼핑홈에서 "{locator1}"검색어로 srp 진입 후 "{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}","{locator6}","{action6}","{locator7}","{action7}" 스텝 진행')
    def test_search00001_aos_step(self, locator1, locator2=None, locator3=None, locator4=None,locator5=None,locator6=None,locator7=None,
                                   action2=None, action3=None, action4=None, action5=None, action6=None, action7=None):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,
                                                                                 st_rt=self.scenario.tags,platform="_aos")
        # ExceptionHandler.aos_exceptions_handler(self, current_function_name,
        #                                         step=lambda: KeywordMapping.execute_keyword(self, "search","aos",
        #                                                                                     {"쇼핑홈_검색": locator1}
        #                                                                                     ))
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step","aos",
                                                                                            {"쇼핑홈_검색": locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action4: locator4},
                                                                                            {action5: locator5},
                                                                                            {action6: locator6},
                                                                                            {action7: locator7}
                                                                                            ))

    # 기대결과 확인용 함수
    @then('"{locator1}"가"{action1}","{expected_result}" 확인 후 "{locator2}"를"{action2}"해서 홈화면 복귀')
    @then('"{locator1}"가"{action1}","{expected_result}" 확인 후 "{locator2}"를"{action2}","{locator3}"를"{action3}"해서 홈화면 복귀')
    @then('"{locator1}"가"{action1}","{expected_result}" 확인 후 "{locator2}"를"{action2}","{locator3}"를"{action3}","{locator4}"를"{action4}"해서 홈화면 복귀')
    def test_common_result00000_aos_check(self, expected_result, action1, action2,locator1,locator2,action3=None,locator3=None,action4=None,locator4=None):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,st_rt=self.scenario.tags,platform="_aos")
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result","aos", "in",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step","aos",
                                                                                                 {action2: locator2},
                                                                                                 {action3: locator3},
                                                                                                 {action4: locator4}
                                                                                                 ))



class Comm_Service:
    @when('쇼핑 -> 퀵메뉴 진입')
    def test_comm_service00014_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: ShoppingQuickMenuCheck.go_quick_menu(self)
                                                )

    @then('퀵메뉴 진입 확인')
    def test_comm_service00014_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, "베스트", ShoppingQuickMenuCheck.actual_result(self)),
                                                back_flow=lambda: ShoppingQuickMenuCheck.back_flow(self))

    @when('쇼핑 -> 카테고리 진입')
    def test_comm_service00015_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: CategoryListCheck.go_category_list(self)
                                                )

    @then('카테고리 리스트 확인')
    def test_comm_service00015_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, [
                                                                                                '카테고리', '테마관', '가구', '패브릭', '조명', '가전', '주방용품',
                                                                                                '장식/소품', '수납/정리', '생활용품', '생필품', '공구/DIY', '리모델링·홈케어',
                                                                                                '반려동물', '실내운동', '유아/아동'], CategoryListCheck.actual_result(self)),
                                                back_flow=lambda: CategoryListCheck.back_flow(self))

    @when('쇼핑 -> 임의 카테고리 진입 (가구)')
    def test_comm_service00022_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: CategoryPageCheck.go_category_page(self)
                                                )

    @then('카테고리 진입 확인')
    def test_comm_service00022_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, ["가구", "소파/거실가구"], CategoryPageCheck.actual_result(self)),
                                                back_flow=lambda: CategoryPageCheck.back_flow(self))

    @when("쇼핑 -> MD'pick 캐러셀에서 pdp 진입")
    def test_comm_service00026_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: MdPickProductCheck.go_md_pick_pdp(self)
                                                )

    @then('pdp 노출 확인')
    def test_comm_service00026_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, True, MdPickProductCheck.actual_result(self)),
                                                back_flow=lambda: MdPickProductCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 카테고리 -> 카테고리 상세 진입")
    def test_comm_service00034_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: CategoryProductListCheck.go_category_pdp(self)
                                                )

    @then('카테고리 상세페이지 확인')
    def test_comm_service00034_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, True, CategoryProductListCheck.actual_result(self)),
                                                back_flow=lambda: CategoryProductListCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 오늘의딜 진입")
    def test_comm_service00016_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: TodayDealCheck.check_today_deal_title(self)
                                                )

    @then('오늘의딜 진입 확인')
    def test_comm_service00016_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, "오늘의딜", TodayDealCheck.actual_result(self)),
                                                back_flow=lambda: TodayDealCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 오늘의딜 -> 상품상세 진입")
    def test_comm_service00017_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: TodayDealPDPCheck.go_today_deal_pdp(self)
                                                )

    @then('오늘의딜 상품상세 진입 확인')
    def test_comm_service00017_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, True, TodayDealPDPCheck.actual_result(self)),
                                                back_flow=lambda: TodayDealPDPCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 오늘의딜 -> 오늘의딜 상세 진입")
    def test_comm_service00036_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: TodayDealMoreCheck.go_today_deal_more_page(self)
                                                )

    @then('오늘의딜 상세페이지 확인')
    def test_comm_service00036_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, "오늘의딜", TodayDealMoreCheck.actual_result(self)),
                                                back_flow=lambda: TodayDealMoreCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 오늘의딜 -> 오늘의딜 상세 -> 상품상세 진입")
    def test_comm_service00043_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: TodayDealMorePDPCheck.go_today_deal_more_pdp(self)
                                                )

    @then('오늘의딜 상세페이지에서 상품상세 확인')
    def test_comm_service00043_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, True, TodayDealMorePDPCheck.actual_result(self)),
                                                back_flow=lambda: TodayDealMorePDPCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 몰랐던 취향까지 발견하기까지 스크롤")
    def test_comm_service00019_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: PopularListCheck.go_popular_list(self)
                                                )

    @then('몰랐던 취향까지 발견하기 타이틀 확인')
    def test_comm_service00019_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, True, PopularListCheck.actual_result(self)),
                                                back_flow=lambda: PopularListCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 몰랐던 취향까지 발견하기까지 스크롤 -> 상품 스크랩")
    def test_comm_service00057_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: PopularProductScrapCheck.do_popular_scrap(self)
                                                )

    @then('인기상품 스크랩 확인')
    def test_comm_service00057_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, "스크랩했습니다.", PopularProductScrapCheck.actual_result(self)),
                                                back_flow=lambda: PopularProductScrapCheck.back_flow(self)
                                                )

    @when("검색 -> 쿠폰있는 상품 상세 진입")
    def test_comm_service00060_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: CouponTextCheck.check_coupon_text(self)
                                                )

    @then('쿠폰 적용 시 텍스트 확인')
    def test_comm_service00060_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, "쿠폰적용시", CouponTextCheck.actual_result(self)),
                                                back_flow=lambda: CouponTextCheck.back_flow(self)
                                                )

    @when("검색 -> 쿠폰있는 상품 상세 진입 -> 쿠폰 다운로드 완료")
    def test_comm_service00062_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: CouponDownloadCheck.check_coupon_download(self)
                                                )

    @then('쿠폰 다운로드 토스트, 상품쿠폰 타이틀, 장바구니 쿠폰 타이틀, 쿠폰적용됨 문구 확인')
    def test_comm_service00062_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, ['사용가능한 쿠폰을 모두 받았어요', '상품쿠폰', '장바구니쿠폰', '쿠폰적용됨'], CouponDownloadCheck.actual_result(self)),
                                                back_flow=lambda: CouponDownloadCheck.back_flow(self)
                                                )

    @when("검색 -> 쿠폰있는 상품 상세 진입 -> 장바구니 쿠폰 다운로드 완료")
    def test_comm_service00065_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: CartCouponTextCheck.check_cart_coupon_text(self)
                                                )

    # self.assertIn('더 할인돼요!', CartCouponTextCheck.actual_result(self)[0])
    # self.assertIn('이상 결제시 장바구니 쿠폰 적용 가능', CartCouponTextCheck.actual_result(self)[1])
    @then('장바구니 쿠폰 적용 문구 확인')
    def test_comm_service00065_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_in_list(self, ['더 할인돼요!','이상 결제시'], CartCouponTextCheck.actual_result(self)),
                                                back_flow=lambda: CartCouponTextCheck.back_flow(self)
                                                )



    @when("쇼핑 -> 몰랐던 취향까지 발견하기까지 스크롤 -> 상품 상세 -> 상품 스크랩")
    def test_comm_service00071_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: PopularPDPScrapCheck.do_popular_pdp_scrap(self)
                                                )

    @then('상품 상세에서 인기상품 스크랩 확인')
    def test_comm_service00071_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, "스크랩했습니다.", PopularPDPScrapCheck.actual_result(self)),
                                                back_flow=lambda: PopularPDPScrapCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 몰랐던 취향까지 발견하기까지 스크롤 -> 상품 상세 -> 유저들의 스타일링샷까지 스크롤 -> 좌우 스크롤 후 더보기")
    def test_comm_service00087_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: UserStylingShotCheck.check_user_styling_shot(self)
                                                )

    @then('썸네일 확인 및 썸네일 상세 진입 확인')
    def test_comm_service00087_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_in(self, "유저들의 스타일링샷", UserStylingShotCheck.actual_result(self)),
                                                back_flow=lambda: UserStylingShotCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 몰랐던 취향까지 발견하기까지 스크롤 -> 상품 상세 -> 리뷰이미지 선택")
    def test_comm_service00099_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: ReviewImageCheck.check_review_image(self)
                                                )

    @then('리뷰 이미지 및 내용 확인')
    def test_comm_service00099_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, True, ReviewImageCheck.actual_result(self)),
                                                back_flow=lambda: ReviewImageCheck.back_flow(self)
                                                )

    @when("검색 -> 모음전 진입")
    def test_comm_service00128_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: CollectionDetailCheck.check_collection_detail(self)
                                                )

    @then('재료상품 확인')
    def test_comm_service00128_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, ['자세히보기', '옵션선택', '자세히보기', '옵션선택'], CollectionDetailCheck.actual_result(self)),
                                                back_flow=lambda: CollectionDetailCheck.back_flow(self)
                                                )

    @when("검색 -> 모음전상세 -> 자세히보기로 재료상품 상세 진압")
    def test_comm_service00129_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: CollectionDetailPageCheck.check_collection_detail_page(self)
                                                )

    @then('재료상품 상세 확인')
    def test_comm_service00129_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_in_list(self,
                                                                                               [True, True],
                                                                                               CollectionDetailPageCheck.actual_result(self)),
                                                back_flow=lambda: CollectionDetailPageCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 베스트 퀵메뉴 -> 실시간베스트 탭")
    def test_comm_service00138_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: RealTimeBestCheck.check_real_time_best_tab(self)
                                                )

    @then('실시간베스트 리스트 확인')
    def test_comm_service00138_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self,
                                                                                               ['1', '2', '3'], RealTimeBestCheck.actual_result(self)),
                                                back_flow=lambda: RealTimeBestCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 오딜 퀵메뉴")
    def test_comm_service00147_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: QuickTodayDealCheck.go_quick_today_deal(self)
                                                )

    @then('퀵메뉴로 들어온 오딜 확인')
    def test_comm_service00147_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self,
                                                                                               "오늘의딜", QuickTodayDealCheck.actual_result(self)),
                                                back_flow=lambda: QuickTodayDealCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 기획전(상세) 퀵메뉴")
    def test_comm_service00149_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: ExhibitionPageCheck.go_quick_exhibition_page(self)
                                                )

    @then('퀵메뉴로 들어온 기획전(상세) 확인')
    def test_comm_service00149_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_in(self,
                                                                                               "기획전", ExhibitionPageCheck.actual_result(self)),
                                                back_flow=lambda: ExhibitionPageCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 프리미엄 퀵메뉴")
    def test_comm_service00152_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: PremiumPageCheck.go_quick_premium_page(self)
                                                )

    @then('퀵메뉴로 들어온 프리미엄 페이지 확인')
    def test_comm_service00152_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self,
                                                                                               True, PremiumPageCheck.actual_result(self)),
                                                back_flow=lambda: PremiumPageCheck.back_flow(self)
                                                )
    @when("쇼핑 -> 기획전(피드) 퀵메뉴")
    def test_comm_service00173_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: ExhibitionFeedCheck.go_quick_exhibition_feed_page(self)
                                                )

    @then('퀵메뉴로 들어온 기획전(피드) 페이지 확인')
    def test_comm_service00173_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self,
                                                                                               "기획전", ExhibitionFeedCheck.actual_result(self)),
                                                back_flow=lambda: ExhibitionFeedCheck.back_flow(self)
                                                )

    @when("쇼핑 -> 기획전(피드) 퀵메뉴 -> 상세페이지")
    def test_comm_service00175_aos_st_rt_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: ExhibitionFeedDetailPageCheck.go_quick_exhibition_feed_detail_page(self)
                                                )

    @then('기획전(피드) 상세 페이지 확인')
    def test_comm_service00175_aos_st_rt_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_in(self,
                                                                                               ExhibitionsAPI().exhibitions_detail_list("android",AppVersion.version("aOS")), ExhibitionFeedDetailPageCheck.actual_result(self)),
                                                back_flow=lambda: ExhibitionFeedDetailPageCheck.back_flow(self)
                                                )

