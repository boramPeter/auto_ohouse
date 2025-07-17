import re
from app.common.app_config.data import AppVersion

def extract_os_version(version_format, jira_key):
    '''
        보안을 위해 제거
        '''