import logging
from logging import handlers
import os
from production.common.data.automation_consts import ProdLoggerPath
def make_logger_web(name=None):
    try:
        #1. 로거 생성
        logger = logging.getLogger(name)

        #2. 로거에 레벨 부여
        logger.setLevel(logging.DEBUG)

        '''
        젠킨스 이관 끝나면 제거필요
        '''
        user_name = None
        working_directory = os.getcwd()
        parts = working_directory.split(os.path.sep)
        if "Users" in parts:
            user_index = parts.index("Users") + 1
            if user_index < len(parts):
                user_name = parts[user_index]

        log_file_path = ProdLoggerPath.jenkins_prod_web_pickle_path if name in ["jenkins_prod_web_log.py","jenkins_web_log.py"] else f'/Users/{user_name}/Downloads/web_automation.log'

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
    except Exception as e:
        print (f"web 로거 예외처리 {e}")
try:
    logger_web = make_logger_web("web_log.py")
except Exception as e:
    print (f"web 로거 생성 예외처리 {e}")