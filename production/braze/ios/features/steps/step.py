from behave import given, when, then
from app.common.base_method.jenkins_exception_func import ExceptionHandler
from app.common.base_method.appium_method import ProviderCommonMethod
from app.common.base_method.app_start_func import AppStart
from app.common.base_method.get_function_name_func import ProviderFunctionName

# api
from production.braze.api.braze_get_user_info import GetUserData

from production.braze.ios.procedure.mkt_00059 import MKTBrazeOffSet
from production.braze.ios.procedure.mkt_00059_2 import MKTBrazeOnSet
from production.braze.ios.procedure.mkt_00063 import BrazePushAppActivate
from production.braze.ios.procedure.mkt_00063_2 import BrazePushAppTerminate

class MktBraze:
    @given('앱 삭제 -> 최신앱설치')
    def mkt_00059_1_braze_ios_given(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: MKTBrazeOffSet.given_test(self))

    @when('브레이즈 계정 로그인')
    def mkt_00059_1_braze_ios_step1(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: MKTBrazeOffSet.is_login(self))
    @when('알림허용 팝업에서 미허용 후 알림설정 진입')
    def mkt_00059_1_braze_ios_step2(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: MKTBrazeOffSet.go_noti_set(self))

    @then('push_advertise,push_active_system off 확인')
    def mkt_00059_1_braze_ios_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, False,GetUserData().get_data_user("24653062"))
                                                ,back_flow=MKTBrazeOffSet.back_flow(self)
                                                )


    @given('알림 off상태에서 알림설정 진입')
    def mkt_00059_2_braze_ios_given(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: MKTBrazeOnSet.given_test(self))

    @when('알림설정 on 변경 후 컨펌에서 설정 변경하기 -> 앱 설정에서 알림변경 on 변경 후 오늘의집 앱 복귀 -> 뒤로가기 후 알림설정 재진입')
    def mkt_00059_2_braze_ios_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: MKTBrazeOnSet.go_noti_on_set(self))


    @then('push_advertise,push_active_system on 확인')
    def mkt_00059_2_braze_ios_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, True,
                                                                                                 GetUserData().get_data_user("24653062")
                                                                                                 )
                                                )

    @given("앱 실행중")
    def mkt_00063_1_braze_ios_given(self):
        AppStart.ios_ohou_restart(self)

    @when('앱 push 발신')
    def mkt_00063_1_braze_ios_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: BrazePushAppActivate.push_app(self))

    @then('수신된 푸쉬 선택 후 랜딩페이지 확인')
    def mkt_00063_1_braze_ios_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, True,
                                                                                                 BrazePushAppActivate.actual_result(self)
                                                                                                 )
                                                )

    @given("앱 종료상태")
    def mkt_00063_2_braze_ios_given(self):
        AppStart.ios_ohou_close(self)

    @when('종료상태에서 앱 push 발신')
    def mkt_00063_2_braze_ios_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler(self, current_function_name,
                                                step=lambda: BrazePushAppTerminate.push_app(self))

    @then('종료상태에서 수신된 푸쉬 선택 후 랜딩페이지 확인')
    def mkt_00063_2_braze_ios_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.ios_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, True,
                                                                                               BrazePushAppTerminate.actual_result(
                                                                                                   self)
                                                                                               )
                                                )

