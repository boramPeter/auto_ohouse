from datetime import datetime
import os,json
import pytz

json_path = "qa_mcp_server/progress_msg.json"


def save_to_json(top_key, sub_key, values):
    """
    JSON 파일에 top_key 안의 sub_key 값을 업데이트하거나 추가함.
    기존 top_key/sub_key가 없으면 생성.
    values는 리스트이며 최대 6개까지만 저장.
    """
    data = {}

    # JSON 파일이 존재하면 로드
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

    # top_key가 없으면 생성
    if top_key not in data or not isinstance(data[top_key], dict):
        data[top_key] = {}

    # sub_key 업데이트 또는 추가 (항상 덮어쓰기)
    data[top_key][sub_key] = values

    # 저장
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def delete_top_key(top_key):
    """
    JSON 파일에서 top_key가 존재하면 해당 키 및 모든 하위 데이터를 삭제함.
    """

    # 파일이 없으면 아무 작업도 하지 않음
    if not os.path.exists(json_path):
        return

    # JSON 파일 로드
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}

    # top_key가 존재하면 삭제
    if top_key in data:
        del data[top_key]

        # 변경된 내용 저장
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


