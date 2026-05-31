# 06. 모듈과 패키지

Python 파일 하나는 모듈이고, 여러 모듈을 디렉토리로 묶으면 패키지가 됩니다.

---

## 모듈

```text
calculator.py
```

```python
def add(a: int, b: int) -> int:
    return a + b
```

다른 파일에서 가져와 사용할 수 있습니다.

```python
from calculator import add

print(add(1, 2))
```

---

## 패키지

```text
myapp/
├── __init__.py
├── calculator.py
└── main.py
```

`__init__.py`는 해당 디렉토리를 패키지로 다룬다는 표시입니다. 최신 Python에서는 없어도 namespace package로 동작할 수 있지만, 학습 단계에서는 명시적으로 두는 편이 이해하기 쉽습니다.

---

## import 기준

- 표준 라이브러리
- 외부 패키지
- 내부 모듈

이 순서로 import를 정리하면 읽기 쉽습니다.

```python
import json
from pathlib import Path

import requests

from myapp.calculator import add
```

---

## 확인 포인트

- 모듈과 패키지의 차이를 설명할 수 있는가?
- 상대 import와 절대 import의 차이를 이해하는가?
- `python file.py`와 `python -m package.module`의 차이를 확인했는가?
