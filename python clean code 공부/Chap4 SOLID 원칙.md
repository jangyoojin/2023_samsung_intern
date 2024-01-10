# S: Single Responsibility Principle
하나의 클래스는 단 하나의 역할만 수행해야 한다.  
(-> 각 클래스가 오직 하나의 매소드만 가져야 한다는 말은 아니다. 여러 매소드가 하나의 역할을 위해 필요하다면 여러 매소드를 가질 수 있다.)

# O: Open/Close Principle
모듈(클래스)이 확장에 대해서는 개방되어 있고, 수정은 폐쇄되어야 한다는 원칙  
= 새로운 코드를 추가할 수 있지만 이를 위해 기존 코드를 변경해야 한다면 잘못 짜여진 모듈이다.  

1. 수정에 폐쇄적이지 않은 코드 예시
    ```python
    # not closed to change original code
    class Event:
        def __init__(self, raw_data):
            self.raw_data = raw_data

    class UnknownEvent(Event):
        ...

    class LoginEvent(Event):
        ...

    class LogoutEvent(Event):
        ...
    # 이 클래스의 한 매서드에서 이벤트 분류 로직을 모두 관리하고 있다
    class SystemMonitor:
        def __init__(self, event_data):
            self.event_data = event_data

        def identify_event(self):
            if(
                self.event_data["before"]["session"] == 0
                and self.event_data["after"]["session"] == 1
            ):
                return LoginEvent(self.event_data)
            elif(
                self.event_data["before"]["session"] == 1
                and self.event_data["after"]["session"] == 0
            ):
                return LogoutEvent(self.event_data)

            return UnknownEvent(self.event_data)
    ```
    하나의 매서드에 모든 로직이 집중되어, LoginEvent를 판별하는 코드를 수정하면 나머지 두 이벤트 판별 코드에도 영향을 미칠 수 있다.  

2. 확장성과 폐쇄성을 가진 시스템
   ```python
   class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data
    @staticmethod
    def meets_condition(event_data: dict):
        return False

    class UnknownEvent(Event):
        ...

    class LoginEvent(Event):
        @staticmethod
        def meets_condition(event_data: dict):
            return (
                event_data["before"]["session"] == 0
                and event_data["after"]["session"] == 1
            )        

    class LogoutEvent(Event):
        @staticmethod
        def meets_condition(event_data: dict):
            return (
                event_data["before"]["session"] == 1
                and event_data["after"]["session"] == 0
            )

    class SystemMonitor:
        def __init__(self, event_data):
            self.event_data = event_data

        def identify_event(self):
            for event_cls in Event.__subclasses__():
                try:
                    if event_cls.meets_condition(self.event_data):
                        return event_cls(self.event_data)
                except KeyError:
                    continue
            return UnknownEvent(self.event_data)
    ```
    @staticmethod는 정적메소드를 의미하는 파이썬 데코레이터이다. 정적메소드는 클래스의 속성에 접근할 수 없고, self를 파라미터로 요구하지 않는다. 즉, 이 함수는 호출되어도 해당 클래스의 인스턴스에는 어떤 변화도 주지 않음을 보장한다.  
    위는 SystemMonitor가 abstract class인 Event를 이용해 각 Event의 자식 클래스들이 이벤트를 판별하도록 하고 있다.  
    이제 새로운 Event type을 추가해도 identify_event(기존 코드)는 수정하지 않고(폐쇄적 수정), 새로운 Event class와 그 안에 meets_condition 매소드를 작성하면 된다.(확장성 증대)
 
 # L: Liskov Substitution Principle
 상위 타입으로 선언된 클래스가 하위 클래스 타입으로 변환해도 상위 클래스의 동작을 그대로 수행해야 한다는 원칙.
 ```python
 class Event:
    ...
    def meets_condition(self, event_data: dict) -> bool:
        return False

class LoginEvent(Event):
    def meets_condition(self, event_data: list) -> bool:
        return bool(event_data)
 ```
위 예시는 LSP가 깨진 대표적 예시다. 상속 관계의 두 클래스에서 다루는 데이터의 형식이 달라졌다. 이 경우 클라이언트는 dict를 생각하고 LoginEvent의 meets_condition을 사용해도 다른 결과가 나올 수 있다.
