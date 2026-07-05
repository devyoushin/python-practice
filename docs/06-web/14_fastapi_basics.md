# 14. FastAPI 기초

FastAPI는 Python 타입 힌트를 활용해 HTTP API를 빠르게 만들 수 있는 웹 프레임워크입니다.

---

## 설치

```bash
pip install fastapi uvicorn
```

---

## 최소 예제

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
```

실행:

```bash
uvicorn app:app --reload
```

---

## 요청 파라미터

```python
@app.get("/services/{name}")
def get_service(name: str, port: int = 80) -> dict[str, object]:
    return {"name": name, "port": port}
```

`name`은 path parameter이고, `port`는 query parameter입니다.

---

## 학습 기준

처음부터 복잡한 백엔드를 만들기보다 다음 순서로 익힙니다.

- health check endpoint
- path/query parameter
- request body
- response model
- logging과 예외 처리
- pytest 기반 API 테스트

---

## 확인 포인트

- `app = FastAPI()`와 route decorator의 역할을 설명할 수 있는가?
- path parameter와 query parameter를 구분할 수 있는가?
- API 코드와 비즈니스 로직을 분리할 수 있는가?
