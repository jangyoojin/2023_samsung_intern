# Todo

## 7월 13일

- Creaton 주제 선정 위한 자료 조사와 팀 회의(오후 1:30 ~ 3:30)
- 파이썬 클린코드 Chap 2에서 Chap 3 중간(80페이지)까지 학습
- 파이썬 개발 환경 셋팅  
- TIL: 파이썬 매직 매서드를 이용한 여러가지 객제를 학습하고 각 객체를 생성하는 방식을 간단히 배움

## 7월 14일

- 인턴 시스템에 OJT 계획서 작성
- 인턴 시스템에 주간 보고서 작성
- 파이썬 클린코드 Chap 1 학습
- 삼성 안전보건교육 2차시 수강
- Creaton 주제 확정을 위한 팀 회의(오전 9:30 ~ 10:30)

## 7월 17일

- 파이썬 클린코드 Chap 3 학습
- fast API 환경 설정하기 및 튜토리얼 경로, 쿼리 매개변수 학습
- 삼성 안전보건교육 3차시 수강
- Creaton 주제 구체화를 위한 팀 회의(오후 4:00 ~ 5:30)

## 7월 18일

- Creaton 선행 연구 자료 조사 및 내용 정리
- 네트워크 사업부 인턴 네트워킹 행사
- fast API 요청 본문(Request Body) 학습

## 7월 19일

- Creaton 진행 상황 점검(오후 2:00 ~ 4:00)
- Creaton 자료조사
- wsl 설치 및 vscode 연동
  
## 7월 20일

- 멘토님과 MongoDB 개념 및 사용법 학습
- WSL anaconda 환경 설정하기  
- fastAPI 쿼리 매개변수수와 문자열 검증, 숫자 검증 학습
- fastAPI 다중 매개변수 사용법 학습하고 allocateNssi model 구현 시도
- Creaton ppt 수합과 검토(오후 2:00 ~ 4:30)
- OJT 실적 입력
  
## 7월 24일

- fastAPI Body 관련 튜토리얼 학습
- NSSMF API allocateNssi response body 생성 함수 구현
- NSSMF API 세미나
  
## 7월 25일

- allocateNssi API 알고리즘 구현: pymongo tutorial 학습, fastAPI response model 학습, httpx 학습(비동기 noti 보내기)
- deallocateNssi API 구현: slicing 방식 조사
- fastAPI router 이해하기

## 7월 26일

- case별 return type 고려해 NetworkSlice CRUD 코드 수정: JSONResponse, response_model 사용
- 파이썬 클린코드 SOLID: SOL까지 읽기
- [인턴 행사] 제조동 투어(오후 1시 45분: 40분 소요)
- status code 설정 방식 계획하기 -> docs로 테스트하다가 에러 발견

## 7월 27일

- docs로 test 및 코드 수정(allocateNssi)
- db 데이터 저장 방법 학습 및 저장된 데이터 확인하기 -> db는 json 형태로만 저장 가능. jsonable_encoder 사용으로 해결
- subscribe test code 작성하기

## 7월 31일

- noti 타입 에러 수정하기 -> CRUD 정상 동작
- network slice get, patch 테스트하기

## 8월 1일

- subscribe test code 작성하기: 기능별로 구현하기
- test code tutorial 학습하기: [https://hackmd.io/@jenc/SJYmGcKsK]
- network slice 연동 테스트 코드 작성하기 -> 작성은 완료, 연동 테스트 목적 이해가 필요
- 안전보건교육 수강 완료 및 시험 응시

## 8월 2일

- subscribe test code 작성하기: 기능별 잘못된 input을 입력하는 경우 작성하기
- subscribe input 예외처리
- 오픈소스 개념 학습

## 8월 3일

- 오후 2시 Docker와 Kubernetes 실습 세미나
- Network Slice API test code 보완
- Network Slice API 리펙토링 -> Subscribe 브렌치로 푸시

## 8월 4일

- docker 명령어 학습
- NSSMF API 도커 이미지 빌드하기

## 8월 7일

- noti 보내는 코드 ip 주소 말고 다른 방식으로 수정하기 -> nssmf-adaptor service로 noti 보내게 수정
- k8s Deployment와 Replicaset 차이 실습
- 도커 이미지를 k8s에서 배포하기

## 8월 8일

- 오전: 함수형 프로그래밍 공부하기  
    <https://mangkyu.tistory.com/111>  
    <https://amzotti.github.io/programming%20paradigms/2015/02/13/what-is-the-difference-between-procedural-function-imperative-and-declarative-programming-paradigms/>  
    <https://dev.to/ruizb/declarative-vs-imperative-4a7l>  
    <https://amzotti.github.io/programming%20paradigms/2015/02/13/what-is-the-difference-between-procedural-function-imperative-and-declarative-programming-paradigms/>  
    <https://dev.to/ruizb/declarative-vs-imperative-4a7l>
- 쿠버네티스 스토리지 학습하기 -> 퀴즈 풀기, 볼륨(emptyDir, hostPath, PV 약간)
- PJT 발표 목차 작성하기

## 8월 9일

- 오전: PJT 발표 자료 만들기
- 포스텍 학생지원팀 간담회
- 발표 자료 만들기

## 8월 10일(PJT **발표**)

- 발표 자료 보완
- PJT 발표(오후 3:30 ~ 4:30)

## 8월 11일

- PV, PVC 학습하기  
  <https://docs.aws.amazon.com/ko_kr/eks/latest/userguide/efs-csi.html>
  <https://docs.aws.amazon.com/ko_kr/efs/latest/ug/whatisefs.html>  
  <https://kubernetes.io/docs/concepts/storage/persistent-volumes/>
- helm 등장 배경과 개념 살짝 맛보기

## 8월 14일

- 스토리지 클래스와 AWS 무엇인지 공부
- 사업부 발표 피피티 준비
- helm으로 배포 실습

## 8월 16일

- oAuth 개념: <https://inpa.tistory.com/entry/WEB-%F0%9F%93%9A-OAuth-20-%EA%B0%9C%EB%85%90-%F0%9F%92%AF-%EC%A0%95%EB%A6%AC>
- 사업부 발표 피피티 마무리
- 