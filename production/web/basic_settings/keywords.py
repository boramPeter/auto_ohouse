from production.web.basic_settings.import_list import *
from playwright.sync_api import Page
from selenium.common.exceptions import TimeoutException
from production.web.web_locator.locator import WebLocator
from production.common.method.jenkins_exception_handler import web_timeout_handler
from production.web.web_procedure.common_procedure import PageElements


def navigate(page: Page, *args):
    for arg in args:
        if "클릭" in arg:
            #print(arg["클릭"])
            locator = getattr(WebLocator(page), arg["클릭"])
            web_timeout_handler(lambda: locator.click(), arg["클릭"])

        if "체크" in arg:
            #print(arg["체크"])
            locator = getattr(WebLocator(page), arg["체크"])
            web_timeout_handler(lambda: locator.check(), arg["체크"])

        if "진입" in arg:
            locator = getattr(WebLocator(page), arg["진입"])
            web_timeout_handler(lambda: page.goto(locator, timeout= 0), arg["진입"])

        if "준비" in arg:
            locator = getattr(WebLocator(page), arg["준비"])
            if locator != page.url:
                web_timeout_handler(lambda: page.goto(locator, timeout= 0), arg["준비"])

        if "입력" in arg:
            parts = arg["입력"].split(' ')
            locator_value = parts[0]
            input_keyword = parts[2]
            locator = getattr(WebLocator(page), locator_value)
            web_timeout_handler(lambda: locator.fill(input_keyword), locator_value)

        if "키 입력" in arg:
            web_timeout_handler(lambda: page.keyboard.press(arg["키 입력"]), arg["키 입력"])
        
        if "대기" in arg:
            seconds = int(arg["대기"].split('초')[0])
            page.wait_for_timeout(seconds * 1000)

        if "o2o팝업처리" in arg:
            locator = getattr(WebLocator(page), arg["o2o팝업처리"])
            if locator.is_visible():
                #x_btn = page.get_by_role("button").first
                x_btn = page.get_by_role("button", name="")
                web_timeout_handler(lambda: x_btn.click(), "o2o팝업처리_x_btn")

        # if "주거공간진입" in arg:
        #     locator = getattr(WebLocator(page), arg["주거공간진입"])
        #     if locator.is_visible():
        #         locator = getattr(WebLocator(page), arg["클릭"])
        #         web_timeout_handler(lambda: locator.click(), arg["클릭"])
        #     else:
        #         page.wait_for_timeout(2000)
        
        if "보이면 클릭" in arg:
            locator = getattr(WebLocator(page), arg["보이면 클릭"])
            if locator.is_visible():
                web_timeout_handler(lambda: locator.click(), arg["보이면 클릭"])
            else:
                page.wait_for_timeout(2000)




def verify(page: Page, *args):
    for arg in args:
        if "노출확인" in arg:
            #print(arg["체크"])
            locator = getattr(WebLocator(page), arg["노출확인"])
            web_timeout_handler(lambda: expect(locator).to_be_visible(), arg["노출확인"])

        if "링크확인" in arg:
            locator = getattr(WebLocator(page), arg["링크확인"])
            check_url = lambda x: x if x in page.url else (_ for _ in ()).throw(AssertionError())
            web_timeout_handler(lambda: check_url(locator), arg["링크확인"])

        if "개수 체크" in arg:
            locator = getattr(WebLocator(page), arg["개수 체크"])
            if type(locator) is list:
                real_count = len(locator)
            else:
                real_count = locator.count()
            check_count = lambda x: x if x > 0 else (_ for _ in ()).throw(AssertionError())
            web_timeout_handler(lambda: check_count(real_count), arg["개수 체크"])

        if "호출확인" in arg:
            locator = getattr(WebLocator(page), arg["호출확인"])
            web_timeout_handler(lambda: PageElements.send_api_get(locator), arg["호출확인"])

        if "대기 후 노출확인" in arg:
            #print(arg["체크"])
            locator = getattr(WebLocator(page), arg["대기 후 노출확인"])
            locator.wait_for(state='visible', timeout=10 * 1000)
            web_timeout_handler(lambda: expect(locator).to_be_visible(), arg["대기 후 노출확인"])
            