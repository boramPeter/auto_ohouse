from web.ObjectSetting.comm_service import *
from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.common_object import *
from web.ObjectSetting.lifestyle import *
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.web_result_binary import ResultWeb
from web.BasicSetting.exception_func import *
qa_home = 'https://qa-web.dailyhou.se/'
qa_recommend = 'https://contents.qa-web.dailyhou.se/topics/recommend'


#lifestyle 1417
@pytest.mark.regression
def test_community_00001(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # GNB 탭 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_gnb_menu(page),
                           check=True)

#lifestyle 1487
@pytest.mark.regression
def test_community_00007(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.into_upload_community(page),
                           check=True)


#lifestyle 1488
@pytest.mark.regression
def test_community_00028(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # GNB 탭 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_upload_community_filter(page),
                           check=True)

#lifestyle 1434
@pytest.mark.regression
def test_community_00029(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # GNB 탭 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_upload_community(page),
                           check=True)



#lifestyle 1440
@pytest.mark.regression
def test_community_00035(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 꿀템발견 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_honeyitem_tab())
    # 꿀템발견 탭 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_honeyitem_top(page),
                           check=True)

#lifestyle 1441
@pytest.mark.regression
def test_community_00036(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 꿀템발견 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_honeyitem_tab())
    # CLP 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_honeyitem_chip(page),
                           check=True)
    
#lifestyle 1459
@pytest.mark.regression
def test_community_00037(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 꿀템발견 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_honeyitem_tab())
    # 꿀템발견 탭 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_honeyitem_top(page),
                           check=True)

#lifestyle 1460
@pytest.mark.regression
def test_community_00038(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 꿀템발견 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_honeyitem_tab())
    # 꿀템발견 서브카테고리 칩 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_honeyitem_subcategory(page),
                           check=True)




#lifestyle 1449
@pytest.mark.regression
def test_community_00046(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 꿀템발견 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_honeyitem_tab())
    # cdp 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_honeyitem_cdp(page),
                           check=True)
    


    
#lifestyle 1466
@pytest.mark.regression
def test_community_00052(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 더보기 피드 진입
    page.goto("https://ozip.qa-web.dailyhou.se/mW7URaY", timeout=0) 
    # 꿀템발견 서브카테고리 칩 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_honeyitem_more(page),
                           check=True)

#lifestyle 1467
@pytest.mark.regression
def test_community_00053(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 더보기 피드 진입
    page.goto("https://ozip.qa-web.dailyhou.se/pYyfcEl", timeout=0) 
    # 꿀템발견 서브카테고리 칩 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_honeyitem_cdpscrap(page),
                           check=True)

#lifestyle 1468
@pytest.mark.regression
def test_community_00054(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 꿀템발견 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_honeyitem_tab())
    # cdp 좋아요 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_cdp_like_btn(page),
                           check=True)

#lifestyle 1469
@pytest.mark.regression
def test_community_00055(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 꿀템발견 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_honeyitem_tab())
    # cdp 좋아요 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_cdp_comment_btn(page),
                           check=True)

#lifestyle 1470
@pytest.mark.regression
def test_community_00056(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 꿀템발견 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_honeyitem_tab())
    # cdp 공유하기 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_cdp_share_btn(page),
                           check=True)
    

#lifestyle 1489
@pytest.mark.regression
def test_community_00058(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_upload_community_edit(page),
                           check=True)


#lifestyle 1473
@pytest.mark.regression
def test_community_00059(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_upload_community_delete(page),
                           check=True)


#lifestyle 1474
@pytest.mark.regression
def test_community_00060(page, login_out):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 꿀템발견 탭 진입
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifesytleFeed(page).enter_honeyitem_tab())
    # 꿀템발견 서브카테고리 칩 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_noti_reply(page),
                           check=True)

#lifestyle 1477
@pytest.mark.regression
def test_community_00062(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    # 메인 링크 진입
    page.goto('https://qa-web.dailyhou.se/', timeout=0) 
    # 새댓글 노출/미노출 확인
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: LifestyleElements.check_noti_delete(page),
                           check=True)


