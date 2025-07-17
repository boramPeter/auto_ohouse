from behave import given, when, then
from app.common.base_method.appium_method import ProviderCommonMethod
from app.common.base_method.get_function_name_func import ProviderFunctionName
from app.common.base_method.exception_func import ExceptionHandler
from app.common.keyword.keyword_decorator import custom_given
from app.common.keyword.keyword_mapping import KeywordMapping
from app.common.app_config.data import UDID

# precondition
from app.android.procedure.precondition.app_install_3_rt import AppInstaller3
from app.android.procedure.precondition.server_change import ServerChangeClass
# 앱설치 -> 서버교체 까지 진행되는 코드
class ServerChange:
    @when("앱 삭제")
    def test_precondtion001_aos_app_del_3(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler_pre_condition(self, current_function_name,
                                                              step=lambda: AppInstaller3.del_app(self,UDID.galaxy_udid_rt),
                                                              opt_result_exception="세번째 디바이스에서 앱 삭제실패 테스트종료",
                                                              opt_title_exception2="pre-condition3",
                                                              opt_result_exception2="fail"
                                                              )

    @when('디플로이게이트 진입 후 버전 찾아서 설치')
    def test_precondtion001_aos_step_3(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler_pre_condition(self, current_function_name,
                                                              step=lambda: AppInstaller3.do_install(self),
                                                              opt_result_exception="세번째 디바이스에서 앱 설치실패 테스트종료",
                                                              opt_title_exception2="pre-condition3",
                                                              opt_result_exception2="fail"
                                                              )

    @then('open 버튼 노출확인으로 설치확인')
    def test_precondtion001_aos_result_3(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler_pre_condition(self,
                                                              current_function_name,
                                                              step=lambda: ProviderCommonMethod.assert_equal(self, "Open",
                                                                                                             AppInstaller3.actual_result(
                                                                                                                 self)),
                                                              back_flow=lambda: AppInstaller3.back_flow(self),
                                                              opt_result="세번째 디바이스 앱 설치 완료",
                                                              opt_title2="pre-condition3",
                                                              opt_result2="pass",
                                                              opt_result_assert="세번째 디바이스 앱 설치 완료 (열기 문구는 다름)",
                                                              opt_title_assert2="pre-condition3",
                                                              opt_result_assert2="pass",
                                                              opt_result_exception="세번째 단말에서 앱 설치 실패. 강제종료함",
                                                              opt_title_exception2="pre-condition3",
                                                              opt_result_exception2="fail"
                                                              )
    @given("앱 최초설치")
    def test_precondtion002_aos(self):
        pass

    @when('인트로 페이지에서 "3초만에 빠른 회원가입" 롱프레스로 서버를 변경')
    def test_precondtion002_aos_step_3(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler_pre_condition(self, current_function_name,
                                               step=lambda: ServerChangeClass.change_qa(self),
                                               opt_result_exception="세번째 디바이스에서 QA 서버 전환 실패. 테스트 강제종료함",
                                               opt_title_exception2="pre-condition3",
                                               opt_result_exception2="fail"
                                               )

    @then('"카카오톡으로 계속하기", "로그인에 문제가 있으신가요?" 문구 확인')
    def test_precondtion002_aos_result_3(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler_pre_condition(self,
                                               current_function_name,
                                               step=lambda: ProviderCommonMethod.assert_equal(self, ["카카오톡으로 계속하기", "로그인에 문제가 있으신가요?"], ServerChangeClass.actual_result(self)),
                                               opt_result="세번째 디바이스에서 QA 서버 전환 완료",
                                               opt_title2="pre-condition3",
                                               opt_result2="pass",
                                               opt_result_assert="세번째 디바이스에서 QA 서버 전환 완료 (로그인 페이지 문구는 실패함)",
                                               opt_title_assert2="pre-condition3",
                                               opt_result_assert2="pass",
                                               opt_result_exception="세번째 디바이스에서 QA 서버 전환 실패. 테스트 강제종료함",
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
class Commerce_Service:
    pass
#     @when('"{locator1}"를 "{action1}" 후 제작카드 정상노출 확인 준비')
#     def test_commerce_service00243_aos_step2(self, action1, locator1):
#         current_function_name = ProviderFunctionName().get_current_function_name()
#         ExceptionHandler.aos_exceptions_handler(self, current_function_name,
#                                                 step=lambda: KeywordMapping.execute_keyword(self, "step",
#                                                                                             {action1: locator1}
#                                                                                             ))