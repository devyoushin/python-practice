# 03. 조건문과 반복문

조건문과 반복문은 코드의 실행 흐름을 제어합니다.

---

## 조건문

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

Python은 중괄호 대신 들여쓰기로 블록을 구분합니다.

---

## truthy / falsy

다음 값들은 조건문에서 거짓으로 취급됩니다.

```python
False
None
0
""
[]
{}
set()
```

명시적으로 비교해야 의미가 선명할 때는 `if items:`보다 `if len(items) > 0:` 같은 표현이 더 나을 수 있습니다.

---

## 반복문

```python
for item in ["nginx", "terraform", "ansible"]:
    print(item)

for index, item in enumerate(["a", "b", "c"], start=1):
    print(index, item)
```

숫자 범위 반복은 `range()`를 씁니다.

```python
for number in range(1, 6):
    print(number)
```

---

## 확인 포인트

- `if`, `elif`, `else`의 실행 순서를 설명할 수 있는가?
- 리스트를 순회하면서 index와 값을 같이 꺼낼 수 있는가?
- truthy/falsy 값 때문에 생길 수 있는 버그를 예상할 수 있는가?
