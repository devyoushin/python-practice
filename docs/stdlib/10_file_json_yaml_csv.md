# 10. 파일, JSON, YAML, CSV

운영 자동화에서 Python은 외부 파일을 읽고 변환하는 데 자주 사용됩니다.

---

## pathlib

```python
from pathlib import Path

path = Path("sample.txt")
path.write_text("hello\n", encoding="utf-8")
content = path.read_text(encoding="utf-8")
```

문자열 경로 조작보다 `pathlib.Path`를 쓰면 OS별 경로 차이를 줄일 수 있습니다.

---

## JSON

```python
import json

data = {"service": "nginx", "port": 80}
text = json.dumps(data, ensure_ascii=False, indent=2)
loaded = json.loads(text)
```

---

## YAML

YAML은 표준 라이브러리에 포함되어 있지 않으므로 보통 `PyYAML`을 설치합니다.

```bash
pip install pyyaml
```

```python
import yaml

data = yaml.safe_load("service: nginx\nport: 80\n")
```

`yaml.load()`는 보안상 위험할 수 있으므로 학습과 실무 모두 `safe_load()`를 기본으로 사용합니다.

---

## CSV

```python
import csv

rows = [
    {"service": "nginx", "port": 80},
    {"service": "https", "port": 443},
]

with open("ports.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["service", "port"])
    writer.writeheader()
    writer.writerows(rows)
```

---

## 확인 포인트

- `Path`로 파일을 읽고 쓸 수 있는가?
- JSON과 YAML의 차이를 설명할 수 있는가?
- CSV를 dict 형태로 읽고 쓸 수 있는가?
