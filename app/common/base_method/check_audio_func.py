import subprocess
import re


class AudioChecker:
    def check_audio_state_android(self, uid, phone_udid, today, times):
        time_conditions = '|'.join(times)
        # ADB 명령어 실행
        udid = phone_udid
        adb_command = f'-s {udid} shell dumpsys audio | grep "uid:{uid}" | grep "{today}" | grep "state:started" | grep -E "{time_conditions}"'
        result = subprocess.run(adb_command, shell=True, capture_output=True, text=True)

        return result.returncode == 0

    def check_uid(self, phone_udid, package_name):
        udid = phone_udid
        get_uid_cmd = f"adb -s {udid} shell pm dump {package_name} | grep 'userId'"
        result = subprocess.run(get_uid_cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            uid_line = result.stdout.strip()
            uid_match = re.search(r'\b(\d+)\b', uid_line)

            if uid_match:
                uid = uid_match.group(1)
                return uid
            else:
                return None
        else:
            return None

