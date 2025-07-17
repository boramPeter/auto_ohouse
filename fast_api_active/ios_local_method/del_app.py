import time,os
from app.common.app_config.data import PackageName

def del_processing_wda(iphone_udid):
    time.sleep(2)
    udid = iphone_udid
    command = os.popen("which ideviceinstaller").read().strip() or "/opt/homebrew/bin/ideviceinstaller"
    app_del = f'{command} -u {udid} -U "com.devicefarm.WebDriverAgentRunner.xctrunner"'
    os.system(app_del)

    

def del_ohouse_app(iphone_udid):
    time.sleep(2)
    udid = iphone_udid
    command = os.popen("which ideviceinstaller").read().strip() or "/opt/homebrew/bin/ideviceinstaller"
    app_del = f'{command} -u {udid} -U {PackageName.ios_bundle_id}'
    os.system(app_del)