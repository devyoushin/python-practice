# Python Deep Dive 학습 프로젝트

Python 3.11+ 기준의 Python 학습 문서와 실습 코드 모음입니다.

## 프로젝트 구조

```
.
├── README.md          # 프로젝트 소개 및 시작점
├── CLAUDE.md          # 이 파일
├── docs/
│   ├── README.md      # 문서 구조 안내
│   ├── install/       # Python 설치, venv, pip
│   ├── basics/        # 기본 문법
│   ├── runtime/       # 실행 모델, 스코프, 예외
│   ├── data/          # 자료구조, 문자열, 날짜
│   ├── oop/           # 클래스, dataclass
│   ├── modules/       # 모듈, 패키지, import
│   ├── io/            # 파일, JSON, YAML, CSV
│   ├── testing/       # pytest, mocking, coverage
│   ├── automation/    # CLI, subprocess, 운영 자동화
│   ├── web/           # HTTP client, FastAPI 기초
│   └── operations/    # logging, typing, packaging, 성능
└── ops/
    ├── examples/      # 실행 가능한 예제 코드
    ├── memory/        # 학습 진행 기록
    └── tools/         # 실습용 보조 도구
```

## 문서 규칙

- 문서 파일명은 `{번호}_{주제}.md` 형식으로 작성합니다.
- 모든 개념 설명 문서는 `docs/` 아래 주제별 폴더에 둡니다.
- 실행 가능한 Python 코드는 `ops/examples/` 또는 `ops/tools/`에 둡니다.
- 한국어로 작성합니다.
- 예제 코드는 가능하면 함수로 나누고, 테스트 가능한 형태를 유지합니다.
