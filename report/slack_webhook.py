import time

import requests
import json
from app.common.app_config.data import Webhook
from production.common.data.automation_consts import ProdWebhook
from app.common.app_config.data import ScreenshotPath
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from glob import glob
import os
import ssl
import textwrap

'''
보안을 위해 제거
'''