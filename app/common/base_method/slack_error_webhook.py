import requests
import json
import time
from app.common.app_config.data import Webhook


class SlackErrorWebhook:
    def slack_error(self, param):
        qa_url = Webhook.auto_log_webhook
        header = {"Content-Type": "application/json"}
        payload = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": param
                    }
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "image",
                            "image_url": "https://emoji.slack-edge.com/T0D8R8GPJ/alert/f3aba07849ecae5b.gif",
                            "alt_text": "삐!"
                        },
                        {
                            "type": "mrkdwn",
                            "text": "자동화 테스트 강제 종료"
                        }
                    ]
                }
            ]
        }

        requests.post(url=qa_url, headers=header, data=json.dumps(payload))

