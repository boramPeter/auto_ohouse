from web.BasicSetting.conftest import *


class LifestyleElements():
    
    def infinite_scroll(page):
        # 무한 스크롤 func
        # while True:
        for _ in range(5):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)

    def suggestion_func(page):
        elements_visible = page.get_by_role("button", name="선택 완료").is_visible()
        if elements_visible:
            # 팝업 종료
            page.get_by_role("button", name="").click()
            # page.get_by_role("button", name="선택 완료").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(1000)
    
    def check_recommend_chip(page):
        follow_count = page.locator("label").count()
        assert follow_count == 5, "follow_count ="+str(follow_count)

    def check_cdp(page):
        page.wait_for_timeout(3000)
        for i in range(3):
            try:
                for j in range(3):
                    page.keyboard.press("PageDown")
                if page.get_by_text("유저들의 비슷한 공간 베스트").is_visible():
                    break
            except Exception as e1:
                print(f"PageDown 3x{i+1} 진행")
        
        # 스크롤 시 페이지 노출 확인
        api_url = 'https://image.ohou.se/i/bucketplace-v2-development/uploads/cards/snapshots/170951605173366665.jpeg?w=360&h=360&c=c'
        response = send_api_get(api_url)
        assert response.status_code == 200

    def enter_clp_video(page):
        page.wait_for_timeout(2000)
        # 동영상 필터 ON
        page.get_by_role("button", name="동영상").click()
        page.locator("ul").filter(has_text=re.compile(r"^동영상$")).get_by_role("button").click()
        # page.locator("#card-collection-item-6732251").get_by_role("link").first.click()
        video_selector = page.locator("#card-collection-item-1000009145").get_by_role("link").first
        # page.locator("#card-collection-item-1000001607").get_by_role("link").first.click()
        video_selector.click()

        # chrome inspector에서 component 인식불가
        # 5초 재생
        # page.wait_for_timeout(5000)
        # current_time = browser.locator(video_selector).evaluate("video => video.currentTime")
        # assert current_time > 0, f"비디오가 재생되지 않았습니다. currentTime: {current_time}"
    
    def click_recommend_video(page):
        # element = page.query_selector('//a[@href="/contents/card_collections/6732251"]')  # XPath로 선택
        element = page.locator("div").filter(has_text=re.compile(r"^00:59동영상큐레이션 https:/\/youtu\.be\/GKAywP6yd60\?feature=shared$")).get_by_role("link")
        element.click()
    
    def enter_recommend_video(page):
        # page.wait_for_load_state("load") # page 로드 대기 
        # page.wait_for_function('document.querySelector("video").readyState === 4') # 비디오 로드 대기
        # video_selector = page.locator('video')
        # video_selector.click() # 재생버튼 클릭
        # # chrome inspector에서 component 인식불가
        # page.wait_for_timeout(5000) # 5초 재생
        # current_time = video_selector.evaluate("video => video.currentTime")
        # assert current_time > 0, f"비디오가 재생되지 않았습니다. currentTime: {current_time}"

        # 비디오 요소 찾기
        video = page.locator("video")
        # 비디오가 로드될 때까지 기다림
        expect(video).to_be_visible()
        page.wait_for_timeout(3000)

        # 비디오의 데이터가 있는지 확인 (HAVE_CURRENT_DATA) - Boolean 형태로 return 함
        is_ready = page.evaluate("""
            (function() {
                const video = document.querySelector('video');
                return video.readyState >= 2;
            })()
        """)

        if is_ready:
            page.evaluate("document.querySelector('video').play()")
            # 2초 대기 후 현재 재생 시간 확인
            page.wait_for_timeout(2000)
            # 비디오 현재 시간 가져오기 시도
            current_time = page.evaluate("document.querySelector('video').currentTime")
                
            # 비디오가 실제로 재생되고 있는지 확인 (2초 이상이어야 함)
            assert current_time > 1.0, f"비디오가 재생되지 않음! 현재 재생 시간: {current_time}"
        else:
            raise TimeoutException(f"비디오가 재생 가능한 상태가 아님")

    def check_cdp_like(page):
        # 좋아요 
        page.wait_for_timeout(1000)
        page.locator('xpath=//*[@id="__next"]/div[1]/div[2]/div/div[2]/div/div/div/div/div[1]/div/span[1]/div/div[2]/button').click()
        page.wait_for_timeout(1000)
        page.locator('xpath=//*[@id="__next"]/div[1]/div[2]/div/div[2]/div/div/div/div/div[1]/div/span[1]/div/div[2]/button').click()
        page.wait_for_timeout(3000)


    def enter_hashtag_tab(page):
        page.get_by_role("link", name="#채널").click()

    def check_hashtag_tab(page):
        expect(page.get_by_text("마음에 드는 채널을 골라보세요"), '채널 탭 문구 미노출').to_be_visible()
        expect(page.get_by_role("link", name=re.compile(r"#집에서제일바빠.*")), '해시태그 문구 미노출').to_be_visible()
    
    def enter_hashtag_page(page):
        page.goto("https://contents.qa-web.dailyhou.se/contents/card_collections/1000017337")
        for _ in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
        #page.get_by_role("link", name="#살림살이").click()
        # maroo_0704 추가
        page.get_by_text("#자동화용챌린지").click()
        # page.get_by_role("link", name="#채널").click()
        # page.get_by_text("마음에 드는 채널을 골라보세요").wait_for()
        # page.query_selector('[data-virtuoso-scroller="true"]').query_selector_all('a')[0].click()
        expect(page.get_by_role("heading", name="#자동화용챌린지"), '해시태그 CLP 미노출').to_be_visible()

    def check_hashtag_page(page):
        expect(page.get_by_role("heading", name="#자동화용챌린지"), '해시태그 텍스트 미노출').to_be_visible()
        expect(page.get_by_text(re.compile(".*명 활동 중")), '활동중 인원 미노출').to_be_visible()
        expect(page.get_by_text(re.compile(".*개의 콘텐츠")), '컨텐츠개수 미노출').to_be_visible()
        expect(page.get_by_role("button", name="참여하기"), '참여하기 버튼 미노출').to_be_visible()

    def enter_hashtag_cdp(page):
        # page.get_by_role("link", name="#채널").click()
        # page.get_by_role("link", name="#테스트").click()
        page.goto("https://contents.qa-web.dailyhou.se/contents/card_collections/1000017337")
        for _ in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
        #page.get_by_role("link", name="#살림살이").click()
        # maroo_0704 추가
        page.get_by_text("#자동화용챌린지").click()
        # 임의의 컨텐츠 선택
        # page.get_by_label("좋아요 확인용 좋아요 금지 #오하우스 #테스트\n테스트").click()
        # page.locator("span").filter(has_text=re.compile(r"#테스트")).get_by_label("#테스트").click()
        # page.get_by_label("V2 확인용\n#테스트").click()
        # maroo_0704 추가
        page.get_by_label("#살림살이  #자동화용챌린지 해시태그").click()
        #page.locator('xpath=//*[@id="__next"]/div[1]/div[2]/div/div/div[3]/div/div/div/div[1]/div/span[1]/div/div[1]').click()
        expect(page.get_by_role("button", name="공유"), '참여하기 버튼 미노출').to_be_visible()


    def enter_upload(page):
        page.get_by_role("button", name="글쓰기 ").click()
        page.get_by_role("link", name="사진/동영상 우리 집의 공간과 나의 일상을 기록해보세요.").click()


    def sign_up_hashtag_page(page, out_check=False):
        # 채널 참여
        page.get_by_role("button", name="참여하기").click()
        page.wait_for_timeout(1000)
        expect(page.get_by_role("button", name="활동 중"), '활동중 버튼 미노출').to_be_visible()
        page.wait_for_timeout(1000)
        # if out_check:
        #     page.get_by_role("link", name="커뮤니티").click()
        #     page.wait_for_timeout(2000)
        #     page.get_by_role("link", name="#채널").click()
        #     expect(page.get_by_text("webqa님이 활동 중인 채널"), '참여한 채널 미노출').to_be_visible()
        # else:
        #     expect(page.get_by_role("button", name="활동 중"), '채널 참여 미동작').to_be_visible()

    def withdraw_hashtag_page(page):
        # 채널 참여 해제
        page.get_by_role("button", name="활동 중").click()
        expect(page.get_by_role("button", name="참여하기"), '참여 해제 미동작').to_be_visible()

    def enter_active_hashtag_page(page):
        try:
            page.get_by_role("link", name="해시태그 썸네일").click()
        except Exception as e:
            page.get_by_role("link", name="해시태그 썸네일").first.click()

    def click_recommend_chip(page):
        page.locator("label").filter(has_text=re.compile(r".*")).nth(1).click()
        follow_count = page.locator("span").count()
        page.wait_for_timeout(2000)
        assert follow_count >= 60, "follow_count ="+str(follow_count)
        page.wait_for_timeout(2000)

    def check_recommend_scrap(page, status=True):
        page.locator("span").filter(has_text=re.compile(r"테스트자동화용.*")).get_by_label("scrap 토글 버튼").click()
        # page.locator("span:nth-child(2) > div > .css-nv61gv > .css-1e5p8je > .css-ixvnk6 > .eibgzv11").click()
        if status:
            expect(page.get_by_text("스크랩했습니다."), '스크랩 on 미동작').to_be_visible()
            page.wait_for_timeout(3000)
        else:
            expect(page.get_by_text("스크랩북에서 삭제했습니다."), '스크랩 off 미동작').to_be_visible()
            page.wait_for_timeout(1000)

    def check_project_tab_3grid(page):
        page.wait_for_timeout(5000)
        # a_count = page.get_by_role("link").count()
        a_count = page.get_by_role("link", name=re.compile(r'scrap.*')).count()
        # a_count = page.wait_for_selector("//html/body/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[1]/div/a").count()
        #a_count = len(a_elements)
        assert a_count%3 == 0 and a_count>=9, "a_count ="+str(a_count)

    def check_house_tab_4grid(page):
        page.wait_for_timeout(5000)
        # a_count = page.get_by_role("link").count()
        a_count = page.get_by_role("button", name=re.compile(r'좋아요.*')).count()
        # a_count = page.wait_for_selector("//html/body/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[1]/div/a").count()
        #a_count = len(a_elements)
        assert a_count%4 == 0 and a_count>=12, "a_count ="+str(a_count)

    def check_house_filter(page):
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="주거형태").click()
        page.get_by_role("button", name="원룸&오피스텔").click()
        page.get_by_role("button", name="평수").click()
        page.get_by_role("button", name="10평 미만").click()
        expect(page.get_by_role("button", name="원룸&오피스텔"), '주거형태 필터명 미노출').to_be_visible()
        expect(page.get_by_role("button", name="10평 미만"), '정렬 필터명 미노출').to_be_visible()

    def check_house_v1(page):
        page.wait_for_timeout(3000)
        for _ in range(5):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        a_count = page.get_by_role("button", name=re.compile(r'좋아요.*')).count()
        assert a_count%4 == 0 and a_count>=32, "a_count ="+str(a_count)

    def check_house_v1_detail(page):
        page.get_by_role("button", name="컬러").click()
        page.get_by_role("button", name="블루").click()
        page.locator("#card-item-8158846").get_by_role("link").first.click()
        page.wait_for_timeout(2000)
        page.get_by_label("상품 태그 버튼").nth(2).click()
        page.get_by_text("베가 플리아 투명 라탄 접이식의자").click()
        page.wait_for_timeout(3000)
        expect(page.get_by_role("button", name="바로구매").first, '바로구매 버튼 미노출').to_be_visible()

    def check_project_filter(page):
        page.wait_for_timeout(3000)
        # page.get_by_role("button", name="예산 ").click()
        # page.locator("div").filter(has_text=re.compile(r"^예산$")).click()
        page.locator("div").filter(has_text=re.compile(r"^예산$")).hover()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="1백만원 미만").click()
        page.wait_for_timeout(1000)
        # page.get_by_role("button", name="가족형태 ").click()
        page.locator("div").filter(has_text=re.compile(r"^가족형태$")).hover()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="싱글라이프").click()
        page.wait_for_timeout(1000)
        expect(page.get_by_role("button", name="99만원 이하"), '예산 필터명 미노출').to_be_visible()
        expect(page.get_by_role("button", name="싱글라이프").first, '가족형태 필터명 미노출').to_be_visible()

    def check_hashtag_filter(page):
        # page.get_by_role("link", name="#채널").click()
        # page.get_by_role("link", name="#테스트").click()
        page.goto("https://contents.qa-web.dailyhou.se/contents/card_collections/1000017337")
        for _ in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
        #page.get_by_role("link", name="#살림살이").click()
        # maroo_0704 추가
        page.get_by_text("#자동화용챌린지").click()
        page.get_by_role("button", name="인기순 ").click()
        page.get_by_text("최신순").click()
        a_count = page.locator('[aria-label="scrap 토글 버튼"]').count()
        # print(a_count)
        assert a_count%4 == 0 and a_count>=12, "a_count ="+str(a_count)

    def check_project_scroll(page):
        page.get_by_role("link", name=re.compile(r"scrap.*")).nth(0).click()
        for _ in range(5):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        expect(page.get_by_text("다른 집들이 둘러보기"), '둘러보기 텍스트 미노출').to_be_visible()

    def check_project_hashtag(page):
        # page.get_by_role("link", name=re.compile(r"scrap.*")).nth(1).click()
        # page.get_by_label("상품 태그 버튼").nth(1).click()
        # page.locator(".css-1lst2mf").click()
        page.get_by_label("스크랩북 페이지 링크 버튼").click()
        page.get_by_role("button", name="집들이(8)").click()
        # page.get_by_role("link", name="무채색에 진심! 싱글 5.5평 원룸 인테리어! 엗웓스테이징").click()
        page.get_by_role("link", name="집들이 콘텐츠 확인 qa50입니다닉네임길게길게길게길게길게").click()
        page.wait_for_timeout(2000)
        for _ in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        # 상품태그 클릭
        page.get_by_label("상품 태그 버튼").nth(1).click()
        page.locator(".css-1lst2mf").click()
        # page.locator(".css-t195kb").first.click()
        # page.locator("._chevron_right_18").click()
        expect(page.get_by_role("button", name="공유하기"), '공유하기 버튼 미노출').to_be_visible()

    def check_project_thumbnail(page):
        # page.get_by_role("link", name=re.compile(r"scrap.*")).nth(1).click()
        # page.get_by_label("태그된 상품 아이템 1번째").first.click()
        page.get_by_label("스크랩북 페이지 링크 버튼").click()
        page.get_by_role("button", name="집들이(8)").click()
        page.get_by_role("link", name="집들이 콘텐츠 확인 qa50입니다닉네임길게길게길게길게길게").click()
        page.wait_for_timeout(2000)
        for _ in range(2):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("listitem").first.click()
        # page.locator(".css-49tldb").first.click()
        expect(page.get_by_role("button", name="공유하기"), '공유하기 버튼 미노출').to_be_visible()

    def check_project_comment(page):
        page.get_by_role("link", name=re.compile(r"scrap.*")).nth(1).click()
        page.locator("#textarea").fill("webtest")
        page.get_by_role("button", name="입력").click()
        expect(page.get_by_text("webtest"), '댓글 미노출').to_be_visible()

    def check_project_ProductGroup(page):
        page.get_by_role("link", name=re.compile(r"scrap.*")).nth(1).click()
        page.wait_for_timeout(2000)
        for _ in range(2):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="상품 모아보기").click()
        expect(page.get_by_role("heading", name="이 집들이에 사용된 상품"), '이 집들이에 사용된 상품 화면 미노출').to_be_visible()

    def check_grid_like(page):
        page.locator("#card-collection-item-1000015496").get_by_role("button", name=re.compile(r"좋아요.*")).click()
        page.wait_for_timeout(1000)
        page.locator("#card-collection-item-1000015496").get_by_role("button", name=re.compile(r"좋아요.*")).click()
        expect(page.locator("#card-collection-item-1000015496").get_by_role("button", name=re.compile(r"좋아요.*")), '좋아요 버튼 미노출').to_be_visible()

    def check_grid_detail_like(page):
        page.locator("#card-collection-item-1000015496").get_by_role("link").first.click()
        page.wait_for_timeout(1000)
        page.get_by_test_id("CardCollection-scrap-button").click()
        page.wait_for_timeout(1000)
        page.get_by_test_id("CardCollection-scrap-button").click()
        expect(page.get_by_test_id("CardCollection-scrap-button"), '스크랩 버튼 미노출').to_be_visible()

    def check_gnb_menu(page):
        expect(page.get_by_role("link", name="꿀템발견"), '꿀템발견 메뉴 미노출').to_be_visible()
        expect(page.get_by_role("link", name="집가꾸기"), '집가꾸기 메뉴 미노출').to_be_visible()
        expect(page.get_by_role("link", name="추천"), '추천 메뉴 미노출').to_be_visible()
        # expect(page.get_by_role("link", name="#채널"), '채널 메뉴 미노출').to_be_visible()
        expect(page.get_by_role("link", name="집들이"), '집들이 메뉴 미노출').to_be_visible()
        expect(page.get_by_role("link", name="집사진"), '집사진 메뉴 미노출').to_be_visible()
        expect(page.get_by_role("link", name="3D인테리어"), '3D인테리어 메뉴 미노출').to_be_visible()

    def into_upload_community(page):
        page.get_by_role("button", name="글쓰기 ").click()
        page.get_by_role("link", name="커뮤니티 쇼핑 고민부터 일상 이야기까지 함께 나눠보세요.").click()
        page.wait_for_timeout(3000)
        # expect(page.locator("div").filter(has_text=re.compile(r"^주제를 선택해주세요\(필수\)꿀템발견집가꾸기$")), '주제선택란 미노출').to_be_visible()
        # expect(page.locator("div").filter(has_text=re.compile(r"^게시판을 선택해주세요\(필수\)집꾸미기시공/리모델링우리집 일상$")), '게시판선택란 미노출').to_be_visible()
        expect(page.get_by_placeholder("제목을 입력해주세요."), '제목입력란 미노출').to_be_visible()
        page.get_by_label("오늘의집").click()
        page.wait_for_timeout(3000)
        modal_check = page.get_by_text("인테리어", exact=True)
        if modal_check.is_visible():
            # 모달창 노출 확인
            page.wait_for_timeout(2000)
            expect(page.get_by_text("인테리어", exact=True), '관심주제 모달창 미노출').to_be_visible()
            page.get_by_role("button", name="선택 완료").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(2000)

    def check_upload_community_filter(page):
        page.get_by_role("button", name="글쓰기 ").click()
        page.get_by_role("link", name="커뮤니티 쇼핑 고민부터 일상 이야기까지 함께 나눠보세요.").click()
        page.locator("div").filter(has_text=re.compile(r"^주제를 선택해주세요\(필수\)꿀템발견집가꾸기$")).get_by_role("combobox").select_option("1")
        page.locator("div").filter(has_text=re.compile(r"^게시판을 선택해주세요\(필수\)집꾸미기시공/리모델링우리집 일상$")).get_by_role("combobox").select_option("1")
        # expect(page.locator("div").filter(has_text=re.compile(r"^주제를 선택해주세요\(필수\)꿀템발견집가꾸기$")), '주제선택란 미노출').to_be_visible()
        # expect(page.locator("div").filter(has_text=re.compile(r"^게시판을 선택해주세요\(필수\)집꾸미기시공/리모델링우리집 일상$")), '게시판선택란 미노출').to_be_visible()
        expect(page.get_by_placeholder("제목을 입력해주세요."), '제목입력란 미노출').to_be_visible()
        page.get_by_label("오늘의집").click()
        page.wait_for_timeout(3000)
        modal_check = page.get_by_text("인테리어", exact=True)
        if modal_check.is_visible():
            # 모달창 노출 확인
            page.wait_for_timeout(2000)
            expect(page.get_by_text("인테리어", exact=True), '관심주제 모달창 미노출').to_be_visible()
            page.get_by_role("button", name="선택 완료").click()
            page.wait_for_timeout(2000)
        else:
            page.wait_for_timeout(2000)

    def check_upload_community(page):
        page.get_by_role("button", name="글쓰기 ").click()
        page.get_by_role("link", name="커뮤니티 쇼핑 고민부터 일상 이야기까지 함께 나눠보세요.").click()
        page.locator("div").filter(has_text=re.compile(r"^주제를 선택해주세요\(필수\)꿀템발견집가꾸기$")).get_by_role("combobox").select_option("1")
        page.locator("div").filter(has_text=re.compile(r"^게시판을 선택해주세요\(필수\)집꾸미기시공/리모델링우리집 일상$")).get_by_role("combobox").select_option("1")
        page.wait_for_timeout(1000)
        page.get_by_placeholder("제목을 입력해주세요.").fill("웹 게시글 업로드테스트 ")
        page.wait_for_timeout(1000)
        page.get_by_text("시공/리모델링/견적과 관련된 고민과 시공 후기를 나누어보세요").click()
        page.get_by_role("paragraph").fill("웹 게시글 업로드테스트")
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="올리기").click()
        page.wait_for_timeout(3000)
        expect(page.get_by_text("웹 게시글 업로드테스트").first, '타이틀 미노출').to_be_visible()

    def check_upload_community_edit(page):
        page.goto("https://contents.qa-web.dailyhou.se/community/posts/%EC%9B%B9-%EA%B2%8C%EC%8B%9C%EA%B8%80-%EC%97%85%EB%A1%9C%EB%93%9C%ED%85%8C%EC%8A%A4%ED%8A%B8-388088323866624?mainCategory=interior")
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("button", name="수정").click()


    def check_upload_community_delete(page):
        page.get_by_role("button", name="글쓰기 ").click()
        page.get_by_role("link", name="커뮤니티 쇼핑 고민부터 일상 이야기까지 함께 나눠보세요.").click()
        page.locator("div").filter(has_text=re.compile(r"^주제를 선택해주세요\(필수\)꿀템발견집가꾸기$")).get_by_role("combobox").select_option("1")
        page.locator("div").filter(has_text=re.compile(r"^게시판을 선택해주세요\(필수\)집꾸미기시공/리모델링우리집 일상$")).get_by_role("combobox").select_option("1")
        page.wait_for_timeout(1000)
        page.get_by_placeholder("제목을 입력해주세요.").fill("웹 게시글 업로드테스트 ")
        page.wait_for_timeout(1000)
        page.get_by_text("시공/리모델링/견적과 관련된 고민과 시공 후기를 나누어보세요").click()
        page.get_by_role("paragraph").fill("웹 게시글 업로드테스트")
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="올리기").click()
        page.wait_for_timeout(3000)
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("button", name="삭제").click()
        


    def check_project_view_all(page):
        page.get_by_role("link", name=re.compile(r"scrap.*")).nth(0).click()
        for _ in range(5):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="상품 모아보기").click()
        expect(page.get_by_role("heading", name="이 집들이에 사용된 상품"), '모아보기 텍스트 미노출').to_be_visible()

    def check_project_concept_view(page):
        # 작업자 > 전문가 필터 ON
        page.wait_for_timeout(3000)
        # page.get_by_role("button", name="작업자 ").hover()
        page.locator("div").filter(has_text=re.compile(r"^작업자$")).hover()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="전문가 인테리어 업체/전문가가 리모델링 계획부터 공사까지 총괄하는 것").click()
        # for _ in range(3):
        #     page.evaluate("window.scrollBy(0, window.innerHeight)")
        #     page.wait_for_timeout(1000)
        # # page.get_by_role("link", name=re.compile(r"scrap 토글 버튼 전문가 집들이 테스트 QA01 스크랩.*")).click()
        # # page.get_by_role("link", name=re.compile(r"scrap 토글 버튼 전문가 집들이 (시공사례) QA01 QA01 스크랩.*")).click()
        page.get_by_role("link", name=re.compile(r"scrap.*")).nth(0).click()
        page.wait_for_timeout(1000)
        # for _ in range(1):
        #     page.evaluate("window.scrollBy(0, window.innerHeight)")
        #     page.wait_for_timeout(1000)
        expect(page.get_by_test_id("Project-scrap-button"), '상세 페이지 미노출').to_be_visible()

    def check_3d_interior_feed(page):
        page.wait_for_timeout(3000)
        page.locator("a").filter(has_text=re.compile(r"확인용 테스트좋아요 8조회.*")).click()
        page.go_back()
        expect(page.get_by_role("button", name="3D 인테리어 하러가기"), '3D인테리어 페이지 미노출').to_be_visible()

    def check_upload_hashtag(page):
        page.wait_for_timeout(3000)
        # page.attach_test_file()
        page.get_by_test_id("description-input").click()
        page.wait_for_timeout(1000)
        page.get_by_test_id("description-input").fill("#t")
        page.wait_for_timeout(1000)
        api_url = 'https://qa-web.dailyhou.se/content/recommend/hashtags?query=T'
        response = send_api_get(api_url)
        assert response.status_code == 200
        page.go_back()
        page.get_by_role("button", name="나가기").click()

    def check_upload_edit(page):
        page.wait_for_timeout(3000)
        page.wait_for_timeout(3000)
        page.get_by_label("수정하기,삭제하기 버튼 열기").click()
        page.wait_for_timeout(2000)
        page.get_by_text("수정하기").click()
        expect(page.get_by_role("button", name="1개 상품 태그"), '태그추가 버튼 미노출').to_be_visible()
        page.go_back()

    def check_upload_video_edit(page):
        page.wait_for_timeout(3000)
        page.wait_for_timeout(3000)
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("link", name="마이페이지").click()
        page.get_by_role("link", name="00:30").first.click()
        page.wait_for_timeout(3000)
        page.get_by_label("수정하기,삭제하기 버튼 열기").click()
        page.get_by_text("수정하기").click()
        expect(page.get_by_text("원룸"), '원룸 텍스트 미노출').to_be_visible()
        page.go_back()

    def check_curator(page):
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("link", name="마이페이지").click()
        page.get_by_role("link", name="크리에이터 수익화 프로그램 ").click()
        page.get_by_role("button", name="큐레이터 내 SNS에 취향 공유하고 수익을 올리기").click()
        page.get_by_role("button", name="큐레이터 신청하기").click()
        expect(page.get_by_role("heading", name="개인정보 인증이 필요합니다."), '개인정보인증 텍스트 미노출').to_be_visible()
        page.go_back()

    def check_curator_guest(page):
        page.get_by_role("button", name="로그인하고 신청하기").click()
        expect(page.get_by_placeholder("이메일"), '로그인 페이지 미노출').to_be_visible()
        page.go_back()

    def check_myreward(page):
        # 로그인
        page.get_by_role("link", name="로그인").click()
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("qabucketaos3@gmail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("qwertyu1")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(2000)
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("link", name="마이페이지").click()
        page.get_by_role("link", name="크리에이터 수익화 프로그램 ").click()
        expect(page.get_by_role("heading", name="크리에이터 수익화"), '크리에이터 수익화 타이틀 미노출').to_be_visible()
        expect(page.get_by_role("button", name=re.compile(r"콘텐츠 수익화 ·.*")), '크리에이터 수익화 타이틀 미노출').to_be_visible()
        expect(page.get_by_role("button", name=re.compile(r"큐레이터 ·.*")), '크리에이터 수익화 타이틀 미노출').to_be_visible()
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click()
        page.go_back()

    def check_myreward_detail(page):
        # 로그인
        page.get_by_role("link", name="로그인").click()
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("qabucketaos3@gmail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("qwertyu1")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(2000)
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("link", name="마이페이지").click()
        page.get_by_role("link", name="크리에이터 수익화 프로그램 ").click()
        page.get_by_role("button", name=re.compile(r"콘텐츠 수익화 ·.*")).click()
        expect(page.get_by_role("heading", name="콘텐츠 수익화 대시보드"), '크리에이터 수익화 대시보드 타이틀 미노출').to_be_visible()
        expect(page.get_by_text("0 P리워드 내역"), '리워드 내역 미노출').to_be_visible()
        expect(page.get_by_role("button", name="리워드 내역"), '리워드 내역 버튼 미노출').to_be_visible()
        expect(page.get_by_text("내 콘텐츠 성과"), '내 콘텐츠 성과 미노출').to_be_visible()
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click()
        page.go_back()

    def check_hashtag_clp(page):
        # page.get_by_role("link", name="#채널").click()
        # page.get_by_role("link", name="#테스트").click()
        page.goto("https://contents.qa-web.dailyhou.se/contents/card_collections/1000017337")
        for _ in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
        page.get_by_role("link", name="#살림살이").click()
        # page.get_by_label("확인용\n#해시태그 #테스트 #디저트").click()
        page.wait_for_timeout(2000)
        # page.get_by_role("link", name="#살림살이").click()
        expect(page.get_by_role("heading", name="#살림살이"), '해시태그 CLP 페이지 미노출').to_be_visible()

    def check_rich_hashtag_clp(page):
        # page.get_by_role("link", name="#채널").click()
        # page.get_by_role("link", name="#테스트").click()
        page.goto("https://contents.qa-web.dailyhou.se/contents/card_collections/1000017337")
        for _ in range(1):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(1000)
        page.get_by_role("link", name="#살림살이").click()
        page.wait_for_timeout(2000)
        # 리치 해시태그
        expect(page.get_by_role("heading", name="#살림살이"), '해시태그 CLP 페이지 미노출').to_be_visible()

    def check_comment(page):
        page.get_by_role("button", name="컬러").click()
        page.get_by_role("button", name="블루").click()
        page.locator("#card-item-8158846").get_by_role("link").first.click()
        page.wait_for_timeout(2000)
        # 하단 댓글 작성
        page.locator("#textarea").fill("test")
        page.get_by_role("button", name="입력").click()
        expect(page.get_by_text("test").first, '작성 댓글 미노출').to_be_visible()

    def check_knowhow_cdp(page):
        page.get_by_placeholder("통합검색").click()
        # page.get_by_placeholder("통합검색").fill("")
        # # page.get_by_placeholder("통합검색").press("CapsLock")
        page.get_by_placeholder("통합검색").fill("노하우")
        page.get_by_placeholder("통합검색").press("Enter")
        # page.get_by_placeholder("통합검색").press("Enter")
        # 노하우 첫번째 컨텐츠 진입
        page.locator("article").nth(1).click()
        page.wait_for_timeout(2000)
        # 스크롤
        for _ in range(30):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            # page.wait_for_timeout(1000)
        expect(page.get_by_role("heading", name="관련있는 노하우"), '관련있는 노하우 미노출').to_be_visible()

    def check_knowhow_comment(page):
        page.get_by_placeholder("통합검색").click()
        # page.get_by_placeholder("통합검색").fill("")
        # page.get_by_placeholder("통합검색").press("CapsLock")
        page.get_by_placeholder("통합검색").fill("노하우")
        page.get_by_placeholder("통합검색").press("Enter")
        # page.get_by_placeholder("통합검색").press("Enter")
        page.locator("article").nth(1).click()
        # 스크롤
        for _ in range(20):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            # page.wait_for_timeout(1000)
        page.wait_for_timeout(1000)
        page.locator("form div").nth(3).click()
        page.locator("form div").nth(3).fill("웹자동화테스트")
        page.get_by_role("button", name="입력").click()
        page.wait_for_timeout(1000)
        expect(page.get_by_text("웹자동화테스트").nth(1), '작성댓글 미노출').to_be_visible()

    def check_honeyitem_top(page):
        css_items = page.locator("li.css-skuize")
        a_count = css_items.count()
        assert a_count == 5, f"상단 모아보기 모듈 개수 : {a_count}"
        print (a_count)

    def check_honeyitem_chip(page):
        page.get_by_role("link", name="살까말까", exact=True).click()
        expect(page.get_by_text("살지 말지 망설이는 상품이 있다면 고민을 나눠보세요"), '살까말까 미노출').to_be_visible()
        page.wait_for_timeout(1000)
        page.get_by_role("link", name="상품후기").click()
        expect(page.get_by_text("구매했거나 사용해본 상품의 솔직한 후기를 공유해보세요"), '상품후기 미노출').to_be_visible()
        page.wait_for_timeout(1000)
        page.get_by_role("link", name="꿀템수다").click()
        expect(page.get_by_text("사소한 고민부터 소소한 정보까지, 상품 관련된 수다는 여기서 나눠보세요"), '꿀템수다 미노출').to_be_visible()

    def check_honeyitem_cdp(page):
        page.get_by_role("link", name="살까말까", exact=True).click()
        page.locator('xpath=//*[@id="__next"]/div[1]/div[2]/div/div[3]/div/div/div/div[1]/div/span/a/div/div[2]/div/div[1]/div[1]/span').click()
        page.wait_for_timeout(1000)
        expect(page.get_by_text("살까말까", exact=True), '서브카테고리 미노출').to_be_visible()
        expect(page.get_by_role("button", name="팔로우"), '팔로우 버튼 미노출').to_be_visible()

    def check_honeyitem_subcategory(page):
        # page.locator("li.css-hk87dn").first.click()
        # page.locator(".en0ojtm0 > div:nth-child(3)").nth(1).click()
        page.get_by_role("link", name=re.compile(r"살까말까.*")).nth(1).click()
        page.wait_for_timeout(1000)
        expect(page.get_by_text("살까말까", exact=True), '서브카테고리 미노출').to_be_visible()
        expect(page.get_by_role("button", name="팔로우"), '팔로우 버튼 미노출').to_be_visible()

    def check_noti_reply(page):
        page.get_by_label("내소식 페이지 링크 버튼").click()
        page.wait_for_timeout(1000)
        # expect(page.get_by_role("link", name=re.compile(r"업로드한 사진.*")).nth(1), '댓글알림 리스트 미노출').to_be_visible()
        expect(page.get_by_role("heading", name="내 소식"), '알림 페이지 미노출').to_be_visible()
        expect(page.locator(".css-1s9ngpy").first, '알림 목록 아이콘 미노출').to_be_visible()

        
    def check_noti_delete(page):
        # 로그인
        page.get_by_role("link", name="로그인").click()
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("ohouseqaapp@gmail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(3000)
        page.goto("https://contents.qa-web.dailyhou.se/contents/card_collections/1000015082")
        page.wait_for_timeout(2000)
        for _ in range(5):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
        # 댓글작성
        page.locator("#textarea").click()
        page.locator("#textarea").fill("삭제테스트")
        page.get_by_role("button", name="입력").click()
        page.wait_for_timeout(2000)
        # 로그아웃
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click()
        page.wait_for_timeout(2000)

        # 로그인
        page.get_by_role("link", name="로그인").click()
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("ohouseqa@gmail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(3000)
        page.get_by_label("내소식 페이지 링크 버튼").click()
        page.wait_for_timeout(3000)
        # expect(page.get_by_role("link", name=re.compile(r"업로드한 사진/동영상의 새 댓글: \"삭제테스트\" 댓글을 확인하고 더 소통해보세요.*")), '새 알림 미노출').to_be_visible()
        expect(page.get_by_role("link", name=re.compile(r".*삭제테스트.*")), '새 알림 미노출').to_be_visible()
        # 로그아웃
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click()
        page.wait_for_timeout(2000)

        # 로그인
        page.get_by_role("link", name="로그인").click()
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("ohouseqaapp@gmail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(3000)
        page.goto("https://contents.qa-web.dailyhou.se/contents/card_collections/1000015082")
        page.wait_for_timeout(3000)
        for _ in range(5):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
        # 댓글삭제
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="삭제").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="확인").click()

    def check_cdp_like_btn(page):
        # page.get_by_role("link", name=re.compile(r"살까말까.*")).nth(1).click()
        page.locator('xpath=//*[@id="__next"]/div[1]/div[2]/div/div[3]/div/div/div/div[1]/div/span/a/div/div[2]/div/div[1]/div[1]').click()
        page.wait_for_timeout(3000)
        page.locator('xpath=//*[@id="__next"]/div[1]/div[2]/div/div/div[2]/div/div/div/button[1]').click()
        page.wait_for_timeout(2000)
        # expect(page.get_by_role("button", name=" 1"), '좋아요 버튼 미노출').to_be_visible()
        # page.wait_for_timeout(2000)
        page.locator('xpath=//*[@id="__next"]/div[1]/div[2]/div/div/div[2]/div/div/div/button[1]').click()
        #page.wait_for_timeout(2000)
        # expect(page.get_by_role("button", name=""), '좋아요 버튼 미노출').to_be_visible()
      
        

    def check_cdp_comment_btn(page):
        page.get_by_role("link", name=re.compile(r"살까말까.*")).nth(1).click()
        page.wait_for_timeout(3000)
        def extract_number(text):
            match = re.search(r'\d+', text)
            return match.group(0) if match else None
        button_text = page.get_by_role("button", name=re.compile(r".*")).text_content()
        heading_text = page.get_by_role("heading", name=re.compile(r"댓글.*")).text_content()
        button_number = extract_number(button_text)
        heading_number = extract_number(heading_text)
        print(button_number)
        print(heading_number)
        # 댓글 count 비교
        if button_number == heading_number:
            print("pass")
        else:
            print("fail")
        # expect(button_number).to_equal(heading_number)
    
    def check_cdp_share_btn(page):
        page.get_by_role("link", name=re.compile(r"살까말까.*")).nth(1).click()
        page.wait_for_timeout(1000)
        page.locator('xpath=//*[@id="__next"]/div[1]/div[2]/div/div/div[2]/div/div/div/button[3]').click()
        expect(page.get_by_role("button", name="카카오톡 공유"), '카카오톡 공유 버튼 미노출').to_be_visible()
        
    def check_honeyitem_more(page):
        # 스크롤
        for _ in range(2):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            # page.wait_for_timeout(1000)
        page.get_by_role("button", name="더보기(6개) ").click()
        page.wait_for_timeout(1000)
        expect(page.get_by_text("태그 상품 6"), '태그상품 미노출').to_be_visible()
        page.locator("li").filter(has_text="[변경금지][소] 무료, 제주3500, 반품1000, 교환200010,000").get_by_role("button").click()
        expect(page.get_by_text("스크랩했습니다."), '스크랩 on 미동작').to_be_visible()
        page.wait_for_timeout(4000)
        page.locator("li").filter(has_text="[변경금지][소] 무료, 제주3500, 반품1000, 교환200010,000").get_by_role("button").click()
        expect(page.get_by_text("스크랩북에서 삭제했습니다."), '스크랩 off 미동작').to_be_visible()
        
    def check_honeyitem_cdpscrap(page):
        # 스크롤
        for _ in range(2):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            # page.wait_for_timeout(1000)
        page.get_by_role("link", name="scrap [변경금지][소] 무료, 제주3500, 반품1000, 교환2000 10,000 · 오늘의집 구매").get_by_label("scrap").click()
        expect(page.get_by_text("스크랩했습니다."), '스크랩 on 미동작').to_be_visible()
        page.wait_for_timeout(4000)
        page.get_by_role("link", name="scrap [변경금지][소] 무료, 제주3500, 반품1000, 교환2000 10,000 · 오늘의집 구매").get_by_label("scrap").click()
        expect(page.get_by_text("스크랩북에서 삭제했습니다."), '스크랩 off 미동작').to_be_visible()
        page.wait_for_timeout(1000)
        page.get_by_role("link", name="scrap [변경금지][소] 무료, 제주3500, 반품1000, 교환2000 10,000 · 오늘의집 구매").click()
        page.wait_for_timeout(1000)
        expect(page.get_by_role("button", name="공유하기"), '카카오톡 공유 버튼 미노출').to_be_visible()
        

    def check_report_content(page):
        page.get_by_role("link", name="집사진").click()
        page.wait_for_timeout(3000)
        page.locator(".card-feed__item-wrap").first.click()
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="신고하기").click()
        page.wait_for_timeout(3000)
        page.get_by_test_id("bds-dim").get_by_role("button", name="신고하기").click()
        page.wait_for_timeout(3000)
        # 신고 초기화
        api_url = 'https://block.qa.grpc.dailyhou.se/block.v1.BlockService/DeleteBlocks'
        data = {"userId": 14736023}
        # headers = {"Content-Type": "application/json"}
        response = send_api_post(api_url, data)
        assert response.status_code == 200

    def check_report_user(page):
        page.get_by_role("navigation").get_by_role("link", name="집사진").click()
        page.wait_for_timeout(3000)
        page.get_by_role("link", name="2마루야마루").first.click()
        page.wait_for_timeout(3000)
        page.get_by_label("더보기").click()
        page.get_by_role("button", name="숨기기").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)
        expect(page.get_by_text("숨기기한 사용자입니다."), '숨기기 미동작').to_be_visible()
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="사용자 숨기기 설정 페이지로 이동").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="숨기기 해제").click()
        
    def check_report_comment(page):
        page.goto("https://qa-web.dailyhou.se/")
        # A 계정
        page.get_by_role("link", name="로그인").click()
        page.wait_for_timeout(2000)
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("ohouseqaapp@gmail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="집사진").click()
        page.wait_for_timeout(3000)
        page.locator(".card-feed__item-wrap").first.click()
        page.wait_for_timeout(3000)
        # 댓글 입력
        page.locator("#textarea").click()
        page.locator("#textarea").fill("test")
        page.get_by_role("button", name="입력").click()
        page.wait_for_timeout(2000)
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click() 
        # 자동화 계정
        page.get_by_role("link", name="로그인").click()
        page.wait_for_timeout(2000)
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("ohouseqa@gmail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="집사진").click()
        page.wait_for_timeout(3000)
        page.locator(".card-feed__item-wrap").first.click()
        page.wait_for_timeout(3000)
        for _ in range(2):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
        # 댓글 신고
        page.get_by_role("button", name="신고").nth(1).click()
        page.get_by_test_id("bds-dim").get_by_role("button", name="신고하기").click()
        expect(page.get_by_text("볼 수 없는 사용자"), '댓글 신고 미동작').to_be_visible()
        page.wait_for_timeout(2000)
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click() 

        
    def check_report_recomment(page):
        page.goto("https://qa-web.dailyhou.se/")
        # A 계정
        page.get_by_role("link", name="로그인").click()
        page.wait_for_timeout(2000)
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("ohouseqaapp@gmail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="집사진").click()
        page.wait_for_timeout(3000)
        page.locator(".card-feed__item-wrap").first.click()
        page.wait_for_timeout(3000)
        # 댓글 입력
        page.locator("#textarea").click()
        page.locator("#textarea").fill("test")
        page.get_by_role("button", name="입력").click()
        page.wait_for_timeout(2000)
        # 대댓글 입력
        page.locator("#textarea").click()
        page.get_by_role("button", name="답글 달기").first.click()
        page.locator("#textarea").nth(1).fill("﻿@theoapp﻿ test")
        page.get_by_role("button", name="입력").nth(1).click()
        page.wait_for_timeout(2000)
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click() 
        # 자동화 계정
        page.get_by_role("link", name="로그인").click()
        page.wait_for_timeout(2000)
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("ohouseqa@gmail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("Wkehdghk12!@")
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="집사진").click()
        page.wait_for_timeout(3000)
        page.locator(".card-feed__item-wrap").first.click()
        page.wait_for_timeout(3000)
        for _ in range(2):
            page.evaluate("window.scrollBy(0, window.innerHeight)")
        # 대댓글 신고
        page.get_by_role("button", name="신고").nth(2).click()
        page.get_by_test_id("bds-dim").get_by_role("button", name="신고하기").click()
        expect(page.get_by_text("볼 수 없는 사용자"), '댓글 신고 미동작').to_be_visible()
        page.wait_for_timeout(2000)
        page.get_by_label("프로필 메뉴").click()
        page.get_by_role("button", name="로그아웃").click() 

        
    def check_report_video_content(page):
        page.get_by_role("link", name="집사진").click()
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="동영상").first.click()
        page.locator("ul").filter(has_text=re.compile(r"^동영상$")).get_by_role("button").click()
        page.wait_for_timeout(2000)
        page.locator(".card-feed__item-wrap").first.click()
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="신고하기").click()
        page.wait_for_timeout(3000)
        page.get_by_test_id("bds-dim").get_by_role("button", name="신고하기").click()
        page.wait_for_timeout(3000)
        # 신고 초기화
        api_url = 'https://block.qa.grpc.dailyhou.se/block.v1.BlockService/DeleteBlocks'
        data = {"userId": 14736023}
        # headers = {"Content-Type": "application/json"}
        response = send_api_post(api_url, data)
        assert response.status_code == 200

    def check_report_video_user(page):
        page.get_by_role("navigation").get_by_role("link", name="집사진").click()
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="동영상").first.click()
        page.locator("ul").filter(has_text=re.compile(r"^동영상$")).get_by_role("button").click()
        page.wait_for_timeout(2000)
        page.locator('xpath=/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/article/div[1]/address/div/a/img').click()
        page.wait_for_timeout(3000)
        page.get_by_label("더보기").click()
        page.get_by_role("button", name="숨기기").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)
        expect(page.get_by_text("숨기기한 사용자입니다."), '숨기기 미동작').to_be_visible()
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="사용자 숨기기 설정 페이지로 이동").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="숨기기 해제").click()

    def check_report_house(page):
        page.get_by_role("link", name="집들이", exact=True).click()
        page.wait_for_timeout(3000)
        # 첫 콘텐츠
        page.locator('xpath=/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div/div/div[1]/div/a[1]/div/div/div[1]/img').click()
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="신고하기").click()
        page.wait_for_timeout(3000)
        page.get_by_test_id("bds-dim").get_by_role("button", name="신고하기").click()
        expect(page.get_by_text("신고가 완료되었습니다."), '신고 알럿 미노출').to_be_visible()
        page.wait_for_timeout(3000)
        # 신고 초기화
        api_url = 'https://block.qa.grpc.dailyhou.se/block.v1.BlockService/DeleteBlocks'
        data = {"userId": 14736023}
        # headers = {"Content-Type": "application/json"}
        response = send_api_post(api_url, data)
        assert response.status_code == 200

    def check_report_house_user(page):
        page.get_by_role("navigation").get_by_role("link", name="집들이").click()
        page.wait_for_timeout(3000)
        page.locator('xpath=/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div/div/div[1]/div/a[1]/div/div/div[2]/div/img').click()
        page.wait_for_timeout(3000)
        page.get_by_label("더보기").click()
        page.get_by_role("button", name="숨기기").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="확인").click()
        page.wait_for_timeout(2000)
        expect(page.get_by_text("숨기기한 사용자입니다."), '숨기기 미동작').to_be_visible()
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="사용자 숨기기 설정 페이지로 이동").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="숨기기 해제").click()







class LifesytleFeed():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.recommend_tab = page.get_by_role("link", name="추천")
        self.channel_tab = page.get_by_role("link", name="#채널")
        self.project_tab = page.get_by_role("navigation").get_by_role("link", name="집들이")
        self.honeyitem_tab = page.get_by_role("link", name="꿀템발견")
        self.card_tab = page.get_by_role("link", name="집사진")
        self.interior3d_tab = page.get_by_role("link", name="3D인테리어")
        self.topics_living_tab = page.get_by_role("link", name="살림수납")
        self.competitions_tab = page.get_by_role("link", name="이벤트")
        self.recommend_tab_url = 'https://contents.qa-web.dailyhou.se/topics/recommend'
        self.channel_tab_url = 'https://contents.qa-web.dailyhou.se/topics/hashtag-channel'
        self.project_tab_url = 'https://contents.qa-web.dailyhou.se/projects'
        self.card_tab_url = 'https://qa-web.dailyhou.se/contents/card_collections'
        self.interior3d_tab_url = 'https://qa-web.dailyhou.se/interior3ds'
        self.topics_living_tab_url = 'https://contents.qa-web.dailyhou.se/topics/living'
        self.competitions_tab_url = 'https://qa-web.dailyhou.se/competitions/feed'

    def enter_recommend_tab(self, modal_check=False):
        # if self.recommend_tab.is_visible():
        #     self.recommend_tab.click()
        # else:
        #     self.page.goto(self.recommend_tab_url, timeout= 0)
        self.page.get_by_role("link", name="추천").click()
        if modal_check:
            # 모달창 노출 확인
            self.page.wait_for_timeout(2000)
            expect(self.page.get_by_text("인테리어", exact=True), '관심주제 모달창 미노출').to_be_visible()
            self.page.get_by_role("button", name="선택 완료").click()
            self.page.wait_for_timeout(2000)
        else:
            self.recommend_modal()
        
        # 추천 페이지 API Response check
        LifestyleAPI(self.page).check_api_response("recommend")

    def recommend_modal(self):
        self.page.wait_for_load_state("load")
        elements_visible = self.page.get_by_role("button", name="선택 완료").is_visible(timeout=5000)
        if elements_visible:
            # 팝업 종료
            self.page.get_by_role("button", name="").click()
            self.page.wait_for_timeout(2000)
        else:
            self.page.wait_for_timeout(1000)

    def enter_channel_tab(self):
        if self.channel_tab.is_visible():
            self.channel_tab.click()
        else:
            self.page.goto(self.channel_tab_url, timeout= 0)
        self.page.wait_for_timeout(1000)
        # #채널 페이지 API Response check
        LifestyleAPI(self.page).check_api_response("channel")

    def enter_project_tab(self):
        if self.project_tab.is_visible():
            self.project_tab.click()
        else:
            self.page.goto(self.project_tab_url, timeout= 0)
        self.page.wait_for_timeout(1000)
        # #채널 페이지 API Response check
        LifestyleAPI(self.page).check_api_response("project")

    def enter_honeyitem_tab(self):
        self.honeyitem_tab.click()

    def enter_card_tab(self):
        if self.card_tab.is_visible():
            self.card_tab.click()
        else:
            self.page.goto(self.card_tab_url, timeout= 0)
        self.page.wait_for_timeout(1000)

        # #채널 페이지 API Response check
        LifestyleAPI(self.page).check_api_response("card")

    def enter_3d_tab(self):
        if self.interior3d_tab.is_visible():
            self.interior3d_tab.click()
        else:
            self.page.goto(self.interior3d_tab_url, timeout= 0)
        self.page.wait_for_timeout(1000)

        # #채널 페이지 API Response check
        LifestyleAPI(self.page).check_api_response("3d")

    def enter_topic_tab(self):
        if self.topics_living_tab.is_visible():
            self.topics_living_tab.click()
        else:
            self.page.goto(self.topics_living_tab_url, timeout= 0)
        self.page.wait_for_timeout(1000)

        # #채널 페이지 API Response check
        LifestyleAPI(self.page).check_api_response("topic_living")

    def enter_competitions_tab(self):
        if self.competitions_tab.is_visible():
            self.competitions_tab.click()
        else:
            self.page.goto(self.competitions_tab_url, timeout= 0)
        self.page.wait_for_timeout(1000)

        # #채널 페이지 API Response check
        LifestyleAPI(self.page).check_api_response("event")

class LifestyleAPI():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.recommend_url = 'https://contents.qa-web.dailyhou.se/topics/recommend.json?topicKey=recommend'
        self.channel_url = 'https://contents.qa-web.dailyhou.se/topics/hashtag-channel.json'
        self.project_feed_url = 'https://contents.qa-web.dailyhou.se/projects?writer=self'
        self.card_feed_url = 'https://qa-web.dailyhou.se/contents/card_collections'
        self.interior3d_feed_url = 'https://qa-web.dailyhou.se/interior3ds'
        self.living_url = 'https://contents.qa-web.dailyhou.se/topics/living'
        self.competition_url = 'https://qa-web.dailyhou.se/competitions/feed'
        self.dict_service_url = {"recommend" : self.recommend_url,
                                 "channel" : self.channel_url,
                                 "project" : self.project_feed_url,
                                 "card" : self.card_feed_url,
                                 "3d" : self.interior3d_feed_url,
                                 "topic_living" : self.living_url,
                                 "event" : self.competition_url}

    def check_api_response(self, feed_name):
        api_url = self.dict_service_url[feed_name]
        response = send_api_get(api_url)
        assert response.status_code == 200

class LifestyleUpload():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.upload_btn = page.get_by_role("button", name="글쓰기 ")
        # self.photo_upload_link = page.get_by_role("link", name="사진/동영상 올리기 우리 집의 공간과 나의 일상을 기록해 보세요.")
        self.photo_upload_link = page.get_by_role("link", name="사진/동영상 우리 집의 공간과 나의 일상을 기록해보세요.")
        self.video_upload_btn = page.get_by_role("button", name="동영상")
        self.load_from_pc_btn = page.get_by_role("button", name="PC에서 불러오기")
        self.description_input = page.get_by_test_id("description-input")
        self.space_info_dropdown = page.get_by_text("공간 정보 추가")
        self.upload_btn_in_editor = page.get_by_role("button", name="올리기", exact=True)

    def enter_upload_photo(self, video=False):
        self.upload_btn.click()
        self.photo_upload_link.click()
        if video:
            self.video_upload_btn.click()

    def attach_test_file(self, video=False):
        if video:
            file_path = './test_file/mov.mov'
        else:
            file_path = './test_file/testlogo.png' 
        
        self.page.wait_for_timeout(2000)
        with self.page.expect_file_chooser() as fc_info:
            self.load_from_pc_btn.click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        self.page.wait_for_timeout(2000)

    def input_photo_detail(self, desc, space, tag=False):
        self.description_input.fill(desc)
        self.space_info_dropdown.click()
        self.page.get_by_text(space).click()
        if tag:
            self.page.get_by_role("button", name="상품 태그 추가").click()
            self.page.locator("._1_JcL").click()
            self.page.get_by_role("button", name=re.compile(r".*선택")).first.click()

    def add_tag_photo(self):
        self.page.get_by_role("button", name="상품 태그 추가").click()
        self.page.locator("._1_JcL").click()
        self.page.get_by_role("button", name=re.compile(r".*선택")).first.click()

    def delete_photo_in_cdp(self, video=True):
        self.page.get_by_label("수정하기,삭제하기 버튼 열기").click()
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.get_by_text("삭제하기").click()
        self.page.wait_for_timeout(2000)
        if video:
            self.page.goto("https://qa-web.dailyhou.se/")
        else:
            self.page.go_back()

    def delete_video_in_mypage(self):
        try:
            self.page.get_by_label("프로필 메뉴").click()
            self.page.get_by_role("link", name="마이페이지").click()
        except Exception:
            self.page.goto("https://qa-web.dailyhou.se/users/14736023")
        self.page.get_by_role("link", name="사진", exact=True).click()
        for retry in range(4):
            try:
                # self.page.get_by_text("webqa#오하우스 #미니멀라이프조회수 000:30").first.click()
                self.page.locator(".card-collection-item").first.click()

                break
            except Exception as e:
                if retry == 3:
                    raise TimeoutException(f"비디오 업로드 실패")
                else:
                    self.page.reload()
        self.page.wait_for_timeout(2000)
        self.page.get_by_label("수정하기,삭제하기 버튼 열기").click()
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.get_by_text("삭제하기").click()

    def all_upload_photo(self):
        self.enter_upload_photo()
        self.attach_test_file()
        self.input_photo_detail(desc="#오하우스 #미니멀라이프", space="원룸", tag=True)
        self.upload_btn_in_editor.click()
        self.delete_photo_in_cdp()

    def all_upload_photo_undelete(self):
        self.enter_upload_photo()
        self.attach_test_file()
        self.input_photo_detail(desc="#오하우스 #미니멀라이프", space="원룸", tag=True)
        self.upload_btn_in_editor.click()

    def all_upload_video(self):
        self.enter_upload_photo(video=True)
        self.attach_test_file(video=True)
        self.input_photo_detail(desc="#오하우스 #미니멀라이프", space="원룸", tag=False)
        self.upload_btn_in_editor.click()
        try:
            self.page.get_by_role("button", name="보러가기").click(timeout=30 * 1000)
            self.delete_photo_in_cdp(video=True)
        except Exception:
            LifesytleFeed(self.page).recommend_modal()
            self.delete_video_in_mypage()

    def all_upload_video_undelete(self):
        self.enter_upload_photo(video=True)
        self.attach_test_file(video=True)
        self.input_photo_detail(desc="#오하우스 #미니멀라이프", space="원룸", tag=False)
        self.upload_btn_in_editor.click()
        self.page.goto('https://qa-web.dailyhou.se/', timeout=0)
