import requests

slack_token = ""
SLACK_API_URL = "https://slack.com/api/views.open"

def send_modal(trigger_id, modal_layout):
    headers = {
        "Authorization": f"Bearer {slack_token}",
        "Content-Type": "application/json; charset=UTF-8"
    }
    payload = {
        "trigger_id": trigger_id,
        "view": modal_layout
    }
    response = requests.post(SLACK_API_URL, json=payload, headers=headers)
    return response.json()

individual_execution_options = {
    "web":
        {
            "type": "section",
            "block_id": "individual_execution_block",
            "text": { "type": "mrkdwn", "text": "*웹 개별실행*" },
            "accessory": {
                "type": "static_select",
                "action_id": "individual_execution_select",
                "initial_option": { "text": { "type": "plain_text", "text": "전체" }, "value": "web_all" },
                "options": [
                    {"text": {"type": "plain_text", "text": "전체"}, "value": "web_all"},
                    {"text": {"type": "plain_text", "text": "OhsWeb"}, "value": "ohsweb"},
                    {"text": {"type": "plain_text", "text": "Contweb"}, "value": "CONTWEB"},
                    {"text": {"type": "plain_text", "text": "Commweb"}, "value": "COMMWEB"},
                    {"text": {"type": "plain_text", "text": "common"}, "value": "common"},
                    {"text": {"type": "plain_text", "text": "home"}, "value": "home"},
                    {"text": {"type": "plain_text", "text": "community"}, "value": "community"},
                    {"text": {"type": "plain_text", "text": "content"}, "value": "content"},
                    {"text": {"type": "plain_text", "text": "affiliate"}, "value": "affiliate"},
                    {"text": {"type": "plain_text", "text": "search"}, "value": "search"},
                    {"text": {"type": "plain_text", "text": "o2o"}, "value": "o2o"},
                    {"text": {"type": "plain_text", "text": "ads"}, "value": "ads"},
                    {"text": {"type": "plain_text", "text": "payment"}, "value": "payment"},
                    {"text": {"type": "plain_text", "text": "claim"}, "value": "claim"},
                    {"text": {"type": "plain_text", "text": "comm_platform"}, "value": "comm_platform"}
                ]
            }
        },
    "android":
        {
            "type": "section",
            "block_id": "individual_execution_block",
            "text": { "type": "mrkdwn", "text": "*안드로이드 개별실행*" },
            "accessory": {
                "type": "static_select",
                "action_id": "individual_execution_select",
                "initial_option": { "text": { "type": "plain_text", "text": "전체" }, "value": "all" },
                "options": [
                    {"text": {"type": "plain_text", "text": "전체"}, "value": "all"},
                    {"text": {"type": "plain_text", "text": "common"}, "value": "common"},
                    {"text": {"type": "plain_text", "text": "comm_service"}, "value": "comm_service"},
                    {"text": {"type": "plain_text", "text": "home"}, "value": "home"},
                    {"text": {"type": "plain_text", "text": "community"}, "value": "community"},
                    {"text": {"type": "plain_text", "text": "content"}, "value": "content"},
                    {"text": {"type": "plain_text", "text": "affiliate"}, "value": "affiliate"},
                    {"text": {"type": "plain_text", "text": "search"}, "value": "search"},
                    {"text": {"type": "plain_text", "text": "o2o"}, "value": "o2o"},
                    {"text": {"type": "plain_text", "text": "ads"}, "value": "ads"},
                    {"text": {"type": "plain_text", "text": "comm_platform"}, "value": "comm_platform"},
                    {"text": {"type": "plain_text", "text": "payment"}, "value": "payment"},
                    {"text": {"type": "plain_text", "text": "mkt"}, "value": "mkt"}
                ]
            }
        },
    "ios":
        {
            "type": "section",
            "block_id": "individual_execution_block",
            "text": {"type": "mrkdwn", "text": "*아이폰 개별실행*"},
            "accessory": {
                "type": "static_select",
                "action_id": "individual_execution_select",
                "initial_option": {"text": {"type": "plain_text", "text": "전체"}, "value": "all"},
                "options": [
                    {"text": {"type": "plain_text", "text": "전체"}, "value": "all"},
                    {"text": {"type": "plain_text", "text": "common"}, "value": "common"},
                    {"text": {"type": "plain_text", "text": "comm_service"}, "value": "comm_service"},
                    {"text": {"type": "plain_text", "text": "home"}, "value": "home"},
                    {"text": {"type": "plain_text", "text": "community"}, "value": "community"},
                    {"text": {"type": "plain_text", "text": "content"}, "value": "content"},
                    {"text": {"type": "plain_text", "text": "affiliate"}, "value": "affiliate"},
                    {"text": {"type": "plain_text", "text": "search"}, "value": "search"},
                    {"text": {"type": "plain_text", "text": "o2o"}, "value": "o2o"},
                    {"text": {"type": "plain_text", "text": "ads"}, "value": "ads"},
                    {"text": {"type": "plain_text", "text": "comm_platform"}, "value": "comm_platform"},
                    {"text": {"type": "plain_text", "text": "payment"}, "value": "payment"},
                    {"text": {"type": "plain_text", "text": "mkt"}, "value": "mkt"}
                ]
            }
        }
}

automation_option = {
    "type": "modal",
    "callback_id": "automation_option",
    "title": {"type": "plain_text", "text": "자동화 실행 및 종료"},
    "blocks": [{
            "type": "section",
            "block_id": "auto_start_opt",
            "text": { "type": "mrkdwn", "text": "*자동화 실행 옵션*" },
            "accessory": {
                "type": "static_select",
                "action_id": "auto_start_opt_select",
                "initial_option": { "text": { "type": "plain_text", "text": "자동화 실행" }, "value": "auto_start" },
                "options": [
                    { "text": { "type": "plain_text", "text": "자동화 실행" }, "value": "auto_start" },
                    { "text": { "type": "plain_text", "text": "자동화 종료" }, "value": "auto_stop" }
                ]
            }
        },
        {
            "type": "input",
            "block_id": "version_block",
            "label": { "type": "plain_text", "text": "버전"},
            "optional": True,
            "element": {
                "type": "plain_text_input",
                "action_id": "version_input",
                "placeholder": {"type": "plain_text", "text": "미입력 시 최신 버전 실행"}
            }
        },
        {
            "type": "section",
            "block_id": "debugging_block",
            "text": { "type": "mrkdwn", "text": "*디버깅*" },
            "accessory": {
                "type": "static_select",
                "action_id": "debugging_select",
                "initial_option": { "text": { "type": "plain_text", "text": "디버깅" }, "value": "디버깅" },
                "options": [
                    { "text": { "type": "plain_text", "text": "디버깅" }, "value": "디버깅" },
                    { "text": { "type": "plain_text", "text": "None 디버깅" }, "value": "None 디버깅" }
                ]
            }
        },
        {
            "type": "section",
            "block_id": "execution_block",
            "text": { "type": "mrkdwn", "text": "*Test Execution*" },
            "accessory": {
                "type": "static_select",
                "action_id": "execution_select",
                "initial_option": { "text": { "type": "plain_text", "text": "RT" }, "value": "RT" },
                "options": [
                    { "text": { "type": "plain_text", "text": "ST" }, "value": "ST" },
                    { "text": { "type": "plain_text", "text": "RT" }, "value": "RT" }
                ]
            }
        }
    ],
"submit": {"type": "plain_text", "text": "자동화 실행"}
}

start_automation_modal = {
    "type": "modal",
    "callback_id": "start_automation_modal",
    "title": { "type": "plain_text", "text": "자동화 플랫폼 선택" },
    "blocks": [
        {
            "type": "section",
            "block_id": "platform_block",
            "text": { "type": "mrkdwn", "text": "*플랫폼*" },
            "accessory": {
                "type": "static_select",
                "action_id": "platform_select",
                "initial_option": {"text": {"type": "plain_text", "text": "웹"}, "value": "web"},
                "options": [
                    { "text": { "type": "plain_text", "text": "웹" }, "value": "web" },
                    { "text": { "type": "plain_text", "text": "안드로이드" }, "value": "android" },
                    { "text": { "type": "plain_text", "text": "아이폰" }, "value": "ios" }
                ]
            }
        }
    ],
    "submit": { "type": "plain_text", "text": "자동화 옵션 선택" }
}


eng_qa_modal = {
    "type": "modal",
    "callback_id": "eng_qa_modal",
    "title": { "type": "plain_text", "text": "eng_qa 명령어 확인" },
    "blocks": [
        {
            "type": "section",
            "block_id": "eng_qa_block",
            "text": { "type": "mrkdwn", "text": "*명령어를 선택해주세요.*" },
            "accessory": {
                "type": "static_select",
                "action_id": "command_select",
                "initial_option": {"text": {"type": "plain_text", "text": "명령어 설명"}, "value": "help"},
                "options": [
                    { "text": { "type": "plain_text", "text": "명령어 설명" }, "value": "help" },
                    { "text": { "type": "plain_text", "text": "STF URL" }, "value": "stf" },
                    { "text": { "type": "plain_text", "text": "그라파나 URL" }, "value": "grafana" },
                    { "text": { "type": "plain_text", "text": "신고삭제" }, "value": "report" },
                    {"text": {"type": "plain_text", "text": "오집사/오박사 URL"}, "value": "ozipsa"},
                    {"text": {"type": "plain_text", "text": "iOS 디바이스팜 URL"}, "value": "ios_farm"},
                    {"text": {"type": "plain_text", "text": "Jenkins URL"}, "value": "jenkins"}
                ]
            }
        }
    ],
    "submit": { "type": "plain_text", "text": "명령어 옵션 선택" }
}

command_list = {
  "type": "modal",
  "callback_id": "eng_qa_help_modal",
  "title": {
    "type": "plain_text",
    "text": "eng-qa 커맨드 모음"
  },
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*자동화 실행 명령어*"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "1. `/eng_qa_자동화`\n   - 자동화 실행 및 종료 가능한 모달 호출"
      }
    },
    {
      "type": "divider"
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*서버 재실행 명령어*"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "`/서버_재시작`\n   - Flask 서버를 재시작함.\n   - 코드 적용이 필요하거나 flag 초기화가 필요할 때 사용. (실행중인 자동화에 영향이 있습니다.)"
      }
    },
    {
      "type": "divider"
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*eng_qa 명령어*"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "1. `/eng_qa 에서 help 옵션` - QA에서 사용 중인 명령어 설명"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "2. `/eng_qa 에서 STF 옵션` - STF URL 반환"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "3. `/eng_qa 에서 그라파나 옵션` - 그라파나 URL 반환"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "4. `/eng_qa 에서 카프카 옵션` - Kafka URL 반환 (deprecated)"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "5. `/eng_qa 에서 신고삭제 옵션` - user_id의 신고 기록 전부 제거"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "6. `/eng_qa 에서 오집사 옵션` - 오집사 Extension 다운로드 링크 반환"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "7. `/eng_qa 에서 iOS 디바이스팜 옵션` - iOS 디바이스팜 URL 반환"
      }
    },
      {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "8. `/eng_qa 에서 젠킨스 옵션` - 젠킨스 QA URL 반환"
      }
    }
  ]
}

def url_return(option):
    url_dict ={
        "stf" : "",
        "grafana":"<",
        "ozipsa":"",
        "ios_farm":"",
        "jenkins":""
    }
    if option == "report":
        blocks = [
    {
      "type": "input",
      "block_id": "report_block",
      "label": {
        "type": "plain_text",
        "text": "user_id를 입력하세요"
      },
      "element": {
        "type": "plain_text_input",
        "action_id": "id_input",
        "placeholder": {
          "type": "plain_text",
          "text": "user_id 입력"
        }
      }
    }
    ]


    else:
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{url_dict.get(option)}"
                }
            }
        ]


    block_kit = {
      "type": "modal",
      "callback_id": "url_return",
      "title": {
        "type": "plain_text",
        "text": "eng-qa 커맨드 모음"
      },
      "blocks": blocks,
        "submit": {"type": "plain_text", "text": "신고삭제 실행"}
    }
    if option != "report":
        block_kit.pop("submit", None)
    return block_kit