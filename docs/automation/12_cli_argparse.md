# 12. CLI와 argparse

운영 자동화 스크립트는 명령행 인자를 받아 동작해야 재사용하기 쉽습니다.

---

## 기본 구조

```python
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("--upper", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    message = f"hello, {args.name}"
    if args.upper:
        message = message.upper()
    print(message)


if __name__ == "__main__":
    main()
```

---

## 실행

```bash
python script.py python
python script.py python --upper
```

---

## 설계 기준

- `parse_args()`와 `main()`을 분리합니다.
- 실제 처리 로직은 별도 함수로 둡니다.
- `print()`는 결과 출력에만 사용하고, 운영 로그는 `logging`을 사용합니다.
- 종료 코드는 성공 `0`, 실패 `1` 이상을 사용합니다.

---

## 확인 포인트

- 필수 인자와 선택 인자를 구분할 수 있는가?
- `--flag` 옵션을 만들 수 있는가?
- CLI 파싱과 실제 로직을 분리할 수 있는가?
