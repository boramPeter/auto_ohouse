Feature: 자동화 실행 전 사전조건
  @PRE
  Scenario: 앱 설치 시나리오
    When 앱 삭제

  @PRE
  Scenario: 구글플레이에서 오늘의집 앱 설치
    When 구글플레이스토어 진입 후 오늘의집 검색 -> 앱 설치
    Then BUCKETPLACE 버튼 노출확인으로 설치확인

