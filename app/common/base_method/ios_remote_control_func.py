import requests
import time
from app.common.app_config.data import UDID

request_url = ""

def request_app_del(
        udid_prod=UDID.iphone_13_mini_udid,
        udid_st_1=UDID.iphone12mini_udid,
        udid_st_2=UDID.iphone11_udid,
        udid_rt=UDID.iphone_rt_udid,
        test_env=None
):
    url = f"{request_url}/app_del"
    body = {
        "udid_prod": udid_prod,
        "udid_st_1": udid_st_1,
        "udid_st_2": udid_st_2,
        "udid_rt": udid_rt,
        "test_env": test_env
    }
    timeout = 10

    try:
        response = requests.post(url, json=body, timeout=timeout)
        if response.status_code == 200:
            return True

        return False

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False

def request_app_del_opt(
        udid_opt
):
    url = f"{request_url}/app_del_opt"
    body = {
        "udid_opt": udid_opt
    }
    timeout = 10

    try:
        response = requests.post(url, json=body, timeout=timeout)
        if response.status_code == 200:
            return True

        return False

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False


def request_wda_stop(
        udid_prod=UDID.iphone_13_mini_udid,
        udid_st_1=UDID.iphone12mini_udid,
        udid_st_2=UDID.iphone11_udid,
        udid_rt=UDID.iphone_rt_udid,
        test_env=None
):
    url = f"{request_url}/wda_stop"
    body = {
        "udid_prod": udid_prod,
        "udid_st_1": udid_st_1,
        "udid_st_2": udid_st_2,
        "udid_rt": udid_rt,
        "test_env": test_env
    }
    timeout = 10

    try:
        response = requests.post(url, json=body, timeout=timeout)
        if response.status_code == 200:
            return True

        return False

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False

def request_wda_del(
        udid_prod=UDID.iphone_13_mini_udid,
        udid_st_1=UDID.iphone12mini_udid,
        udid_st_2=UDID.iphone11_udid,
        udid_rt=UDID.iphone_rt_udid,
        test_env=None
):
    url = f"{request_url}/wda_del"
    body = {
        "udid_prod": udid_prod,
        "udid_st_1": udid_st_1,
        "udid_st_2": udid_st_2,
        "udid_rt": udid_rt,
        "test_env": test_env
    }

    timeout = 50
    check_interval = 5

    try:
        response = requests.post(url, json=body, timeout=timeout)
        time.sleep(30)
        elapsed_time = 30
        while elapsed_time <= timeout:
            if response.status_code == 200:
                return True
            time.sleep(check_interval)
            elapsed_time += check_interval

        return False

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False
def request_wda_del_opt(
        udid_opt
):
    url = f"{request_url}/wda_del_opt"
    body = {
        "udid_opt": udid_opt
    }
    timeout = 10

    try:
        response = requests.post(url, json=body, timeout=timeout)
        if response.status_code == 200:
            return True

        return False

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False

def request_app_restart(
        udid_opt
):
    url = f"{request_url}/app_restart"
    body = {
        "udid_opt": udid_opt
    }
    timeout = 60


    try:
        response = requests.post(url, json=body, timeout=timeout)
        if response.status_code == 200:
            response_json = response.json()
            # 응답이 {"status": "success", "udid": udid} 형태인지 확인
            return True if response_json.get("status") == "success" and "udid" in response_json else False

        return False

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False

def request_wda_run(
        udid_prod=UDID.iphone_13_mini_udid,
        udid_st_1=UDID.iphone12mini_udid,
        udid_st_2=UDID.iphone11_udid,
        udid_rt=UDID.iphone_rt_udid,
        test_env=None
):
    url = f"{request_url}/wda_run"
    body = {
        "udid_prod": udid_prod,
        "udid_st_1": udid_st_1,
        "udid_st_2": udid_st_2,
        "udid_rt": udid_rt,
        "test_env": test_env
    }

    timeout = 50
    check_interval = 5

    try:
        response = requests.post(url, json=body, timeout=timeout)
        time.sleep(30)
        elapsed_time = 30
        while elapsed_time <= timeout:
            if response.status_code == 200:
                return True
            time.sleep(check_interval)
            elapsed_time += check_interval

        return False

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False

def request_ios_sound_check(udid):
    url = f"{request_url}/ios_sound_check/udid_sound_check?udid_value={udid}"
    timeout = 20
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            data = response.json()
            return data.get("result", False)

        return False

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False
