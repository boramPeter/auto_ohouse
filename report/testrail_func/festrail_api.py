import requests
import base64
import json,re
import concurrent.futures
import threading
from app.common.app_config.data import AppVersion
from app.common.base_method.ios_result_binary import Result
from app.common.base_method.aos_result_binary import ResultAndroid
from web.BasicSetting.web_result_binary import ResultWeb

TESTRAIL_URL = "https://testohouse.testrail.io"
API_USER = "qa_auto@bucketplace.net"
API_KEY = "0NWhrLZ/fZfzcAYsu4Hp-klYQpAydc12d4pHLZhbE"

SUITE_DATA = {
  "payment": "2",
  "ads": "4",
  "lifestyle": "5"
}
def get_all_tests_in_run(run_id):
    """
    주어진 run_id의 모든 테스트 정보를 가져와 리턴합니다.
    """
    url = f"{TESTRAIL_URL}/index.php?/api/v2/get_tests/1/{run_id}"
    response = requests.get(url, auth=(API_USER, API_KEY))

    if response.status_code != 200:
        raise Exception(f"API 호출 실패: {response.status_code} - {response.text}")


try:
    auth_string = f"{API_USER}:{API_KEY}"
    auth_bytes = auth_string.encode('utf-8')
    AUTH_HEADER = {
        "Authorization": f"Basic {base64.b64encode(auth_bytes).decode('utf-8')}",
        "Content-Type": "application/json"
    }
except Exception as e:
    print(f"인증 헤더 생성 중 오류: {e}")
    AUTH_HEADER = {} # 오류 시 빈 헤더

def _make_api_request(method, api_endpoint, payload=None):

    url = f"{TESTRAIL_URL.rstrip('/')}/{api_endpoint}"

    try:
        # requests.request를 사용하여 GET/POST 분기 처리
        response = requests.request(
            method,
            url,
            headers=AUTH_HEADER,
            json=payload  # GET에서는 무시되고, POST에서는 body로 전송됨
        )
        response.raise_for_status() # HTTP 오류 발생 시 예외 발생

        # POST 요청 등 일부 API는 응답 본문이 없을 수 있음
        if response.status_code == 204 or not response.content:
            return {} # 성공했지만 내용이 없는 경우 빈 딕셔너리 반환

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"API 요청 중 오류 ({method} {api_endpoint}): {e}")
        # 오류 응답 내용이 있다면 출력 (디버깅에 유용)
        if 'response' in locals() and response.text:
            print(f"    응답 내용: {response.text}")
        return None
    except json.JSONDecodeError:
        print(f"API 응답 파싱 중 오류 ({method} {api_endpoint}).")
        return None

# 프로젝트 ID와 마일스톤 이름으로 마일스톤 ID 찾기 ---
def get_milestone_id_by_name(project_id, milestone_name):
    def _get_milestones_by_project_id(project_id):
        """프로젝트 ID로 마일스톤 리스트를 조회합니다."""
        api_endpoint = f"index.php?/api/v2/get_milestones/{project_id}"
        milestones_data = _make_api_request("GET", api_endpoint)
        return milestones_data.get('milestones', []) if milestones_data else None

    milestones = _get_milestones_by_project_id(project_id)
    if milestones:
        for milestone in milestones:
            if milestone.get('name') == milestone_name:
                return milestone.get('id')
    print(f"마일스톤 '{milestone_name}'을(를) 찾을 수 없습니다.")
    return None

def get_plan_details(plan_id):
    api_endpoint = f"index.php?/api/v2/get_plan/{plan_id}"
    return _make_api_request("GET", api_endpoint)

def get_runs_from_plan_details(plan_details):
    all_runs = []
    if plan_details and 'entries' in plan_details:
        for entry in plan_details['entries']:
            all_runs.extend(entry.get('runs', []))
    return all_runs

"""프로젝트 ID로 테스트 스위트 리스트를 가져옵니다."""
# def get_suites():
#     api_endpoint = f"index.php?/api/v2/get_suites/1"
#     # TestRail API는 'get_suites'에서 리스트를 바로 반환합니다.
#     return _make_api_request("GET", api_endpoint)
def get_filtered_case_ids(suite_id, custom_field_name, expected_value, project_id=1):
    offset = 0
    limit = 250
    all_cases = []

    while True:
        api_endpoint = f"index.php?/api/v2/get_cases/{project_id}&suite_id={suite_id}&limit={limit}&offset={offset}"
        print(f"get_cases API 호출 엔드포인트: {api_endpoint}")

        cases_data = _make_api_request("GET", api_endpoint)
        if not cases_data or 'cases' not in cases_data:
            print("테스트 케이스를 가져오는 데 실패했거나 데이터 없음.")
            break

        cases = cases_data['cases']
        all_cases.extend(cases)

        print(f"{len(cases)}개의 케이스를 가져옴 (offset: {offset})")

        if len(cases) < limit:
            # 마지막 페이지
            break

        offset += limit

    filtered_case_ids = [
        case['id'] for case in all_cases if case.get(custom_field_name) == expected_value
    ]

    print(f"필터 '{custom_field_name} == {expected_value}' 조건에 맞는 케이스 ID 수: {len(filtered_case_ids)}")
    return filtered_case_ids




def add_plan_entry(plan_id, suite_id, name, case_ids=None):
    """
    테스트 플랜에 새 항목(Entry)과 런을 추가합니다.
    구성과 특정 테스트 케이스 ID를 지정할 수 있습니다.
    """
    api_endpoint = f"index.php?/api/v2/add_plan_entry/{plan_id}"
    payload = {
        "suite_id": suite_id,
        "name": name
    }

    # case_ids가 제공되면, 해당 케이스만 포함하고 include_all은 false로 설정
    if case_ids is not None: # 빈 리스트[]도 유효하므로 None 체크
        payload["case_ids"] = case_ids
        payload["include_all"] = False
    else:
        # case_ids가 없으면 모든 케이스를 포함
        payload["include_all"] = True

    return _make_api_request("POST", api_endpoint, payload)



def get_test_plans_by_milestone_name(milestone_name):
    # 2. 마일스톤 ID 찾기
    milestone_id = get_milestone_id_by_name("1", milestone_name)
    if not milestone_id:
        return None

    # 3. 프로젝트 ID와 마일스톤 ID로 테스트 플랜 조회
    # get_plans API는 milestone_id로 필터링 가능
    api_endpoint = f"index.php?/api/v2/get_plans/1&milestone_id={milestone_id}"
    test_plans_data = _make_api_request("GET", api_endpoint)

    # 'plans' 키가 있을 경우 해당 리스트 반환, 없으면 빈 리스트 반환
    return test_plans_data.get('plans', []) if test_plans_data else None

def show_case_fields():
    case_fields = _make_api_request("GET", "index.php?/api/v2/get_case_fields")

    if case_fields:
        print("💡 `get_cases` 필터링 시:")
        print("   - 키(Key)로는 'system_name'을 사용합니다 ")
        print("   - 값(Value)으로는 ID를 사용합니다.")
        print("-" * 50)
        print(json.dumps(case_fields, indent=4, ensure_ascii=False))
        print("-" * 50)
    else:
        print("  테스트 케이스 필드를 조회하지 못했습니다.")


##########################################################

# 런 생성하는 함수
def create_test_runs(platform, test_execution, base_run_names, service_names, max_workers=5):
    """
    여러 서비스에 대한 테스트 런을 병렬로 생성하고,
    결과를 {서비스명: 런_ID, 서비스명_entry: 엔트리_ID} 형태의 딕셔너리로 반환합니다.
    """
    def _process_single_service(platform, auto_plan_id, base_run_name, service_name,
                                existing_run_names_set, name_lock,
                                case_id_cache, cache_lock,
                                results_dict, results_lock):
        """
        단일 서비스에 대한 테스트 런 생성 작업을 처리하는 워커 함수 (스레드에서 실행됨)
        """
        print(f"--- 스레드 시작: {base_run_name} ({service_name}) ---")
        if platform == "aOS":
            prefix_name = "[And]"
        elif platform == "iOS":
            prefix_name = "[iOS]"
        else:
            prefix_name = "[web]"

        # 1. 새 이름 결정 (락으로 보호)
        new_run_name = None
        with name_lock:
            # base_run_name과 일치하는 런의 개수를 세어 다음 번호를 결정합니다.
            # 주의: 접두사(prefix_name)를 고려하여 정확한 base_run_name으로 시작하는지 확인해야 합니다.
            #       여기서는 단순화를 위해 base_run_name으로 시작하는 것으로 가정합니다.
            #       더 정확하게 하려면 정규식이나 분해가 필요할 수 있습니다.
            base_prefix = f"{prefix_name}{base_run_name}"
            count = sum(1 for name in existing_run_names_set if name.startswith(base_prefix))

            if count == 0:
                new_run_name = base_prefix
            else:
                next_num = count + 1
                while True:
                    current_name = f"{base_prefix}_{next_num}"
                    if current_name not in existing_run_names_set:
                        new_run_name = current_name
                        break
                    next_num += 1
            existing_run_names_set.add(new_run_name)  # 로컬 Set 업데이트

        print(f"생성할 이름 (스레드: {base_run_name}): '{new_run_name}'")

        # 2. 스위트 ID 가져오기
        if service_name not in SUITE_DATA:
            print(f"SUITE_DATA에 '{service_name}'가 없습니다. (스레드: {base_run_name})")
            return
        chosen_suite_id = SUITE_DATA[service_name]

        # 3. 케이스 ID 캐시 확인 및 API 호출 (락으로 보호)
        rt_case_ids = None
        with cache_lock:
            if chosen_suite_id in case_id_cache:
                rt_case_ids = case_id_cache[chosen_suite_id]
                print(f"'{service_name}' 케이스 ID 캐시에서 로드 (스레드: {base_run_name}).")
            else:
                case_id_cache[chosen_suite_id] = None

        if rt_case_ids is None:
            print(f"'{service_name}' 케이스 ID API로 조회 (스레드: {base_run_name}).")
            filter_name = "custom_case_rt" if test_execution == "RT" else "custom_case_st"
            fetched_rt_case_ids = get_filtered_case_ids(chosen_suite_id, filter_name, True)
            if fetched_rt_case_ids is None:
                print(f"'{service_name}'의 케이스 ID 조회 실패. (스레드: {base_run_name})")
                with cache_lock:
                    if chosen_suite_id in case_id_cache and case_id_cache[chosen_suite_id] is None:
                        del case_id_cache[chosen_suite_id]
                return
            rt_case_ids = fetched_rt_case_ids
            with cache_lock:
                case_id_cache[chosen_suite_id] = rt_case_ids

        if not rt_case_ids:
            print(f"'{service_name}'에 케이스가 없어 빈 런으로 생성 (스레드: {base_run_name}).")
            rt_case_ids = [] # 빈 런 생성을 위해 빈 리스트 전달

        # 4. 플랜 엔트리/런 추가 및 결과 저장 (수정된 부분)
        new_entry = add_plan_entry(auto_plan_id, chosen_suite_id, new_run_name, case_ids=rt_case_ids)
        print(f"new_entry : {new_entry}")

        if new_entry:
            new_entry_id = new_entry.get('id')
            new_runs = new_entry.get('runs')

            # 엔트리 ID가 있고, runs 리스트가 있으며, 첫 번째 run에 ID가 있는지 확인
            if new_entry_id and new_runs and new_runs[0] and new_runs[0].get('id'):
                new_run_id = new_runs[0].get('id')
                print(f"새 런/엔트리 생성됨: Run ID={new_run_id}, Entry ID={new_entry_id} (스레드: {base_run_name})")
                # 락을 사용하여 결과 딕셔너리에 추가
                with results_lock:
                    results_dict[service_name] = new_run_id
                    results_dict[f"{service_name}_entry"] = new_entry_id
            # 엔트리 ID는 있지만 런 ID가 없는 경우 (예: 빈 런) - 요구사항에 따라 처리
            elif new_entry_id:
                 print(f"'{new_run_name}' 엔트리 생성 (ID={new_entry_id}) 했으나, 유효한 런 ID 없음 (스레드: {base_run_name}).")
            else:
                 print(f"'{new_run_name}' 생성 성공했으나, 엔트리 ID 또는 'runs' 리스트 문제 (스레드: {base_run_name}).")
        else:
            print(f"'{new_run_name}' 생성 실패 (스레드: {base_run_name}).")

    milestone_name = "Ohs-regular " + AppVersion.version(platform)
    test_plans = get_test_plans_by_milestone_name(milestone_name)

    if platform == "aOS":
        auto_plan_name = "Auto_and"
    elif platform == "iOS":
        auto_plan_name = "Auto_iOS"
    else:
        auto_plan_name = "Auto_web"

    if test_plans is None: return None
    auto_plan = next((plan for plan in test_plans if plan.get('name') == auto_plan_name), None)
    if not auto_plan:
        print(f"'{auto_plan_name}' 플랜을 찾을 수 없습니다.")
        return None
    auto_plan_id = auto_plan.get('id')
    print(f"'{auto_plan_name}' 플랜 (ID: {auto_plan_id})을 찾았습니다.")

    plan_details = get_plan_details(auto_plan_id)
    if not plan_details:
        print(f"플랜 상세 정보 조회 실패. 종료합니다.")
        return None
    existing_run_names_set = {run.get('name') for run in get_runs_from_plan_details(plan_details)}
    print(f"기존 런 이름: {existing_run_names_set}")

    results_dict = {}
    case_id_cache = {}

    name_lock = threading.Lock()
    cache_lock = threading.Lock()
    results_lock = threading.Lock()

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_service = {
            executor.submit(
                _process_single_service, platform,
                auto_plan_id, base_run_name, service_name,
                existing_run_names_set, name_lock,
                case_id_cache, cache_lock,
                results_dict, results_lock
            ): service_name
            for base_run_name, service_name in zip(base_run_names, service_names)
        }

        for future in concurrent.futures.as_completed(future_to_service):
            service_name = future_to_service[future]
            try:
                future.result()
                print(f"'{service_name}'에 대한 작업 완료.")
            except Exception as exc:
                print(f"'{service_name}' 처리 중 예외 발생: {exc}")

    return results_dict


# 결과값 입력하는 함수
def add_result_for_case(platform, case_func_name, result, comment=None):
    """
    테스트 케이스에 테스트 결과를 입력합니다.

    - ID: 1, Name: passed
    - ID: 5, Name: failed
    - ID: 2, Name: blocked
    - ID: 3, Name: untested
    - ID: 4, Name: retest
    - ID: 6, Name: na
    - ID: 7, Name: nt

    keyword는 반드시 함수명 내부의 서비스명 기준으로 작성해야 합니다. poc 이후 체크필
    """
    if platform == "android":
        test_run_binary = ResultAndroid()
        keywords = [
            "lifestyle", "ads"
        ]
    elif platform == "iOS":
        test_run_binary = Result()
        keywords = [
            "lifestyle", "ads"
        ]
    else:
        test_run_binary = ResultWeb()
        keywords = [
            "lifestyle"
        ]
    # 정규식을 이용해 숫자 5자리 추출
    match_number = re.search(r"\d{5}", case_func_name)
    tc_id = match_number.group() if match_number else None
    # 문자열에서 키워드 탐색
    service_name = next((keyword for keyword in keywords if keyword in case_func_name), None)
    if not service_name:
        print("키워드가 일치하지 않으므로 결과값 입력 생략.")
        return
    suite_id = SUITE_DATA[service_name]

    run_id = test_run_binary.read_result_slack(service_name+"_run_id")

    case_id = get_filtered_case_ids(suite_id, "custom_case_tc_id", tc_id)[0]
    print(tc_id,case_id,service_name)

    # 문자열 상태 -> status_id 매핑
    if isinstance(result, str):
        result_lower = result.lower()
        if result_lower == 'pass':
            status_id = 1
        elif result_lower == 'fail':
            status_id = 5
        else:
            print(f"지원하지 않는 상태 문자열: '{result}' (pass 또는 fail만 허용됨)")
            status_id = 3
    elif isinstance(result, int):
        status_id = result
    else:
        print(f"result 값이 올바르지 않습니다: {result}")
        return None

    api_endpoint = f"index.php?/api/v2/add_result_for_case/{run_id}/{case_id}"
    payload = {
        "status_id": status_id
    }
    if comment:
        payload["comment"] = comment

    print(f"결과 추가 API 호출: {api_endpoint}")
    print(f"Payload: {payload}")

    response = _make_api_request("POST", api_endpoint, payload)

    return response

def delete_test_run(platform):
    if platform == "aOS":
        test_run_binary = ResultAndroid()
        keywords = [
            "lifestyle", "ads"
        ]
    elif platform == "iOS":
        test_run_binary = Result()
        keywords = [
            "lifestyle", "ads"
        ]
    else:
        test_run_binary = ResultWeb()
        keywords = [
            "lifestyle"
        ]

    milestone_name = "Ohs-regular " + AppVersion.version(platform)

    test_plans = get_test_plans_by_milestone_name(milestone_name)

    if platform == "aOS":
        auto_plan_name = "Auto_and"
    elif platform == "iOS":
        auto_plan_name = "Auto_iOS"
    else:
        auto_plan_name = "Auto_web"

    if test_plans is None: return None
    auto_plan = next((plan for plan in test_plans if plan.get('name') == auto_plan_name), None)
    if not auto_plan:
        print(f"'{auto_plan_name}' 플랜을 찾을 수 없습니다.")
        return None
    auto_plan_id = auto_plan.get('id')

    response_list = []
    for keyword in keywords:
        entry_id = test_run_binary.read_result_slack(keyword+"_entry")
        api_endpoint = f"index.php?/api/v2/delete_plan_entry/{auto_plan_id}/{entry_id}"
        response_list.append(_make_api_request("POST", api_endpoint))

    return response_list


if __name__ == "__main__":
    base_run_names = ["Ads_RT"]
    service_names = ["ads"]
    platform = "aOS"#"aOS / iOS / web"
    test_execution = "RT"
    fetched_rt_case_ids = get_filtered_case_ids("4", "custom_case_rt", True)

    # t = create_test_runs(platform,test_execution, base_run_names, service_names)
    # t = delete_test_run("aOS")
    print(fetched_rt_case_ids)

'''
1. jira버전명을 가져와서 일치하는 마일스톤을 조회한다. 
2. 해당 마일스톤명의 하위플랜에서 auto가 있는지 찾는다.(플랜 3개로 간다면 각각 찾아야한다. 웹 실행시에 웹거를 찾고 그런식)

## 러너함수
3. 플랜 안에서 테스트런의 존재유무를 확인한다.
4. 없다면, 0번으로 런을 생성하고 있다면, 있는 갯수+1해서 런을 생성한다.
5. 테스트스위트를 가져올때 필터링을 해서 가져온다 (RT O만)
6. 4~5번에서 생성한 런의 아이디를 가져와서 바이너리에 넣어둔다.

## 핸들러함수
7. 그 아이디와 케이스를 조회해서 값을 넣어준다. 

'''