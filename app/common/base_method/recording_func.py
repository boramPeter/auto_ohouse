import os,base64,time
from app.common.app_config.data import ScreenshotPath
from selenium.common.exceptions import WebDriverException
import zipfile

class ScreenRecoder:
    def start_recording(self,current_func_name):
        try:
            file_path = ScreenshotPath.screenshot_path
            file_name = current_func_name + '_recording.mp4'
            file_full_path = os.path.join(file_path, file_name)

            if 'ios' in current_func_name:
                params = {'videoType': 'h264', 'timeLimit': 600, "videoFps":7, "videoQuality": "low", 'bitRate': 500000}
            else:
                params = {'bitRate': 1000000, 'videoFps': 7, 'videoSize': '1280x720', 'timeLimit': 600}

            self.driver.start_recording_screen(**params)
            print(f"{file_full_path} 녹화를 시작합니다.")
            return file_full_path
        except Exception as e:
            print(f"{current_func_name} 영상 시작 실패. {e}")


    def stop_recording(self, current_func_name):
        attempt = 0
        max_retries = 3
        while attempt < max_retries:
            try:
                screen_recording = self.driver.stop_recording_screen()

                file_name = current_func_name + '_recording.mp4'
                file_path = ScreenshotPath.screenshot_path
                file_full_path = os.path.join(file_path, file_name)

                with open(file_full_path, 'wb') as f:
                    f.write(base64.b64decode(screen_recording))
                print(f"{file_full_path} 녹화를 종료하고 저장했습니다.")
                break
            except Exception:
                attempt += 1
                time.sleep(2)
        else:
            print(f"{current_func_name} 영상 종료 실패.")
    def delete_recording(self,current_func_name):
        file_name = current_func_name + '_recording.mp4'
        file_path = ScreenshotPath.screenshot_path
        file_full_path = os.path.join(file_path, file_name)

        if 'aos' in current_func_name:
            start_idx = current_func_name.find('prod_') + len('prod_')
            end_idx = current_func_name.find('_aos')
            re_text = current_func_name[start_idx:end_idx] + '_aos'
        elif 'ios' in current_func_name:
            start_idx = current_func_name.find('prod_') + len('prod_')
            end_idx = current_func_name.find('_ios')
            re_text = current_func_name[start_idx:end_idx] + '_ios'
        else:
            re_text = None

        if os.path.exists(file_path):
            for file in os.listdir(file_path):
                if re_text and re_text in file:
                    file_to_delete = os.path.join(file_path, file)
                    if os.path.isfile(file_to_delete):
                        os.remove(file_to_delete)
                        print(f"{file_to_delete} 파일이 삭제되었습니다.")
                    else:
                        print(f"{file_to_delete} 파일이 아닙니다.")
            if not any(re_text in file for file in os.listdir(file_path)):
                print(f"디렉토리 내에 're_text'가 포함된 파일이 없습니다.")
        else:
            print(f"{file_path} 경로가 존재하지 않습니다.")

    def zip_recording_files(self,test_os):
        file_name = "/ios_recording.zip" if test_os == "ios" else "/aos_recording.zip"
        zip_path = ScreenshotPath.screenshot_path + file_name
        files_to_zip = []

        for root, dirs, files in os.walk(ScreenshotPath.screenshot_path):
            for file in files:
                if f'_{test_os}_' in file and '_recording' in file:
                    file_path = os.path.join(root, file)
                    files_to_zip.append(file_path)

        if files_to_zip:
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for file_path in files_to_zip:
                    zipf.write(file_path, os.path.relpath(file_path, ScreenshotPath.screenshot_path))
            print(f"압축 파일이 생성되었습니다: {zip_path}")
        else:
            print("압축할 파일이 없습니다.")

    def delete_mp4_zip_files(self,test_os):
        directory = ScreenshotPath.screenshot_path
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.zip') and test_os in file:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f'{file} deleted successfully.')
                if file.endswith('.mp4') and test_os in file:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f'{file} deleted successfully.')
                if file.endswith('.webm') and test_os in file:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f'{file} deleted successfully.')

