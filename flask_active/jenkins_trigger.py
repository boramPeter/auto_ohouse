import requests,random
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

JENKINS_URL = ""
TOKEN_NAME = "webhook_token"
USER_NAME = "peter.kim"
API_TOKEN = ""

def jenkins_trigger(job_name,test_execution=None, debug=True, service=None, user_id=None,version=None,auto_trigger=None):
    if test_execution == "prod":
        END_POINT = "build"
        params = {"token": TOKEN_NAME}
    else:
        END_POINT = "buildWithParameters"
        params = {
            "token": TOKEN_NAME,
            "TEST_EXECUTION": test_execution,
            "DEBUG": str(debug).lower(),
            "SERVICE": service,
            "USER_ID": user_id,
            "VERSION": version,
            "AutoTrigger": auto_trigger
        }

    URL = 'https://'+USER_NAME+':'+API_TOKEN+'@'+JENKINS_URL+'/job/'+job_name+'/'+END_POINT
    response = requests.post(URL, params=params)
    print(f'statusCode: {response.status_code}')
    return response.status_code

def jenkins_job_monitoring(job_name):
    END_POINT = "lastBuild/api/json"
    params = {"token": TOKEN_NAME}

    URL = f'https://{USER_NAME}:{API_TOKEN}@{JENKINS_URL}/job/{job_name}/{END_POINT}'

    session = requests.Session()
    retries = Retry(total=5, backoff_factor=2, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))

    try:
        response = session.get(URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "buildUrl": data.get("url"),
            "buildNumber": data.get("number"),
            "jobName": data.get("fullDisplayName").split(" #")[0] if "fullDisplayName" in data else None,
            "result": data.get("result"),
            "is_building": data.get("building", False)
        }
    except requests.exceptions.RequestException as e:
        print(f"Jenkins 요청 실패: {e}")
        return None

def jenkins_job_checker(job_names):
    END_POINT = "lastBuild/api/json"
    params = {"token": TOKEN_NAME}  # TOKEN_NAME은 전역으로 정의되었거나 전달되어야 합니다.

    session = requests.Session()
    retries = Retry(total=5, backoff_factor=2, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))

    non_building_jobs = []

    for job_name in job_names:
        URL = f'https://{USER_NAME}:{API_TOKEN}@{JENKINS_URL}/job/{job_name}/{END_POINT}'
        try:
            response = session.get(URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            if not data.get("building", False):
                non_building_jobs.append(job_name)

        except requests.exceptions.RequestException as e:
            print(f"Jenkins 잡 '{job_name}' 요청 실패: {e}")
            continue
        except Exception as e:
            print(f"Jenkins 잡 '{job_name}' 처리 중 알 수 없는 오류 발생: {e}")
            continue

    if non_building_jobs:
        return random.choice(non_building_jobs)
    else:
        return False

job_list = ["Web-Automation-QA3","Web-Automation-QA2","Web-Automation-QA"]
print(jenkins_job_checker(job_list))