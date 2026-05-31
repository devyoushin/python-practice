# 18. 패키징과 pyproject.toml

작은 스크립트에서 시작하더라도 규모가 커지면 의존성, 포맷터, 테스트 설정을 한 곳에서 관리해야 합니다.

---

## pyproject.toml 예시

```toml
[project]
name = "python-practice"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
  "requests",
  "pyyaml",
]

[project.optional-dependencies]
dev = [
  "pytest",
  "ruff",
  "mypy",
]

[tool.ruff]
line-length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
```

---

## 설치

```bash
pip install -e ".[dev]"
```

`-e`는 editable install입니다. 로컬 코드를 수정하면 재설치 없이 바로 반영됩니다.

---

## 확인 포인트

- 런타임 의존성과 개발 의존성을 구분할 수 있는가?
- `pip install -e`의 의미를 설명할 수 있는가?
- 테스트/린트 설정을 프로젝트 파일에 둘 수 있는가?
