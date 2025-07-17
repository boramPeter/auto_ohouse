import google.generativeai as genai
import json
import time
from qa_mcp_server.TC_auto_maker_module.RAG.TC_read_content import read_google_content

API_KEY_ENV_VARIABLE = ''

MODEL_NAME = 'models/gemini-2.5-flash'
#

def configure_gemini():
    genai.configure(api_key=API_KEY_ENV_VARIABLE)
    model = genai.GenerativeModel(MODEL_NAME)
    print(f"Gemini 모델 '{MODEL_NAME}'이(가) 성공적으로 초기화되었습니다.")
    return model

def chunk_runner(test_cases_json_string: str):
    """
    '''
함수 한개만 남겨둡니다.
'''
    """
    print(f"스크립트 main 함수 시작... (현재 시간: {time.strftime('%Y-%m-%d %H:%M:%S')})")
    script_start_time = time.time()

    gemini_model = configure_gemini()
    if not gemini_model:
        print("모델 설정 실패로 스크립트를 종료합니다.")
        return

    print("\n입력받은 JSON 문자열 파싱 중...")
    test_cases_to_process = []
    if not test_cases_json_string or not isinstance(test_cases_json_string, str):
        print("오류: 유효한 JSON 문자열이 main 함수에 전달되지 않았습니다.")
        return

    try:
        loaded_data = json.loads(test_cases_json_string)
        if isinstance(loaded_data, list):
            test_cases_to_process = loaded_data
            print(f"JSON 문자열로부터 {len(test_cases_to_process)}개의 테스트 케이스를 성공적으로 파싱했습니다.")
        else:
            print(f"오류: 파싱된 데이터가 리스트 형태가 아닙니다 (파싱 후 타입: {type(loaded_data)}).")
            return  # 리스트가 아니면 처리 불가

    except json.JSONDecodeError as e:
        print(f"오류: 입력된 JSON 문자열 파싱 중 오류 발생: {e}")
        return
    except Exception as e:
        print(f"오류: 데이터 처리 중 예외 발생: {e}")
        return

    if not test_cases_to_process:
        print("처리할 테스트 케이스가 없습니다. 스크립트를 종료합니다.")
        return

    print(f"\n총 {len(test_cases_to_process)}개의 테스트 케이스 청킹 시작...")
    all_chunked_results = process_test_cases_from_list(gemini_model, test_cases_to_process)

    print("\n--- 모든 청킹 결과 ---")
    successful_chunks_count = 0
    failed_chunks_count = 0
    for result in all_chunked_results:
        print(f"\n[ID: {result['id']}]")
        if result['chunk_text']:
            print("생성된 청크:")
            print(result['chunk_text'])
            successful_chunks_count += 1
        else:
            print("청크 생성에 실패했거나 빈 결과가 반환되었습니다.")
            failed_chunks_count += 1
        print("-" * 40)

    script_end_time = time.time()
    total_time_taken = script_end_time - script_start_time
    print(f"\n==================================================")
    print(f"총 {len(all_chunked_results)}개 테스트 케이스 처리 완료.")
    print(f"  성공적으로 생성된 청크 수: {successful_chunks_count}개.")
    print(f"  생성 실패 또는 빈 청크 수: {failed_chunks_count}개.")
    print(f"총 실행 시간: {total_time_taken:.2f}초")
    print(f"==================================================")
    print(f"스크립트 main 함수 종료. (현재 시간: {time.strftime('%Y-%m-%d %H:%M:%S')})")
    return all_chunked_results

if __name__ == "__main__":
    doc_url = "https://docs.google.com/spreadsheets/d/1B3vbZn_Q_ALBumujXXsMLYjiuEg-T9Zdys-5p_FPVEg/edit?gid=1891204742#gid=1891204742"
    doc_text = read_google_content(doc_url,sheet_name="MKT")
    print(chunk_runner(doc_text))
