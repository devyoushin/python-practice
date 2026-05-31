# 04. 함수

함수는 반복되는 로직에 이름을 붙여 재사용하는 단위입니다.

---

## 기본 형태

```python
def add(a: int, b: int) -> int:
    return a + b
```

좋은 함수는 입력, 처리, 출력이 분명합니다.

---

## 기본값 인자

```python
def greet(name: str, prefix: str = "hello") -> str:
    return f"{prefix}, {name}"
```

주의할 점은 list, dict 같은 mutable 값을 기본값으로 두지 않는 것입니다.

```python
def append_item(item: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## 함수 분리 기준

- 같은 코드가 반복된다.
- 이름을 붙이면 의도가 더 잘 보인다.
- 테스트하고 싶은 단위가 생긴다.
- 한 함수가 여러 일을 하고 있다.

---

## 확인 포인트

- 함수의 인자와 반환값에 타입 힌트를 붙일 수 있는가?
- mutable default argument 문제를 설명할 수 있는가?
- 긴 코드를 작은 함수로 나눌 수 있는가?
