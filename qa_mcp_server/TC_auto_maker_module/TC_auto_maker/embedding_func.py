import google.generativeai as genai
from typing import List, Dict, Any
from qa_mcp_server.TC_auto_maker_module.TC_auto_maker.chunk_test_scope import run_scope_extraction
import time

DEFAULT_GEMINI_EMBEDDING_MODEL = "models/text-embedding-004" #"models/gemini-embedding-exp-03-07" # 또는 "models/embedding-001" 등
genai.configure(api_key="AIzaSyBsKkgCQy0rb4sJzaZYp8WnhKmqu5PQ9-U")


def embedded_test_scope(
        texts_to_embed: List[str],
        model_name: str = DEFAULT_GEMINI_EMBEDDING_MODEL,
        chunk_size: int = 70,
        delay_between_chunks: float = 1.0,
        task_type: str = "RETRIEVAL_DOCUMENT"
) -> List[Dict[str, Any]]:
    if not texts_to_embed:
        print("❗ 입력된 텍스트 리스트가 비어있습니다.")
        return []

    # ... (이전과 동일한 입력값 유효성 검사 부분) ...
    if not isinstance(chunk_size, int) or chunk_size <= 0:
        print(f"❗ 청크 크기(chunk_size)는 0보다 큰 정수여야 합니다. 현재 값: {chunk_size}")
        return []

    if not isinstance(delay_between_chunks, (int, float)) or delay_between_chunks < 0:
        print(f"❗ `delay_between_chunks`는 0 이상의 숫자여야 합니다. 현재 값: {delay_between_chunks}. 기본값 0.0으로 설정합니다.")
        delay_between_chunks = 0.0

    texts_for_api = texts_to_embed
    total_texts = len(texts_for_api)
    all_embedded_results: List[Dict[str, Any]] = []
    processed_texts_count = 0
    current_chunk_number_for_error = 0

    print(f"\n🧠 총 {total_texts}개의 텍스트를 Gemini 모델 ({model_name}, 작업 유형: {task_type})을 사용하여 임베딩합니다.")
    print(f"   각 API 호출당 최대 {chunk_size}개씩 청크로 나누어 처리합니다.")
    if delay_between_chunks > 0:
        print(f"   각 청크 처리 후 {delay_between_chunks:.2f}초 대기합니다.")

    try:
        num_total_chunks = (total_texts + chunk_size - 1) // chunk_size

        for i in range(0, total_texts, chunk_size):
            chunk_original_texts = texts_for_api[i:i + chunk_size]
            current_chunk_actual_size = len(chunk_original_texts)
            current_chunk_number_for_error = i // chunk_size + 1

            if not chunk_original_texts:
                continue

            start_index_display = processed_texts_count + 1
            end_index_display = processed_texts_count + current_chunk_actual_size
            print(
                f"   - 청크 {current_chunk_number_for_error}/{num_total_chunks}: {current_chunk_actual_size}개 텍스트 처리 중 ({start_index_display}~{end_index_display} / {total_texts})...")

            response = genai.embed_content(
                model=model_name,
                content=chunk_original_texts,
                task_type=task_type
            )

            chunk_embeddings: List[List[float]] = []  # 추출된 임베딩을 저장할 리스트 초기화

            if not isinstance(response, dict):
                error_msg = (f"API 응답이 예상된 딕셔너리 형태가 아닙니다 (청크 {current_chunk_number_for_error}). "
                             f"실제 응답 타입: {type(response)}, 응답 내용(일부): {str(response)[:500]}...")
                print(f"🔴 {error_msg}")
                raise ValueError(error_msg)

            retrieved_value_from_singular_key = response['embedding']

            if isinstance(retrieved_value_from_singular_key, list) and \
                    (not retrieved_value_from_singular_key or isinstance(retrieved_value_from_singular_key[0],
                                                                         list)):
                chunk_embeddings = retrieved_value_from_singular_key
                print(
                    f"ℹ️ (청크 {current_chunk_number_for_error}) 'embedding' (단수형) 키의 값을 배치 임베딩 (list of lists)으로 사용합니다.")


            # 임베딩 결과 수 확인
            if len(chunk_embeddings) != len(chunk_original_texts):
                error_msg = (f"청크 {current_chunk_number_for_error} 임베딩 결과 수 불일치: "
                             f"요청 {len(chunk_original_texts)}개, 추출된 임베딩 {len(chunk_embeddings)}개. "
                             f"API 응답(일부): {str(response)[:500]}...")
                print(f"🔴 {error_msg}")
                raise ValueError(error_msg)

            for text, embedding_vector in zip(chunk_original_texts, chunk_embeddings):
                all_embedded_results.append({
                    "scope": text,
                    "embedding": embedding_vector  # 여기서 embedding_vector는 list[float] 여야 함
                })

            processed_texts_count += current_chunk_actual_size
            print(f"   - 청크 {current_chunk_number_for_error}/{num_total_chunks} 완료. 현재까지 {processed_texts_count}개 처리됨.")

            if current_chunk_number_for_error < num_total_chunks and delay_between_chunks > 0:
                print(f"   ⏳ 다음 청크 처리 전 {delay_between_chunks:.2f}초 대기합니다...")
                time.sleep(delay_between_chunks)

    except KeyError as ke:
        print(f"🔴 임베딩 처리 중단 (키 오류): {ke}")
        print(
            f"   오류 발생 추정 청크: {current_chunk_number_for_error if current_chunk_number_for_error > 0 else '시작 전 또는 알 수 없음'}")
        return []
    except ValueError as ve:
        print(f"🔴 임베딩 처리 중단 (값 또는 상태 오류): {ve}")
        print(
            f"   오류 발생 추정 청크: {current_chunk_number_for_error if current_chunk_number_for_error > 0 else '시작 전 또는 알 수 없음'}")
        return []
    except Exception as e:
        print(
            f"🔴 Gemini 임베딩 중 예기치 않은 시스템 오류 발생 (청크 {current_chunk_number_for_error if current_chunk_number_for_error > 0 else '시작 전'} 처리 중): {type(e).__name__} - {e}")
        print("🔴 API 키, 모델 이름, 네트워크, 할당량, 라이브러리 버전 등을 다시 확인해 주세요.")
        return []

    if len(all_embedded_results) != total_texts and total_texts > 0:
        print(f"⚠️ 최종 임베딩 결과 수({len(all_embedded_results)})가 전체 입력 텍스트 수({total_texts})와 일치하지 않습니다!")

    print(f"\n✅ 임베딩 완료: 총 {len(all_embedded_results)}개 항목 반환.")
    return all_embedded_results


# sample_document_scope_content = """1. 신규 광고 인벤토리 노출 및 기본 기능 검증
#
# 1.1. 각 페이지별 신규 광고 모듈 노출 확인:
# 장바구니 리스트 하단에 신규 스타일링샷 광고 모듈 (2-grid) 노출 여부 확인.
# 주문완료 페이지 하단에 신규 스타일링샷 광고 모듈 (2-grid) 노출 여부 확인.
# 마이쇼핑 페이지 하단에 신규 스타일링샷 광고 모듈 (2-grid) 노출 여부 확인.
# 1.2. XPC 실험 그룹에 따른 광고 노출/미노출 확인:
# XPC 그룹 B (실험군) 할당 시, 각 페이지에 신규 스타일링샷 광고 모듈 정상 노출 확인.
# XPC 그룹 A (대조군) 할당 시, 각 페이지에 신규 스타일링샷 광고 모듈 미노출 확인.
# 1.3. 광고 모듈 노출 순서 검증 (XPC B그룹):
# 장바구니: "스타일링샷 광고 (new) > 상품광고 > 추천상품" 순서로 노출되는지 확인.
# 주문완료: "스타일링샷 광고 (new) > 상품광고" 순서로 노출되는지 확인.
# 마이쇼핑: "스타일링샷 광고 (new) > 상품광고" 순서로 노출되는지 확인.
# 1.4. 광고 최소/최대 노출 개수 및 SSP 제어 확인:
# SSP에서 응답 가능한 광고 개수가 2개 미만일 경우, 광고 모듈 자체가 노출되지 않는지 확인.
# 광고가 최대 20개까지 노출되는지 확인 (캐러셀 스와이프 동작 포함).
# 2. 스타일링샷 광고 모듈 UI 및 인터랙션 검증 (2-grid)
#
# 2.1. 모듈 공통 UI 요소 검증:
# 모듈 타이틀 "이런 연출이 가능한 상품은 어떠세요?" 고정 텍스트 노출 및 클릭 불가 상태 확인.
# "AD" 뱃지 노출 및 클릭 시 광고 정보 툴팁(광고 공통 사양) 노출 확인.
# 2.2. 개별 광고 카드 UI 및 인터랙션 검증:
# 스타일링샷 이미지: 1:1.07 비율로 크롭되어 노출되는지, 이미지 전체 영역 클릭 시 연결된 상품의 PDP로 정상 이동하는지 확인.
# 이미지 내 상품 태그: 크롭된 이미지 영역 내 정확한 위치에 노출되는지, 태그 클릭 시 연결된 상품의 PDP로 정상 이동하는지 확인 (크롭 영역 밖 태그는 미노출).
# 상품 정보 영역 (썸네일, 상품명, 가격, 별점, 리뷰/스크랩 수):
# 각 정보가 광고 데이터와 일치하게 정확히 노출되는지 확인.
# 상품명, 가격, 리뷰/스크랩 수가 최대 글자 수 초과 시 말줄임표(...) 처리되고 줄바꿈 없는지 확인.
# 상품 정보 영역 전체 클릭 시 연결된 상품의 PDP로 정상 이동하는지 확인.
# 스크랩 버튼:
# 광고 서버에서 내려주는 초기 스크랩 상태(스크랩/미스크랩)가 정확히 반영되어 아이콘으로 노출되는지 확인.
# 미스크랩 상태에서 버튼 클릭 시 스크랩 처리 및 아이콘 변경, 재클릭 시 언스크랩 처리 및 아이콘 변경 동작 확인.
# 2.3. 캐러셀 UI 동작 검증:
# 여러 개의 광고 카드가 캐러셀 형태로 노출되며, 좌우 스와이프(모바일) 또는 버튼(웹, 있다면)을 통해 다른 광고 카드를 탐색할 수 있는지 확인.
# 썸네일 사이즈 조정(48px → 42px) 및 리뷰 정보 축약형 디자인 변경 사항이 올바르게 반영되었는지 확인.
# 3. 광고 요청 및 응답 데이터 검증
#
# 3.1. 광고 요청 파라미터 검증 (Client → SSP):
# 각 인벤토리별 광고 요청 시 정확한 Inventory Code (장바구니: nhUE79hf, 주문완료: 5NV58zK8, 마이쇼핑: V9PmpCaS)가 사용되는지 확인.
# 광고 요청 API (POST /v1/ads) 호출 시 pageId (ohs-log 기준)가 정상적으로 전달되는지 확인.
# 3.2. 광고 응답 데이터 활용 검증:
# SSP로부터 받은 광고 응답 데이터를 기반으로 스타일링샷 광고 모듈의 각 요소(이미지, 텍스트, 상품 정보, 스크랩 상태 등)가 정확하게 화면에 표시되는지 확인.
# 4. 데이터 로깅 정확성 검증 (ads_log, ohs_log)
#
# 4.1. Impression 로그 검증:
# 스타일링샷 이미지가 화면에 1px 이상 노출 시, ohs-log (장바구니: 1773, 주문완료: 1778, 마이쇼핑: 1783) 및 ads-log (event_type: impression)가 각각 정상 적재되는지 확인.
# 4.2. Viewable Impression 로그 검증:
# 스타일링샷 이미지의 50% 영역이 1초 이상 연속 노출 시, ohs-log (장바구니: 1774, 주문완료: 1779, 마이쇼핑: 1784) 및 ads-log (event_type: viewable_impression)가 각각 정상 적재되는지 확인.
# 4.3. Card Click 로그 검증:
# 스타일링샷 이미지 또는 이미지 내 상품 태그 클릭 시, ohs-log (장바구니: 1775, 주문완료: 1780, 마이쇼핑: 1785, data.click_area로 구분) 및 ads-log (event_type: card_click)가 각각 정상 적재되는지 확인.
# 4.4. Product Click 로그 검증:
# 광고 모듈 내 상품 정보 영역(썸네일, 상품명, 가격 등 텍스트 영역) 클릭 시, ads-log (event_type: product_click)가 정상 적재되는지 확인. (문서 상 ohs-log는 정의되지 않음)
# 4.5. Scrap Click 로그 검증:
# 스크랩 버튼을 클릭하여 스크랩하는 경우, ohs-log (장바구니: 1776, 주문완료: 1781, 마이쇼핑: 1786) 및 ads-log (event_type: scrap_click)가 각각 정상 적재되는지 확인.
# 4.6. Unscrap 로그 검증:
# 스크랩된 아이템의 스크랩 버튼을 다시 클릭하여 언스크랩하는 경우, ohs-log (장바구니: 1777, 주문완료: 1782, 마이쇼핑: 1787)가 정상 적재되는지 확인 (ads-log는 호출 안 함).
# 4.7. 로그 공통 사양 준수 확인:
# 모든 로그 데이터가 공통 문서의 'Creative: Stylingshot - 2grid' 명세를 따르는지 확인.
# 5. XPC 실험 설정 및 동작 연동 검증
#
# 5.1. 각 인벤토리별 XPC 설정값 확인:
# 장바구니 (XPC ID: 1467), 주문완료 (XPC ID: 1468), 마이쇼핑 (XPC ID: 1469) 실험 설정이 올바른지 확인 (그룹 분배 비율 등).
# 5.2. XPC 그룹별 기능 분기 동작 확인:
# 사용자가 XPC 그룹 A (대조군)에 할당되었을 때, 신규 스타일링샷 광고 인벤토리가 노출되지 않고 기존 광고 노출 순서(상품광고 > 추천상품 또는 상품광고)가 유지되는지 확인.
# 사용자가 XPC 그룹 B (실험군)에 할당되었을 때, 신규 스타일링샷 광고 인벤토리가 문서에 정의된 새로운 순서로 정상 노출되는지 확인.
# """
#
# # 러너 함수 호출
# result = final_data_for_embedding = run_scope_extraction(
#     document_content=sample_document_scope_content,  # "스코프" 인자 전달
# )
#
# t = embedded_test_scope(result)
# print(t)