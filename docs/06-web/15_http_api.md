# 15. HTTP API 호출

Python으로 외부 API를 호출할 때는 표준 라이브러리 `urllib`보다 `requests`를 많이 사용합니다.

---

## 설치

```bash
pip install requests
```

---

## GET 요청

```python
import requests

response = requests.get("https://api.github.com", timeout=5)
response.raise_for_status()
data = response.json()
```

`timeout`을 지정하지 않으면 네트워크 문제에서 프로그램이 오래 멈출 수 있습니다.

---

## 에러 처리

```python
try:
    response = requests.get("https://api.github.com", timeout=5)
    response.raise_for_status()
except requests.RequestException as exc:
    print(f"request failed: {exc}")
```

---

## 확인 포인트

- HTTP status code와 예외 처리를 구분할 수 있는가?
- `timeout`을 항상 지정하는 습관이 있는가?
- JSON 응답을 dict/list로 변환할 수 있는가?
