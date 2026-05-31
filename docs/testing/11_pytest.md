# 11. pytest

테스트는 코드가 의도대로 동작하는지 자동으로 확인하는 장치입니다.

---

## 설치

```bash
pip install pytest
```

---

## 기본 테스트

```python
def add(a: int, b: int) -> int:
    return a + b


def test_add() -> None:
    assert add(1, 2) == 3
```

테스트 파일은 보통 `test_*.py` 형식으로 둡니다.

```bash
pytest
pytest -q
```

---

## 예외 테스트

```python
import pytest


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError):
        divide(1, 0)
```

---

## 테스트하기 쉬운 코드

- 입출력을 함수 바깥으로 밀어낸다.
- 순수 함수로 계산 로직을 분리한다.
- 현재 시간, 파일 시스템, 네트워크는 주입하거나 mocking한다.

---

## 확인 포인트

- `assert`로 기대값을 검증할 수 있는가?
- 예외 발생을 테스트할 수 있는가?
- 파일 읽기/쓰기와 계산 로직을 분리할 수 있는가?
