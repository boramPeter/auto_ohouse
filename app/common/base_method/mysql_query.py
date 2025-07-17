import mysql.connector
from datetime import datetime
import os

working_directory = os.getcwd()
index = working_directory.rfind("ohs-qa-automation")
target_directory = working_directory[:index + len("ohs-qa-automation")]

user_name = None
parts = working_directory.split(os.path.sep)
if "Users" in parts:
    user_index = parts.index("Users") + 1
    if user_index < len(parts):
        user_name = parts[user_index]

class DbAccountInfo:
    '''
            보안을 위해 제거
            '''



class UserManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=DbAccountInfo.host,
            user=DbAccountInfo.user,
            password=DbAccountInfo.password,
            database=DbAccountInfo.database
        )
        self.cursor = self.connection.cursor()

    def update_place_for_card_collection(self, card_collection_id):
        '''
                보안을 위해 제거
                '''

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


class QaDataBaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=DbAccountInfo.qa_db_host,
            user=DbAccountInfo.qa_db_user,
            password=DbAccountInfo.qa_db_password,
            database=DbAccountInfo.qa_database,
            port=DbAccountInfo.qa_port
        )
        self.cursor = self.connection.cursor()

    def insert_or_update_device_info(self, device_no, remote_connect_url):
        check_query = "SELECT COUNT(*) FROM android_device_info WHERE device_no = %s"
        check_values = (device_no,)

        try:
            self.cursor.execute(check_query, check_values)
            result = self.cursor.fetchone()
            device_exists = result[0] > 0

            if device_exists:
                update_query = "UPDATE android_device_info SET remote_connect_url = %s WHERE device_no = %s"
                update_values = (remote_connect_url, device_no)
                self.cursor.execute(update_query, update_values)
                self.connection.commit()
                print("디바이스 정보가 업데이트되었습니다.")
            else:
                insert_query = "INSERT INTO android_device_info (device_no, remote_connect_url) VALUES (%s, %s)"
                insert_values = (device_no, remote_connect_url)
                self.cursor.execute(insert_query, insert_values)
                self.connection.commit()
                print("디바이스 정보가 삽입되었습니다.")
        except mysql.connector.Error as error:
            print("MySQL 오류 발생:", error)
        finally:
            self.close_connection()

    def get_remote_connect_url(self, device_no):
        query = "SELECT remote_connect_url FROM android_device_info WHERE device_no = %s"
        value = (device_no,)

        try:
            self.cursor.execute(query, value)
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                print("해당 device_no에 대한 remote_connect_url을 찾을 수 없습니다.")
                return None
        except mysql.connector.Error as error:
            print("MySQL 오류 발생:", error)
        finally:
            self.close_connection()

    def insert_test_result(self,list):
        case_no = None
        service_name = None
        failure_yn = None
        description = None
        result = None
        platform = None
        current_time = None
        table_name = "prod_automation"

        # 데이터 삽입
        for key, value in list.items():
            print(f"insert_test_result 키,밸류 : {key,value}")

            if 'case_no' in key:
                case_no = value
            if 'service_name' in key:
                service_name = value
            if 'failure_yn' in key:
                failure_yn = value
            if 'description' in key:
                description = value
            if 'result' in key:
                result = str(value)
            if 'test_os' in key:
                platform = value
            if 'run_date' in key:
                current_time = value
        if result is not None and service_name != "precondition":
            sql = f"INSERT INTO {table_name} (case_no, service_name, run_date, failure_yn, description, result, platform) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (case_no, service_name, current_time, failure_yn, description, result, platform)
            print(f"val:{val}")
            self.cursor.execute(sql, val)
            self.connection.commit()
        self.close_connection()


    def insert_not_running_result(self,func_list,run_date,test_platform):
        current_time = run_date[0]['run_date']
        table_name = "prod_automation"
        for func in func_list:
            case_no = func
            service_name = func[:-5]
            failure_yn = 0
            description = "미실행건"
            result = "fail"
            platform = test_platform
            sql = f"INSERT INTO {table_name} (case_no, service_name, run_date, failure_yn, description, result, platform) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (case_no, service_name, current_time, failure_yn, description, result, platform)
            print(val)
            self.cursor.execute(sql, val)
        self.connection.commit()
        self.close_connection()


    def close_connection(self):
        self.cursor.close()
        self.connection.close()