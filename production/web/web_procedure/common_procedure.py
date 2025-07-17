from playwright.sync_api import *
import requests

class PageElements():
    # def __init__(self, page: Page):
    #     self.page = page

    def goto_ohouse_main(page):
        page.goto('https://ohou.se/', timeout= 0)

    def goto_ohouse_main_debug(page):
        page.goto('https://ohou.se/', timeout= 0)
        page.get_by_role("link", name="로그인").click()
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("ohouseqa@gmail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(2000)

    def goto_o2o(page):
        page.goto('https://ohou.se/experts', timeout= 0)

    def goto_comm_service(page):
        page.goto('https://store.ohou.se/', timeout= 0)

    def goto_login(page):
        page.goto('https://ohou.se/users/sign_in', timeout= 0)

    def goto_profile(page):
        page.goto('https://ohou.se/users/22590422/edit', timeout= 0)
    
    def goto_profile_myshop(page):
        page.goto('https://ohou.se/user_shopping_pages/order_list', timeout= 0)

    def goto_shop_goods(page):
        page.goto('https://ohou.se/productions/884868/selling', timeout= 0)




    def login_func(page):
        # 로그인
        page.get_by_role("link", name="로그인").click()
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("ohouseqa@gmail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(2000)

    def login_func_2(page1):
        # 로그인
        page1.get_by_role("link", name="로그인").click()
        page1.get_by_placeholder("이메일").click()
        page1.get_by_placeholder("이메일").fill("ohouseqa@gmail.com")
        page1.get_by_placeholder("비밀번호").click()
        page1.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
        page1.get_by_role("button", name="로그인").click()
        page1.wait_for_timeout(2000)

    def logout_func(page):
        # 로그아웃
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click()
        page.wait_for_timeout(2000)

        
    def send_api_get(api_url):
        response = requests.get(api_url, verify=False, timeout=10)
        assert response.status_code == 200
        return response

    def guest_purchase_func(page):
        with page.expect_popup() as page1_info:
            page.get_by_role("button", name="바로구매").first.click()
        page1 = page1_info.value
        page.wait_for_timeout(2000)
        page1.get_by_role("button", name="비회원 구매하기").click()
        page.wait_for_timeout(2000)

    def guest_purchase_func_cart(page):
        with page.expect_popup() as page1_info:
            page.get_by_role("button", name="1개 상품 구매하기").first.click()
        page1 = page1_info.value
        page.wait_for_timeout(2000)
        page1.get_by_role("button", name="비회원 구매하기").click()
        page.wait_for_timeout(2000)




        
    # def get_title(page):
        # return page.title()