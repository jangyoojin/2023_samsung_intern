# 단원 주요 내용
- 디자인과 계약
- 에러 처리와 경고(assertion)
- 소프트웨어의 쉬운 변경을 위한 캡슐화 전략
- 개발 지침 약어
- 상속이 안 좋은 이유

## 계약에 의한 디자인
여기서 말하는 계약은 소프트웨어 구성 요소 간 통신에서 지켜야하는 규칙을 말한다. 소프트웨어에 기대하는 바를 관계자(예를 들면, 서버와 클라이언트)들이 모두 동의하는 계약을 만들고 이를 어길 시 에러 등을 발생시켜 소프트웨어를 중단하는 방식으로 개발한다.  
  
<span style="font-size:130%"> 1. 계약의 종류  <span>
   * 사전조건  
    : 함수를 실행하기 전 검사할 조건. 사전조건에 오류가 있다면 호출자의 책임이다.  
    : 함수에 전달할 데이터의 타입 등 유효성을 검사  
    ! 함수를 호출하는 쪽에서 검사할 지, 함수 내에서 검사할 지는 상관없으나 둘 중 하나에서만 조건을 검사해야 한다(중복 제거 원칙)  

   * 사후조건  
    : 함수를 실행 후 리턴 값에 대한 조건. 오류가 있다면 해당 컴포넌트(작성자)의 책임이다.  
   * 불변식
   * 부작용  

<span style="font-size:130%"> 2. 계약의 구현  <span>
  
계약 구현 시, 사전조건 검사와 사후조건 검사와 함수의 기능은 분리된 상태로 유지하는 것이 좋다. 더 작은 함수를 만들거나 데코레이터를 사용하는 것이 추천된다.

## 방어적 프로그래밍  
발생할 수 있는 모든 에러를 처리하는 것보다 불가피한 에러만 처리(에러 핸들링)하고 발생해서는 안되는 에러는 미리 차단하는 방식(assertion)을 방어적 프로그래밍이라 한다.  

<span style="font-size:130%"> 1. 에러 핸들링 <span>  

에러 핸들링의 주요 목적은 발생할 에러를 처리하고 프로그램을 계속 실행할지 프로그램을 중단할지 결정하는 것이다.  
1. 값 대체: 잘못된 값을 적절한 다른 값으로 대체해 프로그램이 잘못된 결과를 도출하지 않게 하는 방식  
   ex) 함수의 누락된 파라미터 값을 기본값으로 대체해 값이 정의되지 않는 상황을 방지  
   ```
   >>> configuration.get("dbhost", "localhost")
   'localhost'
   ```
   * 올바른 수준의 추상화 단계에서 예외 처리  
      함수는 한 가지 작업만 처리해야 하고, 예외는 오직 한 가지 일만 하는 함수의 일부여야 한다.
      ```
      class DataTransport:
          """다른 레벨에서 예외를 처리하는 객체의 예"""

          retry_threshold: int = 5
          retry_n_times: int = 3

          def __init__(self, connector):
              self._connector = connector
              self.connection = None

          def deliver_event(self, event):
              try:
                  self.connect()
                  data = event.decode()
                  self.send(data)
              except ConnectionError as e:
                  logger.info("연결 실패: %s", e)
                  raise
              except ValueError as e:
                  logger.error("%r 잘못된 데이터 포함: %s", event, e)
                  raise

          def connect(self):
              for _ in range(self.retry_n_times):
                  try:
                      self.connection = self._connector.connect()
                  except ConnectionError as e:
                      logger.info(
                          "%s: 새로운 연결 시도 %is",
                          e,
                          self.retry_threshold
                      )
                      time.sleep(self.retry_threshold)
                  else:
                      return self.connection
              raise ConnectionError(
                  f"{self.retry_n_times} 번째 재시도 연결 실패"
              )

          def send(self, data):
              return self.connection.send(data)
      ```
      
      위의 예시에서는 deliver_event에서 ConnectionError, ValueError로 두가지 에러를 처리하고 있는데, 각 에러의 발생 위치는 connect함수와 send 함수에서 발생했으므로 그 함수 내에서 처리하는 것이 바람직하다. 여러 에러를 한 함수에서 처리하기보다 한가지 역할을 하는 함수로 분리하는 것이 필요하다.  
   * Traceback 노출 금지  
      오류의 발생 위치를 보여주는 trackback을 외부 사용자가 볼 수 없게 작성해야 한다. 해커에게도 유용한 정보이기 때문이다.
   * except 블록 비워두는 것 지양
   * 원본 예외 포함: 오류 처리 과정에서 다른 오류를 발생시키고 메시지를 변경하는 경우 원본 에러가 무엇이었는지 표시

<span style="font-size:130%"> 2. assertion 활용 <span>

assertion은 불가능한 조건을 작성해 디버깅을 돕는 방법이다. 파라미터의 데이터 타입을 지정하는 등 분명한 조건이 있을 경우 사용할 수 있다.  
```
try:
   assert condition.holds(), "조건에 맞지 않음"
except AssertionError:
   alternative_procedure()
```
위 코드는 Assertion이 발생하면 이를 except 블록으로 처리하는데 assertion은 불가능한 조건이므로 소프트웨어 제어 흐름 로직에 포함시키기 보다 프로그램을 중단하는 것이 바람직하다. 
```
result = condition.holds()
assert result > 0, "에러 {0}".format(result)
```

## 관심사의 분리
소프트웨어의 쉬운 변경과 유지보수를 위한 개념이다.
- 각 객체는 오직 한 가지 일만 맡아야 한다.(높은 응집력,choesion)
- 높은 결합력(coupling)을 갖는 두 객체는 특수한 경우에만 사용될 수 있으므로 **낮은 재사용성**을 갖고, 서로 영향을 미쳐 **파급 효과**를 가지며, 서로 다른 추상화 레벨에서 에러를 처리하기 어렵다(**낮은 수준의 추상화**).

## 개발 지침 약어
- DRY: Do not Repeat Yourself
- OAOO: Once and Only Once
- YAGNI: You Ain't Gonna Need It, 처음 디자인에서 내린 결정으로 다른 제약 없이 개발 가능하다면 추가 개발 없이 진행하라(프로그램 복잡도 상승을 예방)
- KIS: Keep It Simple, 최소한의 기능을 구현하라