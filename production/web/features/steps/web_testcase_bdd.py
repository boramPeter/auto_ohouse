from playwright.sync_api import *
from pytest_bdd import scenarios, given, when, then, parsers
from production.common.method.get_function_name_func import ProviderFunctionName
from production.common.method.jenkins_exception_handler import JenkinsExceptionHandler

# from production.web.web_procedure.o2o_procedure import O2oFunctions
from production.web.web_procedure.common_procedure import PageElements
# from production.web.web_procedure.lifestyle_procedure import LifestyleProcedure
from production.web.basic_settings.web_keyword_mapping import execute_keyword

# Reuseable ################################################################################################

#   - pre ----------------------------------------------------------------------------------------------------
# 페이지 이동 (goto) - 'locator 링크로 진입'
@given(parsers.parse('"{locator1}" 링크로 "{action1}"'))
def prod_reuseable00001_web_pre(page,action1,locator1,get_scenario_name):
    current_function_name = ProviderFunctionName().get_current_function_name(get_scenario_name)
    JenkinsExceptionHandler().web_exceptions_handler(page, current_function_name,
                            step=lambda: execute_keyword(page,"step",{action1:locator1}))  

# 현재 url 확인하고 기대결과와 다르면 해당 url 로 이동 (goto) - 'locator 사전조건 준비'
@given(parsers.parse('"{locator1}" 사전조건 "{action1}"'))
def prod_reuseable00002_web_pre(page,action1,locator1,get_scenario_name):
    current_function_name = ProviderFunctionName().get_current_function_name(get_scenario_name)
    JenkinsExceptionHandler().web_exceptions_handler(page, current_function_name,
                            step=lambda: execute_keyword(page,"step",{action1:locator1}))  
'''
일부만 남기고 제거
'''