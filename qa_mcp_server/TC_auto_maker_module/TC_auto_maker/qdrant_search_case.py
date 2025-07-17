from qdrant_client import QdrantClient
from typing import List, Dict, Any, Optional,Union


QDRANT_CLOUD_URL ="https://1c2fed00-5b2a-4a34-9f92-885be36697f8.eu-central-1-0.aws.cloud.qdrant.io:6333"
QDRANT_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.DKkFha8_tO_9I8SwA2S3nSS_QBupVnsKcjLpJL5nrcQ"
QDRANT_COLLECTION_NAME = "QDRANT_COLLECTION_NAME", "TestCase"
SCORE_THRESHOLD = 0.85  # 스코어 임계값 설정

def search_from_qdrant(
    items_to_search: List[Dict[str, Union[str, List[float]]]],
    qdrant_url: str = QDRANT_CLOUD_URL,
    qdrant_api_key: str = QDRANT_API_KEY,
    qdrant_collection_name: str = QDRANT_COLLECTION_NAME
) -> List[Dict[str, Any]]:

    if not isinstance(items_to_search, list) or not items_to_search:
        print("❗ 입력된 `items_to_search`가 리스트가 아니거나 비어있습니다.")
        return []

    if qdrant_url == "YOUR_QDRANT_CLOUD_URL_PLACEHOLDER" or \
       qdrant_api_key == "YOUR_QDRANT_API_KEY_PLACEHOLDER" or \
       qdrant_collection_name == "YOUR_COLLECTION_NAME_PLACEHOLDER" or \
       not qdrant_url or not qdrant_api_key or not qdrant_collection_name:
        print("❗ Qdrant 클라우드 URL, API 키 또는 컬렉션 이름이 올바르게 설정되지 않았습니다. "
              "코드 내의 플레이스홀더 값을 실제 정보로 수정해주세요.")
        return []

    all_search_outputs: List[Dict[str, Any]] = []
    client: Optional[QdrantClient] = None

    try:
        client = QdrantClient(
            url=qdrant_url,
            api_key=qdrant_api_key,
            timeout=20
        )
        print(f"🔩 Qdrant 클라이언트 초기화 완료. 총 {len(items_to_search)}개 항목에 대한 검색을 시작합니다.")
    except Exception as e_client:
        print(f"❌ Qdrant 클라이언트 초기화 중 오류 발생: {e_client}")
        return []

    for index, item_dict in enumerate(items_to_search):
        item_number_display = index + 1

        if not isinstance(item_dict, dict):
            print(f"⚠️ 항목 {item_number_display}: 딕셔너리 형태가 아닙니다. 건너뜁니다. (받은 값: {item_dict})")
            continue

        original_text = item_dict.get("scope")
        embedding = item_dict.get("embedding")

        if not isinstance(original_text, str) or not original_text.strip():
            print(f"⚠️ 항목 {item_number_display} (scope 값: {original_text}): 유효한 'scope' 문자열을 찾을 수 없거나 비어 있습니다. 건너뜁니다.")
            continue
        if not isinstance(embedding, list) or not embedding:
            print(f"⚠️ 항목 {item_number_display} (scope: {original_text[:30]}...): 유효한 'embedding' 리스트를 찾을 수 없거나 비어 있습니다. 건너뜁니다.")
            continue
        if not all(isinstance(x, (float, int)) for x in embedding):
            print(f"⚠️ 항목 {item_number_display} (scope: {original_text[:30]}...): 'embedding' 리스트의 모든 요소가 숫자가 아닙니다. 건너뜁니다.")
            continue

        text_preview = original_text[:30] + "..." if len(original_text) > 30 else original_text
        print(f"\n🔍 Qdrant 검색 ({item_number_display}/{len(items_to_search)}): \"{text_preview}\" (벡터 차원: {len(embedding)})...")

        try:
            search_result_qdrant = client.search(
                collection_name=qdrant_collection_name,
                query_vector=embedding,
                limit=3
            )

            high_score_results = []
            for hit in search_result_qdrant:
                if hit.score >= SCORE_THRESHOLD:
                    payload_content = hit.payload if hit.payload else {}
                    # 'text_chunk' 값 추출, 없으면 None
                    text_chunk_value = payload_content.get('text_chunk')

                    high_score_results.append({
                        "테스트케이스": text_chunk_value
                    })

            if high_score_results:
                print(f"  Qdrant 검색 완료. 상위 {len(search_result_qdrant)}개 중 {len(high_score_results)}개가 스코어 {SCORE_THRESHOLD}점 이상입니다.")
                all_search_outputs.append({
                    "테스트 범위": original_text,
                    "유사 테스트 케이스": high_score_results
                })
            else:
                print(f"  Qdrant 검색 완료. 상위 {len(search_result_qdrant)}개 결과 중 스코어 {SCORE_THRESHOLD}점 이상인 결과가 없어 이 항목은 최종 결과에 포함되지 않습니다.")

        except Exception as e_search:
            print(f"❌ 항목 \"{text_preview}\"에 대한 Qdrant 검색 중 오류 발생: {e_search}. 이 항목은 건너뜁니다.")
            continue

    print(f"\n✅ Qdrant 전체 검색 완료. 총 {len(all_search_outputs)}개 항목의 검색 결과 반환 (스코어 {SCORE_THRESHOLD}점 이상 필터링 및 text_chunk 추출 적용).")
    return all_search_outputs




if __name__ == '__main__':
    result = ""
    search_results = search_from_qdrant(embedding_item=result)








