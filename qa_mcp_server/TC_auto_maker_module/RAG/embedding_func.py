import os
import time
import google.generativeai as genai
from qa_mcp_server.TC_auto_maker_module.RAG.spreadsheet_chunking import chunk_runner
from qa_mcp_server.TC_auto_maker_module.RAG.TC_read_content import read_google_content


# 임베딩 모델 설정
EMBEDDING_MODEL_NAME = ''
API_KEY_ENV_VARIABLE = ''





def run_embedding_pipeline(test_cases_json_string: str, batch_size: int = 50) -> list[dict] | None:
    """
    '''
    함수 한개만 남겨둡니다.
    '''
    """
    print("임베딩 파이프라인 시작...")
    pipeline_start_time = time.time()

    # 1. 임베딩 API 설정
    if not configure_embedding_api():
        print("임베딩 API 설정 실패. 파이프라인을 중단합니다.")
        return None

    # 2. 다른 파일의 main 함수를 호출하여 청킹된 데이터 가져오기
    print("\n단계 1: 청킹된 데이터 가져오기 시작...")
    chunking_start_time = time.time()
    chunked_results = chunk_runner(test_cases_json_string)
    chunking_duration = time.time() - chunking_start_time
    print(f"청킹된 데이터 가져오기 완료 (소요 시간: {chunking_duration:.2f}초).")

    if chunked_results is None:
        print("청킹된 데이터를 가져오는데 실패했습니다. 파이프라인을 중단합니다.")
        return None
    if not chunked_results:
        print("처리할 청크가 없습니다. 파이프라인을 종료합니다.")
        return []

    print(f"총 {len(chunked_results)}개의 청크를 성공적으로 받았습니다.")

    # 3. 배치 임베딩을 위해 텍스트만 추출 (아이디는 나중에 매핑)
    ids_for_mapping = []
    texts_to_embed = []

    for item in chunked_results:
        if item.get('chunk_text') and isinstance(item['chunk_text'], str) and item['chunk_text'].strip():
            texts_to_embed.append(item['chunk_text'])
            ids_for_mapping.append(item['id'])
        else:
            print(f"경고: ID '{item.get('id', 'N/A')}'의 항목은 유효한 'chunk_text'가 없어 임베딩에서 제외됩니다.")

    if not texts_to_embed:
        print("필터링 후 임베딩할 유효한 텍스트가 없습니다. 파이프라인을 종료합니다.")
        return []

    # 4. 텍스트 청크 배치 임베딩 (수정된 부분)
    num_texts_to_embed = len(texts_to_embed)
    print(f"\n단계 2: {num_texts_to_embed}개의 텍스트 청크 임베딩 시작 (배치 크기: {batch_size})...")
    embedding_start_time = time.time()

    all_embedding_vectors = []
    total_batches = (num_texts_to_embed + batch_size - 1) // batch_size  # 전체 배치 수 계산

    for i in range(0, num_texts_to_embed, batch_size):
        batch_texts = texts_to_embed[i:i + batch_size]
        current_batch_num = (i // batch_size) + 1

        print(f"\n  배치 {current_batch_num}/{total_batches} 처리 중 ({len(batch_texts)}개 텍스트)...")

        batch_embedding_vectors = embed_texts_batch(batch_texts)

        if batch_embedding_vectors is None:
            print(f"  오류: 배치 {current_batch_num} 임베딩 실패. 파이프라인을 중단합니다.")
            return None

        if len(batch_embedding_vectors) != len(batch_texts):
            print(f"  오류: 배치 {current_batch_num}에서 요청한 텍스트 수({len(batch_texts)})와 "
                  f"생성된 임베딩 벡터 수({len(batch_embedding_vectors)})가 일치하지 않습니다. 파이프라인을 중단합니다.")
            return None

        all_embedding_vectors.extend(batch_embedding_vectors)
        print(f"  배치 {current_batch_num}/{total_batches} 완료. 현재까지 총 {len(all_embedding_vectors)}개 임베딩 생성.")

        # 마지막 배치가 아니면 API 속도 제한을 피하기 위해 약간의 지연 추가
        if current_batch_num < total_batches:
            delay_seconds = 10
            print(f"  다음 배치를 위해 {delay_seconds}초 대기...")
            time.sleep(delay_seconds)

    embedding_vectors = all_embedding_vectors
    embedding_duration = time.time() - embedding_start_time

    # 최종적으로 수집된 임베딩 벡터의 수가 원본 텍스트 수와 일치하는지 확인
    if len(embedding_vectors) != num_texts_to_embed:
        print(f"오류: 전체 요청한 텍스트 수({num_texts_to_embed})와 "
              f"최종 생성된 임베딩 벡터 수({len(embedding_vectors)})가 일치하지 않습니다. 파이프라인을 중단합니다.")
        return None

    print(f"\n텍스트 임베딩 완료 (총 소요 시간: {embedding_duration:.2f}초).")

    # 5. 아이디, 원본 청크, 임베딩 벡터 결합
    final_embedded_data = []
    for idx in range(len(ids_for_mapping)):  # ids_for_mapping과 texts_to_embed, embedding_vectors는 길이가 같아야 함
        final_embedded_data.append({
            "id": ids_for_mapping[idx],
            "chunk_text": texts_to_embed[idx],
            "embedding_vector": embedding_vectors[idx]
        })

    pipeline_duration = time.time() - pipeline_start_time
    print(f"\n단계 3: 최종 임베딩된 데이터 준비 완료.")
    print(f"총 {len(final_embedded_data)}개의 항목이 성공적으로 임베딩되었습니다.")
    print(f"총 파이프라인 실행 시간: {pipeline_duration:.2f}초")
    return final_embedded_data


if __name__ == '__main__':
다.")