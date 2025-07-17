from behave import given, when, then
from app.common.base_method.appium_method import ProviderCommonMethod
from app.common.base_method.ios_result_binary import Result
from app.common.base_method.get_function_name_func import ProviderFunctionName
from app.common.base_method.exception_func import ExceptionHandler
from app.common.app_config.data import AppVersion
from app.common.base_method.mysql_query import UserManager
from app.common.app_config.data import AccountInfo
from app.common.app_config.data import PackageName
from app.common.app_config.data import UDID

from app.common.keyword.keyword_mapping import KeywordMapping


# precondition
from app.ios.procedure.precondition.app_install import AppInstaller
from app.ios.procedure.precondition.server_change import ServerChangeClass
from app.ios.procedure.precondition.sign_up import SignUp
from app.common.base_method.proxy import SetMitmproxy

# 앱설치 -> 서버교체 까지 진행되는 코드
class ServerChange:
    @given('프리컨디션 바이너리 설정')
    def test_precondtion001_ios_dict_set(self):
        Result().write_result("pre-condition3", "none")

    @when('앱 삭제 후 테스트플라이트 진입 후 버전 및 빌드그룹 -> 버전 매핑 후 앱 설치')
    def test_precondtion001_ios_3_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler_pre_condition(self, current_function_name,
                                                              step=lambda: AppInstaller.del_app(self,"rt"),
                                                              opt_result_exception="세번째 디바이스 앱 설치실패 테스트종료",
                                                              opt_title_exception2="pre-condition3",
                                                              opt_result_exception2="fail"
                                                              )

    @then('열기 버튼 노출확인으로 설치확인')
    def test_precondtion001_ios_3_result(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler_pre_condition(self,
                                                              current_function_name,
                                                              step=lambda: ProviderCommonMethod.assert_equal(self,
                                                                                                             "열기",
                                                                                                             AppInstaller.actual_result(
                                                                                                                 self,'rt')),
                                                              back_flow=lambda: AppInstaller.back_flow(self),
                                                              opt_result="세번째 디바이스 앱 설치 완료",
                                                              opt_title2="pre-condition3",
                                                              opt_result2="pass",
                                                              opt_result_assert="세번째 디바이스 앱 설치 완료 (열기 문구는 다름)",
                                                              opt_title_assert2="pre-condition3",
                                                              opt_result_assert2="pass",
                                                              opt_result_exception="세번째 디바이스 앱 설치 실패. 강제종료함",
                                                              opt_title_exception2="pre-condition3",
                                                              opt_result_exception2="fail"
                                                              )

    @given("앱 최초설치 확인")
    def test_precondtion002_ios_3(self):
        if Result().read_result_slack("pre-condition3") != "pass":
            Result().write_result("pre-condition3", "fail")
            self.scenario.skip(reason="설치 실패로 스킵 : test_precondtion003_ios_2")
        else:
            Result().write_result("pre-condition3", "pass")

    @when('qa_auto@bucketplace.net 계정으로 로그인')
    def test_precondtion002_ios_3_step1(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler_pre_condition(self, current_function_name,
                                               step=lambda: ServerChangeClass.is_login_qa_account(self),
                                               opt_result_exception="세번째 디바이스 login 실패. 테스트 강제종료함",
                                               opt_title_exception2="pre-condition3",
                                               opt_result_exception2="fail"
                                               )

    @when('홈 버튼 롱프레스로 QA서버 변경')
    def test_precondtion002_ios_3_step2(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler_pre_condition(self, current_function_name,
                                               step=lambda: ServerChangeClass.change_qa(self),
                                               opt_result_exception="세번째 디바이스 QA 서버 전환 실패. 테스트 강제종료함",
                                               opt_title_exception2="pre-condition3",
                                               opt_result_exception2="fail"
                                               )

    @then('"카카오톡으로 계속하기", "로그인에 문제가 있으신가요?" 문구로 확인')
    def test_precondtion002_ios_3_result(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler_pre_condition(self,
                                               current_function_name,
                                               step=lambda: ProviderCommonMethod.assert_equal(self, "이메일로 로그인", ServerChangeClass.actual_result(self)),
                                               opt_result="세번째 디바이스 QA 서버 전환 완료",
                                               opt_title2="pre-condition3",
                                               opt_result2="pass",
                                               opt_result_assert="세번째 디바이스 QA 서버 전환 완료 (로그인 페이지 문구는 실패함)",
                                               opt_title_assert2="pre-condition3",
                                               opt_result_assert2="pass",
                                               opt_result_exception="세번째 디바이스 QA 서버 전환 실패. 테스트 강제종료함",
                                               opt_title_exception2="pre-condition3",
                                               opt_result_exception2="fail"
                                               )

# 공통함수 모음
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

    def test_precondition00000_ios_step(self, action1, locator1,locator2=None,locator3=None,locator4=None,locator5=None,locator6=None,locator7=None,locator8=None,locator9=None,locator10=None,locator11=None,locator12=None,locator13=None,locator14=None,locator15=None,action2=None,action3=None,action4=None,action5=None,action6=None,action7=None,action8=None,action9=None,action10=None,action11=None,action12=None,action13=None,action14=None,action15=None):
         current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,
                                                                                 st_rt=self.scenario.tags,
                                                                                 platform="_ios")
         ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step","ios",
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
    def test_precondition00000_ios_step2(self, action1, locator1, locator2=None, locator3=None, locator4=None,
                                        locator5=None, locator6=None, locator7=None, locator8=None, action2=None,
                                        action3=None, action4=None, action5=None, action6=None, action7=None,
                                        action8=None):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,
                                                                                 st_rt=self.scenario.tags,
                                                                                 platform="_ios")
        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step","ios",
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
    def test_login00000_ios_step_login(self, id):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,st_rt=self.scenario.tags,platform="_ios")
        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "login","ios",{"로그인": id}))

    @given('로그아웃 실행')
    def test_logout00000_ios_step_logout(self):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,st_rt=self.scenario.tags,platform="_ios")
        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "logout","ios"))


    @when('앱 재시작')
    def test_restart00000_ios_step_restart(self):
         current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,
                                                                                 st_rt=self.scenario.tags,
                                                                                 platform="_ios")
         ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "restart","ios",
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
    def test_search00000_ios_step(self, locator1, locator2=None, locator3=None, locator4=None, locator5=None,
                                  locator6=None, locator7=None, locator8=None, locator9=None, action2=None,
                                  action3=None, action4=None, action5=None, action6=None, action7=None, action8=None,
                                  action9=None):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,
                                                                                 st_rt=self.scenario.tags,
                                                                                 platform="_ios")
        # ExceptionHandler.ios_exceptions_handler(self, current_function_name,
        #                                         step=lambda: KeywordMapping.execute_keyword(self, "search","ios",
        #                                                                                     {"홈화면_검색": locator1}
        #                                                                                     ))

        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step", "ios",
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
    def test_search00001_ios_step(self, locator1, locator2=None, locator3=None, locator4=None, locator5=None,
                                  locator6=None, locator7=None,
                                  action2=None, action3=None, action4=None, action5=None, action6=None, action7=None):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,
                                                                                 st_rt=self.scenario.tags,
                                                                                 platform="_ios")
        # ExceptionHandler.ios_exceptions_handler(self, current_function_name,
        #                                         step=lambda: KeywordMapping.execute_keyword(self, "search","ios",
        #                                                                                     {"쇼핑홈_검색": locator1}
        #                                                                                     ))
        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step", "ios",
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
    def test_common_result00000_ios_check(self, expected_result, action1, action2,locator1,locator2,action3=None,action4=None,locator3=None,locator4=None):
         current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name,
                                                                                 st_rt=self.scenario.tags,
                                                                                 platform="_ios")
         ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "ios","in",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step","ios",
                                                                                                 {action2: locator2},
                                                                                                 {action3: locator3},
                                                                                                 {action4: locator4}
                                                                                                 ))
class Commerce_Service:
    pass
    # @then('"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인')
    # def prod_commerce_service00001_ios_step1(self, expected_result,action1, locator1):
    #     current_function_name = ProviderFunctionName().get_current_function_name()
    #     ExceptionHandler.ios_exceptions_handler(self, current_function_name,
    #                                             step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
    #                                                                                         expected_result,
    #                                                                                         {action1: locator1}
    #                                                                                         ))