# 07. 실행 모델과 스코프

Python 코드는 위에서 아래로 실행되고, 이름을 찾을 때는 정해진 스코프 규칙을 따릅니다.

---

## 실행 흐름

Python 파일을 실행하면 최상위 코드가 순서대로 실행됩니다.

```python
print("first")


def hello() -> None:
    print("hello")


print("second")
hello()
```

함수 정의는 함수를 실행하는 것이 아니라, 함수 객체를 이름에 바인딩하는 작업입니다.

---

## `__name__ == "__main__"`

```python
def main() -> None:
    print("run")


if __name__ == "__main__":
    main()
```

파일을 직접 실행할 때만 `main()`이 호출됩니다. 다른 파일에서 import할 때 실행 부작용을 줄이는 기본 패턴입니다.

---

## 스코프

Python은 이름을 찾을 때 LEGB 순서를 따릅니다.

| 순서 | 의미 |
|------|------|
| Local | 현재 함수 내부 |
| Enclosing | 바깥 함수 |
| Global | 모듈 전역 |
| Built-in | 내장 이름 |

---

## 확인 포인트

- import할 때 실행되면 안 되는 코드를 `main()` 아래로 분리할 수 있는가?
- Local과 Global 스코프의 차이를 설명할 수 있는가?
- 같은 이름을 여러 스코프에 둘 때 어떤 값이 선택되는지 예상할 수 있는가?
