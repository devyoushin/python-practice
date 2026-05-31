# 02. 변수와 타입

Python의 변수는 값을 담는 상자가 아니라, 객체를 가리키는 이름입니다.

---

## 기본 타입

| 타입 | 예시 | 용도 |
|------|------|------|
| `int` | `10` | 정수 |
| `float` | `3.14` | 실수 |
| `str` | `"hello"` | 문자열 |
| `bool` | `True` | 참/거짓 |
| `NoneType` | `None` | 값 없음 |

```python
name = "python"
version = 3.11
enabled = True
empty = None
```

---

## 타입 확인

```python
print(type(name))
print(isinstance(name, str))
```

`type()`은 정확한 타입을 볼 때 쓰고, `isinstance()`는 상속 관계까지 고려해 검사할 때 씁니다.

---

## 타입 힌트

```python
def greet(name: str) -> str:
    return f"hello, {name}"
```

타입 힌트는 런타임 검사가 아니라 읽기 좋은 계약입니다. `mypy`, IDE, 리뷰 과정에서 실수를 줄이는 데 도움을 줍니다.

---

## 확인 포인트

- 변수와 객체의 차이를 설명할 수 있는가?
- `None`과 빈 문자열 `""`을 구분할 수 있는가?
- 함수에 타입 힌트를 붙일 수 있는가?
