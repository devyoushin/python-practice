# 17. 타입 힌트

타입 힌트는 Python 코드를 읽기 쉽게 만들고, 도구가 실수를 잡도록 돕습니다.

---

## 기본 타입 힌트

```python
def normalize_name(name: str) -> str:
    return name.strip().lower()
```

---

## 컬렉션 타입

```python
def total(values: list[int]) -> int:
    return sum(values)


def find_port(ports: dict[str, int], name: str) -> int | None:
    return ports.get(name)
```

Python 3.10 이상에서는 `Optional[int]` 대신 `int | None` 표현을 쓸 수 있습니다.

---

## 타입 힌트의 한계

타입 힌트는 기본적으로 런타임 검사가 아닙니다. 실행 중 타입 검증이 필요하면 별도 로직이나 pydantic 같은 도구가 필요합니다.

---

## 확인 포인트

- 함수 인자와 반환값에 타입 힌트를 붙일 수 있는가?
- `list[str]`, `dict[str, int]`, `str | None`을 읽을 수 있는가?
- 타입 힌트가 런타임 검사가 아니라는 점을 이해하는가?
