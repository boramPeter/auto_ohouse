from behave import given, when, then
from app.common.base_method.jenkins_exception_func import ExceptionHandler
from app.common.base_method.appium_method import ProviderCommonMethod
from app.common.base_method.permission_func import grant_permission_jenkins
from app.common.base_method.app_start_func import AppStart
from app.common.base_method.get_function_name_func import ProviderFunctionName
from app.common.app_config.data import PackageName

# api
from production.braze.api.braze_get_user_info import GetUserData

from production.braze.aos.procedure.mkt_00059 import MKTBrazeOffSet
from production.braze.aos.procedure.mkt_00059_2 import MKTBrazeOnSet
from production.braze.aos.procedure.mkt_00063 import BrazePushAppActivate
from production.braze.aos.procedure.mkt_00063_2 import BrazePushAppTerminate
from app.common.app_config.data import UDID
class MktBraze:
    @when('앱 삭제 및 설치')
    def mkt_00059_1_braze_aos_given_deploy(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: MKTBrazeOffSet.given_deploy_test(self,UDID.aos_prod_udid))

    @given('브레이즈 앱 설치 확인')
    def mkt_00059_1_braze_aos_given(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: MKTBrazeOffSet.given_test(self))
    @when('브레이즈 로그인')
    def mkt_00059_1_braze_aos_step1(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: MKTBrazeOffSet.is_login(self))
    @when('알림설정 진입 후 설정화면 리프레쉬')
    def mkt_00059_1_braze_aos_step2(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: MKTBrazeOffSet.go_noti_set(self))

    @then('push_advertise,push_active_system off 확인')
    def mkt_00059_1_braze_aos_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                    step = lambda: ProviderCommonMethod.assert_equal(self, False,GetUserData().get_data_user("22053457")
                                                    )
                                                )
    @given('알림권한 강제 on')
    def mkt_00059_2_braze_aos_given(self):
        grant_permission_jenkins(PackageName.aos_package_name, UDID.aos_prod_udid,"android.permission.POST_NOTIFICATIONS")

    @when('앱 재시작 -> 알림설정 on 변경 -> 재시작 2번 후 새로고침')
    def mkt_00059_2_braze_aos_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: MKTBrazeOnSet.go_noti_set(self))
    @then('push_advertise,push_active_system on 확인')
    def mkt_00059_2_braze_aos_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, True,
                                                                                                 GetUserData().get_data_user("22053457")
                                                                                                 )
                                                )

    @given("앱 실행중")
    def mkt_00063_1_braze_aos_given(self):
        AppStart.force_app_restart(self, PackageName.aos_package_name)

    @when('앱 push 발신')
    def mkt_00063_1_braze_aos_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: BrazePushAppActivate.push_app(self))

    @then('수신된 푸쉬 선택 후 랜딩페이지 확인')
    def mkt_00063_1_braze_aos_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, True,
                                                                                               BrazePushAppActivate.actual_result(
                                                                                                   self)
                                                                                               )
                                                )

    @given("앱 종료상태")
    def mkt_00063_2_braze_aos_given(self):
        AppStart.android_ohou_close(self)

    @when('종료상태에서 앱 push 발신')
    def mkt_00063_2_braze_aos_step(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self, current_function_name,
                                                step=lambda: BrazePushAppTerminate.push_app(self))

    @then('종료상태에서 수신된 푸쉬 선택 후 랜딩페이지 확인')
    def mkt_00063_2_braze_aos_check(self):
        current_function_name = ProviderFunctionName().get_current_function_name()
        ExceptionHandler.aos_exceptions_handler(self,
                                                current_function_name,
                                                step=lambda: ProviderCommonMethod.assert_equal(self, True,
                                                                                               BrazePushAppTerminate.actual_result(
                                                                                                   self)
                                                                                               )
                                                )


