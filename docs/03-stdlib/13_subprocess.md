# 13. subprocess

Python에서 외부 명령을 실행할 때는 `subprocess` 모듈을 사용합니다.

---

## 기본 실행

```python
import subprocess

result = subprocess.run(
    ["python3", "--version"],
    check=True,
    text=True,
    capture_output=True,
)

print(result.stdout)
```

---

## shell=True 주의

가능하면 문자열 명령과 `shell=True`를 피하고, 인자 리스트를 넘깁니다.

```python
subprocess.run(["ls", "-la"], check=True)
```

사용자 입력이 섞인 문자열을 shell로 실행하면 명령 주입 취약점이 생길 수 있습니다.

---

## 실패 처리

```python
try:
    subprocess.run(["false"], check=True)
except subprocess.CalledProcessError as exc:
    print(f"command failed: {exc.returncode}")
```

---

## 확인 포인트

- 외부 명령의 stdout/stderr를 캡처할 수 있는가?
- `check=True`의 의미를 설명할 수 있는가?
- `shell=True`가 위험한 이유를 설명할 수 있는가?
