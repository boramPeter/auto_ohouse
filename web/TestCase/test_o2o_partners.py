from web.ObjectSetting.comm_service import *
from web.ObjectSetting.comm_platform import *
from web.ObjectSetting.common_object import *
from web.ObjectSetting.o2o import *
from web.ObjectSetting.o2o_partners import *
from app.common.base_method.get_function_name_func import ProviderFunctionName
from web.BasicSetting.exception_func import *
from web.BasicSetting.web_result_binary import ResultWeb


@pytest.mark.regression
def test_o2o_partners_00001(page):
    current_function_name = ProviderFunctionName().get_current_function_name()
    PageElements.qaweb_o2o_partners_url(page)
    web_exceptions_handler(page, current_function_name, 
                           step=lambda: o2oPCElements.into_partners_main(page),
                           check=True)
