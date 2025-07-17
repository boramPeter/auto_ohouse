import pytest
from playwright.sync_api import sync_playwright
from web.ObjectSetting.common_object import PageElements, CommonElements, AccountInfo
import web.BasicSetting.exception_func as ex

@pytest.fixture()
def login_out(page, request):
    current_function_name = request.node.name
    qa_home = ''
    ex.web_exceptions_handler(page, current_function_name, 
                           step=lambda: PageElements.qaweb_main_url(page))
    ex.web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.login_func(page),
                           prev_page=qa_home)
    yield
    ex.web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.logout_func(page))
    
@pytest.fixture()
def pay_login_out(page, request):
    current_function_name = request.node.name
    qa_home = ''
    ex.web_exceptions_handler(page, current_function_name, 
                           step=lambda: PageElements.qaweb_main_url(page))
    ex.web_exceptions_handler(page, current_function_name, 
                           step=lambda: CommonElements.login_payment_func(page,AccountInfo.payment_id,AccountInfo.payment_pw),
                           prev_page=qa_home)
    yield
    ex.web_exceptions_handler(page, current_function_name,
                           step=lambda: CommonElements.logout_func(page))


