import time
import concurrent.futures
from flask_active.jenkins_trigger import jenkins_job_monitoring
import requests

URL = "url"

def get_notified_builds():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            return set(tuple(item) for item in response.json())
    except requests.RequestException as e:
        print(f"API 요청 실패: {e}")
    return set()

def run_monitoring():
    job_names = [
        "iOS-Automation-Prod",
        "Android-Automation-Prod",
        "Web-Automation-Prod",
        "iOS-Automation-QA",
        "Android-Automation-QA",
        "Web-Automation-QA"]
    notified_builds = get_notified_builds()

    start_time = time.time()
    duration = 35 * 60

    while time.time() - start_time < duration:
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            results = executor.map(jenkins_job_monitoring, job_names)

        for result in results:
            job_name = result.get("jobName")
            build_number = result.get("buildNumber")
            print(f'젠킨스 빌드 진행 결과 : {result}')
            print(f'notified_builds 저장값 조회 : {notified_builds}')
            if result.get("result") == "ABORTED":
                if (job_name, build_number) not in notified_builds:
                    print(result)
                    data = {
                        "result": result.get("result"),
                        "buildUrl": result.get("buildUrl"),
                        "jobName": result.get("jobName"),
                        "buildNumber": result.get("buildNumber"),
                        "is_building": result.get("is_building")
                    }
                    requests.post(URL, json=data)
                    notified_builds.add((job_name, build_number))

        time.sleep(60)
        print("1분 경과.")

if __name__ == '__main__':
    run_monitoring()
