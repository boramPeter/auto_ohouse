from logging import handlers
from app.common.app_config.data import LoggerPath
from production.common.data.automation_consts import ProdLoggerPath
import logging


def make_logger_aos(name=None):
    #1. 로거 생성
    logger = logging.getLogger(name)

    #2. 로거에 레벨 부여
    logger.setLevel(logging.DEBUG)
    if name == "prod_aos_log.py":
        log_file_path = ProdLoggerPath.prod_aos_pickle_path
    elif name == "jenkins_prod_aos_log.py":
        log_file_path = ProdLoggerPath.jenkins_prod_and_pickle_path
    else:
        log_file_path = LoggerPath.aos_pickle_path

# formatter 객체 생성
    formatter = logging.Formatter(fmt="[%(asctime)s][Line No: %(lineno)d] - %(name)s - %(levelname)s - %(message)s")

    #3-1. handler 객체 생성
    stream_handler = logging.StreamHandler()
    file_Handler = handlers.TimedRotatingFileHandler(log_file_path, encoding='utf-8')
    file_Handler.setLevel(logging.DEBUG)
    logger.addHandler(file_Handler)


    #3-2. handler에 level 설정
    stream_handler.setLevel(logging.DEBUG)
    file_Handler.setLevel(logging.DEBUG)

    #3-3. handler에 format 설정
    stream_handler.setFormatter(formatter)
    file_Handler.setFormatter(formatter)
    file_Handler.suffix = "%Y%m%d"

    #4. logger에 handler 추가
    logger.addHandler(stream_handler)
    logger.addHandler(file_Handler)
    return logger

def make_logger_ios(name=None,path=None):
    #1. 로거 생성
    logger = logging.getLogger(name)

    #2. 로거에 레벨 부여
    logger.setLevel(logging.DEBUG)

    if path is not None:
        log_file_path = path
    else:
        if name == "ios_ads.py":
            log_file_path = LoggerPath.ios_ad_log_path
        elif name == "prod_ios_log.py":
            log_file_path = ProdLoggerPath.prod_ios_pickle_path
        elif name == "jenkins_prod_ios_log.py":
            log_file_path = ProdLoggerPath.jenkins_prod_ios_pickle_path
        else:
            log_file_path = LoggerPath.ios_pickle_path


    # formatter 객체 생성
    formatter = logging.Formatter(fmt="[%(asctime)s][Line No: %(lineno)d] - %(name)s - %(levelname)s - %(message)s")

    #3-1. handler 객체 생성
    stream_handler = logging.StreamHandler()
    file_Handler = handlers.TimedRotatingFileHandler(log_file_path, encoding='utf-8')
    file_Handler.setLevel(logging.DEBUG)
    logger.addHandler(file_Handler)


    #3-2. handler에 level 설정
    stream_handler.setLevel(logging.DEBUG)
    file_Handler.setLevel(logging.DEBUG)

    #3-3. handler에 format 설정
    stream_handler.setFormatter(formatter)
    file_Handler.setFormatter(formatter)
    file_Handler.suffix = "%Y%m%d"

    #4. logger에 handler 추가
    logger.addHandler(stream_handler)
    logger.addHandler(file_Handler)
    return logger