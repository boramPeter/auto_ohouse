from web.BasicSetting.conftest import *
from web.ObjectSetting.comm_orders import *




class CommClaimElements:   

    #입금 대기 취소 
    def account_cancel(page,order_id):
        page.goto(f"https://qa-web.dailyhou.se/orders/{order_id}")
        page.wait_for_timeout(2000)
        locator_count = page.get_by_role("button", name="주문취소").count()
        print(f"옵션의 수는 {locator_count}입니다.")

        if locator_count==1 : 
            page.get_by_role("button", name="주문취소").click()
            page.wait_for_timeout(2000)
        else:
            page.get_by_role("button", name="주문취소").first.click()
            page.wait_for_timeout(2000)
        page.get_by_role("button", name="취소하기").click()
        page.wait_for_timeout(2000)
    

    #주문상세 > 주문 취소 (즉시 취소)
    def order_cancel(page,order_id,cancel_type=None):       

        page.goto(f"https://qa-web.dailyhou.se/orders/{order_id}")
        page.wait_for_timeout(5000)               

        #상태 변경되지 않은 옵션이 있는지 체크
        retry = 0 
        locator = page.get_by_text("입금대기")        
        while retry < 5 :
            count_opt = locator.count()
            if count_opt > 0 :
                print(f"미변경 옵션 {count_opt}개. 새로고침 합니다.")
                page.reload() 
                retry +=1
                page.wait_for_timeout(5000)      
            else:
                print("상태 미변경건 없음")
                break      
        if retry == 5 and count_opt > 0:
            error_message = "retry 5회 진행. 옵션 상태가 변경되지 않았습니다."
            raise AssertionError(error_message)

        cancel_locator = page.get_by_role("button", name="주문취소")

        #단일 옵션 취소 
        if cancel_locator.count() == 1:    
            print(f"단일 옵션 취소 요청 진행합니다. ")
            cancel_locator.click()   
            page.wait_for_timeout(2000)

        elif cancel_locator.count() >=2:             
            #묶음일 경우, 각각 버튼 존재
            print(f"중복 옵션 취소 요청 진행합니다. ")
            cancel_locator.first.click()   
            page.wait_for_timeout(2000)                
            
            if cancel_type == "all":
                print("중복 옵션, 전체 취소 진행합니다.")           
                #전체선택 디폴트 체크 여부 확인 
                checkbox = page.get_by_role("checkbox", name = "전체 선택")
                
                if not checkbox.is_checked():
                   print("추가 옵션 선택 > 전체 선택 check Y")
                   page.get_by_role("checkbox", name="전체 선택").check()               
                else:
                    print("필수 옵션 선택 > 전체 선택 check N")
                page.wait_for_timeout(2000)                
            
            elif cancel_type == "part":
                print("중복 옵션, 부분 취소 진행합니다.")
        
        page.get_by_role("button", name="다음").click()
        page.wait_for_timeout(2000)                
        page.get_by_text("색상, 사이즈를 바꾸고 싶어요").click()   
        page.wait_for_timeout(2000)                
        page.get_by_role("button", name="다음").click()
        page.wait_for_timeout(2000)                
        page.get_by_role("button", name="주문취소").click(timeout=90000)
        page.wait_for_timeout(2000)                



    #주문 상세 > 취소 요청 (승인 취소)
    def cancel_request(page,order_id,cancel_type=None):
        page.goto(f"https://qa-web.dailyhou.se/orders/{order_id}")
        page.wait_for_timeout(2000)  

        #상태 변경되지 않은 옵션이 있는지 체크
        retry = 0 
        
        while retry < 5 :
            count_opt = page.get_by_text("결제완료").count()
            if count_opt > 0 :
                print(f"미변경 옵션 {count_opt}개. 새로고침 합니다.")
                page.reload() 
                retry +=1
                page.wait_for_timeout(5000)      
            else:
                print("상태 미변경건 없음")
                break      
        if retry == 5 and count_opt > 0:
            error_message = "retry 5회 진행. 옵션 상태가 변경되지 않았습니다."
            raise AssertionError(error_message)

        
        locator_count = page.get_by_role("button", name="취소요청").count()        
        print(f"옵션의 수는 {locator_count}입니다.")
        page.wait_for_timeout(2000)

        #단일 옵션 취소 
        if locator_count == 1:    
            print(f"단일 옵션 취소 요청 진행합니다. ")
            page.get_by_role("button", name="취소요청").click()
            page.wait_for_timeout(2000)
            page.get_by_role("button", name="계속하기").click()       
            page.wait_for_timeout(2000)

        elif locator_count >=2:             
            #묶음일 경우, 각각 버튼 존재
            print(f"중복 옵션 취소 요청 진행합니다. ")
            page.get_by_role("button", name="취소요청").first.click()   
            page.wait_for_timeout(2000)                
            page.get_by_role("button", name="계속하기").click()            
            page.wait_for_timeout(2000)                            
            if cancel_type == "all":
                print("중복 옵션, 전체 취소 진행합니다.")                
                #전체선택 디폴트 체크 여부 확인 
                checkbox = page.get_by_role("checkbox", name = "전체 선택")
                
                if not checkbox.is_checked():
                   print("추가 옵션 선택 > 전체 선택 check Y")
                   page.get_by_role("checkbox", name="전체 선택").check()               
                else:
                    print("필수 옵션 선택 > 전체 선택 check N")                
                page.wait_for_timeout(2000)                
            
            elif cancel_type == "part":
                print("중복 옵션, 부분 취소 진행합니다.")

        page.get_by_role("button", name="다음").click()
        page.wait_for_timeout(2000)                
        page.get_by_text("색상, 사이즈를 바꾸고 싶어요").click()   
        page.wait_for_timeout(2000)                
        page.get_by_role("button", name="다음").click()
        page.wait_for_timeout(2000)                
        page.get_by_role("button", name="취소요청").click(timeout=90000)
        page.wait_for_timeout(5000)


    #주문상세 > 반품/교환 요청 
    def claim_request(page,order_id,claim_type):

        page.goto(f"https://qa-web.dailyhou.se/orders/{order_id}")
        page.wait_for_timeout(2000)  

        #상태 변경되지 않은 옵션이 있는지 체크
        retry = 0 
        
        while retry < 5 :
            count_opt = page.get_by_text("결제완료").count()
            count_opt_2 = page.get_by_text("배송준비중").count()
            total_opt = count_opt+count_opt_2

            if total_opt > 0 :
                print(f"미변경 옵션 {total_opt}개. 새로고침 합니다.")
                page.reload() 
                retry +=1
                page.wait_for_timeout(5000)      
            else:
                print("상태 미변경건 없음")
                break      
        if retry == 5 and count_opt > 0:
            error_message = "retry 5회 진행. 옵션 상태가 변경되지 않았습니다."
            raise AssertionError(error_message)

        locator_count = page.get_by_role("button", name="반품·교환").count()
        print(f"옵션의 수는 {locator_count}입니다.")
        page.wait_for_timeout(2000)

        if locator_count == 1:
            print(f"단일 옵션 반품/교환 요청 진행합니다. ")
            page.get_by_role("button", name="반품·교환").click()
        elif locator_count >=2: 
            print(f"중복 옵션 반품/교환 요청 진행합니다. ")
            page.get_by_role("button", name="반품·교환").first.click()               
        page.wait_for_timeout(2000)

        if claim_type == "refund":
            page.get_by_role("button", name="반품요청").click()
        elif  claim_type == "exchange":
            page.get_by_role("button", name="교환요청").click()
        page.wait_for_timeout(2000)
        


            
    # 환불 flow(옵션 선택부터 신청 완료까지)
    def refund_func(page, refund_type, fault_type, collection_type):
        
        # refund_type
        if refund_type == "all":
            checkbox = page.get_by_role("checkbox", name="전체 선택")
            if not checkbox.is_checked():
                print("추가 옵션 선택 > 전체 선택 check Y")
                checkbox.check()
            else:
                print("필수 옵션 선택 > 전체 선택 check N")
        else:
            pass
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="다음").click()
        page.wait_for_timeout(2000)

        # 귀책 fault_type
        if fault_type == "seller":
            page.get_by_text("파손된 상품을 받았어요").click()
        elif fault_type == "buyer":
            page.get_by_text("색상, 사이즈를 바꾸고 싶어요").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="다음").click()
        page.wait_for_timeout(2000)

        # 송장 입력
        def input_invoice_info():
            page.get_by_text("상품을 이미 판매자에게 택배로 보냈어요").click()
            page.wait_for_timeout(2000)    
            page.get_by_title("택배사 선택").select_option("1")
            page.wait_for_timeout(2000)    
            page.get_by_placeholder("송장번호 입력").click()
            page.get_by_placeholder("송장번호 입력").fill("1234567890")
            page.wait_for_timeout(2000)    
        
        # collection_type
        if collection_type == "direct":
            #일반 상품 아니면, 송장 입력 처리 해야함
            try:                
                page.get_by_text("상품을 직접 수거해주세요").click()
                page.wait_for_timeout(2000)    
            except TimeoutError:
                input_invoice_info()
        elif collection_type == "courier":
            input_invoice_info()

        page.get_by_role("button", name="다음").click()
        page.wait_for_timeout(2000)
        
        page.get_by_role("button", name="반품요청").click()
        page.wait_for_timeout(5000)
        
               
                    

    #교환 flow
    def exchange_func(page,exchange_type,fault_type,collection_type):

        if exchange_type =="all":
            #전체선택 디폴트 체크 여부 확인 
            checkbox = page.get_by_role("checkbox", name = "전체 선택")                
            if not checkbox.is_checked():
                print("추가 옵션 선택 > 전체 선택 check Y")
                page.get_by_role("checkbox", name="전체 선택").check()               
            else:
                print("필수 옵션 선택 > 전체 선택 check N")
            page.wait_for_timeout(2000)  
        elif exchange_type == "part":
            page.wait_for_timeout(2000)  
        page.get_by_role("button", name="다음").click()
        page.wait_for_timeout(2000)  
        
        #fault_type
        if fault_type == "seller":
            page.get_by_text("상품 정보와 실제 상품이 달라요").click()
        elif fault_type == "buyer":
            page.get_by_text("색상, 사이즈를 바꾸고 싶어요").click()
        page.get_by_role("button", name="다음").click()
        page.wait_for_timeout(2000) 
    

        #송장 입력
        def input_invoice_info():
            page.get_by_text("상품을 이미 판매자에게 택배로 보냈어요").click()
            page.wait_for_timeout(2000)    
            page.get_by_title("택배사 선택").select_option("1")
            page.wait_for_timeout(2000)    
            page.get_by_placeholder("송장번호 입력").click()
            page.get_by_placeholder("송장번호 입력").fill("1234567890")
            page.wait_for_timeout(2000)    

        
        #collection_type
        if collection_type == "direct":
            try:
                page.get_by_text("상품을 직접 수거해주세요").click()
                page.wait_for_timeout(2000)     
            except TimeoutError:
                input_invoice_info()
        elif collection_type == "courier":
            input_invoice_info()

        page.wait_for_timeout(2000)     
        page.get_by_role("button", name="교환요청").click()
        page.wait_for_timeout(2000)





    #구매확정
    def purchase_confirm_func(page,order_id,option_count):
        def order_detail():
            page.goto(f'https://qa-web.dailyhou.se/orders/{order_id}', timeout=90000)   
            page.wait_for_timeout(2000)
        
        #상태 변경되지 않은 옵션이 있는지 체크
        order_detail()
        retry = 0 

        while retry < 5 :            
            count_opt = page.get_by_text("취소요청").count()
            count_opt_2 = page.get_by_text("주문취소").count()
            total_opt = count_opt+count_opt_2 

            if total_opt > 0 :
                print(f"미변경 옵션 {total_opt}개. 새로고침 합니다.")
                page.reload() 
                retry +=1
                page.wait_for_timeout(5000)      
            else:                
                print("상태 미변경건 없음")
                break      

        if retry == 5 and total_opt > 0:
            error_message = "retry 5회 진행. 옵션 상태가 변경되지 않았습니다."
            raise AssertionError(error_message)
        

        order_detail()        
        locator = page.get_by_role("button", name="구매확정")
        locator_count = locator.count()
        print(f" total 옵션 수 {locator_count}개 입니다.")
    
        #로케이터 1개 (무조건 1개 옵션 구매확정)
        if locator_count == 1:
            locator.click()   
            page.wait_for_timeout(2000)
            order_detail()

        elif locator_count >=2:
            retry =0 
            while retry < option_count : 
                try:
                    locator.first.click()
                except Exception as e:
                    print("잔여 옵션 1개, 구매확정 시도")
                    try:
                        locator.click()            
                    except Exception as e2:
                        print("구매확정 클릭 실패")
                        break

                page.wait_for_timeout(2000)
                page.get_by_test_id("bds-dim").get_by_role("button", name="구매확정").click()
                retry += 1
                print(f"요청된 구매 확정 옵션 개수 {option_count} 개 중 {retry}개 구매확정 완료")
                order_detail()                  



     #반품 철회(임시- 1개 케이스만 커버 진행)
    def refund_cancel(page,order_id):
        page.goto(f'https://qa-web.dailyhou.se/orders/{order_id}', timeout=90000)
        page.wait_for_timeout(5000) 
        page.get_by_role("button", name="반품철회").first.click()
        page.wait_for_timeout(2000) 
        page.get_by_role("button", name="철회하기").click()
        page.wait_for_timeout(2000) 

