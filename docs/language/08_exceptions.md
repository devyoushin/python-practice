# 08. 예외 처리

예외 처리는 실패할 수 있는 코드를 명시적으로 다루는 방법입니다.

---

## 기본 형태

```python
try:
    number = int("10")
except ValueError as exc:
    print(f"숫자로 변환할 수 없습니다: {exc}")
else:
    print(number)
finally:
    print("항상 실행")
```

---

## 예외를 잡는 기준

너무 넓게 `except Exception`으로 잡으면 실제 버그가 숨을 수 있습니다. 가능한 구체적인 예외를 잡습니다.

```python
try:
    content = path.read_text()
except FileNotFoundError:
    content = ""
```

---

## 직접 예외 발생

```python
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
```

---

## 확인 포인트

- 실패 가능성이 있는 지점을 찾을 수 있는가?
- 어떤 예외를 잡아야 하는지 판단할 수 있는가?
- 예외 메시지를 운영자가 이해할 수 있게 작성할 수 있는가?
