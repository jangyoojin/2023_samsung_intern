# docker 이미지 배포하는 방법

1. pod 만들기  
   pod 생성을 위해 yaml 파일을 작성한다. 아래와 같은 양식으로 작성하고 해당 파일을 적용한다.
   - yaml 파일 예시

    ```
    apiVersion: v1

    kind: Pod
    metadata:
      name: nginx
    spec:
      containers:

    - name: nginx
        image: nginx:1.14.2
        ports:
      - containerPort: 80

    ```

    - yaml 파일 적용하기

    ```
        kubectl apply -f [yaml file name]
    ```

2. image를 레지스트리에 올리기

   ```
   # 도커 이미지 만들기
   docker build -t [image name]:[image tag] [Dockerfile dir]
   # 도커 이미지 이름 바꾸기
   docker tag [image name]:[image tag] [registry IP]:[registry port]/[image name]:[image tag]
   # 도커 허브에 올리기
   docker push [registry IP]:[registry port]/[image name]:[image tag]
   ```

3. 1에서 만든 yaml 파일을 다시 어플라이 해서 이미지를 허브에서 끌어오기
