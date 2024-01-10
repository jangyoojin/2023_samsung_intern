# fast API tutorial
헛갈리는 부분  
1. request body: 클라이언트가 API로 데이터를 보낼 때 사용되는 데이터. Pydantic model들을 사용해 구현  
   response body: API가 request의 응답으로 클라이언트에게 보내는 데이터
2. path parameter VS query parameter VS body parameter  
   **path, query**는 **URL**에서 확인할 수 있는 데이터, **body**는 **그 외**의(URL에 보이지 않는) 데이터를 실어보낸다


## 1. 경로 매개변수
### 모든 경로 매개변수 받기
- 함수 파라미터를 경로에 넣을 수 있음
  ```python
  @app.get("/items/{item_id}")
  async def read_item(item_id: int):
    return {"item_id": item_id}
  ```
- 더 긴 경로가 먼저 정의되도록 할 것
  ```python
    @app.get("/users/me")
    async def read_user_me():
        return {"user_id":"the current user"}

    @app.get("/users/{user_id}")
    async def read_user(user_id: str):
        return {"user_id":user_id}
  ```

### 미리 정의된 경로 매개변수 값만 받기
Enum 클래스를 기반으로 받을 매개변수 값을 미리 정의할 수 있다.
- Enum으로 받을 매개변수 값을 리스트화 해서 미리 지정해두면 enum에 속하는 값만 받는다.
  ```python
    from enum import Enum
    from fastapi import FastAPI

    class ModelName(str, Enum):
        alexnet = "alexnet"
        resnet = "resnet"
        lenet = "lenet"

    app = FastAPI()

    @app.get("/models/{model_name}")
    async def get_model(model_name: ModelName):
        if model_name == ModelName.alexnet:
            return {"model_name": model_name, "message": "Deep Learning FTW"}

        if model_name.value == "lenet":
            return {"model_name": model_name, "message": "LeCNN all the images"}

        return {"model_name": model_name, "message": "Have some residuals"}
  ```

## 2. 쿼리 매개변수
경로 매개변수의 일부가 아닌 함수 매개변수로 선언하면 이를 쿼리라고 한다. 쿼리는 경로가 끝나고 ? 뒤에 등장하며 &로 쿼리들을 구분한다.
```
ex_ http://127.0.0.1:8000/items/?skip=0&limit=10
```
- 쿼리 매개변수 초기화  
  * Union 타입: 여러 개 타입이 허용되는 상황에서 사용. Optional[int]와 Union[int, None]은 같은 효과를 갖는다.
  ```python
    # = 으로 쿼리값 초기화
    # None으로 초기화해서 q를 선택적으로 받음
    # 여러 개 경로/쿼리 매개변수 사용 가능
    @app.get("/users/{user_id}/items/{item_id}")
    async def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
        item = {"item_id": item_id, "owner_id": user_id}
        if q:
            item.update({"q": q})
        if not short:
            item.update(
                {"description": "This is an amazing item that has a long description"}
            )
        return item
    ```
- 쿼리 매개변수를 필수로 만드려면 변수의 기본값을 선언할 수 없다.
  ```python
    @app.get("/items/{item_id}")
    async def read_user_item(item_id: str, needy: str):
        item = {"item_id": item_id, "needy": needy}
        return item
  ```

## 3. Request Body(요청 본문)
클라이언트(브라우저)가 API에 데이터를 보낼 때 사용하는 것.   
API는 클라이언트로 보통 response body(응답 본문)을 보낸다.

```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```
- request body를 선언할 때는 Pydantic 모델을 사용
- Pydantic 모델 중 BaseModel을 이용해 Item 클래스를 만듦 -> JSON 형식으로 본문이 해석됨
- 매개변수 item에 수신한 데이터를 전달
- 모델의 JSON 스키마를 정의하고 자동 UI 문서화에 사용됨

## 4. Query parameters and String Validations
FastAPI를 통해 매개변수에 대한 추가 정보와 검증을 선언할 수 있다.  
매개변수에 대한 추가 정보?  ex) Optional, Union, 초기값 설정 등으로 해당 매개변수가 필수가 아니라거나 None 등의 특정 타입이 될 수 있음을 알림
매개변수에 대한 **검증을 선언**? Query를 이용해 명시적으로 쿼리 매개변수를 선언함. max_length와 같은 검증 조건을 추가할 수 있음
ex) 
```python
from typing import Union
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None,max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```
```python
# 검증 추가
async def read_items(q: Union[str, None] = Query(default=None, min_length=3,max_length=50)):
```
```python
# 정규식 추가
async def read_items(q: Union[str, None] = Query(default=None, min_length=3,max_length=50, regex="^fixedquery$")):
```
```python
# 기본값 추가
async def read_items(q: str = Query(default="fixedquery", min_length=3,max_length=50)):
```
```python
# 필수로 만들기 / ... 사용
async def read_items(q: str = Query(...)):
```
```python
# q에 여러 값을 받기
async def read_items(q: Union[List[str], None] = Query(default=None)):
```
q에 다중 값을 리스트 등을 통해 받으면 아래와 같은 URL에서 q를 받을 수 있다.
```http://localhost:8000/items/?q=foo&q=bar```

- 기타 메타데이터: title, description, alias, deprecated
- 문자열 검증: min_length, max_length, regex

## 5. Path parameter and Numeric validations 
쿼리 매개변수에서는 문자열 검증을 살펴봤다. 경로 매개변수도 쿼리와 같이 검증할 수 있는데 숫자 검증 방식을 알아보자.  
- 같은 이름의 query를 Path로 선언해서 메타데이터 추가
- *을 이용해서 임의의 개수 값을 key-value pair로 인지(a.k.a kwargs)
- 숫자 검증
  - 1보다 크거나 같다: ge=1
  - 1보다 작거나 같다: le=1
  - 1보다 크다: gt=1
  - 1보다 작다: lt=1
  ```python
  from fastapi import FastAPI, Path
  app = FastAPI()

  @app.get("/items/{item_id}")
  async def read_items(
    *, item_id: int = Path(title="The ID of the item to get", ge=1), q: str
  ):
    results = {"item_id": item_id}
    if q:
      results.update("q":q)
    return results
  ```
## 6. Body
Query, Path가 무엇이고 어떤 옵션이 있는지를 살펴봤다면 이제는 이 파라미터들을 body에서 쓰는 법을 알아봅시다
### a. Multiple Parameters
 ### multiple body parameters
  ```python
  from typing import Union
  from fastapi import FastAPI, Body
  from pydantic import BaseModel

  app = FastAPI()

  class Item(BaseModel):
      name: str
      description: Union[str, None] = None
      price: float
      tax: Union[float, None] = None

  class User(BaseModel):
      username: str
      full_name: Union[float, None] = None

  @app.put("/items/{item_id}")
  async def update_item(item_id: int, user: User, importance: int = Body(), item: Union[Item, None] = None):
      results = {"item_id": item_id, "user": user, "importance": importance}
      if item:
          results.update({"item": item})
      return results
  ```
- 하나의 함수에서 body parameter 여러 개 사용 가능 ex) item, user
- single parameter를 body parameter로 사용하려면 FastAPI의 Body 사용 ex) importance
- body parameter도 기본값설정 가능 ex) item  

### single parameter
   - single parameter는 자동으로 query로 처리되기에 명시적으로 Query를 추가할 필요 없음 ex) q
```python
async def update_item(q: str | None = None):
```

- single body parameter를 키를 가진 JSON으로 예측하길 원하면 Body의 embed parameter 사용
```python
async def update_item(item_id: int, item:Item = Body(embed=True)):
```
### b. Fields  
Pydantic의 Field를 사용해 Pydantic Model 내부에서 검증 및 메타데이터 선언  
(path operation function의 파라미터들은 Query, Path, Body를 이용해 내부 검증(max_length, min_length, regex) 및 메타데이터(title, alias, description, deprecated) 사용)
```python
from typing import Union
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float,None]= None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
```
### c. Nested Models
두 가지 주제를 다룸
1. List, Set, Tuple 등 타입 선언하기: typing에서 import해서 List[형식]와 같이 사용
2. nested model 작성법

- List 타입
  ```python
  import typing import List
  my_list: List[str]
  ```
- Set 타입
  ```python
  from typing import Set
  tags: Set[str] = set() # = 뒷 부분은 초기값 설정을 위해(필수 아님)
  ```

- Nested model  
  BaseModel로 선언한 model을 다른 model의 타입으로 사용 가능
  ```python
  from typing import Union, Set
  from fastapi import FastAPI
  from pydantic import BaseModel

  app = FastAPI()

  class Image(BaseModel):
      url: str
      name: str

  class Item(BaseModel):
      image: Union[Image, None] = None

  @app.put("/items/{item_id}")
  async def update_item(item_id: int, item: Item):
      results = {"item_id": item_id, "item": Item}
      return results
  ```
  ```json
  json에서는 이렇게 보인다
  {
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
  }
  ```
  pydantic에서 제공하는 model을 사용하면 조건 검사 등을 해줍니다 최고~  
  아래와 같은 url 속성을 HttpUrl로 타입 선언하면 올바른 url 형태인지 검사합니다.
  ```python
  class Image(BaseModel):
    url: HttpUrl
    name: str
  ```
- deeply nested models example
  ```python
  from typing import Union, Set, List
  from fastapi import FastAPI
  from pydantic import BaseModel, HttpUrl

  app = FastAPI()

  class Image(BaseModel):
      url: HttpUrl
      name: str

  class Item(BaseModel):
      name: str
      description: Union[str, None] = None
      price: float
      tax: Union[float, None] = None
      tags: Set[str] = set()
      images: Union[List[Image], None] = None

  class Offer(BaseModel):
      name: str
      description: Union[str, None] = None
      price: float
      items: List[Item]

  @app.post("/offers/")
  async def create_offer(offer: Offer):
      return offer
  ```
