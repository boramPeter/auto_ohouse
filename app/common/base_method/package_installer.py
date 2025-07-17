import subprocess
import getpass,os

working_directory = os.getcwd()
index = working_directory.rfind("ohs-qa-automation")
target_directory = working_directory[:index + len("ohs-qa-automation")]

def install_requirements():
    requirements_path = f'{target_directory}/requirements.txt'

    subprocess.check_call(['pip3', 'install', '-r', requirements_path])

    additional_packages = ['pyparsing==3.0.9', 'httplib2==0.22.0']

    subprocess.check_call(['pip3', 'install'] + additional_packages)

    script_url = "https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh"
    script_path = "/tmp/homebrew_install.sh"

    subprocess.check_call(['curl', '-fsSL', script_url, '-o', script_path])

    password = input("############ npm 설치를 위한 sudo password 입력필요 ################: ")
    subprocess.check_call(['echo', password, '|', 'sudo', '-S', '/bin/bash', script_path])

    os.remove(script_path)
