import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    examples = sorted((root / "examples").glob("*.py"))
    example_args = {
        "05_argparse_cli.py": ["python", "--upper"],
    }

    for example in examples:
        print(f"==> {example.name}")
        subprocess.run(
            [sys.executable, str(example), *example_args.get(example.name, [])],
            check=True,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
