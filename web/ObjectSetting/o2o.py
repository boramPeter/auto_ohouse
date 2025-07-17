from web.BasicSetting.conftest import *
from app.common.base_method.exception_func import timeout_handler

'''
[naming rule]
1. xxxx_func : 여러 케이스에서 참조하는 함수 (expect 없어도됨)
2. into_xxxx : 특정 페이지 진입 +expect로 마무리
3. check_xxxx : complex step 케이스 +expect로 마무리
'''


class o2oElements():
    ''' ########################### Func List ###########################'''
    def remodeling_func(page):
        # O2O 홈병합 A/B안
        page.wait_for_timeout(3000)
        elements_visible = page.get_by_role("link", name="주거공간시공").is_visible()
        if elements_visible:
            # A안
            o2oElements.remodeling_func_a(page)
            page.wait_for_timeout(2000)
        else:
            # B안
            o2oElements.remodeling_func_b(page)
            page.wait_for_timeout(1000)
    
    def remodeling_func_a(page):
        # O2O 홈병합 B안
        page.get_by_role("link", name="인테리어/생활").click()
        page.get_by_role("link", name="주거공간시공").click()
        page.wait_for_timeout(5000)
        elements_visible = page.get_by_text("업체 찾기 전 잠깐").is_visible()
        if elements_visible:
            # 팝업 종료
            page.get_by_role("button", name="").click()
            # page.get_by_role("button", name="분쟁 걱정없이 시공하는 법").click()
            # page.get_by_role("button", name="책임보장 업체 보기").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)

    def remodeling_func_b(page):
        # O2O 홈병합 B안
        page.get_by_role("link", name="인테리어/생활").click()
        page.wait_for_timeout(5000)
        elements_visible = page.get_by_text("업체 찾기 전 잠깐").is_visible()
        if elements_visible:
            # 팝업 종료
            page.get_by_role("button", name="").click()
            # page.get_by_role("button", name="분쟁 걱정없이 시공하는 법").click()
            # page.get_by_role("button", name="책임보장 업체 보기").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)

    def simpleqna_func(page):
        timeout_handler(lambda: page.get_by_role("link", name="인테리어/생활").click())
        timeout_handler(lambda: page.get_by_role("link", name="부분시공").click())
        expect(page.get_by_role("tab", name="간편상담"), '상업공간시공 요소 미노출').to_be_visible()

    def construction_func(page):
        page.wait_for_timeout(2000)
        # page.get_by_text("부분 시공").click()
        # page.get_by_label("창호/샷시").check()
        # page.get_by_label("바닥재", exact=True).check()
        # page.get_by_label("도배", exact=True).check()
        # page.get_by_role("button", name="다음").click()
        # page.get_by_text("도배", exact=True).click()
        # page.get_by_role("button", name="다음").click()
        page.get_by_label("아파트").check()
        page.get_by_label("10평 이하 (~33m²)").check()
        page.get_by_label("현재 공실").check()
        page.get_by_label("집 전체 시공시공 분야가 구체적이지 않더라도 업체와 상담하며 조율할 수 있어요.").check()
        page.get_by_label("2주~1달 이내").check()
        # page.get_by_label("50~100만 원").check()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="다음").click() # 주소
        page.wait_for_timeout(1000)
        page.get_by_placeholder("특이사항, 세부시공내역, 원하는 스타일 등").click()
        page.get_by_placeholder("특이사항, 세부시공내역, 원하는 스타일 등").fill("test")
        # page.get_by_text("아래 내용에 모두 동의합니다. (필수)").check()
        page.get_by_role("button", name="신청완료").click()
        page.wait_for_timeout(2000)
        expect(page.get_by_role("button", name="확인"), '상담 신청완료 페이지 미노출').to_be_visible()
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)
        # 이사 팝업 종료
        elements_visible = page.get_by_role("button", name="").is_visible()
        if elements_visible:
            page.get_by_role("button", name="").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
        page.wait_for_timeout(2000)

    def concept_construction_func(page):
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="종합리모델링").click()
        page.get_by_role("button", name="다음").click()
        page.get_by_label("아파트").check()
        page.get_by_label("10평 이하 (~33m²)").check()
        page.get_by_label("현재 공실").check()
        page.get_by_label("집 전체 시공시공 분야가 구체적이지 않더라도 업체와 상담하며 조율할 수 있어요.").check()
        page.get_by_label("2주~1달 이내").check()
        # page.get_by_label("50~100만 원").check()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="다음").click() # 주소
        page.wait_for_timeout(1000)
        page.get_by_placeholder("특이사항, 세부시공내역, 원하는 스타일 등").click()
        page.get_by_placeholder("특이사항, 세부시공내역, 원하는 스타일 등").fill("test")
        # page.get_by_text("아래 내용에 모두 동의합니다. (필수)").check()
        page.get_by_role("button", name="신청완료").click()
        page.wait_for_timeout(2000)
        expect(page.get_by_role("button", name="확인"), '상담 신청완료 페이지 미노출').to_be_visible()
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)
        # 이사 팝업 종료
        elements_visible = page.get_by_role("button", name="").is_visible()
        if elements_visible:
            page.get_by_role("button", name="").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
        page.wait_for_timeout(2000)




    ''' ########################### into List ###########################'''
    # def into_remodeling_page(page):
    #     o2oElements.remodeling_func(page)
    #     page.wait_for_timeout(2000)
    #     elements_visible = page.get_by_role("link", name="주거공간시공").is_visible()
    #     # A안
    #     if elements_visible:
    #         page.get_by_role("link", name="주거공간시공").click()
    #         page.get_by_role("button", name="").click()
    #         page.wait_for_timeout(2000)
    #         expect(page.get_by_role("tab", name="시공업체"), '시공업체 요소 미노출').to_be_visible()
    #     # B안
    #     else:
    #         page.get_by_role("button", name="").click()
    #         page.wait_for_timeout(1000)

    def into_remodeling_page(page):
        # o2oElements.remodeling_func(page)
        page.get_by_role("link", name="인테리어/생활").click()
        page.wait_for_timeout(2000)
        # elements_visible = page.get_by_role("link", name="주거공간시공").is_visible()
        # A안
        # if elements_visible:
        #     page.get_by_role("link", name="주거공간시공").click()
        #     elements_visible1 = page.get_by_role("button", name="").is_visible()
        #     if elements_visible1:
        #         page.get_by_role("button", name="").click()
        #         page.wait_for_timeout(2000)
        #     else:
        #         page.wait_for_timeout(1000)  
        #     expect(page.get_by_role("tab", name="시공업체"), '시공업체 요소 미노출').to_be_visible()
        # # B안
        # else:
        #     page.get_by_role("button", name="").click()
        #     page.wait_for_timeout(1000)  
        page.get_by_role("link", name="주거공간시공").click()
        page.wait_for_timeout(3000)  
        # 팝업제거
        elements_visible = page.get_by_role("button", name="").is_visible()
        if elements_visible:
            page.get_by_role("button", name="").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)  
        expect(page.get_by_role("tab", name="시공업체"), '시공업체 요소 미노출').to_be_visible()
        




    def into_simple_councel(page):
        page.get_by_role("link", name="인테리어/생활").click()
        page.get_by_role("link", name="상업공간시공").click()
        expect(page.get_by_role("tab", name="간편상담"), '상업공간시공 요소 미노출').to_be_visible()

    def into_parts_shortcut(page):
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="인테리어/생활").click()
        # o2oElements.remodeling_func(page)
        # page.get_by_role("button", name="부분시공").click()
        # page.get_by_text("원하는 부분만 견적 받기").click()
        # page.get_by_test_id("home-discovery-page-view").get_by_role("link", name="부분시공").click()
        expect(page.get_by_text("원하는 부분만 견적 받기"), '부분시공페이지 요소 미노출').to_be_visible()

    def into_parts_services(page):
        o2oElements.remodeling_func(page)
        page.get_by_role("link", name="부분시공").click()
        expect(page.get_by_role("heading", name="원하는 시공분야를 선택해주세요"), '부분시공페이지 요소 미노출').to_be_visible()

    def into_parts_gnb(page):
        o2oElements.remodeling_func(page)
        page.get_by_role("link", name="부분시공").click()
        # page.get_by_role("navigation").get_by_role("link", name="부분시공").click()
        expect(page.get_by_role("heading", name="원하는 시공분야를 선택해주세요"), '부분시공페이지 요소 미노출').to_be_visible()





    ''' ########################### Check List ###########################'''
    def check_myvilage_plus(page):
        o2oElements.remodeling_func(page)
        page.wait_for_timeout(2000)
        # expect(page.get_by_role("button", name="우리동네 플러스 광고"), '우리동네 플러스 요소 미노출').to_be_visible()
        expect(page.get_by_role("link", name="새로운 시공의 기준 더보기"), '스탠다드 요소 미노출').to_be_visible()

    def check_portpolio(page):
        # o2oElements.remodeling_func(page)
        o2oElements.into_remodeling_page(page)
        page.wait_for_timeout(2000)
        page.get_by_text("리뷰 많은 순").click()
        page.wait_for_timeout(3000)
        # page.get_by_role('article').nth(0).click()
        page.get_by_label("0 of 3").get_by_role("link", name="전문가 이미지 1").click()
        page.wait_for_timeout(2000)
        page.get_by_role('article').nth(0).click()
        page.wait_for_timeout(2000)
        expect(page.get_by_role("button", name="팔로우").first, '팔로우 버튼 요소 미노출').to_be_visible()

    def check_direct_councle(page):
        # 로그인
        page.get_by_role("link", name="로그인").click()
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("ohouseqaapp@gmail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(3000)
        o2oElements.remodeling_func_a(page)
        page.wait_for_timeout(3000)
        for _ in range(5):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        expect(page.get_by_role("button", name="추천받으러 가기"), '팔로우 버튼 요소 미노출').to_be_visible()
        page.get_by_role("button", name="추천받으러 가기").click()
        # 상담 폼
        expect(page.get_by_role("heading", name="시공할 공간의 종류를 선택해주세요."), '팔로우 버튼 요소 미노출').to_be_visible()


    def check_simple_councle_flow(page):
        page.wait_for_timeout(2000)
        o2oElements.remodeling_func_a(page)
        page.wait_for_timeout(2000)
        # 간편상담
        page.get_by_role("tab", name="간편매칭").click()
        page.get_by_test_id("home-consultation-hero").get_by_role("link", name="시공 정보 입력하기").click()
        # page.get_by_role("button", name="다음").click()
        page.wait_for_timeout(2000)
        page.get_by_label("아파트").check()
        page.get_by_label("10평 이하 (~33m²)").check()
        page.get_by_label("현재 공실").check()
        page.get_by_label("집 전체 시공시공 분야가 구체적이지 않더라도 업체와 상담하며 조율할 수 있어요.").check()
        page.get_by_label("2주~1달 이내").check()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="다음").click() # 주소
        # page.get_by_label("아니오. 괜찮아요.").check()
        page.get_by_placeholder("특이사항, 세부시공내역, 원하는 스타일 등").click()
        page.get_by_placeholder("특이사항, 세부시공내역, 원하는 스타일 등").fill("")
        page.get_by_placeholder("특이사항, 세부시공내역, 원하는 스타일 등").press("CapsLock")
        page.get_by_placeholder("특이사항, 세부시공내역, 원하는 스타일 등").fill("test")
        # page.get_by_text("아래 내용에 모두 동의합니다. (필수)").click()
        page.get_by_role("button", name="신청완료").click()
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)
        # page.get_by_role("button", name="").click()
        elements_visible = page.get_by_role("button", name="").is_visible()
        # 이사 팝업 종료
        if elements_visible:
            page.get_by_role("button", name="").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
        page.wait_for_timeout(2000)

    def check_scrap(page):
        # o2oElements.into_remodeling_page(page)
        page.get_by_role("link", name="인테리어/생활").click()
        page.wait_for_timeout(2000)
        # 스크랩 진입
        page.get_by_label("스크랩북 페이지 링크 버튼").click()
        expect(page.get_by_role("link", name="webqa"), '로그인계정 요소 미노출').to_be_visible()
        page.get_by_role("link", name="인테리어/생활").click()
        page.wait_for_timeout(2000)
        # 장바구니 진입
        page.get_by_label("장바구니 페이지 링크 버튼").click()
        expect(page.get_by_text("총 상품금액"), '장바구니 페이지 미노출').to_be_visible()
        
    def check_counsel_list(page):
        o2oElements.remodeling_func(page)
        page.wait_for_timeout(2000)
        # 신청내역 진입
        page.get_by_text("전체 신청내역").click()
        # page.get_by_role("button", name=" 신청내역").click()
        expect(page.get_by_role("button", name="신청내역"), '신청내역 요소 미노출').to_be_visible()

    def check_counsel_list_detail(page):
        page.get_by_role("link", name="인테리어/생활").click()
        page.wait_for_timeout(2000)
        # 신청내역 상세 진입
        page.get_by_text("전체 신청내역").click()
        # page.get_by_role("button", name=" 신청내역").click()
        # page.locator(".css-1t7w7u6").nth(0).click()
        # page.locator("a").nth(0).click()
        # page.locator("a").filter(has_text=re.compile(r"종합리모델링.*")).nth(0).click()
        page.locator('xpath=//*[@id="__next"]/div[1]/main/div/div[2]/div[2]/div/div[4]/div/div/div/div/div/div[1]').click()
        expect(page.get_by_text("내 신청정보"), '신청내역 요소 미노출').to_be_visible()

    def check_chat_list(page):
         # 로그인 상태인지 체크하여 로그인/로그아웃 진행
        elements_visible = page.get_by_role("link", name="로그인").is_visible()
        if elements_visible:
            # 로그인
            page.get_by_role("link", name="로그인").click()
            page.get_by_placeholder("이메일").click()
            page.get_by_placeholder("이메일").fill("qa22@bucketplace.org")
            page.get_by_placeholder("비밀번호").click()
            page.get_by_placeholder("비밀번호").fill("123asd!@")
            page.get_by_role("button", name="로그인").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="인테리어/생활").click()
        page.wait_for_timeout(2000)
        # 채팅내역 진입
        # page.get_by_text("전체 신청내역").click()
        # page.get_by_role("button", name="채팅").click()
        page.get_by_text("채팅").click()
        expect(page.get_by_role("button", name="채팅"), '채팅내역 요소 미노출').to_be_visible()
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click()
        expect(page.get_by_role("link", name="로그인"), '로그인 메뉴 요소 미노출').to_be_visible()

    def check_chat_list_detail(page):
         # 로그인 상태인지 체크하여 로그인/로그아웃 진행
        elements_visible = page.get_by_role("link", name="로그인").is_visible()
        if elements_visible:
            # 로그인
            page.get_by_role("link", name="로그인").click()
            page.get_by_placeholder("이메일").click()
            page.get_by_placeholder("이메일").fill("qa22@bucketplace.org")
            page.get_by_placeholder("비밀번호").click()
            page.get_by_placeholder("비밀번호").fill("123asd!@")
            page.get_by_role("button", name="로그인").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="인테리어/생활").click()
        page.wait_for_timeout(2000)
        # 채팅내역 상세 진입
        page.get_by_text("채팅").click()
        with page.expect_popup() as page1_info:
            # page.locator("xpath=//html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div/div/div/a[1]").click()
            page.get_by_role("link", name=re.compile(r"QATEST.*")).nth(0).click()
        page1 = page1_info.value
        expect(page1.get_by_text("QATEST"), '채팅상세 요소 미노출').to_be_visible()
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click()
        expect(page.get_by_role("link", name="로그인"), '로그인 메뉴 요소 미노출').to_be_visible()

    def check_remodeling_category(page):
        o2oElements.into_remodeling_page(page)
        # page.get_by_role("link", name="인테리어/생활").click()
        # page.get_by_role("link", name="주거공간시공").click()
        page.wait_for_timeout(2000)
        # 시공업체 진입
        page.get_by_role("tab", name="시공업체").click()
        expect(page.get_by_role("link", name="새로운 시공의 기준 더보기"), '시공업체 요소 미노출').to_be_visible()
        # 시공사례 진입
        page.get_by_role("tab", name="시공사례").click()
        expect(page.get_by_text("지역"), '시공사례 요소 미노출').to_be_visible()
        # 간편매칭 진입
        page.get_by_role("tab", name="간편매칭").click()
        expect(page.get_by_test_id("home-consultation-hero").get_by_role("link", name="시공 정보 입력하기"), '간편매칭 요소 미노출').to_be_visible()
        # 부분시공 진입
        # page.get_by_role("link", name="부분시공").click()
        # expect(page.get_by_role("heading", name="원하는 시공을 선택해주세요"), '부분시공 요소 미노출').to_be_visible()

    def check_councel_remodeling(page):
        o2oElements.into_remodeling_page(page)
        page.wait_for_timeout(2000)
        page.get_by_text("리뷰 많은 순").click()
        page.wait_for_timeout(3000)
        page.get_by_label("0 of 3").get_by_role("link", name="전문가 이미지 1").click()
        page.wait_for_timeout(2000)
        # 상담 신청
        page.get_by_role("button", name="상담신청").click()
        page.get_by_role("button", name="종합리모델링").click()
        page.get_by_role("button", name="다음").click()
        page.wait_for_timeout(1000)
        # 상담 flow
        o2oElements.construction_func(page)
        page.wait_for_timeout(1000)
        # 신청내역 진입
        # page.get_by_role("button", name=" 신청내역 N").click()
        page.get_by_text("전체 신청내역").click()
        page.wait_for_timeout(1000)
        # page.locator(".css-1t7w7u6").nth(0).click()
        # page.locator("a").filter(has_text=re.compile(r"도배QA01.*")).first.click()
        # page.locator(".css-928nli").nth(0).click()
        # page.locator('xpath=//*[@id="__next"]/div[1]/main/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div/a/article').click()
        page.locator('xpath=//*[@id="__next"]/div[1]/main/div/div[2]/div[2]/div/div[4]/div/div/div/div/div/div[1]').click()
        page.wait_for_timeout(1000)
        expect(page.get_by_text("꼬시나꼬시나꼬시나꼬시나꼬시나"), '시공업체명 미노출').to_be_visible()
        expect(page.get_by_text("오하우스"), '고객명 미노출').to_be_visible()

    def check_concept_remodeling(page):
        page.get_by_label("스크랩북 페이지 링크 버튼").click()
        page.get_by_role("button", name=re.compile(r"집들이.*")).click()
        page.get_by_role("link", name="전문가 집들이 역삼 아이파크 시공 사례 QA01ppppppp1").click()
        page.wait_for_timeout(2000)
        # 스크롤
        for _ in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="이 컨셉 시공상담").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="종합리모델링").click()
        page.get_by_role("button", name="다음").click()
        # 상담 flow
        o2oElements.construction_func(page)
        page.wait_for_timeout(1000)
        # 신청내역 진입
        # page.get_by_role("button", name=" 신청내역 N").click()
        page.get_by_text("전체 신청내역").click()
        # page.locator(".css-1t7w7u6").nth(0).click()
        # page.locator("a").filter(has_text=re.compile(r"도배QA01.*")).first.click()
        # page.locator('xpath=//*[@id="__next"]/div[1]/main/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]').click()
        page.locator('xpath=//*[@id="__next"]/div[1]/main/div/div[2]/div[2]/div/div[4]/div/div/div/div/div/div[1]').click()
        expect(page.get_by_text("QA01"), '시공업체명 미노출').to_be_visible()
        expect(page.get_by_text("오하우스"), '고객명 미노출').to_be_visible()
        
    def check_recommand_remodeling(page):
        o2oElements.remodeling_func(page)
        page.get_by_role("button", name="추천받으러 가기").click()
        page.get_by_role("button", name="다음").click()
        # 상담 flow
        o2oElements.construction_func(page)
        # 신청내역 진입
        page.get_by_role("button", name=" 신청내역 N").click()
        # page.locator(".css-1t7w7u6").nth(0).click()
        page.locator("a").filter(has_text=re.compile(r"종합리모델링QA01.*")).first.click()
        expect(page.get_by_text("QA01"), '시공업체명 미노출').to_be_visible()
        expect(page.get_by_text("오하우스"), '고객명 미노출').to_be_visible()

    def check_parts_remodeling(page):
        # o2oElements.into_remodeling_page(page)
        page.get_by_role("link", name="부분시공").click()
        page.get_by_role("link", name="도배").click()
        # 상담 flow
        page.get_by_label("아파트").check()
        page.get_by_label("10평 이하 (~33m²)").check()
        page.get_by_label("현재 공실").check()
        page.get_by_label("1주일 이내").check()
        page.get_by_label("50~100만 원").check()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="다음").click()
        page.get_by_placeholder("특이사항, 세부시공내역, 원하는 스타일 등").click()
        page.get_by_placeholder("특이사항, 세부시공내역, 원하는 스타일 등").fill("test")
        # page.get_by_label("아래 내용에 모두 동의합니다. (필수)").check()
        page.get_by_role("button", name="신청완료").click()
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)
        # 신청내역 진입
        # page.get_by_role("button", name=" 신청내역 N").click()
        page.get_by_text("전체 신청내역").click()
        page.locator("a").filter(has_text=re.compile(r"도배업체 .*")).first.click()
        expect(page.locator("span").filter(has_text="도배"), '시공분야명 미노출').to_be_visible()
        expect(page.get_by_text("오하우스"), '고객명 미노출').to_be_visible()

    def check_house_checklist(page):
        page.get_by_role("link", name="인테리어/생활").click()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="집보기체크리스트").click()
        elements_visible = page.get_by_label("전체 동의").is_visible()
        if elements_visible:
            # 로그인
            page.get_by_label("전체 동의").click()
            page.get_by_role("button", name="완료").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
        page.wait_for_timeout(2000)
        expect(page.get_by_role("button", name="새로운 매물 체크 시작하기"), '버튼 요소 미노출').to_be_visible()

    def check_house_checklist_detail(page):
        page.get_by_role("link", name="인테리어/생활").click()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="집보기체크리스트").click()
        page.get_by_role("button", name="내 평가 자세히 보기").click()
        page.wait_for_timeout(2000)
        expect(page.get_by_role("button", name="공유하기"), '공유하기 버튼 요소 미노출').to_be_visible()

    def check_remodiling_reference(page):
        page.get_by_role("link", name="인테리어/생활").click()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="아파트시공사례").click()
        # 주소 검색 노출
        page.get_by_test_id("town-desktop-layout").get_by_text("주소 또는 아파트 이름을 입력해주세요.").click()
        expect(page.get_by_text("주소 검색"), '주소검색 요소 미노출').to_be_visible()
        page.get_by_role("button", name="").click()
        page.wait_for_timeout(2000)
        # 주변 아파트 노출
        expect(page.get_by_test_id("town-desktop-layout").get_by_role("link").first, '주변아파트 요소 미노출').to_be_visible()

    def check_remodiling_reference_change(page):
        page.get_by_role("link", name="인테리어/생활").click()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="아파트시공사례").click()
        # 주소 변경
        page.get_by_test_id("town-desktop-layout").get_by_text("주소 또는 아파트 이름을 입력해주세요.").click()
        page.wait_for_timeout(1000)
        page.get_by_placeholder("도로명, 건물명, 지번검색").click()
        page.get_by_placeholder("도로명, 건물명, 지번검색").fill("서초대로74길 4")
        page.get_by_placeholder("도로명, 건물명, 지번검색").press("Enter")
        page.get_by_role("button", name="우편번호 06620서울특별시 서초구 서초대로74길 4 (서초동, 삼성생명서초타워)").click()
        page.wait_for_timeout(2000)
        # 주변 아파트 노출 (서초동)
        expect(page.get_by_text(re.compile(r"주변아파트서초동.*")), '주변아파트 요소 미노출').to_be_visible()

    def check_remodiling_reference_detail(page):
        page.get_by_role("link", name="인테리어/생활").click()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="아파트시공사례").click()
        # 첫번째 아파트 상세 진입
        page.locator(".css-wtdyim > div > div > .css-lb6usm").first.click()
        page.wait_for_timeout(2000)
        expect(page.get_by_text("평수별로 집안을 살펴보세요.비슷한 구조의 집도 함께 볼 수 있어요."), '주변아파트 상세 미노출').to_be_visible()

    def check_partnercenter_home(page):
        page.get_by_role("link", name="로그인").click()
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("qa01@1.net")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("a1234567!")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(2000)
        # 사장님센터 홈 이동 후 로그인
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("qa01@1.net")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("123Asd!@")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(2000)
        expect(page.get_by_text("QA01스탠다드"), '로그인 계정 미노출').to_be_visible()



