from behave import given, when, then
from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler
from app.common.base_method.appium_method import ProviderCommonMethod
from production.common.method.get_function_name_func import ProviderFunctionName

# api


# precondition
from production.app.ios.ios_procedure.app_install import AppInstaller

# keyword
from production.app.common_method.keyword_mapping import KeywordMapping
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

    def prod_precondition00000_ios_step(self, action1, locator1,locator2=None,locator3=None,locator4=None,locator5=None,locator6=None,locator7=None,locator8=None,locator9=None,locator10=None,locator11=None,locator12=None,locator13=None,locator14=None,locator15=None,action2=None,action3=None,action4=None,action5=None,action6=None,action7=None,action8=None,action9=None,action10=None,action11=None,action12=None,action13=None,action14=None,action15=None):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
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
    def prod_precondition00000_ios_step2(self, action1, locator1, locator2=None, locator3=None, locator4=None,
                                        locator5=None, locator6=None, locator7=None, locator8=None, action2=None,
                                        action3=None, action4=None, action5=None, action6=None, action7=None,
                                        action8=None):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action4: locator4},
                                                                                            {action5: locator5},
                                                                                            {action6: locator6},
                                                                                            {action7: locator7},
                                                                                            {action8: locator8}
                                                                                            ))
    # 로그인 키워드
    @given('"{id}"로 로그인')
    def prod_login00000_ios_step_login(self, id):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "login","ios",{"로그인": id}))

    @given('로그아웃 실행')
    def prod_logout00000_ios_step_logout(self):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "logout","ios"))


    @when('앱 재시작')
    def prod_restart00000_ios_step_restart(self):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "restart","ios",
                                                                                            ))


    # 기대결과 확인용 함수
    @then('"{locator1}"가"{action1}","{expected_result}" 확인 후 "{locator2}"를"{action2}"해서 홈화면 복귀')
    @then('"{locator1}"가"{action1}","{expected_result}" 확인 후 "{locator2}"를"{action2}","{locator3}"를"{action3}"해서 홈화면 복귀')
    @then('"{locator1}"가"{action1}","{expected_result}" 확인 후 "{locator2}"를"{action2}","{locator3}"를"{action3}","{locator4}"를"{action4}"해서 홈화면 복귀')
    def prod_common_result00000_ios_check(self, expected_result, action1, action2,locator1,locator2,action3=None,locator3=None,action4=None,locator4=None):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "in",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action3: locator3},
                                                                                                 {action4: locator4}
                                                                                                 ))
class Precondition:
    @when("앱 삭제")
    def prod_precondition00001_ios_app_del(self):
        AppInstaller.del_app(self)

    @when('앱스토어 진입 후 오늘의집 검색 -> 앱 설치')
    def prod_precondition00001_ios_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                              step=lambda: AppInstaller.app_install(self),
                                                              opt_title_exception2="pre-condition",
                                                              opt_result_exception2="fail"
                                                              )

    @then('열기 버튼 노출확인으로 설치확인')
    def prod_precondition00001_ios_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda:ProviderCommonMethod.assert_equal(self, True,AppInstaller.actual_result(self)),
                                                back_flow=lambda: AppInstaller.back_flow(self),
                                                opt_title2="pre-condition",
                                                opt_result2="pass",
                                                opt_title_exception2="pre-condition",
                                                opt_result_exception2="fail"
                                                )

class Common:
    @when('앱 실행 후 "{locator1}" "{action1}" "{locator2}"을 "{action2}" 후 홈화면 진입')
    def prod_common00001_ios_step(self,action1,action2,locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self,"step",{action1:locator1},{action2:locator2})
                                                )

    @then('"{locator1}"가 "{action1}" 되었는지,"{locator2}"가 "{action1}" 되었는지 확인하여 "{expected_result}"를 확인')
    def prod_common00001_ios_check(self,expected_result,action1,locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self,"result","equal",expected_result,{action1:locator1},{action1:locator2}))

    @when('"{locator1}"를 "{action1}"해서 페이지 진입')
    def prod_common00002_ios_step(self,action1,locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self,"step",{action1:locator1})
                                                )

    @then('"{locator1}","{locator2}","{locator3}"를 "{action1}"하고 "{expected_result}"와 비교해서 정상노출 확인한 후 "{locator4}"을 "{action2}"해서 로그인화면으로 복귀')
    def prod_common00002_ios_check(self,expected_result,action1,action2,locator1,locator2,locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self,"result","equal",expected_result,{action1:locator1},{action1:locator2},{action1:locator3}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self,"step",{action2:locator4})
                                                )

    @when('"{locator1}" 다음 "{locator2}"를 "{action1}"하여 비밀번호 재설정페이지 진입')
    def prod_common00004_ios_step(self,action1,locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self,"step",{action1:locator1},{action1:locator2}))

    @then('"{locator1}"가 "{action1}"된지 확인하고 "{locator2}"를 "{action2}" 하여 "{expected_result}"와 비교해서 정상인지 확인 후, "{locator3}", "{locator4}"을 순서대로 "{action3}" 해서 로그인화면으로 복귀')
    def prod_common00004_ios_check(self,expected_result,action1,action2,action3,locator1,locator2,locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1},
                                                                                            {action2: locator2}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self,"step",{action3:locator3},{action3:locator4})
                                                )

    @when('"{locator1}", "{locator2}"을 순서대로 "{action1}"해서 둘러보기를 통한 메인 페이지 진입')
    def prod_common00005_ios_step(self,action1,locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self,"step",{action1:locator1},{action1:locator2}))

    @when('"{locator1}" "{action1}" "{locator2}" "{action2}" 다음 "{locator3}","{locator4}" "{action3}"해서 둘러보기를 통한 홈화면 진입')
    def prod_common00005_ios_step2(self,action1,action2,action3,locator1,locator2,locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self,"step",{action1:locator1},{action2:locator2},{action3:locator3},{action3:locator4}))

    @then('"{locator1}"과 "{locator2}"가 "{action1}" 된지 확인 후 "{expected_result}"과 비교해서 둘러보기를 통한 홈화면 진입 체크 그 후 "{action2}" 해서 로그인화면 복귀')
    def prod_common00005_ios_check(self,expected_result,action1,action2,locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result","equal",
                                                                                            expected_result,
                                                                                            {action1: locator1},
                                                                                            {action1: locator2}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self,"step",action2)
                                                )

    @when('로그인 페이지에서 "{account}"계정으로 로그인 시도')
    def prod_common00011_ios_step(self,account):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self,"login",account))

    @when('"{locator1}"를 "{action1}"해서 광고제거 후 홈화면 진입해서 정상동작 체크준비 "{locator2}","{action1}"')
    def prod_common00011_ios_step2(self, action1, locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step", {action1: locator1},{action1: locator2}))

    @then('"{locator1}"과 "{locator2}"가 "{action1}"된지 확인 후 "{expected_result}"와 비교해서 로그인 된지 확인')
    def prod_common00011_ios_check(self,expected_result,action1,locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result","equal",
                                                                                            expected_result,
                                                                                            {action1: locator1},
                                                                                            {action1: locator2}))

class Home:
    @when('"{locator1}"를 "{action1}"한뒤에 홈화면 노출 확인')
    def prod_home00014_ios_step(self,action1,locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self,"step",{action1:locator1}))


    @then('"{locator1}"와 "{locator2}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교하여 홈화면이 정상노출되는지 확인')
    def prod_home00014_ios_check(self,expected_result,action1,locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1},
                                                                                            {action1: locator2}))

    @when('"{locator1}"를 "{action1}"한뒤에 "{locator2}", "{locator3}" 가 노출되면 "{action2}"을 하고 둘러보기 진입')
    def prod_home00015_ios_step(self,action1,locator1,action2,locator2,locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self,"step",{action1:locator1},{action2:locator2},{action2:locator3}))


    @then('"{locator1}"의 "{action1}"을 하고 "{locator2}"가 "{action2}" 된지 확인 후 "{expected_result}" 와 비교해서 정상노출되는지 확인. 그 후에 "{locator3}"를 "{action3}"하여 홈화면으로 복귀')
    def prod_home00015_ios_check(self,expected_result,action1,action2,action3,locator1,locator2,locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1},
                                                                                            {action2: locator2}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self,"step",{action3:locator3}))

    @when('"{locator1}"을 "{action1}"한뒤에 "{locator2}" "{action2}", "{locator3}"가 노출되면 "{action3}"을 하고 쇼핑홈 진입 "{locator4}" "{action4}"')
    def prod_home00016_ios_step(self, action1, locator1, action2, locator2, action3,action4, locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action4: locator4}))
    @then(
        '"{locator1}" 와 "{locator2}"이 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 쇼핑홈이 정상노출되는지 확인. "{locator3}"가 노출되면 "{action2}"을 한 뒤에 "{locator4}"를 "{action3}"하여 홈화면으로 복귀')
    def prod_home00016_ios_check(self, expected_result, action1, action2,action3, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1},
                                                                                            {action1: locator2}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator3},
                                                                                                 {action3: locator4}))

    @when('"{locator1}"를 "{action1}"한뒤에 o2o화면 노출 확인')
    def prod_home00017_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}))

    @then(
        '"{locator1}"이 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 o2o홈화면이 정상노출되는지 확인. 그 후 "{locator2}"를 "{action2}"하여 홈화면으로 복귀')
    def prod_home00017_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))

    @when('홈화면에서 "{locator1}"를 "{action1}"한뒤에 스크랩화면 노출 확인')
    def prod_home00019_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 스크랩페이지가 정상노출되는지 확인. 그 후 "{locator2}"를 "{action2}"하여 홈화면으로 복귀')
    def prod_home00019_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))
    @when('홈화면에서 "{locator1}"를 "{action1}"한뒤에 알림페이지 노출 확인')
    def prod_home00020_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}))

    @then(
        '"{locator1}","{locator2}","{locator3}"이 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 알림페이지가 정상노출되는지 확인. 그 후 "{locator4}"를 "{action2}"하여 홈화면으로 복귀')
    def prod_home00020_ios_check(self, expected_result, action1, action2, locator1, locator2,locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator4}))

    @when('홈화면에서 "{locator1}" 다음 "{locator2}" 를 순서대로 "{action1}"한뒤에 프로필이미지 확인 준비')
    def prod_home00021_ios_step(self, action1, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2}))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 프로필이미지 정상노출되는지 확인. 그 후 "{locator2}" 와 "{locator3}"를 순서대로 "{action2}"하여 홈화면으로 복귀')
    def prod_home00021_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))


    @when('홈화면에서 "{locator1}"를 "{action1}"한뒤에 장바구니 진입')
    def prod_home00022_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))


    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 장바구니페이지가 정상노출되는지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면으로 복귀')
    def prod_home00022_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))

    @when('홈화면에서 "{locator1}"를 "{action1}"한뒤에 플로팅메뉴 노출시킴')
    def prod_home00026_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '플로팅메뉴에서 "{locator1}","{locator2}","{locator3}","{locator4}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 플로팅메뉴가 정상노출되는지 확인. 그 후 "{locator5}"을 "{action2}"하여 플로팅메뉴 종료')
    def prod_home00026_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4, locator5):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3},
                                                                                            {action1: locator4}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator5}))

    @when(
        '홈화면에서 "{locator1}"를 "{action1}" 후 배너체크 준비')
    def prod_home00043_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '홈화면에서 "{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 메인배너가 정상노출되는지 확인 후 "{locator2}"을 "{action2}" 해서 홈화면 최상단 복귀')
    def prod_home00043_ios_check(self, expected_result, action1, locator1, locator2, action2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))

    @when('홈화면에서 "{locator1}"를 "{action1}"한뒤에 쿠폰 미리받기 페이지 진입')
    def prod_home00045_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 쿠폰미리받기 페이지 정상노출되는지 확인. 그 후 "{action2}"하여 홈화면 복귀 (페이지가 자주 바뀔수 있어 타이틀 요소로만 체크)')
    def prod_home00045_ios_check(self, expected_result, action1, action2, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 action2))


    @when('홈화면에서 "{locator1}"를 "{action1}"한뒤에 오늘의딜 페이지 진입')
    def prod_home00046_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))


    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 오늘의딜 페이지 정상노출되는지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀 (페이지가 자주 바뀔수 있어 타이틀 요소로만 체크)')
    def prod_home00046_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))


    @when('홈화면에서 "{locator1}"를 "{action1}"한뒤에 둘러보기 페이지의 집들이탭 진입')
    def prod_home00047_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))


    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 집들이탭 정상진입 확인. 그 후 "{locator2}"다음 "{locator3}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_home00047_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))


    @when('홈화면에서 "{locator2}" 만큼 "{action2}","{locator1}"를 "{action1}"한뒤에 행운출첵 페이지 진입')
    def prod_home00048_ios_step(self, action1,action2, locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action2: locator2},
                                                                                            {action1: locator1}
                                                                                            ))
    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 행운출첵 페이지 정상노출되는지 확인. 그 후 "{action2}"하여 홈화면 복귀')
    def prod_home00048_ios_check(self, expected_result, action1, action2, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 action2))
    @when('홈화면에서 "{locator1}" "{action1}" "{locator2}" 만큼 "{action2}"한 뒤에 다시 "{locator1}" "{action1}" 그다음 "{locator3}"을 "{action3}" 하여 챌린지참여 페이지 진입')
    def prod_home00049_ios_step(self, action1,action2,action3, locator1,locator2,locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action1: locator1},
                                                                                            {action3: locator3}
                                                                                            ))
    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 챌린지참여 페이지 정상노출되는지 확인. 그 후 "{locator2}"을 "{action2}" 하여 홈화면 복귀 후 "{locator3}" 만큼 "{action3}"')
    def prod_home00049_ios_check(self, expected_result, action1, action2,action3, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action3: locator3}))


    @when(
        '홈화면에서 "{locator1}" "{action1}" "{locator2}" 만큼 "{action2}"한 뒤에 다시 "{locator1}" "{action1}" 그다음 "{locator3}"을 "{action3}" 하여 크리에이터 페이지 진입')
    def prod_home00050_ios_step(self, action1, action2, action3, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action1: locator1},
                                                                                            {action3: locator3}
                                                                                            ))


    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 크리에이터 페이지 정상노출되는지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀 후 "{locator3}" 만큼 "{action3}"')
    def prod_home00050_ios_check(self, expected_result, action1, action2, action3, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action3: locator3}))


    @when(
        '홈화면에서 "{locator1}" "{action1}" "{locator2}" 만큼 "{action2}"한 뒤에 다시 "{locator1}" "{action1}" 그다음 "{locator3}"을 "{action3}" 하여 장보기 페이지 진입')
    def prod_home00051_ios_step(self, action1, action2, action3, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action1: locator1},
                                                                                            {action3: locator3}
                                                                                            ))


    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 장보기 페이지 정상노출되는지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀 후 "{locator3}" 만큼 "{action3}"')
    def prod_home00051_ios_check(self, expected_result, action1, action2, action3, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action3: locator3}))


    @when(
        '홈화면에서 "{locator1}" "{action1}" "{locator2}" 만큼 "{action2}"한 뒤에 다시 "{locator1}" "{action1}" 그다음 "{locator3}"을 "{action3}" 하여 리모델링 페이지 진입')
    def prod_home00053_ios_step(self, action1, action2, action3, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action1: locator1},
                                                                                            {action3: locator3}
                                                                                            ))


    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 리모델링 페이지 정상노출되는지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀 후 "{locator3}" 만큼 "{action3}"')
    def prod_home00053_ios_check(self, expected_result, action1, action2, action3, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action3: locator3},
                                                                                                 {action3: locator3}))


    @when(
        '홈화면에서 "{locator1}" "{action1}" "{locator2}" 만큼 "{action2}"한 뒤에 1번더 반복, 그다음 "{locator3}"을 "{action3}" 하여 입주청소 페이지 진입')
    def prod_home00054_ios_step(self, action1, action2, action3, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action1: locator1},
                                                                                            {action3: locator3}
                                                                                            ))
    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 입주청소 페이지 정상노출되는지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀 후 "{locator3}" "{action3}" 그다음 "{locator4}" 만큼 "{action4}"를 한번더 반복')
    def prod_home00054_ios_check(self, expected_result, action1, action2, action3,action4, locator1, locator2, locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action3: locator3},
                                                                                                 {action4: locator4},
                                                                                                 {action3: locator3},
                                                                                                 {action4: locator4}
                                                                                                 ))
class MyPage:
    @when('홈화면에서 "{locator1}"를 "{action1}"한 뒤에 마이페이지 진입')
    def prod_my_page00001_ios_step(self, action1,locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then('"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 마이페이지 정상노출 된지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_my_page00001_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))
    @when('홈화면에서 "{locator1}" 다음 "{locator2}"를 순서대로 "{action1}" 해서 마이페이지의 쇼핑탭 진입')
    def prod_my_page00002_ios_step(self, action1, locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2}
                                                                                            ))

    @then('"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 마이페이지의 쇼핑탭이 정상노출 된지 확인. 그 후 "{locator2}", "{locator3}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_my_page00002_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},{action2: locator3}))

    @when('홈화면에서 "{locator1}", "{locator2}", "{locator3}"를 순서대로 "{action1}" 해서 나의리뷰 페이지 진입 "{action2}","{locator4}"')
    def prod_my_page00003_ios_step(self, action1,action2, locator1,locator2,locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3},
                                                                                            {action2: locator4}
                                                                                            ))

    @then('"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 쇼핑탭의 나의리뷰페이지가 정상노출 된지 확인. 그 후 "{locator2}", "{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_my_page00003_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},{action2: locator3},{action2: locator4}))

    @when('홈화면에서 "{locator1}", "{locator2}", "{locator3}" 를 순서대로 "{action1}" 해서 "{locator4}" "{action2}" 내정보수정 페이지 진입')
    def prod_my_page00004_ios_step(self, action1,action2, locator1,locator2,locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3},
                                                                                            {action2: locator4}))

    @then('"{locator1}"과 "{locator2}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 내정보수정 페이지가 정상노출 된지 확인. 그 후 "{locator3}"을 한번, 그리고 "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_my_page00004_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1},
                                                                                            {action1: locator2}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator3},{action2: locator4}))
    @when('홈화면에서 "{locator1}", "{locator2}", "{locator3}" 를 순서대로 "{action1}" 해서 알림설정 페이지 진입')
    def prod_my_page00005_ios_step(self, action1, locator1,locator2,locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}))

    @then('"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 알림설정 페이지가 정상노출 된지 확인. 그 후 "{locator2}", "{locator3}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_my_page00005_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},{action2: locator3}))


    @when('홈화면에서 "{locator1}", "{locator2}", "{locator3}" 를 순서대로 "{action1}" 해서 비밀번호변경 페이지 진입')
    def prod_my_page00008_ios_step(self, action1, locator1,locator2,locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}))

    @then('"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 비밀번호변경 페이지가 정상노출 된지 확인. 그 후 "{action2}"하여 홈화면 복귀')
    def prod_my_page00008_ios_check(self, expected_result, action1, action2, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2}))

    @when('홈화면에서 "{locator1}", "{locator2}", "{locator3}" 를 순서대로 "{action1}" 해서 상품 스크랩북 페이지 진입')
    def prod_my_page00011_ios_step(self, action1, locator1,locator2,locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}))

    @then('"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 상품 스크랩북 페이지가 정상노출 된지 확인. 그 후 "{locator2}", "{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_my_page00011_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},{action2: locator3},{action2: locator4}))
    @when('홈화면에서 "{locator1}", "{locator2}", "{locator3}" 를 순서대로 "{action1}" 해서 나의 문의내역 페이지 진입 "{locator4}","{action2}"')
    def prod_my_page00012_ios_step(self, action1,action2, locator1,locator2,locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action2: locator4},
                                                                                            {action1: locator3}))

    @then('"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 나의 문의내역 페이지가 정상노출 된지 확인. 그 후 "{locator2}", "{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_my_page00012_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},{action2: locator3},{action2: locator4}))

    @when('홈화면에서 "{locator1}", "{locator2}", "{locator3}" 를 순서대로 "{action1}" 해서 고객센터 페이지 진입 "{locator4}","{action2}"')
    def prod_my_page00015_ios_step(self, action1,action2, locator1, locator2, locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action2: locator4},
                                                                                            {action1: locator3}))

    @then('"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 고객센터 페이지가 정상노출 된지 확인. 그 후 "{locator2}", "{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_my_page00015_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},{action2: locator3},{action2: locator4}))

class LifeStyle:
    @when('홈화면에서 "{locator1}"를 "{action1}"한 뒤에 둘러보기 페이지 진입')
    def prod_lifestyle00002_ios_step(self, action1,locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then('"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 둘러보기에서 임의의 해시태그가 정상노출 된지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00002_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))

    @when('홈화면에서 "{locator1}","{locator2}","{locator3}" 를 순서대로 "{action1}" 해서 집들이 상세페이지 진입')
    def prod_lifestyle00003_ios_step(self, action1, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}
                                                                                            ))

    @then(
        '"{locator1}"이 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 집들이의 CDP 정상노출 된지 확인. 그 후 "{locator2}", "{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00003_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    @when('홈화면에서 "{locator1}", "{locator2}"를 "{action1}"하고 "{locator3}"를 "{action2}" 한 뒤에 집사진 상세 페이지 진입')
    def prod_lifestyle00004_ios_step(self, action1,action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action2: locator3}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 집사진의 CDP가 정상노출 된지 확인. 그 후 "{locator2}", "{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00004_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    # @when('홈화면에서 "{locator1}", "{locator2}"를 순서대로 "{action1}" 해서 살림수납 탭 진입 후 "{locator3}" "{action2}" "{locator4}"를 "{action3}" 해서 광고를 제거함.')
    # def prod_lifestyle00005_ios_step(self, action1, action2,action3, locator1, locator2, locator3, locator4):
    #     current_function_name = ProviderFunctionName().get_current_function_name()
    #     JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
    #                                             step=lambda: KeywordMapping.execute_keyword(self, "step",
    #                                                                                         {action1: locator1},
    #                                                                                         {action1: locator2},
    #                                                                                         {action2: locator3},
    #                                                                                         {action3: locator4},
    #                                                                                         ))

    @when('홈화면에서 "{locator1}", "{locator2}","{locator3}"를 순서대로 "{action1}" 해서 살림수납 탭 진입 후 "{locator4}" "{action2}" "{locator5}"를 "{action3}" 해서 광고를 제거함.')
    def prod_lifestyle00005_ios_step(self, action1, action2,action3, locator1, locator2, locator3, locator4,locator5):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3},
                                                                                            {action2: locator4},
                                                                                            {action3: locator5}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 살림수납 페이지가 정상노출 된지 확인. 그 후 "{locator2}","{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00005_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                        ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    # @when('홈화면에서 "{locator1}", "{locator2}"를 순서대로 "{action1}" 해서 콜렉터블 탭 진입')
    # def prod_lifestyle00006_ios_step(self, action1, locator1, locator2):
    #     current_function_name = ProviderFunctionName().get_current_function_name()
    #     JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
    #                                             step=lambda: KeywordMapping.execute_keyword(self, "step",
    #                                                                                         {action1: locator1},
    #                                                                                         {action1: locator2}
    #                                                                                         ))

    @when('홈화면에서 "{locator1}", "{locator2}","{locator3}"를 순서대로 "{action1}" 해서 콜렉터블 탭 진입')
    def prod_lifestyle00006_ios_step(self, action1, locator1, locator2,locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 콜렉터블 페이지가 정상노출 된지 확인. 그 후 "{locator2}","{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00006_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    # @when('홈화면에서 "{locator1}" 다음 "{locator2}" 만큼 "{action1}" 하고 "{locator3}"를 순서대로 "{action2}" 해서 홈스토랑 탭 진입')
    # def prod_lifestyle00007_ios_step(self, action1,action2, locator1, locator2, locator3):
    #     current_function_name = ProviderFunctionName().get_current_function_name()
    #     JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
    #                                             step=lambda: KeywordMapping.execute_keyword(self, "step",
    #                                                                                         {action2: locator1},
    #                                                                                         {action1: locator2},
    #                                                                                         {action2: locator3}
    #                                                                                         ))

    @when('홈화면에서 "{locator1}", "{locator2}","{locator3}"를 순서대로 "{action1}" 해서 홈스토랑 탭 진입')
    def prod_lifestyle00007_ios_step(self, action1, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 홈스토랑 페이지가 정상노출 된지 확인. 그 후 "{locator2}","{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00007_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    # @when('홈화면에서 "{locator1}" 다음 "{locator2}" 만큼 "{action1}" 하고 "{locator3}"를 순서대로 "{action2}" 해서 핫플레이스 탭 진입')
    # def prod_lifestyle00008_ios_step(self, action1, action2, locator1, locator2, locator3):
    #     current_function_name = ProviderFunctionName().get_current_function_name()
    #     JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
    #                                             step=lambda: KeywordMapping.execute_keyword(self, "step",
    #                                                                                         {action2: locator1},
    #                                                                                         {action1: locator2},
    #                                                                                         {action2: locator3}
    #                                                                                         ))

    @when('홈화면에서 "{locator1}", "{locator2}","{locator3}"를 순서대로 "{action1}" 해서 핫플레이스 탭 진입')
    def prod_lifestyle00008_ios_step(self, action1, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 핫플레이스 페이지가 정상노출 된지 확인. 그 후 "{locator2}","{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00008_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    # @when('홈화면에서 "{locator1}" 다음 "{locator2}" 만큼 "{action1}"를 두번 하고 "{locator3}"를 순서대로 "{action2}" 해서 육아 탭 진입')
    # def prod_lifestyle00009_ios_step(self, action1, action2, locator1, locator2, locator3):
    #     current_function_name = ProviderFunctionName().get_current_function_name()
    #     JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
    #                                             step=lambda: KeywordMapping.execute_keyword(self, "step",
    #                                                                                         {action2: locator1},
    #                                                                                         {action1: locator2},
    #                                                                                         {action1: locator2},
    #                                                                                         {action2: locator3}
    #                                                                                         ))

    @when('홈화면에서 "{locator1}", "{locator2}","{locator3}"를 순서대로 "{action1}" 해서 육아 탭 진입')
    def prod_lifestyle00009_ios_step(self, action1, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 육아 페이지가 정상노출 된지 확인. 그 후 "{locator2}","{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00009_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    # @when('홈화면에서 "{locator1}" 다음 "{locator2}" 만큼 "{action1}"를 두번 하고 "{locator3}"를 순서대로 "{action2}" 해서 플랜테리어 탭 진입')
    # def prod_lifestyle00010_ios_step(self, action1, action2, locator1, locator2, locator3):
    #     current_function_name = ProviderFunctionName().get_current_function_name()
    #     JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
    #                                             step=lambda: KeywordMapping.execute_keyword(self, "step",
    #                                                                                         {action2: locator1},
    #                                                                                         {action1: locator2},
    #                                                                                         {action1: locator2},
    #                                                                                         {action2: locator3}
    #                                                                                         ))

    @when('홈화면에서 "{locator1}", "{locator2}","{locator3}"를 순서대로 "{action1}" 해서 플랜테리어 탭 진입')
    def prod_lifestyle00010_ios_step(self, action1, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 플랜테리어 페이지가 정상노출 된지 확인. 그 후 "{locator2}","{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00010_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))
    # @when('홈화면에서 "{locator1}" 다음 "{locator2}" 만큼 "{action1}"를 두번 하고 "{locator3}"를 순서대로 "{action2}" 해서 반려동물 탭 진입')
    # def prod_lifestyle00011_ios_step(self, action1, action2, locator1, locator2, locator3):
    #     current_function_name = ProviderFunctionName().get_current_function_name()
    #     JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
    #                                             step=lambda: KeywordMapping.execute_keyword(self, "step",
    #                                                                                         {action2: locator1},
    #                                                                                         {action1: locator2},
    #                                                                                         {action1: locator2},
    #                                                                                         {action2: locator3}
    #                                                                                         ))

    @when('홈화면에서 "{locator1}", "{locator2}","{locator3}"를 순서대로 "{action1}" 해서 반려동물 탭 진입')
    def prod_lifestyle00011_ios_step(self, action1, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 반려동물 페이지가 정상노출 된지 확인. 그 후 "{locator2}","{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00011_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    # @when('홈화면에서 "{locator1}" 다음 "{locator2}" 만큼 "{action1}"를 세번 하고 "{locator3}"를 순서대로 "{action2}" 해서 캠핑 탭 진입')
    # def prod_lifestyle00012_ios_step(self, action1, action2, locator1, locator2, locator3):
    #     current_function_name = ProviderFunctionName().get_current_function_name()
    #     JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
    #                                             step=lambda: KeywordMapping.execute_keyword(self, "step",
    #                                                                                         {action2: locator1},
    #                                                                                         {action1: locator2},
    #                                                                                         {action1: locator2},
    #                                                                                         {action1: locator2},
    #                                                                                         {action2: locator3}
    #                                                                                         ))

    @when('홈화면에서 "{locator1}", "{locator2}","{locator3}"를 순서대로 "{action1}" 해서 캠핑 탭 진입')
    def prod_lifestyle00012_ios_step(self, action1, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 캠핑 페이지가 정상노출 된지 확인. 그 후 "{locator2}","{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00012_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    # @when('홈화면에서 "{locator1}" 다음 "{locator2}" 만큼 "{action1}"를 세번 하고 "{locator3}"를 순서대로 "{action2}" 해서 취미 탭 진입')
    # def prod_lifestyle00013_ios_step(self, action1, action2, locator1, locator2, locator3):
    #     current_function_name = ProviderFunctionName().get_current_function_name()
    #     JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
    #                                             step=lambda: KeywordMapping.execute_keyword(self, "step",
    #                                                                                         {action2: locator1},
    #                                                                                         {action1: locator2},
    #                                                                                         {action1: locator2},
    #                                                                                         {action1: locator2},
    #                                                                                         {action2: locator3}
    #                                                                                         ))

    @when('홈화면에서 "{locator1}", "{locator2}","{locator3}"를 순서대로 "{action1}" 해서 취미 탭 진입')
    def prod_lifestyle00013_ios_step(self, action1, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 취미 페이지가 정상노출 된지 확인. 그 후 "{locator2}","{locator3}", "{locator4}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00013_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    @when('"{locator1}","{locator2}","{locator3}" 를 순서대로 "{action1}" 해서 바텀시트를 통해 집들이탭 진입')
    def prod_lifestyle00014_ios_step(self, action1, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}
                                                                                            ))

    @then(
        '"{locator1}"이 "{action1}" 된지 확인 후 "{expected_result}"와 비교해서 집들이탭의 페이지가 정상노출 된지 확인. 그 후 "{locator2}", "{locator3}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_lifestyle00014_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

class Search:
    @given('홈화면에서 "{locator1}"를 "{action1}"한다음 "{locator2}"를 "{action2}"하고 "{locator3}"를 "{action3}"하여 SRP 진입')
    def prod_search00001_ios_step(self, action1,action2,action3,locator1,locator2,locator3):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3}
                                                                                            ))

    @then('"{locator1}"의 "{action1}" 하고나서 "{expected_result}" 텍스트가 맞는지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_search00001_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))

    @when('"{locator1}"만큼 "{action1}"해서 "{locator2}" 버튼을 "{action2}"')
    def prod_search00002_ios_step(self, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2}
                                                                                            ))

    @then('"{locator1}"이 "{action1}" 된지 확인하고 "{expected_result}" 가 맞는지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_search00002_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))


    @when('"{locator1}"을 "{action1}" 해서 필터뷰를 노출시킴')
    def prod_search00003_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then('"{locator1}"이 "{action1}" 된지 확인하고 "{expected_result}" 가 맞는지 확인. 그 후 "{locator2}" , "{locator3}"을 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_search00003_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @when('"{locator1}"을 "{action1}" 해서 사진 타이틀을 찾기 시도')
    def prod_search00004_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then('"{locator1}"의 "{action1}" 하고나서 쇼핑 텍스트가 아닌 "{expected_result}" 텍스트가 맞는지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_search00004_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))



    @when('"{locator1}"을 "{action1}" 해서 더보기를 찾은 뒤 "{action2}"')
    def prod_search00005_ios_step2(self, action1,action2, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator1}
                                                                                            ))

    @then('"{locator1}"가 "{action1}" 된지 확인하고 "{expected_result}" 가 맞는지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_search00005_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))

    @when('"{locator1}"만큼 "{action1}"한 뒤에 "{locator2}"을 "{action2}" 해서 노하우 컨텐츠 타이틀을 찾기 시도')
    def prod_search00006_ios_step(self, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2}
                                                                                            ))

    @then('"{locator1}"가 "{action1}" 된지 확인하고 "{expected_result}" 가 맞는지 확인해서 노하우컨텐츠 타이틀이 노출된지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_search00006_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))



    @when('"{locator1}"만큼 "{action1}"한 뒤에 "{locator2}"을 "{action2}" 해서 노하우 컨텐츠의 더보기 찾은 뒤 "{action3}"')
    def prod_search00007_ios_step2(self, action1, action2, action3, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator2}
                                                                                            ))

    @then('"{locator1}"가 "{action1}" 된지 확인하고 "{expected_result}" 가 맞는지 확인해서 컨텐츠의 노하우 필터가 정상적인지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_search00007_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))


    @when('"{locator1}"만큼 "{action1}"한 뒤에 "{locator2}"을 "{action2}" 해서 집들이 컨텐츠 타이틀을 찾기 시도')
    def prod_search00008_ios_step2(self, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2}
                                                                                            ))

    @then('"{locator1}"가 "{action1}" 된지 확인하고 "{expected_result}" 가 맞는지 확인해서 집들이컨텐츠 타이틀이 노출된지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_search00008_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))

    @when('"{locator1}"만큼 "{action1}"한 뒤에 "{locator2}"을 "{action2}" 해서 집들이 컨텐츠의 더보기 찾은 뒤 "{action3}"')
    def prod_search00009_ios_step2(self, action1, action2, action3, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator2}
                                                                                            ))

    @then('"{locator1}"가 "{action1}" 된지 확인하고 "{expected_result}" 가 맞는지 확인해서 컨텐츠의 집들이 필터가 정상적인지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_search00009_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))

    @when('"{locator1}" "{action1}" "{locator2}"을 "{action2}" 해서 시공업체 타이틀을 찾기 시도')
    def prod_search00010_ios_step2(self, action1, locator1, action2, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2}
                                                                                            ))

    @then('"{locator1}"가 "{action1}" 된지 확인하고 "{expected_result}" 가 맞는지 확인해서 시공업체 타이틀이 노출된지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_search00010_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))

    @when('"{locator1}"만큼 "{action1}"한 뒤에 "{locator2}"을 "{action2}" 해서 시공업체의 더보기 찾은 뒤 "{action3}"')
    def prod_search00011_ios_step2(self, action1, action2, action3, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator2}
                                                                                            ))

    @then('"{locator1}"가 "{action1}" 된지 확인하고 "{expected_result}" 가 맞는지 확인해서 시공업체 페이지가 정상적인지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_search00011_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))

    @when('"{locator1}"을 "{action1}"해서 유저탭 진입')
    def prod_search00012_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then('"{locator1}"가 "{action1}" 된지 확인하고 "{expected_result}" 가 맞는지 확인해서 유저탭의 유저가 정상노출 되는지 확인. 그 후 "{locator2}"을 "{action2}"하여 홈화면 복귀')
    def prod_search00012_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}))

class O2O:
    @given('홈화면에서 "{locator1}","{action1}","{locator2}"를 "{action2}"해서 주거공간 시공페이지 진입 확인 "{locator3}","{action3}","{locator4}","{action4}","{locator5}","{action5}"')
    def prod_o2o00001_ios_step(self, action1,action2,action3,action4,action5,locator1,locator2,locator3,locator4,locator5):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3}
                                                                                            ,{action4: locator4}
                                                                                            ,{action5: locator5}
                                                                                            ))

    @when('"{locator1}"가 보이면 "{action1}" 해서 주거공간 시공페이지의 광고를 제거 후 "{locator2}"를 "{action2}" 마무리')
    def prod_o2o00001_ios_step(self, action1, locator1,action2,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 주거시공 페이지가 정상노출된지 체크. 그 후 "{locator3}", "{locator4}" 를 순서대로 "{action3}"하여 홈화면 복귀')
    def prod_o2o00001_ios_check(self, expected_result, action1, locator1, locator3, locator4, action3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action3: locator3},
                                                                                                 {action3: locator4}))

    @given('홈화면에서 "{locator1}","{locator2}"를 "{action1}"해서 상업 시공페이지 진입 확인')
    def prod_o2o00002_ios_step(self, action1, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},{action1: locator2}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 상업시공 페이지가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00002_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @when('홈화면에서 "{locator1}","{locator2}"를 "{action1}"해서 인테리어 상담소 페이지 진입 확인')
    def prod_o2o00003_ios_step(self, action1, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 인테리어 상담소 페이지가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00003_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @given('홈화면에서 "{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}"해서 o2o 자재랭킹 페이지 진입 확인')
    def prod_o2o00004_ios_step(self, action1,action2,action3,locator1,locator2,locator3):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3}
                                                                                            ))

    @when('"{locator1}","{action1}"해서 o2o 자재랭킹 페이지 진입 확인')
    def prod_o2o00004_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 o2o 자재랭킹 페이지가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00004_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @given('홈화면에서 "{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3}","{locator4}","{action4}"해서 o2o 계약서진단 페이지 진입 확인')
    def prod_o2o00005_ios_step(self, action1,action2,action3,action4,locator1,locator2,locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action4: locator4}
                                                                                            ))

    @when('"{locator1}","{action1}"해서 o2o 계약서진단 페이지 진입 확인')
    def prod_o2o00005_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 o2o 계약서진단 페이지가 정상노출된지 체크. 그 후 "{locator2}","{locator3}","{locator4}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00005_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    @given('홈화면에서 "{locator1}","{action1}","{locator2}","{action2}","{locator3}","{action3},"{locator4}","{action4}"해서 o2o 견적계산기 페이지 진입 확인')
    def prod_o2o00006_ios_step(self, action1,action2,action3,action4,locator1,locator2,locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action4: locator4}
                                                                                            ))

    @when('"{locator1}","{action1}"해서 o2o 견적계산기 페이지 진입 확인')
    def prod_o2o00006_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 o2o 견적계산기 페이지가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00006_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @when('홈화면에서 "{locator1}","{locator2}"를 "{action1}"해서 o2o 이사 페이지 진입 확인')
    def prod_o2o00007_ios_step(self, action1, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 o2o 이사 페이지가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00007_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @when('홈화면에서 "{locator1}","{locator2}"를 "{action1}"해서 o2o 입주청소 페이지 진입 확인')
    def prod_o2o00008_ios_step(self, action1, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 o2o 입주청소 페이지가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00008_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @when('홈화면에서 "{locator1}","{locator2}"를 "{action1}"해서 o2o 제품설치 페이지 진입 확인')
    def prod_o2o00009_ios_step(self, action1, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator2}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 o2o 제품설치 페이지가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00009_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @when('홈화면에서 "{locator1}"를 "{action1}"해서 o2o 전체서비스 페이지 진입 확인')
    def prod_o2o00010_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @when('"{locator1}"를 "{action1}" 해서 전체서비스 페이지 진입 확인')
    def prod_o2o00010_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @when('"{locator1}"만큼 "{action1}"해서 집보기 체크리스트 노출 확인')
    def prod_o2o00010_ios_step3(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @when('"{locator1}"를 "{action1}" 해서 집보기 체크리스트 페이지 진입 확인')
    def prod_o2o00010_ios_step4(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @when('"{locator1}"가 보이면 "{action1}" 해서 집보기 체크리스트 바텀시트를 제거')
    def prod_o2o00010_ios_step5(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 o2o 집보기 체크리스트 페이지가 정상노출된지 체크. 그 후 "{locator2}"를 "{action2}"하여 홈화면 복귀')
    def prod_o2o00010_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}
                                                                                                 ))

    @when('홈화면에서 "{locator1}"를 "{action1}"해서 o2o 페이지 진입 확인(아파트 시공사례)')
    def prod_o2o00011_ios_step(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @when('"{locator1}"를 "{action1}"해서 전체서비스 페이지 진입 확인(아파트 시공사례)')
    def prod_o2o00011_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @when('"{locator1}"만큼 "{action1}"해서 아파트 시공사례 노출 확인')
    def prod_o2o00011_ios_step3(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))
        
    @when('"{locator1}"를 "{action1}"해서 아파트 시공사례 페이지 진입 확인')
    def prod_o2o00011_ios_step4(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))
        
    @then(
        '"{locator1}"이 "{action1}"된지 확인하고 "{expected_result}"된지 확인하여 o2o 아파트 시공사례 페이지가 정상노출된지 체크. 그 후 "{locator2}"를 "{action2}"하여 홈화면 복귀')
    def prod_o2o00011_ios_check(self, expected_result, action1, action2, locator1, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2}
                                                                                                ))

    @then(
        '"{locator1}"이 "{action1}"된지 확인하고 "{expected_result}"된지 확인하여 주거시공 페이지의 시공업체탭이 정상노출된지 체크. 그 후 "{locator2}","{locator3}"를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00012_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))
    
    
    @when('"{locator1}"를 "{action1}" 해서 시공사례 탭 진입')
    def prod_o2o00013_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 주거시공 페이지의 시공사례탭이 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00013_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @when('"{locator1}"를 "{action1}" 해서 간편매칭 탭 진입')
    def prod_o2o00014_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 주거시공 페이지의 간편매칭탭이 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00014_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @when('"{locator1}"를 "{action1}" 해서 부분시공 탭 진입')
    def prod_o2o00015_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 주거시공 페이지의 부분시공탭이 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00015_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 상업시공 페이지의 간편상담 탭이 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00016_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @when('"{locator1}"를 "{action1}" 해서 업체찾기 탭 진입')
    def prod_o2o00017_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 상업시공 페이지의 업체찾기 탭이 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_o2o00017_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))


class Commerce_Service:
    @given('홈화면에서 "{locator1}"을 "{action1}"해서 쇼핑홈 페이지 진입 확인')
    def prod_commerce_service00001_ios_step1(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @when('"{locator1}"를 "{action1}" 하고 "{locator2}"을 "{action2}"해서 쇼핑홈 검색페이지 진입')
    def prod_commerce_service00001_ios_step2(self, action1, locator1,action2, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 검색 페이지가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_service00001_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @when('"{locator1}"를 "{action1}" 하고 "{locator2}"을 "{action2}"해서 쇼핑홈 배너페이지 진입')
    def prod_commerce_service00002_ios_step2(self, action1,action2, locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 배너 페이지가 정상노출된지 체크. 그 후 "{locator2}" "{action2}", "{locator3}"를 "{action3}" 하고 "{locator4}" 를 "{action4}"하여 홈화면 복귀')
    def prod_commerce_service00002_ios_check(self, expected_result, action1, action2,action3, action4, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action3: locator3},
                                                                                                 {action4: locator4}))

    @when('"{locator1}","{action1}" 후 다음스텝 진행')
    def prod_commerce_service00003_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))
    @then(
        '"{locator1}", "{locator2}", "{locator3}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 캐래설이 정상노출된지 체크. 그 후 "{locator5}","{locator4}" 을 "{action2}"하여 홈화면 복귀')
    def prod_commerce_service00003_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4,locator5):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator5},
                                                                                                 {action2: locator4}))

    @when('"{locator1}"를 "{action1}" 하고 "{locator2}","{action2}", "{locator3}" "{action3}","{locator3}","{locator4}"을 순서대로 "{action4}"해서 쇼핑홈 카테고리페이지 진입')
    def prod_commerce_service00004_ios_step2(self, action1, action2,action3,action4, locator1, locator2,locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action4: locator3},
                                                                                            {action4: locator4}
                                                                                            ))

    @then(
        '"{locator1}", "{locator2}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 1~4뎁스가 정상노출된지 체크. 그 후 "{locator3}", "{locator4}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_service00004_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1},
                                                                                            {action1: locator2}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    @when('"{locator1}"를 "{action1}"한 뒤에 "{locator2}" "{action2}" "{locator3}"을 순서대로 "{action3}"해서 쇼핑홈 배너 진입 "{action4}"')
    def prod_commerce_service00005_ios_step2(self, action1,action2,action3,action4, locator1, locator2,locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action4: locator1},
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3}
                                                                                            ))

    @then(
        '"{locator1}"이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 카테고리 배너가 정상노출된지 체크. 그 후 "{action2}" 하여 홈화면 복귀')
    def prod_commerce_service00005_ios_check(self, expected_result, action1, action2, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2}))

    @when('"{locator1}"를 "{action1}" 하고 "{locator2}"를 "{action2}"한 뒤에 "{locator3}"가 "{action3}" 한 뒤에 "{locator4}" "{action4}"해서 mds pick의 pdp 진입 "{action5}"')
    def prod_commerce_service00006_ios_step2(self, action1,action2,action3,action4,action5, locator1, locator2,locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action5: locator2},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action4: locator4}
                                                                                            ))

    @then(
        '"{locator1}"이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 mds pick의 pdp가 정상노출된지 체크. 그 후 "{locator2}","{locator3}"를 "{action2}" 하고 "{locator4}" 를 순서대로 "{action3}"하여 홈화면 복귀')
    def prod_commerce_service00006_ios_check(self, expected_result, action1, action2,action3, locator1, locator2, locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action3: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action3: locator4}))

    @when('"{locator1}"를 "{action1}" 하고 "{locator2}"를 "{action2}"한 뒤에 "{locator3}"가 "{action3}" 한 뒤에 "{locator4}" "{action4}" 후 "{action5}"해서 카테고리 필터 노출 "{action6}"')
    def prod_commerce_service00007_ios_step2(self, action1,action2,action3,action4,action5,action6, locator1, locator2, locator3,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action6: locator2},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action4: locator4},
                                                                                            {action5: locator3},
                                                                                            ))

    @then(
        '"{locator1}"이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 카테고리 필터가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}", "{locator5}"를 "{action3}", "{locator4}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_service00007_ios_check(self, expected_result, action1, action2,action3, locator1, locator2, locator3, locator4,locator5):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action3: locator5},
                                                                                                 {action2: locator4}))

    @when('"{locator5}"를 "{action6}" 하고 "{locator1}"를 "{action1}"한 뒤에 "{locator2}"가 "{action2}" 한 뒤에 "{locator3}" "{action3}" 후 "{locator4}"가 "{action4}" 하고나서 "{action5}"해서 카테고리 상품리스트의 pdp 진입 "{action7}"')
    def prod_commerce_service00008_ios_step2(self, action1,action2,action3,action4, action5,action6,action7, locator1, locator2, locator3, locator4, locator5):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action6: locator5},
                                                                                            {action7: locator1},
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action4: locator4},
                                                                                            {action5: locator4}
                                                                                            ))

    @then(
        '"{locator1}"이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 카테고리의 상품리스트 pdp가 정상노출된지 체크. 그 후 "{locator2}" "{action2}" 한 뒤에 "{action3}" 하고 "{locator3}" 를 순서대로 "{action4}"하여 홈화면 복귀')
    def prod_commerce_service00008_ios_check(self, expected_result, action1, action2,action3,action4,locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action3: locator2},
                                                                                                 {action4: locator3}))

    @when('"{locator1}"를 "{action1}" 하고 "{locator4}","{action4}", "{locator2}"를 "{action2}" 한 뒤에 "{action3}" 해서 아이템캐러셀 pdp 진입')
    def prod_commerce_service00009_ios_step2(self, action1,action2,action3,action4, locator1,locator2,locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action4: locator4},
                                                                                            {action2: locator2},
                                                                                            {action3: locator2}
                                                                                            ))

    @then(
        '"{locator1}"이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 아이템캐러셀 상품리스트 pdp가 정상노출된지 체크. 그 후"{action2}"하여 홈화면 복귀')
    def prod_commerce_service00009_ios_check(self, expected_result, action1, action2, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 action2))

    @when('"{locator1}"를 "{action1}" 한 뒤에 아이템캐러셀에서 오늘의 추천상품 타이틀에서 멈춤')
    def prod_commerce_service00010_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 아이템캐러셀 오늘의 추천상품 광고가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_service00010_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))
    @when('"{locator1}"를 "{action1}" 하고 "{locator2}"를 "{action2}" 한 뒤에 아이템캐러셀에서 BEST메뉴에서 멈춤')
    def prod_commerce_service00011_ios_step2(self, action1,action2, locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 아이템캐러셀 BEST메뉴가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_service00011_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))
    @when('"{locator1}"를 "{action1}" 한 뒤에 아이템캐러셀에서 오늘의딜메뉴에서 멈춤')
    def prod_commerce_service00012_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 아이템캐러셀 오늘의딜메뉴가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_service00012_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @when('"{locator1}"를 "{action1}" 한 뒤에 아이템캐러셀 오늘의딜 타이틀에서 멈춤')
    def prod_commerce_service00014_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @when('"{locator1}"를 "{action1}" 한 뒤에 "{action2}"해서 아이템캐러셀에서 오늘의딜메뉴의 더보기 진입')
    def prod_commerce_service00014_ios_step3(self, action1, action2, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator1}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 아이템캐러셀 오늘의딜 상세페이지가 정상노출된지 체크. 그 후 "{locator2}","{locator5}"를 "{action3}","{locator3}", "{locator4}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_service00014_ios_check(self, expected_result, action1, action2,action3, locator1, locator2, locator3, locator4,locator5):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action3: locator5},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))
    @when('"{locator1}"만큼 "{action1}"해서 쇼핑홈 인기검색어 스크롤 준비')
    def prod_commerce_service00017_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @when('"{locator1}"를 "{action1}" 한 뒤에 아이템캐러셀 실시간인기검색어 타이틀에서 멈춤')
    def prod_commerce_service00017_ios_step3(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 아이템캐러셀 실시간인기검색어가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_service00017_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

    @when('"{locator1}"만큼 "{action1}"해서 쇼핑홈 광고 카테고리1 스크롤 준비')
    def prod_commerce_service00018_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @when('"{locator1}"를 "{action1}" 한 뒤에 아이템캐러셀 광고카테고리1 타이틀에서 멈춤')
    def prod_commerce_service00018_ios_step3(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}"가 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 아이템캐러셀 광고카테고리1이 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_service00018_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))
    @when('"{locator1}"만큼 "{action1}"해서 쇼핑홈 광고 카테고리2 스크롤 준비')
    def prod_commerce_service00019_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @when('"{locator1}"를 "{action1}" 한 뒤에 한번더 반복해서 아이템캐러셀 광고카테고리2 타이틀에서 멈춤')
    def prod_commerce_service00019_ios_step3(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action1: locator1}
                                                                                            ))

    @then('"{locator1}"가 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑홈 아이템캐러셀 광고카테고리2가 정상노출된지 체크. 그 후 "{locator2}", "{locator3}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_service00019_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}
                                                                                            ),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3}))

class Commerce_Platform:
    @given('앱 재시작')
    def prod_commerce_platform00001_ios_step0(self):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "restart"
                                                                                            ))
    @given('홈화면에서 "{locator1}"를 "{action1}"한 뒤에 "{condition}" "{locator2}"가 "{action2}"되어있으면 "{locator3}"를 "{action3}" "{locator4}"을 "{action4}"해서 담겨있는 상품 제거 후 "{locator5}"을 "{action5}" 하여 홈화면 복귀')
    def prod_commerce_platform00001_ios_step1(self, action1,condition, locator1, action2, locator2, action3,action4,action5, locator3,locator4, locator5):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {condition:{action2:locator2,action3:locator3,action4:locator4}},
                                                                                            {action5: locator5}
                                                                                            ))

    @when(
        '스크랩화면에서 "{condition}","{locator1}"가 "{action1}"되어있다면 "{locator2}"를 "{action2}"하고"{locator3}"을 "{action3}"한뒤에 "{locator4}"을 "{action4}" 하여 홈화면 복귀')
    def prod_commerce_platform00001_ios_step1_2(self, action1, condition, locator1, action2, locator2, action3, action4,locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {condition: {action1: locator1,action2: locator2,action3: locator3,action4: locator4}}

                                                                                            ))

    @when('스크랩화면 진입 후 "{locator1}"을 "{action1}"해서 pdp 페이지 진입 "{locator2}"')
    def prod_commerce_platform00001_ios_step2(self, action1, locator1,locator2):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator2},
                                                                                            {action1: locator1}
                                                                                            ))

    @when('"{locator7}","{action4}",pdp에서 "{locator1}" 을 "{action1}" 하고 "{locator2}" "{action2}" "{locator3}"를 "{action3}" 하고 "{locator2}" "{action2}" "{locator4}", "{locator5}", "{locator6}"를 순서대로 "{action3}"해서 장바구니에 담은 뒤 장바구니 진입')
    def prod_commerce_platform00001_ios_step3(self, action1, action2,action3, action4,locator1, locator2, locator3, locator4, locator5, locator6,locator7):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action4: locator7},
                                                                                            {action1: locator1},
                                                                                            {action2: locator2},
                                                                                            {action3: locator3},
                                                                                            {action2: locator2},
                                                                                            {action3: locator4},
                                                                                            {action2: locator2},
                                                                                            {action3: locator5},
                                                                                            {action3: locator6},
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 장바구니에 상품이 담긴지 체크. 그 후 "{locator2}"을 "{action2}" 한뒤에 "{locator3}"을 "{action3}"해서 담겨있는 상품 제거 후 "{action4}" 하여 홈화면 복귀')
    def prod_commerce_platform00001_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, action3, action4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action3: locator3},
                                                                                                 action4))

    @when('홈화면에서 앱 간헐적 실패를 막기위한"{action2}"후,"{locator1}"를 "{action1}"한뒤에 스크랩화면 노출 확인')
    def prod_commerce_platform00003_ios_step1(self, action1, locator1,action2):
        current_function_name = ProviderFunctionName().get_current_function_name(scenario=self.scenario.name)
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                       step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                   action2,
                                                                                                   {action1: locator1}))

    @when('"{locator5}","{action2}",pdp에서 "{locator1}","{locator2}","{locator3}", "{locator4}" 를 순서대로 "{action1}"해서 주문서 진입')
    def prod_commerce_platform00003_ios_step3(self, action1,action2, locator1, locator2, locator3, locator4,locator5):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action2: locator5},
                                                                                            {action1: locator1},
                                                                                            {action1: locator2},
                                                                                            {action1: locator3},
                                                                                            {action1: locator4}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 주문서 페이지 정상진입 확인. 그 후 "{locator2}","{locator3}", "{locator4}" 를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_platform00003_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    @when('"{locator1}" "{action1}" 장바구니에서 "{locator2}"을 "{action2}"해서 장바구니 -> 주문서 이동')
    def prod_commerce_platform00005_ios_step4(self, action1, locator1, action2, locator2):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1},
                                                                                            {action2: locator2}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 장바구니를 통한 주문서 페이지 정상진입 확인. 그 후 "{locator2}","{locator3}"를 순서대로 "{action2}"하고 "{locator4}" , "{locator5}" 만큼 "{action3}" 실행 후 "{action4}"하여 홈화면 복귀 "{locator6}","{action5}')
    def prod_commerce_platform00005_ios_check(self, expected_result, action1, action2,action3,action4,action5, locator1, locator2, locator3, locator4, locator5,locator6):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action5: locator6},
                                                                                                 {action2: locator3},
                                                                                                 {action3: locator4},
                                                                                                 {action3: locator5},
                                                                                                 action4))

    @when('"{locator1}"을 "{action1}" 해서 쇼핑탭의 주문배송 목록 페이지 진입')
    def prod_commerce_platform00007_ios_step4(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 주문배송 목록 페이지 정상진입 확인. 그 후 "{locator2}","{locator3}", "{locator4}"를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_platform00007_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    @given('commerce_platform00008 결과값 확인해서 데이터셋 반복 여부 체크')
    def prod_commerce_platform00008_ios_pre(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "skip",
                                                                                            current_function_name
                                                                                            ))
    @when('"{locator1}"을 "{action1}" 해서 주문배송 상태페이지 진입')
    def prod_commerce_platform00008_ios_step4(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 주문배송 상태페이지가 "{expected_result}" 인지 확인. 그 후 "{locator2}", "{locator3}" "{locator4}"를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_platform00008_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    @when('"{locator1}"을 "{action1}" 해서 쇼핑탭의 포인트 페이지 진입')
    def prod_commerce_platform00009_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑탭 포인트 페이지 정상진입 확인. 그 후 "{locator2}","{locator3}", "{locator4}"를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_platform00009_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    @when('"{locator1}"을 "{action1}" 해서 쇼핑탭의 쿠폰 페이지 진입')
    def prod_commerce_platform00010_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑탭 쿠폰 페이지 정상진입 확인. 그 후 "{locator2}","{locator3}", "{locator4}"를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_platform00010_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))

    @when('"{locator1}"을 "{action1}" 해서 쇼핑탭의 회원등급 페이지 진입')
    def prod_commerce_platform00011_ios_step2(self, action1, locator1):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                            {action1: locator1}
                                                                                            ))

    @then(
        '"{locator1}" 이 "{action1}"된지 확인하고 "{expected_result}" 된지 확인하여 쇼핑탭 회원등급 페이지 정상진입 확인. 그 후 "{locator2}","{locator3}", "{locator4}"를 순서대로 "{action2}"하여 홈화면 복귀')
    def prod_commerce_platform00011_ios_check(self, expected_result, action1, action2, locator1, locator2, locator3, locator4):
        current_function_name = ProviderFunctionName().get_current_function_name()
        JenkinsExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: KeywordMapping.execute_keyword(self, "result", "equal",
                                                                                            expected_result,
                                                                                            {action1: locator1}),
                                                back_flow=lambda: KeywordMapping.execute_keyword(self, "step",
                                                                                                 {action2: locator2},
                                                                                                 {action2: locator3},
                                                                                                 {action2: locator4}))