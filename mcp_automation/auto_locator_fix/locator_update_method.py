import re

def update_locator(platform, locator_name, locator, dir):

    if platform == "android":
        file_path = f"{dir}/app/android/locator/all_locator/locator.py"
        class_name = "ProviderLocatorAndroid"
    else:
        file_path = f"{dir}/app/ios/locator/all_locator/locator.py"
        class_name = "ProviderLocatorIos"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"[!] 오류: 파일을 찾을 수 없습니다: {file_path}")
        return
    except Exception as e:
         print(f"[!] 파일 읽기 오류 {file_path}: {e}")
         return

    inside_class = False
    collecting = False
    start_index = None
    end_index = None
    buffer = []

    pattern_class = re.compile(rf'^\s*class\s+{class_name}\s*\(.*\):')
    pattern_var_start = re.compile(rf'^\s*{locator_name}\s*(?::\s*\w+)?\s*=\s*\(') # 타입 힌트 고려

    for idx, line in enumerate(lines):
        # 클래스 블록 내 indent 확인
        if inside_class and not line.startswith(" ") and line.strip():
             inside_class = False
             collecting = False # 클래스 블록 벗어나면 수집 중단
             continue
        # 클래스 시작 탐색
        if not inside_class and pattern_class.match(line):
            inside_class = True
            continue

        if inside_class:
            # 변수 할당 시작 탐색 (수집 중이 아닐 때만)
            if not collecting and pattern_var_start.match(line):
                collecting = True
                start_index = idx
                buffer = [line] # 현재 줄부터 버퍼 시작
                # 튜플이 같은 줄에서 끝나는지 확인
                if line.strip().endswith(')'):
                    end_index = idx; collecting = False; break
                continue

            # 변수 할당 라인 수집 중
            if collecting:
                buffer.append(line)
                # 수집 중인 라인에서 튜플 종료 괄호 확인
                if ')' in line.strip():
                     # 종료 괄호를 포함하는 라인을 찾으면 해당 라인까지 수집하고 종료
                     end_match = re.search(r'\)', line)
                     if end_match:
                         end_index = idx; collecting = False; break

    if start_index is None or end_index is None:
        print(f"[!] 로케이터 변수 '{locator_name}' 정의를 클래스 '{class_name}' ({file_path}) 내에서 찾을 수 없거나 완전하지 않습니다.")
        return

    # 튜플 전체 문자열 추출
    tuple_lines = ''.join(buffer)
    # 괄호 안의 내용 추출 (MULTILINE 옵션 추가)
    tuple_match = re.search(rf'=\s*\((.*)\)', tuple_lines, re.DOTALL | re.MULTILINE) # locator_name 부분을 느슨하게 변경

    if not tuple_match:
        print(f"[!] '{locator_name}'의 튜플 내용을 추출하지 못했습니다:\n{tuple_lines}")
        return

    # 괄호 안의 내용 가져오기
    tuple_content_raw = tuple_match.group(1).strip()

    # 따옴표/괄호 내부 콤마 무시하고 최상위 콤마 개수 세기
    num_original_elements = 0
    try:
        level = 0; in_single_quotes = False; in_double_quotes = False; comma_count = 0
        for char in tuple_content_raw:
            if char == "'" and not in_double_quotes: in_single_quotes = not in_single_quotes
            elif char == '"' and not in_single_quotes: in_double_quotes = not in_double_quotes
            elif char == '(' and not in_single_quotes and not in_double_quotes: level += 1
            elif char == ')' and not in_single_quotes and not in_double_quotes: level -= 1
            # 최상위 레벨이고, 따옴표 안에 있지 않을 때만 콤마 카운트
            elif char == ',' and level == 0 and not in_single_quotes and not in_double_quotes: comma_count += 1
        num_original_elements = comma_count + 1 # 요소 개수 = 콤마 개수 + 1
    except Exception as e:
         print(f"[!] 경고: 원본 튜플 구조 분석 중 오류 발생: {e}. 2개 요소로 가정합니다.")
         num_original_elements = 2 # 분석 실패 시 2개로 가정 (폴백)

    first_value = "AppiumBy.XPATH"
    new_tuple = "" # 새 튜플 문자열 초기화

    # *** 개선된 조건 사용 ***
    if num_original_elements >= 3:
        # 3개 이상 요소일 경우, 원본 세 번째 요소 추출 시도 (정규식 사용)
        third_value_str = None
        # 전체 원본 줄(`tuple_lines`)에서 세 번째 부분을 정규식으로 찾기
        # (첫번째요소, 두번째요소, 세번째요소...) 구조 가정
        match_third = re.search(r"""
            \([^,]+,       # 시작 '(' 와 첫번째 요소, 첫번째 콤마 매칭
            [^,]+,       # 두번째 요소와 두번째 콤마 매칭
            (.*)         # 세번째 요소 이후 모든 내용 캡처
            \)$          # 마지막 ')' 매칭 (공백/개행 고려)
            """, tuple_lines, re.DOTALL | re.VERBOSE | re.MULTILINE)

        if match_third:
            third_value_raw = match_third.group(1).strip()
            # 간단한 정리: 후행 콤마 제거 (있을 경우)
            if third_value_raw.endswith(','):
                 third_value_raw = third_value_raw[:-1].strip()
            # 의미있는 내용이 캡처되었는지 확인
            if third_value_raw:
                 third_value_str = third_value_raw # 원본 문자열 값 유지
                 # 3개 요소 튜플 구성 (repr 사용으로 안전하게 문자열 처리)
                 new_tuple = f"({first_value}, {repr(locator)}, {third_value_str})"
            else: # 내용 없으면 2개로 폴백
                print(f"[!] 경고: 3개 요소 구조 감지, 세 번째 요소 비어있음. '{locator_name}' 2개 요소로 생성.")
                new_tuple = f"({first_value}, {repr(locator)})"
        else: # 정규식 매칭 실패 시 2개로 폴백
            print(f"[!] 경고: {num_original_elements}개 요소 분석, 세 번째 요소 추출 실패. '{locator_name}' 2개 요소로 생성.")
            new_tuple = f"({first_value}, {repr(locator)})"
    else:
        # 2개 요소인 경우 (repr 사용으로 안전하게 문자열 처리)
        new_tuple = f"({first_value}, {repr(locator)})"

    # 시작 줄의 들여쓰기 가져오기
    indent = re.match(r"^(\s*)", lines[start_index]).group(1) if lines else ""
    # 새 코드로 교체할 라인 생성
    new_code = f"{indent}{locator_name} = {new_tuple}\n"

    # 원본 라인들을 새 코드로 교체
    lines[start_index : end_index + 1] = [new_code]

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"클래스 '{class_name}' 내 '{locator_name}' 업데이트 완료 → xpath: {locator}")
    except Exception as e:
         print(f"[!] 업데이트된 파일 쓰기 오류 {file_path}: {e}")