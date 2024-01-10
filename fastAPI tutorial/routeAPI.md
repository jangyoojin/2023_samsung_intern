# APIRoute로 프로젝트 관리하기
(https://lucky516.tistory.com/110)  
프로젝트가 커지면 하나의 파일에 모든 코드를 작성하지 않고 기능별로 파일 구조를 형성해 관리한다.
```
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin

```
서로 다른 패키지와 모듈(폴더와 파일)에 있는 함수를 main에 있는 app(FastAPI 객체)가 인식하려면 route를 이용해 다른 모듈의 함수를 알리는 것이 필요하다. 다른 모듈의 함수를 하나로 묶고 이를 app에 전달하는 것이 APIRoute가 하는 일이다.  

## APIRoute 사용법
1. router가 필요한 모듈 안에서 APIRouter 객체를 생성
2. APIRouter 객체에 대해서 path decorater 작성
3. main에서 모든 router를 app(FastAPI 객체)에 include_router로 묶는다.

### dependence란?


### tags란?
openAPI에서 아래와 같이 각 메서드를 tag 기준으로 분리해 docs를 작성한다.
![Alt text](image.png)