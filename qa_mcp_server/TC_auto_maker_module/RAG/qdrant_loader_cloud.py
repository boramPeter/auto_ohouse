import sys
import time
from qdrant_client import QdrantClient
from qdrant_client.http import models

from qa_mcp_server.TC_auto_maker_module.RAG.embedding_func import run_embedding_pipeline
from qa_mcp_server.TC_auto_maker_module.RAG.TC_read_content import read_google_content
import datetime

QDRANT_CLOUD_URL =""
QDRANT_API_KEY = ""
QDRANT_COLLECTION_NAME = "QDRANT_COLLECTION_NAME", "TestCase"


VECTOR_DIMENSION = 768
DISTANCE_METRIC = models.Distance.COSINE
QDRANT_BATCH_SIZE = 200


def FTC_run_qdrant():
    '''
    함수 한개만 남겨둡니다.
    '''
    print("\nFTC Qdrant 실행 시작...")
    today = datetime.date.today()
    start_date = datetime.date(2025, 5, 16)

    days_passed = (today - start_date).days
    params = []

    if not params:  # params가 비어있는 경우 방지
        print("오류: `params` 리스트가 비어있습니다.")
        return

    index = days_passed % len(params)
    selected_param = params[index]
    print(f"오늘 날짜({today}) 기준 선택된 파라미터: '{selected_param}' (days_passed: {days_passed}, index: {index})")

    doc_url = ""

    print(f"선택된 시트 이름으로 Google Sheets 내용 읽기: '{selected_param}'")

    delete = None
    if selected_param == "삭제":
        delete=True

    doc_text = read_google_content(doc_url, sheet_name=selected_param)

    if not doc_text:
        print(f"'{selected_param}' 시트에서 내용을 읽어오지 못했거나 내용이 없습니다. Qdrant 로더를 실행하지 않습니다.")
        return

    main_qdrant_loader(doc_text,delete=delete)
    print("FTC Qdrant 실행 완료.")
'''
삭제 차례 일경우, title-아이디 형식으로 조회 먼저 해보고 일치한다면 삭제하도록 코드구성해야함
'''

if __name__ == '__main__':
    print("Qdrant 로더 스크립트 직접 실행 모드입니다.")
    FTC_run_qdrant()
