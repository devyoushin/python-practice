# 05. 컬렉션 타입

Python에서 데이터를 묶어 다룰 때는 `list`, `tuple`, `dict`, `set`을 주로 사용합니다.

---

## 타입별 사용 기준

| 타입 | 특징 | 적합한 경우 |
|------|------|-------------|
| `list` | 순서 있음, 변경 가능 | 순서대로 처리할 목록 |
| `tuple` | 순서 있음, 변경 불가 | 고정된 값 묶음 |
| `dict` | key-value | 이름으로 값을 찾을 때 |
| `set` | 중복 없음 | 중복 제거, 포함 여부 검사 |

---

## 자주 쓰는 패턴

```python
names = ["nginx", "terraform", "ansible"]
upper_names = [name.upper() for name in names]
```

```python
ports = {"http": 80, "https": 443}
print(ports.get("http", 8080))
```

```python
unique_tags = set(["prod", "dev", "prod"])
print(unique_tags)
```

---

## 선택 기준

자료구조를 고를 때는 "어떻게 조회하고 변경할 것인가"를 먼저 봅니다.

- 순회가 중심이면 `list`
- key로 빠르게 찾으면 `dict`
- 중복 제거가 핵심이면 `set`
- 변경되면 안 되는 묶음이면 `tuple`

---

## 확인 포인트

- list comprehension을 읽고 쓸 수 있는가?
- `dict.get()`과 `dict["key"]`의 차이를 설명할 수 있는가?
- 중복 제거에 `set`을 사용할 수 있는가?
