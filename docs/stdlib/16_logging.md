# 16. logging

운영용 스크립트에서는 `print()`보다 `logging`을 사용하는 것이 좋습니다.

---

## 기본 설정

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)
logger.info("started")
```

---

## 로그 레벨

| 레벨 | 의미 |
|------|------|
| `DEBUG` | 개발 중 상세 정보 |
| `INFO` | 정상 흐름 |
| `WARNING` | 이상하지만 계속 진행 가능 |
| `ERROR` | 작업 실패 |
| `CRITICAL` | 즉시 대응 필요 |

---

## 예외 로그

```python
try:
    raise RuntimeError("failed")
except RuntimeError:
    logger.exception("job failed")
```

`logger.exception()`은 stack trace를 함께 남깁니다.

---

## 확인 포인트

- 상황에 맞는 로그 레벨을 고를 수 있는가?
- 예외를 stack trace와 함께 남길 수 있는가?
- 자동화 스크립트에서 출력과 로그를 구분할 수 있는가?
