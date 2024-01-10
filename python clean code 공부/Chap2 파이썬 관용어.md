## 인덱스와 슬라이스
- 슬라이싱 결과   
   슬라이싱 결과는 항상 input과 같은 데이터 타입을 리턴해야 한다.  
   ex) range(1,100)[25:75] 
- index  
    [시작:끝:간격]
- \_\_getitem__, __len__으로 자체 시퀀스 구현 가능

## 컨텍스트 관리자
- \_\_enter__, \_\_exit__으로 구성
- 예외 처리에 유용
- 키워드 with과 함께 사용한 객체는 예외 처리로 동작
- 컨텍스트 관리자 구현 방법   
    방법1. \_\_enter__, \_\_exit__ 구현  
    방법2. contextlib 모듈 사용 ex) @contextlib.contextmanager + 제너레이터 함수

  
## 속성과 객체 매서드 타입
- 파이썬 객체의 모든 속성은 public
- 관용적으로 private으로 취급하는 표현들이 있으나 외부에서 변경할 수 있음. 언더바(_) 하나를 속성 이름 앞에 붙이면 이는 해당 속성이 private이라는 의미.  
  이중 언더바 사용 자제
- @property 사용하기  
    @property로 private 속성의 값을 외부로 리턴(getter 함수의 역할), @[property_name].setter로 private 속성 값을 (조건 검사 후) 업데이트

## 이터러블 객체 만들기
- 이터러블 객체 만들기: \_\_iter__,\_\_next__ 매서드 포함한 객체  
  ```
  class DateRangeContainerIterable:  
    def __init__(self, start_date, end_date):  
        self.start_date = start_date
        self.end_date = end_date
    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_dat += timedelta(days=1)
    ```
- 시퀀스 만들기: \_\_len__, \_\_getitem__ 매서드로 구성, 메모리는 O(n), x번째 원소 접근은 O(1)
  ```
  from datetime import timedelta
  class DateRangeSequence:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days=[]
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __len__(self):
        return len(self._range)

    def __getitem__(self, day_no):
        return self._range[day_no]
    ```

## 컨테이너 객체
- \_\_contains__ 매서드로 구현한 객체
  ```
    element in container => container.__contains__(element)
    ```
- 컨테이너 객체를 사용하면 조건 검사를 직관적인 코드로 작성할 수 있고, 더 작은 객체로 구체적인 조건 검사를 넘길 수 있다.
  ```
  class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __contains__(self,coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height

    class Grid:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.limits = Boundaries(width, height)

        def __contains__(self, coord):
            return coord in self.limits

    # use
    board = Grid(10,15)
    print((2,3) in board)
    ```
## callable object(호출형 객체)
함수처럼 동작하는 객체.  
객체는 state를 저장할 수 있어 함수를 호출 사이에 데이터를 저장할 수 있다는 장점이 있다. \_\_call__ 매직 매서드로 구현 가능

## 파이썬 코드에서 절대 하지 말 것
1. mutable 객체를 파라미터의 기본 값으로 설정하지 말 것  
   : 함수 본문에서 파라미터 값을 수정하면 다음 객체 호출 시 처음과 다르게 동작
2. built-in type 확장하기  
   : 내장된 데이터 타입의 매서드를 수정하는 것은 그것을 기반으로 하는 다른 매서드에 적용되지 않아 의도된 바와 다르게 동작할 수 있다. 예를 들어, 리스트의 각 원소에 'A_', 'B_'와 같은 두가지 prefix를 붙이려 한다. 아래와 같이 내가 정의한 새로운 list의 \_\_getitem__를 아래와 같이 변경했다.
   ```
   class BadList(list):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even_"
        else:
            prefix = "odd_"
        return f"[{prefix}] {value}"
    ```
    그럼 list의 다른 매서드인 join에는 변경된 __getitem__을 호출하지 않고, 기존 list의 매서드를 호출하므로 문제가 발생.  
    => 해결 방법: collections의 UserList를 상속받기
    ```
    from collections import UserList
    class GoodList(UserList):
        def __getitem__(self, index):
            #(이전 예시와 동일함)
    ```
