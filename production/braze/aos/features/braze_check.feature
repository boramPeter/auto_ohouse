Feature: mkt 브레이즈 검증

  Scenario: 앱 알림설정, 디바이스 알림권한 브레이즈 off 적용 확인
    Given 브레이즈 앱 설치 확인
    When 브레이즈 로그인
    When 알림설정 진입 후 설정화면 리프레쉬
    Then push_advertise,push_active_system off 확인

  Scenario: 앱 알림설정, 디바이스 알림권한 브레이즈 on 적용 확인
#    Given 알림권한 강제 on
    When 앱 재시작 -> 알림설정 on 변경 -> 재시작 2번 후 새로고침
    Then push_advertise,push_active_system on 확인

  Scenario: 앱 실행중 푸시 수신 확인
    Given 앱 실행중
    When 앱 push 발신
    Then 수신된 푸쉬 선택 후 랜딩페이지 확인


  Scenario: 앱 실행중 푸시 수신 확인
    Given 앱 종료상태
    When 종료상태에서 앱 push 발신
    Then 종료상태에서 수신된 푸쉬 선택 후 랜딩페이지 확인