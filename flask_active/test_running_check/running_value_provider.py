import requests

# API URL
url = ''
def get_terminate_value(platform):
    # API 호출
    response = requests.get(url)
    if response.status_code == 200:

        data = response.json()
        terminate_value = data[platform]['terminate']
        print(f"get_terminate_value : {platform},{terminate_value}")
        return terminate_value
    return False


def send_test_running_terminate_value(data):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        res = response.json()
        result = res['status']
        print(f"send_test_running_terminate_value : {result}")
        return result

# get_terminate_value("android")

