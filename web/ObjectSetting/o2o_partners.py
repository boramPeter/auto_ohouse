from web.BasicSetting.conftest import *
from app.common.base_method.exception_func import timeout_handler

'''
[naming rule]
1. xxxx_func : 여러 케이스에서 참조하는 함수 (expect 없어도됨)
2. into_xxxx : 특정 페이지 진입 +expect로 마무리
3. check_xxxx : complex step 케이스 +expect로 마무리
'''

class o2oPCElements():
    ''' ########################### Func List ###########################'''
    def login_func(page):
        page.get_by_test_id("email").click()
        page.get_by_test_id("email").fill("qa01@1.net")
        page.get_by_test_id("password").click()
        page.get_by_test_id("password").fill("123Asd!@")
        page.get_by_label("로그인 버튼").click()
        page.wait_for_timeout(2000)
    

    ''' ########################### into List ###########################'''
    def into_partners_main(page):
        page.wait_for_timeout(3000)
        o2oPCElements.login_func(page)
        page.wait_for_timeout(1000)
        expect(page.get_by_text("QA01스탠다드"), '메인화면 미노출').to_be_visible()
        

    ''' ########################### Check List ###########################'''
    # def check_myvilage_plus(page):
    #     o2oPCElements.remodeling_func(page)
    #     page.wait_for_timeout(2000)
    #     # expect(page.get_by_role("button", name="우리동네 플러스 광고"), '우리동네 플러스 요소 미노출').to_be_visible()
    #     expect(page.get_by_role("link", name="새로운 시공의 기준 더보기"), '스탠다드 요소 미노출').to_be_visible()
