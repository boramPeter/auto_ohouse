import re
import json,uuid
from google.oauth2 import service_account
from googleapiclient.discovery import build

# 인증 JSON 파일 경로
json_file_path = ""


def read_google_content(link: str, sheet_name=None) -> str:
    SCOPES = ['https://www.googleapis.com/auth/documents.readonly',
              'https://www.googleapis.com/auth/spreadsheets.readonly']

    try:
        creds = service_account.Credentials.from_service_account_file(json_file_path, scopes=SCOPES)
    except FileNotFoundError:
        return f"서비스 계정 파일({json_file_path})을 찾을 수 없습니다. 경로를 확인하세요."
    except Exception as e:
        return f"서비스 계정 인증 중 오류 발생: {e}"

    match = re.search(r"/d/([a-zA-Z0-9-_]+)", link)
    if not match:
        return "잘못된 Google Docs/Sheets 링크입니다."
    file_id = match.group(1)

    service = build('sheets', 'v4', credentials=creds)
    try:
        sheet_metadata = service.spreadsheets().get(spreadsheetId=file_id).execute()
    except Exception as e:
        return f"Google Sheets API 호출 중 오류 (메타데이터 가져오기): {e}"

    sheet_titles = [s['properties']['title'] for s in sheet_metadata.get('sheets', [])]

    if not sheet_titles:
        return "시트를 찾을 수 없습니다."

    json_list = []
    '''
    한번 싹 돌린 뒤에 
    삭제 시트는 밑에서 500개만 가져와서 처리하도록 수정해야한다. 7월 22일 이후
    '''
    if sheet_name == "삭제":
        target_columns = ['B', 'C', 'S', 'U', 'V']
        col_indices = [ord(c) - ord('A') for c in target_columns]

        result = service.spreadsheets().values().get(
            spreadsheetId=file_id,
            range=sheet_name
        ).execute()

        values = result.get('values', [])


        for row in values[4:]:  # 5번째 행부터 시작
            selected = [row[i] if i < len(row) else '' for i in col_indices]

            # 모든 선택된 셀이 빈 문자열이거나 공백일 경우 스킵
            if all(cell.strip() == "" for cell in selected):
                continue

            original_id = selected[1].strip()
            if not original_id:
                continue  # ID가 비어있으면 저장하지 않음

            # UUID로 변환
            generated_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{selected[0]}-{original_id}"))

            json_obj = {
                "TestCaseID": generated_uuid,
                "TestObjective": selected[2],
                "PreCondition": selected[2],
                "TestSteps": selected[3],
                "ExpectedResult": selected[4]
            }
            json_list.append(json_obj)
    ## 기존 로직(삭제를 제외한 데이터 적재용도)
    else:
        if sheet_name:
            if sheet_name in sheet_titles:
                sheets_to_read = [sheet_name]
            else:
                print(f"경고: 시트 '{sheet_name}'을(를) 찾을 수 없습니다. 모든 시트를 읽습니다.")
                sheets_to_read = sheet_titles
        else:
            sheets_to_read = sheet_titles

        target_columns = ['B', 'R', 'S', 'T', 'U']
        col_indices = [ord(c) - ord('A') for c in target_columns]

        for title in sheets_to_read:
            try:
                result = service.spreadsheets().values().get(
                    spreadsheetId=file_id,
                    range=title
                ).execute()
            except Exception as e:
                print(f"시트 '{title}' 읽기 중 오류 발생: {e}")
                continue

            values = result.get('values', [])
            if not values or len(values) <= 4:
                continue

            for row in values[4:]:  # 5번째 행부터 시작
                selected = [row[i] if i < len(row) else '' for i in col_indices]

                # 모든 선택된 셀이 빈 문자열이거나 공백일 경우 스킵
                if all(cell.strip() == "" for cell in selected):
                    continue

                original_id = selected[0].strip()
                if not original_id:
                    continue  # ID가 비어있으면 저장하지 않음

                # UUID로 변환
                generated_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{title}-{original_id}"))

                json_obj = {
                    "TestCaseID": generated_uuid,
                    "TestObjective": selected[1],
                    "PreCondition": selected[2],
                    "TestSteps": selected[3],
                    "ExpectedResult": selected[4]
                }
                json_list.append(json_obj)

    return json.dumps(json_list, ensure_ascii=False, indent=2)
