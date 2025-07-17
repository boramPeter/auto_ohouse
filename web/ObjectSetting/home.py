from web.BasicSetting.conftest import *
from app.common.base_method.exception_func import timeout_handler

'''
[naming rule]
1. xxxx_func : 여러 케이스에서 참조하는 함수 (expect 없어도됨)
2. into_xxxx : 특정 페이지 진입 +expect로 마무리
3. check_xxxx : complex step 케이스 +expect로 마무리
'''

class HomeElements():
    def into_best_module(page):
        # 베스트 클릭
        page.get_by_text("베스트").scroll_into_view_if_needed()
        page.locator("label").filter(has_text="테마관").click()
        # API Response check
        api_url = 'https://qa-web.dailyhou.se/commerces/ranks.json?v=2&type=best&category=21'
        response = send_api_get(api_url)
        assert response.status_code == 200
        page.locator("label").filter(has_text="가구").locator("span").click()
        # API Response check
        api_url = 'https://qa-web.dailyhou.se/commerces/ranks.json?v=2&type=best&category=0'
        response = send_api_get(api_url)
        assert response.status_code == 200
        page.locator("label").filter(has_text="패브릭").locator("span").click()
        # API Response check
        api_url = 'https://qa-web.dailyhou.se/commerces/ranks.json?v=2&type=best&category=1'
        response = send_api_get(api_url)
        assert response.status_code == 200
        page.locator("label").filter(has_text="조명").locator("span").click()
        # API Response check
        api_url = 'https://qa-web.dailyhou.se/commerces/ranks.json?v=2&type=best&category=23'
        response = send_api_get(api_url)
        assert response.status_code == 200
        page.locator("label").filter(has_text="가전").locator("span").click()
        # API Response check
        api_url = 'https://qa-web.dailyhou.se/commerces/ranks.json?v=2&type=best&category=3'
        response = send_api_get(api_url)
        assert response.status_code == 200

    def into_bestrank_module(page):
        # 베스트 클릭
        page.get_by_text("베스트").scroll_into_view_if_needed()
        page.locator("div").filter(has_text=re.compile(r"^베스트더보기$")).get_by_role("button").click()
        expect(page.get_by_role("button", name="역대 베스트"), '역대베스트 미노출').to_be_visible()

    def check_moreview_module(page):
        page.locator("div").filter(has_text=re.compile(r"^맞춤 정보 없는 유저 1$")).first.scroll_into_view_if_needed()
        page.locator("div").filter(has_text=re.compile(r"^맞춤 정보 없는 유저 1더보기$")).get_by_role("button").click()
        expect(page.get_by_role("button", name="정렬 "), '정렬 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="주거형태 "), '주거형태 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="평수 "), '평수 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="예산 "), '예산 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="가족형태 "), '가족형태 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="스타일 "), '스타일 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="컬러 "), '컬러 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="세부공사 "), '세부공사 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="분야 "), '분야 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="작업자 "), '작업자 필터 비노출됨').to_be_visible()
        PageElements.qaweb_main_url(page)
        page.wait_for_timeout(1000)

        # 오늘의 스토리 두번째 모둘의 더보기 > 집들이 페이지 노출화인(필터로 체크)
        print("test_home_024 : 두번째 모듈 노출 % 더보기 동작 확인", end='')
        page.locator("div").filter(has_text=re.compile(r"^모두 노출 1$")).first.scroll_into_view_if_needed()
        page.locator("div").filter(has_text=re.compile(r"^모두 노출 1더보기$")).get_by_role("button").click()
        expect(page.get_by_role("button", name="정렬 "), '정렬 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="주거형태 "), '주거형태 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="평수 "), '평수 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="예산 "), '예산 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="가족형태 "), '가족형태 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="스타일 "), '스타일 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="컬러 "), '컬러 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="세부공사 "), '세부공사 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="분야 "), '분야 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="작업자 "), '작업자 필터 비노출됨').to_be_visible()
        PageElements.qaweb_main_url(page)
        page.wait_for_timeout(1000)

        # 오늘의 스토리 세번째 모둘의 더보기 > 집들이 페이지 노출화인(필터로 체크)
        print("test_home_024 : 세번째 모듈 노출 % 더보기 동작 확인", end='')
        page.locator("div").filter(has_text=re.compile(r"^모두 노출 2$")).first.scroll_into_view_if_needed()
        page.locator("div").filter(has_text=re.compile(r"^모두 노출 2더보기$")).get_by_role("button").click()
        expect(page.get_by_role("button", name="정렬 "), '정렬 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="주거형태 "), '주거형태 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="평수 "), '평수 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="예산 "), '예산 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="가족형태 "), '가족형태 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="스타일 "), '스타일 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="컬러 "), '컬러 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="세부공사 "), '세부공사 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="분야 "), '분야 필터 비노출됨').to_be_visible()
        expect(page.get_by_role("button", name="작업자 "), '작업자 필터 비노출됨').to_be_visible()
        PageElements.qaweb_main_url(page)
        page.wait_for_timeout(1000)
        
    def check_today_scrap(page):
        page.get_by_text("맞춤 정보 없는 유저 1").scroll_into_view_if_needed()
        # page.locator("div").filter(has_text=re.compile(r"^맞춤 정보 없는 유저 1더보기231무채색에 진심! 싱글 5\.5평 원룸 인테리어!ttw전문가유저 반셀프일반유저 셀프TEST$")).get_by_label("scrap 토글 버튼").first.click()
        page.locator("div").filter(has_text=re.compile(r"^오늘의 스토리\) 맞춤 정보 없는 유저 1더보기231무채색에 진심! 싱글 5\.5평 원룸 인테리어!ttw전문가유저 반셀프일반유저 셀프TEST$")).get_by_label("scrap 토글 버튼").first.click()
        expect(page.locator("div").filter(has_text=re.compile(r"^맞춤 정보 없는 유저 1더보기231무채색에 진심! 싱글 5\.5평 원룸 인테리어!ttw전문가유저 반셀프일반유저 셀프TEST$"))).to_be_enabled()
        page.wait_for_timeout(1000)
        page.locator("div").filter(has_text=re.compile(r"^오늘의 스토리\) 맞춤 정보 없는 유저 1더보기231무채색에 진심! 싱글 5\.5평 원룸 인테리어!ttw전문가유저 반셀프일반유저 셀프TEST$")).get_by_label("scrap 토글 버튼").first.click()
        
        # 폴더에 담기 > 새로운 폴더 추가 > 폴더명 1 > 완료
        # page.get_by_role("button", name="폴더에 담기").click()
        # page.get_by_role("button", name=" 새로운 폴더 추가하기").click()
        # page.get_by_placeholder("폴더명을 입력하세요").click()
        # page.get_by_placeholder("폴더명을 입력하세요").fill("1")
        # page.get_by_role("button", name="완료").click()
        # page.once("dialog", lambda dialog: dialog.accept())
        # expect(page.get_by_text("'1'폴더로 이동했습니다."))

                
        # 스크랩북 보기> 스크랩한 콘텐츠 상세 진입 > 제목 확인
        # page.wait_for_timeout(1000) # 페이지 로딩 속도 때문에 딜레이 넣지 않으면 Fail 뜸
        # page.get_by_role("button", name="스크랩북 보기").click()
        # expect(page.get_by_text("스크랩북1설정공유하기")).to_be_visible()
        # page.get_by_role("link", name="집들이", exact=True).click()
        # page.wait_for_timeout(5000) # 페이지 로딩 속도 때문에 딜레이 넣지 않으면 Fail 뜸
        # expect(page.get_by_text("무채색에 진심! 싱글 5.5평 원룸 인테리어!"), "제목이 일치 하지 않습니다.").to_be_visible()

        # 홈 이동 > 스크랩 해제한 콘텐츠 스크랩 disable 확인
        # page.get_by_role("link", name="홈", exact=True).click()
        # expect(page.locator("div").filter(has_text=re.compile(r"^맞춤 정보 없는 유저 1더보기231무채색에 진심! 싱글 5\.5평 원룸 인테리어!ttw전문가유저 반셀프일반유저 셀프TEST$"))).to_be_enabled()
        # page.locator("div").filter(has_text=re.compile(r"^맞춤 정보 없는 유저 1더보기231무채색에 진심! 싱글 5\.5평 원룸 인테리어!ttw전문가유저 반셀프일반유저 셀프TEST$")).get_by_label("scrap 토글 버튼").first.click()
        # expect(page.get_by_text("스크랩북에서 삭제했습니다.")).to_be_visible()
            
    def into_footer(page):
        # 최하단 스크롤 > 고객센터 진입 > 홈화면 되돌아오기
        page.get_by_text("고객센터").scroll_into_view_if_needed()
        print("고객센터 링크 동작 확인 및 이동된 페이지 확인", end='')
        page.get_by_role("link", name="고객센터").click()
        page.wait_for_timeout(1000)
        expect(page.get_by_role("heading", name="무엇을 도와드릴까요?"), "고객센터 화면에 진입하지 못하였습니다.").to_be_visible()
        PageElements.qaweb_main_url(page)
        page.wait_for_timeout(1000)
        print(" - Pass")

       # 최하단 스크롤 > 카톡 상담 진입 > 홈화면 되돌아오기
        page.get_by_text("고객센터").scroll_into_view_if_needed()
        print("카톡 상담 링크 동작 확인 및 이동된 페이지 확인", end='')
        with page.expect_popup() as page2_info:
            page.get_by_role("button", name="카톡 상담(평일 09:00~18:00)").click()
        page2 = page2_info.value
        page.wait_for_timeout(1000)
        expect(page2.get_by_role("heading", name="Kakao").locator("span").first , "카톡 상담 로그인 페이지 접근하지 못하였습니다.").to_be_visible()
        page2.close()
        PageElements.qaweb_main_url(page)
        page.wait_for_timeout(1000)
        print(" - Pass")

        # 최하단 스크롤 > 회사소개 진입 > 홈화면 되돌아오기
        page.get_by_text("고객센터").scroll_into_view_if_needed()
        print("회사소개 문의 링크 동작 확인 및 이동된 페이지 확인", end='')
        page.get_by_role("link", name="회사소개").click()
        page.wait_for_timeout(300)
        expect(page.get_by_role("heading", name="'이렇게 살아보고 싶다'는 전 세계 사람들의 꿈을 현실로 만듭니다"), "최사소개 페이지 접근하지 못하였습니다.").to_be_visible()
        PageElements.qaweb_main_url(page)
        print(" - Pass")

        # 최하단 스크롤 > 채용정보 진입 > 홈화면 되돌아오기
        page.get_by_text("고객센터").scroll_into_view_if_needed()
        print("채용정보 링크 동작 확인 및 이동된 페이지 확인", end='')
        page.get_by_role("link", name="채용정보").click()
        page.wait_for_timeout(300)
        expect(page.get_by_role("heading", name="모두의 삶을 함께 바꿔나갈 기회"), "채용정보 페이지 접근하지 못하였습니다.").to_be_visible()
        PageElements.qaweb_main_url(page)
        print(" - Pass")

        # 최하단 스크롤 > 이용약관 진입 >홈화면 되돌아오기
        page.get_by_text("고객센터").scroll_into_view_if_needed()
        print("이용약관 링크 동작 확인 및 이동된 페이지 탭별 노출 확인", end='')
        page.get_by_role("link", name="이용약관").click()
        page.wait_for_timeout(300)
        expect(page.get_by_role("heading", name="오늘의집 서비스 이용 약관"), "고객 이용약관 페이지 접근하지 못하였습니다.").to_be_visible()
        PageElements.qaweb_main_url(page)
        print(" - Pass")

        # 최하단 스크롤 > 개인정보 처리 방침 진입 > 파트너개인정보처리방침, 상품운영정책 탭별 확인 > 홈화면 되돌아오기
        page.get_by_text("고객센터").scroll_into_view_if_needed()
        print("개인정보처리방침 링크 동작 확인 및 이동된 페이지 확인", end='')
        page.get_by_role("link", name="개인정보 처리방침", exact=True).click()
        page.wait_for_timeout(300)
        expect(page.get_by_text("오늘의집 서비스 개인정보 처리방침"), "개인정보처리방침 페이지 접근하지 못하였습니다.").to_be_visible()
        page.get_by_role("list").get_by_text("파트너 개인정보 처리방침").click()
        page.wait_for_timeout(300)
        expect(page.get_by_role("heading", name="오늘의집 파트너 개인정보 처리방침"), "파트너 개인정보처리방침 페이지 접근하지 못하였습니다.").to_be_visible()
        # page.get_by_text("상품운영정책").click()
        # page.wait_for_timeout(300)
        # expect(page.locator("h1").filter(has_text=re.compile(r"^상품운영정책$")), "상품운영정책 페이지 접근하지 못하였습니다.").to_be_visible()
        PageElements.qaweb_main_url(page)
        print(" - Pass")

        # 최하단 스크롤 > 공지사항 >홈화면 되돌아오기
        page.get_by_text("고객센터").scroll_into_view_if_needed()
        print("공지사항 링크 동작 확인 및 이동된 페이지 탭별 노출 확인", end='')
        page.get_by_role("link", name="공지사항").click()
        page.wait_for_timeout(300)
        expect(page.get_by_role("heading", name="공지사항"), "공지사항 페이지 접근하지 못하였습니다.").to_be_visible()
        PageElements.qaweb_main_url(page)
        print(" - Pass")

        # 최하단 스크롤 > 안전거래센터 >홈화면 되돌아오기
        # page.get_by_text("고객센터").scroll_into_view_if_needed()
        # print("안전거래센터 링크 동작 확인 및 이동된 페이지 탭별 노출 확인", end='')
        # with page.expect_popup() as page3_info:
        #         page.get_by_role("link", name="안전거래센터").click()
        # page3 = page3_info.value
        # page.wait_for_timeout(500)
        # expect(page3.get_by_role("heading", name="무엇을 도와드릴까요?"), "안전거래센터 페이지 접근하지 못하였습니다.").to_be_visible()
        # page3.close()
        # PageElements.qaweb_main_url(page)
        # print(" - Pass")

       # 최하단 스크롤 > 입점신청 >홈화면 되돌아오기
        # page.get_by_text("고객센터").scroll_into_view_if_needed()
        # print("입점신청 링크 동작 확인 및 이동된 페이지 탭별 노출 확인", end='')
        # page.get_by_role("link", name="입점신청").click()
        # page.wait_for_timeout(500)
        # expect(page.get_by_role("heading", name="오늘의집 입점안내"), "입점신청 페이지 접근하지 못하였습니다.").to_be_visible()
        # PageElements.qaweb_main_url(page)
        # print(" - Pass")

       # 최하단 스크롤 > 제휴/광고문의 >홈화면 되돌아오기
        page.get_by_text("고객센터").scroll_into_view_if_needed()
        print("제휴/광고문의 링크 동작 확인 및 이동된 페이지 탭별 노출 확인", end='')
        page.get_by_role("link", name="제휴/광고 문의").click()
        page.wait_for_timeout(500)
        expect(page.locator("p").filter(has_text="제휴/광고 문의"), "제휴/광고문의 페이지 접근하지 못하였습니다.").to_be_visible()
        PageElements.qaweb_main_url(page)
        print(" - Pass")

       # 최하단 스크롤 > 시공파트너 안내 >홈화면 되돌아오기
        page.get_by_text("고객센터").scroll_into_view_if_needed()
        print("시공파트너 안내 링크 동작 확인 및 이동된 페이지 탭별 노출 확인", end='')
        page.get_by_role("link", name="시공파트너 안내").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("heading", name="오늘의집에서\n우리지역 고객을 만나보세요"), "제휴/광고문의 페이지 접근하지 못하였습니다.").to_be_visible()
        PageElements.qaweb_main_url(page)
        print(" - Pass")

       # 최하단 스크롤 > 상품광고 소개 >홈화면 되돌아오기
        page.get_by_text("고객센터").scroll_into_view_if_needed()
        print("상품광고 소개 링크 동작 확인 및 이동된 페이지 탭별 노출 확인", end='')
        page.get_by_role("link", name="상품광고 소개").click()
        page.wait_for_timeout(500)
        expect(page.get_by_role("heading", name="오늘의집 광고 비즈니스"), "제휴/광고문의 페이지 접근하지 못하였습니다.").to_be_visible()
        PageElements.qaweb_main_url(page)
        print(" - Pass")

       # 최하단 스크롤 > 고객의소리 >홈화면 되돌아오기
        page.get_by_text("고객센터").scroll_into_view_if_needed()
        print("고객의 소리 링크 동작 확인 및 이동된 페이지 탭별 노출 확인", end='')
        page.get_by_role("link", name="고객의 소리").click()
        page.wait_for_timeout(500)
        expect(page.get_by_text("이메일 문의하기"), "제휴/광고문의 페이지 접근하지 못하였습니다.").to_be_visible()
        PageElements.qaweb_main_url(page)
        print(" - Pass")
        
    def check_email_qna(page):
         # [로그인] 최하단 스크롤 > 이메일 문의 진입 > 
        page.get_by_text("고객센터").scroll_into_view_if_needed()
        print("이메일 문의 링크 동작 확인 및 이동된 페이지 확인", end='')
        page.get_by_role("link", name="이메일 문의").click()
        page.wait_for_timeout(500)
        expect(page.get_by_text("이메일 문의하기"), "이메일 문의 페이지 접근하지 못하였습니다.").to_be_visible()
        print(" - Pass")
        
        # [로그인] 이메일 문의 진행하기
        print("이메일 문의 진행 동작 확인", end='')
        page.locator("select[name=\"type\"]").select_option("9")
        page.get_by_placeholder("이름").click()
        page.get_by_placeholder("이름").fill("test")
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("ohouseqa@gmail.com")
        page.get_by_placeholder("이메일").press("Tab")
        page.get_by_placeholder("제목").fill("test")
        page.get_by_placeholder("문의 내용").click()
        page.get_by_placeholder("문의 내용").fill("test")
        ''' #파일 업로드는 지정된 파일로만 해야해서 원격으로 실행에 대한 체크만 될 수 있고 지정된 PC에는 1.png라는 이름의 파일이 있어야하는 문제가 있음
        page.get_by_text("첨부파일").click()
        page.locator("body").set_input_files("1.png")
        page.get_by_role("button", name="제출하기").click() 
        '''
        page.get_by_role("button", name="제출하기").click()
        page.wait_for_timeout(500)
        expect(page.get_by_text("의견이 접수되었습니다"), "이메일 문의 제출 완료 되지 못하였습니다.").to_be_visible()
        print(" - Pass")

    def check_footer(page):
        # 푸터 이동
        page.get_by_role("link", name="회사소개").scroll_into_view_if_needed()
        expect(page.get_by_text("|(주)버킷플레이스"), '회사명 미노출').to_be_visible()
        expect(page.get_by_text("사업자등록번호 119-86-91245"), '사업자등록번호 미노출').to_be_visible()
        page.get_by_role("link", name="이용약관").click()
        expect(page.get_by_role("heading", name="오늘의집 서비스 이용 약관"), '사업자등록번호 미노출').to_be_visible()




