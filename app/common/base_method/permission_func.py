import subprocess
import time,os
# android.permission.POST_NOTIFICATIONS,
# android.permission.READ_EXTERNAL_STORAGE,
# android.permission.READ_MEDIA_IMAGES,
# android.permission.READ_MEDIA_AUDIO,
# android.permission.READ_MEDIA_VIDEO
import sys
from app.common.base_method.user_context import get_current_user_data


def grant_permission(package_name, phone_udid, permission):
    user_name = get_current_user_data()[2]
    '''
            보안을 위해 제거
            '''
