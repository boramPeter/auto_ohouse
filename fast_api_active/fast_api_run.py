from fastapi import FastAPI,BackgroundTasks
import uvicorn
from pydantic import BaseModel
from typing import Optional
from fast_api_active.ios_local_method.app_restart import restart_device
from fast_api_active.wda_run_prod import run_prod_wda,wda_prod_stop
from fast_api_active.wda_run_st_rt import run_st_rt_wda,wda_st_rt_stop
from fast_api_active.ios_local_method.del_app import del_processing_wda,del_ohouse_app
from app.common.base_method.idevicesyslog_func import SoundCheckProvider

app = FastAPI()

class Combined(BaseModel):
    udid_prod: Optional[str] = None
    udid_st_1: Optional[str] = None
    udid_st_2: Optional[str] = None
    udid_rt: Optional[str] = None
    udid_opt: Optional[str] = None
    test_env: Optional[str] = None

@app.post("/app_del")
def app_del(data: Combined):
    if data.test_env == "prod":
        del_ohouse_app(data.udid_prod)
    elif data.test_env == "st1":
        del_ohouse_app(data.udid_st_1)
    elif data.test_env == "st2":
        del_ohouse_app(data.udid_st_2)
    elif data.test_env == "rt":
        del_ohouse_app(data.udid_rt)
    else:
        pass
    return {"status": "success"}

@app.post("/wda_del")
def wda_del(data: Combined):
    if data.test_env == "prod":
        del_processing_wda(data.udid_prod)

    else:
        del_processing_wda(data.udid_st_1)
        del_processing_wda(data.udid_st_2)
        del_processing_wda(data.udid_rt)
    return {"status": "success"}

@app.post("/wda_del_opt")
def wda_del_opt(data: Combined):
    del_processing_wda(data.udid_opt)
    return {"status": "success"}
@app.post("/app_del_opt")
def app_del_opt(data: Combined):
    del_ohouse_app(data.udid_opt)
    return {"status": "success"}

@app.post("/app_restart")
async def app_restart(data: Combined):
    result = await restart_device(data.udid_opt)
    return result

@app.post("/wda_run")
def wda_run(data: Combined, background_tasks: BackgroundTasks):
    if data.test_env == "prod":
        del_processing_wda(data.udid_prod)
        background_task = run_prod_wda()
        background_tasks.add_task(background_task)

    else:
        del_processing_wda(data.udid_st_1)
        del_processing_wda(data.udid_st_2)
        del_processing_wda(data.udid_rt)
        background_task = run_st_rt_wda()
        background_tasks.add_task(background_task)
    return {"status": "success"}

@app.post("/wda_stop")
def wda_stop(data: Combined):
    if data.test_env == "prod":
        wda_prod_stop(udid_prod=data.udid_prod)
    else:
        wda_st_rt_stop(udid1=data.udid_st_1,udid2=data.udid_st_2,udid3=data.udid_rt)
    return {"status": "success"}

@app.get("/ios_sound_check/{udid_sound_check}")
def return_check_log_existence(udid_sound_check :str, udid_value :str ):
    udid = {"udid_sound_check":udid_sound_check,"udid_value":udid_value}
    result = SoundCheckProvider().actual_result(udid["udid_value"])
    return {"result": result}

if __name__ == "__main__" :
    uvicorn.run(
        "fast_api_run:app",
        host="0.0.0.0",
        port=8000
    )