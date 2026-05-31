import json
from pathlib import Path


def write_service(path: Path, service: dict[str, object]) -> None:
    path.write_text(json.dumps(service, ensure_ascii=False, indent=2), encoding="utf-8")


def read_service(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    path = Path("/tmp/python-practice-service.json")
    write_service(path, {"name": "nginx", "port": 80})
    print(read_service(path))


if __name__ == "__main__":
    main()
