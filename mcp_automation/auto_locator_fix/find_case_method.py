import os

def search_scenario_in_feature(keyword, dirs, base_path):
    matches = []
    print(f"keyword: {keyword}")
    print(f"dirs: {dirs}")
    print(f"base_path: {base_path}")
    for directory in dirs:
        print(f"\n디렉토리 탐색 중: {directory}")
        for root, _, files in os.walk(directory):
            print(f"root: {root}")
            print(f"files: {files}")
            for file in files:
                filepath = os.path.join(root, file)
                print(f"filepath: {filepath}")

                if not file.endswith('.feature'):
                    continue

                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    try:
                        with open(filepath, 'r', encoding='ISO-8859-1') as f:
                            content = f.read()
                    except Exception as e:
                        print(f"인코딩 실패: {filepath} - {e}")
                        continue

                lines = content.splitlines()
                block = []
                temp_block = []
                collecting = False

                for line in lines:
                    stripped = line.strip()

                    if stripped.startswith('@'):
                        # 태그 감지 → 새 블록 시작
                        if collecting:
                            break
                        temp_block = [line]

                    elif stripped.startswith('Scenario:'):
                        if keyword in line:
                            collecting = True
                            temp_block.append(line)
                        else:
                            # 다른 시나리오 시작 → 중단
                            if collecting:
                                break
                            temp_block = []

                    elif collecting:
                        temp_block.append(line)
                        if stripped.startswith('Then'):
                            # Then 라인 포함 → 끝으로 간주 (필요시 조건 확장 가능)
                            block = temp_block.copy()
                            collecting = False

                if block:
                    relative_path = os.path.relpath(filepath, base_path)
                    print(f"\n키워드 발견! -> {relative_path}")
                    print("Scenario 블록:")
                    print("\n".join(block))
                    matches.append((relative_path, block))

    return matches

def append_scenario_to_feature_file(target_file,scenario_block):
    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 첫 번째 Feature: 라인 찾기
        feature_line = ""
        for line in lines:
            if line.strip().startswith("Feature:"):
                feature_line = line
                break

        if not feature_line:
            print("Feature: 라인을 찾을 수 없습니다. 파일 형식 확인 필요.")
            return

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(feature_line.strip() + '\n\n')  # Feature 라인 유지
            f.write("\n".join(scenario_block))
            f.write("\n")

        print(f"시나리오 블록이 성공적으로 입력되었습니다. -> {target_file}")

    except Exception as e:
        print(f"파일 처리 중 오류 발생: {target_file} - {e}")

def find_and_append_runner(keyword:str,platform:str):
    working_directory = os.getcwd()
    index = working_directory.rfind("ohs-qa-automation")
    target_directory = working_directory[:index + len("ohs-qa-automation")]

    platform_os = "android" if platform in ["android","안드로이드"] else "ios"

    directories = [
        os.path.join(target_directory, f'app/{platform_os}/features'),
        os.path.join(target_directory, f'app/{platform_os}/features_2'),
        os.path.join(target_directory, f'app/{platform_os}/features_3'),
    ]

    results = search_scenario_in_feature(keyword, directories, target_directory)
    first_block = results[0][1]  # (경로, 시나리오블록) 중 블록만 가져옴
    target_file = os.path.join(target_directory, f'app/{platform_os}/features_local/common.feature')

    append_scenario_to_feature_file(target_file, first_block)
    return True
