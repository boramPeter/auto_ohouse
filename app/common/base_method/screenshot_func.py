import inspect
import os,base64
from app.common.app_config.data import ScreenshotPath
import hashlib

class CaptureClass:
    def capture_screenshot(self):
        # 현재 실행중인 함수 이름 가져오기
        current_func_name = inspect.stack()[1][3]

        # 파일 경로 및 이름 지정
        file_path = ScreenshotPath.screenshot_path
        file_name = current_func_name + '.png'
        file_full_path = os.path.join(file_path, file_name)

        # 스크린샷 촬영
        self.driver.save_screenshot(file_full_path)

        return file_full_path

    def capture_screenshot_put_name(self, current_func_name):
        # 파일 경로 및 이름 지정
        file_path = ScreenshotPath.screenshot_path
        file_name = current_func_name + '.png'
        file_full_path = os.path.join(file_path, file_name)

        # 스크린샷 촬영
        self.driver.save_screenshot(file_full_path)

        return file_full_path

    def delete_png_files(self,test_os):
        directory = ScreenshotPath.screenshot_path
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.png') and test_os in file and file.startswith('test'):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f'{file} deleted successfully.')

    def delete_png_files_prod(self,test_os):
        directory = ScreenshotPath.screenshot_path
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.png') and test_os in file and file.startswith('prod'):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f'{file} deleted successfully.')

    def compare_and_delete_screenshots(self, file1, file2):
        def file_hash(filepath):
            hasher = hashlib.md5()
            with open(filepath, 'rb') as file:
                buffer = file.read()
                hasher.update(buffer)
            return hasher.hexdigest()

        hash1 = file_hash(file1)
        hash2 = file_hash(file2)

        # 스크린샷 파일 삭제
        os.remove(file1)
        os.remove(file2)

        # 비교 결과 반환
        return hash1 == hash2

    def multi_compare_and_delete_screenshots(self,*files):
        def file_hash(filepath):
            hasher = hashlib.md5()
            with open(filepath, 'rb') as file:
                buffer = file.read()
                hasher.update(buffer)
            return hasher.hexdigest()

        hashes = [file_hash(f) for f in files]

        # 파일 삭제
        for f in files:
            os.remove(f)

        # 하나라도 같은 해시가 있다면 True
        return len(hashes) != len(set(hashes))

