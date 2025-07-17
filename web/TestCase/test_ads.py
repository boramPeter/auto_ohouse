from web.ObjectSetting.comm_service import *
from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.common_object import *

def checkout(page):
    CommonElements.login_func(page)
    page.wait_for_timeout(2000)
    CommPlatformElements.checkout_func(page)
    page.wait_for_timeout(2000)


def test_search_001(page):
    print("\ntest_search_001 : 로그인 확인", end='')
    PageElements.qaweb_product_url(page)
    page.wait_for_timeout(2000)
    # expect(page.get_by_label("오늘의집 로고"), '"오늘의집 로고" 요소 미노출').to_be_visible()
    page.close()




