# 09. 클래스와 dataclass

클래스는 데이터와 동작을 함께 묶는 방법입니다.

---

## 기본 클래스

```python
class Service:
    def __init__(self, name: str, port: int) -> None:
        self.name = name
        self.port = port

    def endpoint(self) -> str:
        return f"{self.name}:{self.port}"
```

```python
service = Service("nginx", 80)
print(service.endpoint())
```

---

## dataclass

값을 담는 객체가 필요하다면 `dataclass`가 더 간결합니다.

```python
from dataclasses import dataclass


@dataclass
class Service:
    name: str
    port: int

    def endpoint(self) -> str:
        return f"{self.name}:{self.port}"
```

---

## 언제 클래스를 쓰는가

- 같은 데이터 묶음이 여러 함수에 반복해서 전달된다.
- 데이터와 그 데이터를 다루는 동작이 강하게 연결되어 있다.
- 상태를 가진 객체가 필요하다.

함수 몇 개로 충분한 문제에 클래스를 먼저 도입할 필요는 없습니다.

---

## 확인 포인트

- `self`의 의미를 설명할 수 있는가?
- 일반 클래스와 dataclass의 차이를 이해하는가?
- 함수형 구조와 클래스 구조 중 어느 쪽이 단순한지 판단할 수 있는가?
