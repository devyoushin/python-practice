# python-practice

Python을 기초 문법부터 자동화, 테스트, 운영 스크립트 작성까지 공부하기 위한 개인 학습 공간입니다.

## 어디서 시작할까

- 문서 지도: `docs/README.md`
- 첫 문서: `docs/install/01_environment.md`
- 실습 예제: `ops/examples/`
- 운영 보조 자료: `ops/README.md`
- AI 작업 지침: `CLAUDE.md`

## 구조

| 경로 | 내용 |
|------|------|
| `docs/` | 설치, 언어 기초, 표준 라이브러리, 도구, 자동화, 웹 문서 |
| `ops/` | 실행 예제, 학습 기록, 보조 도구 |
| `CLAUDE.md` | 이 레포에서 AI가 참고할 작업 지침 |

## 빠른 명령

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python ops/examples/01_hello.py
```

## 학습 방향

이 저장소는 단순 문법 암기보다 "작게 만들고 실행하고 테스트하는 방식"을 우선합니다.

- 문서는 핵심 개념과 판단 기준을 정리합니다.
- 예제는 직접 실행 가능한 코드로 둡니다.
- 반복해서 쓰는 패턴은 `ops/tools/`에 도구 형태로 분리합니다.
- 나중에 Nginx 로그 분석, Terraform/Ansible 보조 스크립트 같은 DevOps 자동화로 확장합니다.

## Learning Path

```
1. Environment      -> docs/install/
   └── Python, venv, pip 실행 환경

2. Language Basics  -> docs/language/
   ├── 변수, 타입, 조건문, 반복문, 함수
   └── 컬렉션, 스코프, 예외, 클래스

3. Standard Library -> docs/stdlib/
   ├── 모듈/패키지, 파일, JSON/YAML/CSV
   └── subprocess, logging

4. Tooling          -> docs/tooling/
   ├── pytest, typing, packaging
   └── pyproject.toml 기반 프로젝트 관리

5. Practical Topics -> docs/automation/ + docs/web/
   ├── argparse CLI 자동화
   └── HTTP API, FastAPI 기초
```
