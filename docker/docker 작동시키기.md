# docker container 생성
1. MongoDB Image 가져오기: docker pull mongo
2. MongoDB Image container 만들기: docker run --name mongodb-con -v ~/mongodb/:/data/db -d -p 27017:27017 mongo

---
1. docker 이미지 띄우기
   ```
   docker start mongodb-con
   ```
2. python MongoClient가 동작하면서 로컬과 포트 번호로 연결해준다.
   ```python
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")

    db = client.Nssi
    ```
3. shell에서 mongodb 내용 보기
   1) docker exec -it /bin/bash
   2) mongosh
   3) mongodb 명령어 사용하기


# docker image 생성

## 1. Dockerfile 작성
   
   1) FROM base_image: OS와 같은 기본이 되는 image 불러오기
   2) RUN ...: 필요한 라이브러리 설치
   3) WORKDIR [dir]: 컨테이너 내부에 디렉토리 만들기
   4) COPY [local_dir] [container_dir]: 로컬 파일을 컨테이너 내부로 복사하기
   5) CMD ["명","령","어"]: 프로그램 시작 명령어 작성하기  


## 2. docker build -t [image_name]:[tag]: 이미지로 만들기
   도커는 이미지를 만들 때 실제로 컨테이너를 띄우고 이 위에 Dockerfile에 있는 명령을 실제로 수행한 다음, 해당 환경의 스냅샷을 찍어서 이미지의 바이너리 파일과 같이 사용한다. 즉, 도커 이미지는 컨테이너 실행 결과를 캡쳐한 것이기에 실제로 동작한다는 것을 보장한다.

## 3. docker images | grep [image_name]: 만든 이미지 확인하기
