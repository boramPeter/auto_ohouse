import re, json
import urllib.parse # URL 파싱을 위해 추가
from google.oauth2 import service_account
from googleapiclient.discovery import build


'''
함수 한개만 남겨둡니다.
'''
def read_google_content(link: str, sheet_name=None) -> str:
    SCOPES = ['https://www.googleapis.com/auth/documents.readonly',
              'https://www.googleapis.com/auth/spreadsheets.readonly']

    try:
        creds = service_account.Credentials.from_service_account_file(json_file_path, scopes=SCOPES)
    except FileNotFoundError:
        return json.dumps({"response_code": 500, "error": f"서비스 계정 파일({json_file_path})을 찾을 수 없습니다. 경로를 확인하세요."}, ensure_ascii=False,
                          indent=2)
    except Exception as e:
        return json.dumps({"response_code": 500, "error": f"서비스 계정 인증 중 오류 발생: {e}"}, ensure_ascii=False, indent=2)

    match = re.search(r"/d/([a-zA-Z0-9-_]+)", link)
    if not match:
        return json.dumps({"response_code": 400, "error": "잘못된 Google Docs/Sheets 링크입니다."}, ensure_ascii=False, indent=2)
    file_id = match.group(1)

    if "docs.google.com/document" in link:
        parsed_url = urllib.parse.urlparse(link)
        query_string = parsed_url.query
        extracted_tab_id = None

        if query_string:
            params = urllib.parse.parse_qs(query_string)
            if 'tab' in params:
                extracted_tab_id = params['tab'][0]
                print(f"Target extracted_tab_id from URL: {extracted_tab_id}")

        service = build('docs', 'v1', credentials=creds)
        try:
            doc = service.documents().get(documentId=file_id, includeTabsContent=True).execute()
        except Exception as e:
            # API 호출 실패 시 주로 권한 문제일 가능성이 높으므로 403을 사용합니다.
            return json.dumps({"response_code": 403, "error": f"Google Docs API 호출 중 오류 발생: {e}"}, ensure_ascii=False, indent=2)

        final_data_to_return = {"documentId": file_id}

        # 문서 전체의 배치된 이미지 정보 추출
        positioned_images_list = extract_positioned_images_info(doc.get('positionedObjects', {}))
        if positioned_images_list:
            final_data_to_return['positionedImages'] = positioned_images_list

        all_doc_tabs_data = doc.get('tabs', [])
        tab_found_for_json_processing = False

        if extracted_tab_id is not None:
            final_data_to_return["requestedTabId"] = extracted_tab_id
            found_specific_tab_dict = None

            for main_tab_data in all_doc_tabs_data:
                if tab_found_for_json_processing: break
                main_tab_properties = main_tab_data.get('tabProperties', {})
                main_tab_id = main_tab_properties.get('tabId')
                main_tab_title = main_tab_properties.get('title', 'Untitled Main')

                if main_tab_id == extracted_tab_id:
                    found_specific_tab_dict = _convert_tab_to_dict_recursive(main_tab_data, "Main Tab")
                    tab_found_for_json_processing = True;
                    break

                for child_tab_data in main_tab_data.get('childTabs', []):
                    if tab_found_for_json_processing: break
                    child_tab_properties = child_tab_data.get('tabProperties', {})
                    child_tab_id = child_tab_properties.get('tabId')
                    child_tab_title = child_tab_properties.get('title', 'Untitled Child')
                    if child_tab_id == extracted_tab_id:
                        found_specific_tab_dict = _convert_tab_to_dict_recursive(child_tab_data, "Child Tab",
                                                                                 direct_parent_display_title=main_tab_title,
                                                                                 direct_parent_actual_id=main_tab_id)
                        tab_found_for_json_processing = True;
                        break

                    for grandchild_tab_data in child_tab_data.get('childTabs', []):
                        if tab_found_for_json_processing: break
                        grandchild_tab_properties = grandchild_tab_data.get('tabProperties', {})
                        grandchild_tab_id = grandchild_tab_properties.get('tabId')
                        grandchild_tab_title = grandchild_tab_properties.get('title', 'Untitled Grandchild')
                        if grandchild_tab_id == extracted_tab_id:
                            found_specific_tab_dict = _convert_tab_to_dict_recursive(grandchild_tab_data,
                                                                                     "Grandchild Tab",
                                                                                     direct_parent_display_title=child_tab_title,
                                                                                     direct_parent_actual_id=child_tab_id)
                            tab_found_for_json_processing = True;
                            break

                        for gg_child_tab_data in grandchild_tab_data.get('childTabs', []):
                            if tab_found_for_json_processing: break
                            gg_child_tab_properties = gg_child_tab_data.get('tabProperties', {})
                            gg_child_tab_id = gg_child_tab_properties.get('tabId')
                            if gg_child_tab_id == extracted_tab_id:
                                found_specific_tab_dict = _convert_tab_to_dict_recursive(gg_child_tab_data,
                                                                                         "Great-Grandchild Tab",
                                                                                         direct_parent_display_title=grandchild_tab_title,
                                                                                         direct_parent_actual_id=grandchild_tab_id)
                                tab_found_for_json_processing = True;
                                break
                        if tab_found_for_json_processing: break
                    if tab_found_for_json_processing: break

            if found_specific_tab_dict:
                final_data_to_return["response_code"] = 200
                final_data_to_return["tabInfo"] = found_specific_tab_dict
            else:
                final_data_to_return["response_code"] = 404
                final_data_to_return["error"] = f"Tab with ID '{extracted_tab_id}' not found."
        else:
            processed_tabs_list = []
            for main_tab_data in all_doc_tabs_data:
                tab_dict = _convert_tab_to_dict_recursive(main_tab_data, "Main Tab")
                processed_tabs_list.append(tab_dict)
            final_data_to_return["response_code"] = 200
            final_data_to_return["tabs"] = processed_tabs_list

        return json.dumps(final_data_to_return, ensure_ascii=False, indent=2)


    elif "docs.google.com/spreadsheets" in link:
        return json.dumps({"message": "Google Sheets 처리는 추후 구현 예정.", "file_id": file_id},
                          ensure_ascii=False, indent=2)
    else:
        return json.dumps({"error": "링크는 Google Docs 또는 Sheets URL이어야 합니다."}, ensure_ascii=False, indent=2)
