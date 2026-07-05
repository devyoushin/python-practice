# 01. Python 실행 환경

Python 학습은 전역 환경을 직접 오염시키지 않고, 프로젝트별 가상환경을 만들어 시작하는 것이 좋습니다.

---

## 설치 확인

```bash
python3 --version
which python3
```

Python 3.11 이상을 기준으로 공부합니다. macOS에서는 보통 Homebrew Python을 쓰거나 `pyenv`로 버전을 고정합니다.

```bash
brew install python
python3 --version
```

---

## 가상환경 만들기

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

가상환경이 활성화되면 `python`, `pip`가 `.venv` 아래의 실행 파일을 가리킵니다.

```bash
which python
which pip
```

---

## 패키지 설치 흐름

```bash
pip install requests
pip freeze
pip freeze > requirements.txt
pip install -r requirements.txt
```

초기 학습에서는 `requirements.txt`로도 충분합니다. 프로젝트 패키징까지 다룰 때 `pyproject.toml`을 사용합니다.

---

## 확인 포인트

- `python3`와 `python`이 어떤 실행 파일을 가리키는지 확인할 수 있는가?
- 가상환경을 만들고 활성화/비활성화할 수 있는가?
- 패키지를 설치하고 목록을 파일로 남길 수 있는가?
