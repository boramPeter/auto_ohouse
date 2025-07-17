Feature: mkt 브레이즈 검증

  Scenario: 앱 알림설정, 디바이스 알림권한 브레이즈 off 적용 확인
    Given 앱 삭제 -> 최신앱설치
    When 브레이즈 계정 로그인
    When 알림허용 팝업에서 미허용 후 알림설정 진입
    Then push_advertise,push_active_system off 확인
