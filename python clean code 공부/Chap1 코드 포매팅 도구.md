# 단원 주요 내용
- Docstring
- 어노테이션

## Docstring
Docstring은 코드 파일에 있는 문서를 말한다. 이는 주석(comment)과는 다른데, 주석은 코드만으로 충분히 그 동작을 설명하지 못했을 때 코드 근처에 달아두는 것으로 코드 업데이트 과정에서 주석의 업데이트는 누락되거나 코드 해석 시간을 늘어나게 함으로써 개발에 불편함을 초래한다.  
Docstring은 코드의 특정 컴포넌트에 대한 문서화다. 파이썬은 동적 타이핑을 하므로 코드만 보면 어떤 타입의 파라미터를 사용했는지 파악하기 어렵다. 아래와 같이 docstring의 내용을 확인할 수 있고, \_\_doc__ 매서드로도 접근할 수 있다.
```
In [1]: dict.update?? #명령어 입력
#출력
Docstring:
D.update([E, ]**F) -> None. Update D from dict/iterable E and F. 
...
```  

## annotation
```
class Point:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

def locate(latitude: float, longitude:float) -> Point:
    """맵에서 좌표에 해당하는 객체 검색"""
```
locate 함수는 변수 latitude, longitude가 어떤 데이터 타입인지 명시한다. 그러나 이 표현은 프로그래머에게 변수의 타입을 명시할 뿐 코드적으로 해당 타입을 강제할 수는 없다.

## Mypy
정적 타입 검사기. annotation을 통해 동적 타입 언어이 파이썬에서 정적 타입 검사기 Mypy를 사용할 수 있다.

