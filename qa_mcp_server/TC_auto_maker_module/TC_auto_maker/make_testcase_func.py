import time,re
from datetime import datetime
# 정규표현식은 현재 버전에서 명시적으로 사용되지 않지만, 복잡한 패턴에 대비해 남겨둘 수 있습니다.
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from qa_mcp_server.slack_func.send_slack_msg import send_slack_message

json_file_path = "qa_mcp_server/reference-baton-407904-f3077f350ab8.json"

# def parse_markdown_table(markdown_text: str) -> list[list[str]] | None:
#     """
#     주어진 마크다운 텍스트에서 첫 번째 테이블을 파싱하여
#     리스트의 리스트 형태로 반환합니다.
#     텍스트 내에 테이블이 섞여 있어도 첫 번째 유효한 테이블을 찾습니다.
#     테이블 내에서 헤더와 컬럼 수가 다른 '|...|' 형식의 라인도
#     데이터 행으로 파싱 결과에 포함합니다.
#     테이블이 없거나 파싱할 유효한 데이터 행이 없으면 None을 반환합니다.
#
#     Args:
#         markdown_text: 마크다운 형식의 텍스트 문자열.
#
#     Returns:
#         테이블 데이터를 담은 리스트의 리스트 (헤더 포함).
#         테이블을 찾지 못하거나 헤더 외 유효한 행이 없으면 None.
#         **주의: 반환된 리스트 내 각 행(내부 리스트)의 길이가 다를 수 있습니다.**
#     """
#     # 라인을 분리하고 각 라인의 앞뒤 공백 제거.
#     lines = [line.strip() for line in markdown_text.strip().split('\n')]
#     # 빈 라인은 테이블 종료 조건으로 사용될 수 있으므로 제거하지 않음
#
#     table_data = []
#     table_found = False
#     # num_columns는 헤더 기준으로 파악은 하지만, 이제 데이터 행 추가 조건으로는 사용하지 않음
#     # num_columns = 0
#
#     # 구분선 라인을 찾는 정규식: (이전과 동일)
#     separator_pattern_robust = re.compile(r'^\s*\|(?:\s*[-:]+\s*\|)+(?:\s*[-:]*\s*)?$', re.IGNORECASE)
#
#     # 테이블 라인 (헤더 또는 데이터)을 셀 리스트로 파싱하는 함수 (이전과 동일)
#     def _parse_line_to_cells(line_text: str) -> list[str]:
#         stripped_line = line_text.strip()
#         if not (stripped_line.startswith('|') and stripped_line.endswith('|')):
#              return [] # 유효한 테이블 라인 형식이 아님
#         cells = stripped_line[1:-1].split('|')
#         return [cell.strip() for cell in cells]
#
#     # 텍스트 라인을 순회하며 첫 번째 유효한 테이블의 헤더와 구분선을 찾습니다.
#     i = 0
#     while i < len(lines):
#         current_line = lines[i]
#
#         # 현재 라인이 구분선 패턴과 일치하는지 확인
#         if separator_pattern_robust.match(current_line):
#             # 구분선 라인을 찾았습니다 (인덱스 i).
#             # 바로 이전 라인(i-1)이 헤더 라인인지 확인
#             if i > 0:
#                 header_candidate_line = lines[i-1].strip()
#                 # 헤더 후보 라인이 마크다운 테이블 라인 형식인지 확인 ('|'로 시작/끝)
#                 if header_candidate_line.startswith('|') and header_candidate_line.endswith('|'):
#                      # 헤더 후보 라인을 셀로 파싱하여 유효한 헤더인지 확인
#                      header_cells_candidate = _parse_line_to_cells(header_candidate_line)
#
#                      # 헤더 후보가 비어있지 않다면 (실질적인 컬럼이 있고)
#                      # 헤더 후보와 구분선의 파이프 개수가 일치하는지 확인하여 유효한 헤더-구분선 쌍인지 판단
#                      header_pipe_count = header_candidate_line.count('|')
#                      separator_pipe_count = current_line.strip().count('|')
#
#                      if header_cells_candidate and header_pipe_count >= 2 and header_pipe_count == separator_pipe_count:
#                         # 첫 번째 유효한 테이블의 헤더-구분선 쌍을 찾았습니다!
#                         table_found = True
#                         table_data.append(header_cells_candidate) # 헤더 추가
#                         # num_columns = len(header_cells_candidate) # 더 이상 엄격하게 사용 안함
#                         # 데이터 라인 파싱은 구분선 바로 다음 라인부터 시작
#                         data_row_index = i + 1
#                         break # 테이블 시작점을 찾았으니 외부 루프 종료
#
#         i += 1 # 다음 라인으로 이동하여 검색 계속
#
#     # 테이블 시작점을 찾지 못한 경우
#     if not table_found:
#         return None
#
#     # 테이블 시작점을 찾았다면, 해당 위치부터 데이터 라인을 파싱합니다.
#     for j in range(data_row_index, len(lines)):
#         data_line = lines[j]
#         stripped_data_line = data_line.strip()
#
#         # 빈 라인은 테이블의 끝을 나타냅니다.
#         if not stripped_data_line:
#              break
#
#         # 현재 라인이 마크다운 테이블 라인 형식인지 확인 ('|'로 시작하고 끝남)
#         if stripped_data_line.startswith('|') and stripped_data_line.endswith('|'):
#             # 이 라인이 구분선 라인은 아닌지 다시 확인
#             if separator_pattern_robust.match(data_line):
#                 break # 구분선 발견 시 테이블 종료
#
#             # 컬럼 수 비교 없이 '|...|' 형식인 라인은 모두 데이터 행으로 파싱하여 추가
#             row_cells = _parse_line_to_cells(data_line)
#             table_data.append(row_cells)
#
#         else:
#             # '|...|' 형식이 아닌 라인을 만나면 테이블이 끝난 것으로 간주하고 파싱 중지
#             break
#
#     # 최소한 헤더 라인 외에 하나 이상의 행 (컬럼 수가 다르더라도 '|...|' 형식인 라인)이
#     # 파싱되어야 유효한 결과로 간주합니다. (len(table_data) > 1)
#     if len(table_data) > 1:
#         return table_data
#     else:
#         # 헤더와 구분선만 찾았거나, 그 뒤에 유효한 '|...|' 형식의 라인이 하나도 없는 경우
#         return None
def parse_markdown_table(markdown_text: str) -> list[list[str]] | None:
    """
    마크다운 텍스트 내의 모든 유효한 테이블을 파싱합니다.
    하나라도 훼손된 테이블이 있으면 전체 결과를 None으로 반환합니다.
    여러 테이블이 있을 경우 각 테이블 사이에 [""] (공백 줄)과 ["다음 테스트 케이스"], [""]를 삽입합니다.
    테이블이 아닌 줄도 별도로 결과 리스트에 포함됩니다.

    Returns:
        모든 테이블과 일반 텍스트 라인을 포함한 리스트 또는 None
    """
    lines = [line.rstrip() for line in markdown_text.strip().split('\n')]
    separator_pattern_robust = re.compile(r'^\s*\|(?:\s*[-:]+\s*\|)+(?:\s*[-:]*\s*)?$', re.IGNORECASE)

    def _parse_line_to_cells(line_text: str) -> list[str]:
        stripped_line = line_text.strip()
        if not (stripped_line.startswith('|') and stripped_line.endswith('|')):
            return []
        return [cell.strip() for cell in stripped_line[1:-1].split('|')]

    all_output = []
    i = 0
    table_count = 0

    while i < len(lines):
        current_line = lines[i]

        if separator_pattern_robust.match(current_line):
            if i == 0:
                return None

            header_line = lines[i - 1].strip()
            if not (header_line.startswith('|') and header_line.endswith('|')):
                return None

            header_cells = _parse_line_to_cells(header_line)
            header_pipe_count = header_line.count('|')
            separator_pipe_count = current_line.count('|')

            if not header_cells or header_pipe_count != separator_pipe_count:
                return None

            table_data = [header_cells]
            j = i + 1
            while j < len(lines):
                line = lines[j].strip()
                if not line:
                    break
                if separator_pattern_robust.match(line):
                    break
                if line.startswith('|') and line.endswith('|'):
                    row_cells = _parse_line_to_cells(line)
                    table_data.append(row_cells)
                else:
                    break
                j += 1

            if len(table_data) == 1:
                return None

            if all_output and all_output[-1] != [""]:
                all_output.append([""])

            all_output.extend(table_data)
            all_output.append([""])
            table_count += 1
            i = j
        else:
            if not (i + 1 < len(lines) and separator_pattern_robust.match(lines[i + 1])):
                if lines[i].strip():
                    all_output.append([lines[i].strip()])
            i += 1

    # 추가된 조건: 리스트 안에 48000자를 넘는 문자열이 있다면 None 반환
    for row in all_output:
        for cell in row:
            if len(cell) > 48000:
                return None

    return all_output if table_count > 0 else None

def write_to_spreadsheet(data: list[list[str]], sheet_name="Sheet1", start_cell="B2") -> str:
    SCOPES = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/spreadsheets'
    ]
    creds = Credentials.from_service_account_file(json_file_path, scopes=SCOPES)
    # Sheets API 서비스 객체
    sheets_service = build('sheets', 'v4', credentials=creds)

    def _make_spread_sheet():
        today_date = datetime.now().strftime('%y%m%d_%H%M')
        # 스프레드시트 제목 생성
        spreadsheet_title = f"[오박사] 테스트케이스_{today_date}"

        # 스프레드시트 생성 요청
        spreadsheet_body = {
            'properties': {
                'title': spreadsheet_title
            }
        }
        folder_id = "1wP1brrtMfrsSCs3jULU3FJu8t7ceKoTo"

        max_retries = 3
        spreadsheet_id = None

        for attempt in range(max_retries):
            try:
                response = sheets_service.spreadsheets().create(body=spreadsheet_body).execute()
                spreadsheet_id = response.get('spreadsheetId')
                print(f"response, spreadsheet_id : {response, spreadsheet_id}")

                if spreadsheet_id is not None:
                    print(f"스프레드시트 ID: {spreadsheet_id}")
                    break  # 성공하면 반복문 탈출
                else:
                    send_slack_message(f"write_to_spreadsheet spreadsheetId가 응답에 없음 또는 None: {response}")
                    raise Exception(f"spreadsheetId가 응답에 없음 또는 None: {response}")

            except Exception as e:
                print(f"스프레드시트 생성 실패 ({attempt + 1}/{max_retries}): {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # 2, 4초 점진적 대기 후 재시도
                else:
                    print("최대 재시도 횟수 초과. 스프레드시트 생성 실패.")
                    spreadsheet_id = None
            return spreadsheet_id

        # Drive API 서비스 객체
        drive_service = build('drive', 'v3', credentials=creds)

        # 스프레드시트를 폴더에 이동
        file = drive_service.files().update(
            fileId=spreadsheet_id,
            addParents=folder_id,
            fields="id, parents",
            supportsAllDrives=True
        ).execute()

        return spreadsheet_id

    spreadsheet_id = _make_spread_sheet()
    print(f"spreadsheet_id : {spreadsheet_id}")
    processed_data = []
    for row in data:
        new_row = []
        for cell_value in row:
            if isinstance(cell_value, str):
                new_row.append(cell_value.replace('<br>', '\n'))
            else:
                new_row.append(cell_value)
        processed_data.append(new_row)

    max_retries = 3

    for attempt in range(max_retries):
        try:
            range_name = f"{sheet_name}!{start_cell}"
            body = {
                'values': processed_data
            }
            result = sheets_service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption='USER_ENTERED',
                body=body
            ).execute()
            print(f"{result.get('updatedCells')}개의 셀이 업데이트되었습니다.")
            return f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}"

        except Exception as e:
            print(f"스프레드시트 작성 실패 ({attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # 2, 4초 점진적 대기 후 재시도
            else:
                print("최대 재시도 횟수 초과. 스프레드시트 작성 실패.")
                send_slack_message(f"write_to_spreadsheet 최대 재시도 횟수 초과. 스프레드시트 작성 실패. {e}")
                return f"최대 재시도 횟수 초과. 스프레드시트 작성 실패. {e}"


# --- 테스트 예제 (섞인 텍스트) ---
# markdown_mixed_text = """
# ========== 최종 통합 테스트 범위 분석 결과 ==========
# ## Common 테스트 케이스
#
# | Test Case ID | 대상 기능/화면 | 테스트 목적/시나리오 | 전제 조건 (Pre-condition) | 테스트 경로/절차 (Test Steps) | 예상 결과 (Expected Result) | 중요도 (Priority) | 플랫폼/환경 | 비고 |
# |---|---|---|---|---|---|---|---|---|
# | COMM-FILT-001 | 필터 화면 | 검색창에 유효한 검색어 입력 시, 검색 결과가 정상적으로 필터링 되는지 확인 | 앱 실행 후 필터 화면 진입 | 1. 검색창에 "20대" 입력 2. 검색 버튼 클릭 (또는 엔터 키 입력) | 검색 결과에 20대 관련 정보만 표시됨 | P0 | All | 검색 결과 화면에 대한 상세 디자인 확인 필요 |
# | COMM-FILT-002 | 필터 화면 | 검색창에 유효하지 않은 검색어 입력 시, 적절한 안내 메시지가 표시되는지 확인 | 앱 실행 후 필터 화면 진입 | 1. 검색창에 특수문자 "@" 입력 2. 검색 버튼 클릭 | "검색 결과가 없습니다" 또는 "유효하지 않은 검색어입니다" 와 같은 안내 메시지 표시 | P0 | All | 에러 메시지 문구 확인 필요 |
# | COMM-FILT-003 | 필터 화면 | 카테고리 드롭다운 선택 시, 해당 카테고리에 맞는 검색 결과가 표시되는지 확인 | 앱 실행 후 필터 화면 진입. 카테고리 드롭다운 옵션 존재 가정 | 1. 카테고리 드롭다운에서 "건강" 선택 | 건강 관련 카테고리 검색 결과 표시 | P0 | All | 카테고리 종류 및 검색 결과 화면에 대한 상세 디자인 확인 필요 |
# | COMM-FILT-004 | 필터 화면 | 각 필터 옵션 (전체, 건강, 상품...) 선택 시, 해당 옵션에 맞는 검색 결과가 표시되는지 확인 | 앱 실행 후 필터 화면 진입 | 1. "상품" 필터 옵션 선택 | 상품 관련 필터링된 검색 결과 표시 | P0 | All | 각 필터 옵션의 기능 및 검색 결과 화면에 대한 상세 디자인 확인 필요 |
# | COMM-FILT-005 | 필터 화면 | 추가 필터 옵션 (전체, 주문 취소) 선택 시, 해당 옵션에 맞는 검색 결과가 표시되는지 확인 | 앱 실행 후 필터 화면 진입 | 1. "주문 취소" 필터 옵션 선택 | 주문 취소된 항목만 표시 | P0 | All | 검색 결과 화면에 대한 상세 디자인 확인 필요 |
# | COMM-ORDE-001 | 미결제 주문 & 배송/시공 준비중 | 미결제 주문 버튼 클릭 시, 미결제 주문 목록 화면으로 이동하는지 확인 | 앱 실행 후 해당 화면 진입. 미결제 주문 존재 가정 | 1. "미결제 주문" 버튼 클릭 | 미결제 주문 목록 화면으로 이동 | P1 | All | 미결제 주문 목록 화면에 대한 상세 디자인 확인 필요 |
# | COMM-ORDE-002 | 미결제 주문 & 배송/시공 준비중 | 배송/시공 준비중 버튼 클릭 시, 배송/시공 준비중 목록 화면으로 이동하는지 확인 | 앱 실행 후 해당 화면 진입. 배송/시공 준비중 주문 존재 가정 | 1. "배송/시공 준비중" 버튼 클릭 | 배송/시공 준비중 목록 화면으로 이동 | P1 | All | 배송/시공 준비중 목록 화면에 대한 상세 디자인 확인 필요 |
# | COMM-PAYI-001 | 결제 상품 정보 (화면 14, 30) | 결제 상품 정보 화면에서 상품 정보가 정확하게 표시되는지 확인 | 앱 실행 후 결제 상품 정보 화면으로 진입 (진입 경로 불명확 - 비고 참조) | 1. 상품 이미지, 상품명, 상품 옵션, 수량, 가격, 날짜 정보 확인 | 상품 정보가 정확하게 표시됨 | P1 | All | 결제 상품 정보 화면 진입 경로 확인 필요 |
# | COMM-ORST-001 | 주문 상태 화면 (15~24, 29, 33) | 각 주문 상태 화면에서 주문 정보가 정확하게 표시되는지 확인 | 앱 실행 후 각 주문 상태 화면으로 진입 (진입 경로 불명확 - 비고 참조) | 1. 상품 이미지, 상품명, 상품 옵션, 수량, 가격, 날짜 정보 확인 | 주문 정보가 정확하게 표시됨 | P1 | All | 각 주문 상태 화면 진입 경로 확인 필요 |
# | COMM-ORST-002 | 주문 상태 화면 (15, 16, 17, 19, 20, 21, 22, 23, 24) | "주문 상세" 버튼 클릭 시, 주문 상세 화면으로 이동하는지 확인 | 앱 실행 후 "주문 상세" 버튼이 있는 주문 상태 화면으로 진입 (진입 경로 불명확 - 비고 참조) | 1. "주문 상세" 버튼 클릭 | 주문 상세 화면으로 이동 | P1 | All | 주문 상세 화면 디자인 및 진입 경로 확인 필요 |
# | COMM-PAYC-001 | 결제 전 최종 확인 (화면 25) | 결제 버튼 클릭 시, 결제 화면으로 정상적으로 이동하는지 확인 | 앱 실행 후 결제 전 최종 확인 화면 진입 (진입 경로 불명확 - 비고 참조) | 1. 결제 버튼 클릭 | 결제 화면으로 이동 | P0 | All | 결제 화면 디자인 및 진입 경로 확인 필요 |
# | COMM-PAYM-001 | 결제 화면 (26, 27, 31, 32) | 결제 정보 입력 후 결제 버튼 클릭 시, 결제가 정상적으로 처리되는지 확인 | 앱 실행 후 결제 화면 진입 (진입 경로 불명확 - 비고 참조) | 1. 결제 정보 입력 2. 결제 버튼 클릭 | 결제 완료 화면으로 이동, 결제 성공 메시지 표시 | P0 | All | 결제 연동 방식 및 결제 완료 화면 디자인 확인 필요 |
# | COMM-PAYM-002 | 결제 화면 (26, 27, 31, 32) | 잘못된 결제 정보 입력 시, 적절한 에러 메시지가 표시되는지 확인 | 앱 실행 후 결제 화면 진입 (진입 경로 불명확 - 비고 참조) | 1. 유효하지 않은 결제 정보 입력 2. 결제 버튼 클릭 | "잘못된 결제 정보입니다" 와 같은 에러 메시지 표시 | P0 | All | 에러 메시지 문구 확인 필요 |
# | COMM-PAYF-001 | 결제 완료 (화면 28) | "최종 결제 확인" 버튼 클릭 시, 최종 결제 확인 화면으로 이동하는지 확인 | 앱 실행 후 결제 완료 화면 진입 (진입 경로 불명확 - 비고 참조) | 1. "최종 결제 확인" 버튼 클릭 | 최종 결제 확인 화면으로 이동 | P0 | All | 최종 결제 확인 화면 디자인 및 기능 확인 필요 |
# | COMM-PAYF-002 | 결제 완료 (화면 28) | "결제" 버튼 클릭 시, 어떤 동작이 수행되는지 확인 | 앱 실행 후 결제 완료 화면 진입 (진입 경로 불명확 - 비고 참조) | 1. "결제" 버튼 클릭 | 버튼 기능 확인 필요 (비고 참조) | P0 | All | "결제" 버튼 기능 확인 필요 |
# | COMM-OHOU-001 | 오하우스 공급서 (화면 63~66) | "계좌 확인" 버튼 클릭 시, 계좌 정보 화면으로 이동하는지 확인 | 앱 실행 후 오하우스 공급서 화면 진입 (진입 경로 불명확 - 비고 참조) | 1. "계좌 확인" 버튼 클릭 | 계좌 정보 화면으로 이동 | P0 | All | 계좌 정보 화면 디자인 확인 필요 |
# | COMM-OHOU-002 | 오하우스 공급서 (화면 63~66) | "입금 확인" 버튼 클릭 시, 입금 확인 처리가 정상적으로 수행되는지 확인 | 앱 실행 후 오하우스 공급서 화면 진입 (진입 경로 불명확 - 비고 참조) | 1. "입금 확인" 버튼 클릭 | 입금 확인 완료 메시지 표시 | P0 | All | 입금 확인 처리 로직 및 관련 화면 디자인 확인 필요 |
#
#
# ## 세일즈포스 테스트 케이스
#
# | Test Case ID | 대상 기능/화면 | 테스트 목적/시나리오 | 전제 조건 (Pre-condition) | 테스트 경로/절차 (Test Steps) | 예상 결과 (Expected Result) | 중요도 (Priority) | 플랫폼/환경 | 비고 |
# |---|---|---|---|---|---|---|---|---|
# | SALEF-PROD-001 | 결산 상품 등록 | 상품 정보를 모두 입력하고 등록 버튼을 클릭하면 상품이 정상적으로 등록되는가? | 세일즈포스 시스템 로그인 상태 | 1. 상품 이미지, 상품명, 가격, 상품 설명 입력 2. 등록일, 수정일 확인 3. '등록' 버튼 클릭 | 상품이 등록되고, 등록 성공 메시지 표시 | P1 | All | '등록' 버튼 기능 및 등록 성공 메시지 확인 필요 |
# | SALEF-PROD-002 | 결산 상품 등록 | 필수 정보(상품명, 가격)를 입력하지 않고 등록 버튼을 클릭하면 에러 메시지가 표시되는가? | 세일즈포스 시스템 로그인 상태 | 1. 상품명, 가격 입력 필드를 비워둔 채 '등록' 버튼 클릭 |  필수 정보 누락 에러 메시지 표시 | P1 | All | 에러 메시지 내용 확인 필요 |
# | SALEF-ARRI-001 | 결산 도착 | '결산 만료일 알림' 버튼 클릭 시 알림이 설정되고, 설정 성공 메시지가 표시되는가? | 세일즈포스 시스템 로그인 상태 | 1. '결산 만료일 알림' 버튼 클릭 | 알림 설정 성공 메시지 표시 | P1 | All | 알림 설정 성공 메시지, 알림 기능 구현 방식 확인 필요 |
# | SALEF-PAYM-001 | 결제 기능 | 결제 금액을 확인하고 결제를 진행할 수 있는가? | 세일즈포스 시스템 로그인, 결제할 상품 존재 | 1. 결제 금액 확인 2. 결제 수단 선택 3. '결제' 버튼 클릭 | 결제 진행 화면으로 이동 | P0 | All | 결제 진행 화면 디자인 및 결제 연동 방식 확인 필요 |
# | SALEF-PAYM-002 | 결제 기능 | '결제 정보 확인' 버튼 클릭 시 결제 정보 확인 화면으로 이동하는가? | 세일즈포스 시스템 로그인 | 1. '결제 정보 확인' 버튼 클릭 | 결제 정보 확인 화면으로 이동 | P0 | All | 결제 정보 확인 화면 디자인 확인 필요 |
# | SALEF-BALA-001 | 잔액/입점 확인 | 공급사의 잔액 및 입점 상태를 확인할 수 있는가? | 세일즈포스 시스템 로그인 | 1. 공급사 선택 2. 잔액, 입점 상태 확인 | 공급사의 잔액 및 입점 상태 정보 표시 | P0 | All |  |
# | SALEF-BALA-002 | 잔액/입점 확인 | '잔액 확인' 버튼 클릭 시 상세 잔액 정보 화면으로 이동하는가? | 세일즈포스 시스템 로그인 | 1. '잔액 확인' 버튼 클릭 | 상세 잔액 정보 화면으로 이동 | P0 | All | 상세 잔액 정보 화면 디자인 확인 필요 |
# | SALEF-BALA-003 | 잔액/입점 확인 | '입점 확인' 버튼 클릭 시 상세 입점 정보 화면으로 이동하는가? | 세일즈포스 시스템 로그인 | 1. '입점 확인' 버튼 클릭 | 상세 입점 정보 화면으로 이동 | P0 | All | 상세 입점 정보 화면 디자인 확인 필요 |
# | SALEF-PAYC-001 | 결제 방법 확인 | 결제 과정 및 실효/환불 정책을 확인할 수 있는가? | 세일즈포스 시스템 로그인 | 1. 결제 과정 설명, 실효 정책, 환불 정책 확인 | 결제 과정 및 정책 정보 표시 | P2 | All |  |
#
#
#
#
#
# ## Common 테스트 케이스
#
# | Test Case ID | 대상 기능/화면 | 테스트 목적/시나리오 | 전제 조건 (Pre-condition) | 테스트 경로/절차 (Test Steps) | 예상 결과 (Expected Result) | 중요도 (Priority) | 플랫폼/환경 | 비고 |
# |---|---|---|---|---|---|---|---|---|
# | COMM-FILT-001 | 필터 화면 | 검색창에 유효한 검색어 입력 시, 검색 결과가 정상적으로 필터링 되는지 확인 | 앱 실행 후, 필터 화면 진입 | 1. 검색창에 "20대" 입력  2. 검색 버튼 클릭 (또는 엔터 키 입력) | 검색 결과에 20대 관련 정보만 표시됨 | P0 | All | 검색 결과 화면에 대한 상세 디자인 확인 필요 |
# | COMM-FILT-002 | 필터 화면 | 검색창에 유효하지 않은 검색어 입력 시, 적절한 메시지가 표시되는지 확인 | 앱 실행 후, 필터 화면 진입 | 1. 검색창에 특수 문자 "&#@!" 입력 2. 검색 버튼 클릭 | "검색 결과가 없습니다" 또는 "유효하지 않은 검색어입니다" 와 같은 메시지 표시 | P0 | All | 에러 메시지 및 처리 방식에 대한 상세 디자인 확인 필요 |
# | COMM-FILT-003 | 필터 화면 | 검색창에 빈 값 입력 후 검색 시, 전체 결과가 표시되는지 확인 | 앱 실행 후, 필터 화면 진입 | 1. 검색창을 빈 상태로 검색 버튼 클릭 | 전체 검색 결과 표시 | P0 | All |  |
# | COMM-FILT-004 | 필터 화면 | 각 필터 옵션 선택 시, 검색 결과가 정상적으로 필터링 되는지 확인 | 앱 실행 후, 필터 화면 진입 | 1. "건강" 필터 옵션 선택 2. 검색 버튼 클릭 | 검색 결과에 "건강" 카테고리에 해당하는 정보만 표시 | P0 | All | 각 필터 옵션에 따른 검색 결과 화면에 대한 상세 디자인 확인 필요 |
# | COMM-FILT-005 | 필터 화면 | 카테고리 드롭다운 선택 시, 해당 카테고리에 맞는 검색 결과가 표시되는지 확인 | 앱 실행 후, 필터 화면 진입. 카테고리 드롭다운 존재 가정 | 1. 카테고리 드롭다운에서 "상품" 선택 2. 검색 버튼 클릭 | 검색 결과에 "상품" 카테고리에 해당하는 정보만 표시 | P0 | All | 카테고리 종류 및 각 카테고리에 따른 검색 결과 화면에 대한 상세 디자인 확인 필요 |
# | COMM-ORDE-001 | 미결제 주문 & 배송/시공 준비중 | 미결제 주문 버튼 클릭 시, 미결제 주문 목록 화면으로 이동하는지 확인 | 앱 실행 후, 해당 화면 진입. 미결제 주문 숫자 > 0 | 1. "미결제 주문" 버튼 클릭 | 미결제 주문 목록 화면으로 이동 | P1 | All | 미결제 주문 목록 화면에 대한 상세 디자인 확인 필요 |
# | COMM-ORDE-002 | 미결제 주문 & 배송/시공 준비중 | 배송/시공 준비중 버튼 클릭 시, 배송/시공 준비중 목록 화면으로 이동하는지 확인 | 앱 실행 후, 해당 화면 진입. 배송/시공 준비중 숫자 > 0 | 1. "배송/시공 준비중" 버튼 클릭 | 배송/시공 준비중 목록 화면으로 이동 | P1 | All | 배송/시공 준비중 목록 화면에 대한 상세 디자인 확인 필요 |
# | COMM-PAYM-001 | 결제 화면 (26, 27, 31, 32) | 결제 금액 입력 후 결제 버튼 클릭 시, 결제가 정상적으로 진행되는지 확인 | 앱 실행 후 결제 화면 진입. 결제할 상품이 존재 | 1. 결제 금액 입력 2. 결제 버튼 클릭 | 결제 완료 화면으로 이동, 결제 성공 메시지 표시 | P0 | All | 결제 연동 방식 및 결제 완료 화면에 대한 상세 디자인 확인 필요 |
# | COMM-PAYM-002 | 결제 화면 (26, 27, 31, 32) | 결제 금액을 입력하지 않고 결제 버튼 클릭 시, 에러 메시지가 표시되는지 확인 | 앱 실행 후 결제 화면 진입. 결제할 상품이 존재 | 1. 결제 금액 입력 필드를 빈 상태로 둠 2. 결제 버튼 클릭 | "결제 금액을 입력해주세요" 와 같은 에러 메시지 표시 | P0 | All | 에러 메시지 내용 확인 필요 |
# | COMM-PAYM-003 | 결제 화면 (26, 27, 31, 32) | 잘못된 결제 금액 입력 시, 에러 메시지가 표시되는지 확인 | 앱 실행 후 결제 화면 진입. 결제할 상품이 존재 | 1. 결제 금액에 잘못된 값 (예: 음수, 문자) 입력 2. 결제 버튼 클릭 | "잘못된 결제 금액입니다" 와 같은 에러 메시지 표시 | P0 | All | 에러 메시지 내용 확인 필요 |
# | COMM-COMP-001 | 결제 완료 (28) | 결제 완료 화면에서 "최종 결제 확인" 버튼 클릭 시, 최종 결제 내역 확인 화면으로 이동하는지 확인 | 앱 실행 후 결제 완료 화면 진입 | 1. "최종 결제 확인" 버튼 클릭 | 최종 결제 내역 확인 화면으로 이동 | P0 | All | 최종 결제 내역 확인 화면에 대한 상세 디자인 확인 필요 |
# | COMM-COMP-002 | 결제 완료 (28) | 결제 완료 화면에서 "결제" 버튼 클릭 시, 어떤 동작이 발생하는지 확인 | 앱 실행 후 결제 완료 화면 진입 | 1. "결제" 버튼 클릭 | 상세 기능 정의 필요 (새로운 결제 화면으로 이동? 이전 결제 내역 확인?) | P0 | All | 버튼 기능에 대한 상세 디자인 확인 필요 |
# | COMM-INVO-001 | 오하우스 공급서 (63~66) | "계좌 확인" 버튼 클릭 시, 계좌 정보 화면으로 이동하는지 확인 | 앱 실행 후 오하우스 공급서 화면 진입 | 1. "계좌 확인" 버튼 클릭 | 계좌 정보 화면으로 이동 | P0 | All | 계좌 정보 화면에 대한 상세 디자인 확인 필요 |
# | COMM-INVO-002 | 오하우스 공급서 (63~66) | "입금 확인" 버튼 클릭 시, 입금 확인 절차가 정상적으로 진행되는지 확인 | 앱 실행 후 오하우스 공급서 화면 진입 | 1. "입금 확인" 버튼 클릭 | 입금 확인 완료 메시지 표시 또는 입금 확인 진행 화면으로 이동 | P0 | All | 입금 확인 절차에 대한 상세 디자인 확인 필요 |
#
#
# ## 세일즈포스 테스트 케이스
#
# | Test Case ID | 대상 기능/화면 | 테스트 목적/시나리오 | 전제 조건 (Pre-condition) | 테스트 경로/절차 (Test Steps) | 예상 결과 (Expected Result) | 중요도 (Priority) | 플랫폼/환경 | 비고 |
# |---|---|---|---|---|---|---|---|---|
# | SALE-PROD-001 | 결산 상품 등록 | 상품 정보를 모두 입력하고 등록 버튼 클릭 시 상품이 정상적으로 등록되는지 확인 | 세일즈포스 시스템 로그인 | 1. 상품 이미지 업로드 2. 상품명, 가격, 상품 설명 입력 3. 등록 버튼 클릭 | 상품 등록 성공 메시지 표시, 등록된 상품 목록에 추가 | P1 | Web |  |
# | SALE-PROD-002 | 결산 상품 등록 | 필수 정보(상품명, 가격)를 입력하지 않고 등록 버튼 클릭 시 에러 메시지가 표시되는지 확인 | 세일즈포스 시스템 로그인 | 1. 상품명, 가격 입력 필드를 빈 상태로 둠 2. 등록 버튼 클릭 | "상품명과 가격은 필수 입력 항목입니다." 와 같은 에러 메시지 표시 | P1 | Web |  |
# | SALE-ARRI-001 | 결산 도착 | "결산 만료일 알림" 버튼 클릭 시 알림이 설정되는지 확인 | 세일즈포스 시스템 로그인, 결산 도착 정보 존재 | 1. "결산 만료일 알림" 버튼 클릭 | 알림 설정 완료 메시지 표시 | P1 | Web | 알림 설정 방식 (이메일, 푸시 등) 에 대한 상세 디자인 확인 필요 |
# | SALE-PAYM-001 | 결제 기능 | 결제 금액 확인 후 결제 버튼 클릭 시 결제가 정상적으로 진행되는지 확인 | 세일즈포스 시스템 로그인, 결제할 상품 존재 | 1. 결제 금액 확인 2. 결제 버튼 클릭 | 결제 완료 페이지로 이동, 결제 성공 메시지 표시 | P0 | Web | 결제 연동 방식 및 결제 완료 페이지 디자인 확인 필요 |
# | SALE-PAYM-002 | 결제 기능 | "결제 정보 확인" 버튼 클릭 시 결제 정보 확인 페이지로 이동하는지 확인 | 세일즈포스 시스템 로그인, 결제할 상품 존재 | 1. "결제 정보 확인" 버튼 클릭 | 결제 정보 확인 페이지로 이동 | P0 | Web | 결제 정보 확인 페이지 디자인 확인 필요 |
# | SALE-BALA-001 | 잔액/입점 확인 | "잔액 확인" 버튼 클릭 시 공급사의 잔액 정보가 정상적으로 표시되는지 확인 | 세일즈포스 시스템 로그인 | 1. "잔액 확인" 버튼 클릭 | 공급사의 잔액 정보 표시 | P0 | Web | 잔액 정보 표시 형식 확인 필요 |
# | SALE-BALA-002 | 잔액/입점 확인 | "입점 확인" 버튼 클릭 시 공급사의 입점 상태가 정상적으로 표시되는지 확인 | 세일즈포스 시스템 로그인 | 1. "입점 확인" 버튼 클릭 | 공급사의 입점 상태 정보 표시 | P0 | Web | 입점 상태 정보 표시 형식 확인 필요 |
#
#
# **화면 3~13, 34~62 (Common)는 정보 부족으로 테스트 케이스 작성이 어렵습니다. 추가 정보 제공 시 작성 가능합니다.**
#
#
# 위 테스트 케이스는 제공된 정보를 바탕으로 작성되었으며, 추가적인 요구사항 및 상세 디자인 확인 후 수정 및 보완이 필요할 수 있습니다. 특히 화면 간 이동 흐름 및 각 기능의 상세 동작 방식에 대한 추가 정보가 필요합니다.
#
#
# """
#
# parsed_table = parse_markdown_table(markdown_mixed_text)
# if parsed_table:
#     print("섞인 텍스트 내 테이블 파싱 결과:")
#     for row in parsed_table:
#         print(row)
# else:
#     print("섞인 텍스트 내 테이블 파싱 실패")
#
# write_to_spreadsheet(parsed_table)