1. 로그 보기
   ```
   docker logs "hashId or container name"
   ```
2. docker 실행
   ```
   docker run --name mongodb-con -v ~/mongodb/:/data/db -d -p 27017:27017 mongo
   ```
3. exit 상태 모든 container 삭제
   ```
   docker image prune
   ```