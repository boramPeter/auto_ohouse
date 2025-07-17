from playwright.sync_api import *
import requests

class LifestyleProcedure():

    def suggestion_func(page):
        elements_visible = page.locator("div").filter(has_text="선택 완료").nth(4).is_visible()
        if elements_visible:
            # 팝업 종료
            page.get_by_role("button", name="").click()
            # page.get_by_role("button", name="선택 완료").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
        
    def check_recommend_chip(page):
        elements_visible = page.get_by_role("button", name="").is_visible()
        if elements_visible:
            # 팝업 종료
            page.get_by_role("button", name="").click()
            # page.get_by_role("button", name="선택 완료").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
        # follow_count = page.locator("label").count()
        # assert follow_count == 5, "follow_count ="+str(follow_count)
