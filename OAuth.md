- 구성 요소
  - Resource Owner: 내 API를 사용하는 고객
  - Client: 내 API
  - Authorization Server: code, token 발행해주는 서버
  - Resoruce Server: 개인정보 관리하는 서버

- 용어
  - Client ID: 앱(서비스)을 식별하는 ID
  - Client Secret: Client ID 에 대한 PW
  - Authorized redirect URLs: Owner의 개인정보를 콜백할 주소
  - scope: Resource Server에서 사전에 사용 가능하도록 미리 정의한 기능

- Resource Server에 저장되는 정보
  - Client ID
  - Client Secret 
  - Redirect URL
  - user id: client와 연결된 Resource Owner의 id
  - scope: client Resource Owner가 허락한 기능들

- 검사를 받는 시점
  - Owner가 Authorization Server에 로그인 페이지를 요청 시: Client ID, Redirect URL이 서버에 저장된 내용과 일치하는지 검사
  - (첫 접근)Client가 Owner로부터 Authorization code를 전달받고 Authorization Server에 접근할 때: Authorization code가 같은지 검사
  - (두번째 접근부터) Client가 Resource Server에 정보 요청: Access Token이 일치하는지 검사