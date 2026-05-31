import argparse


def build_message(name: str, upper: bool = False) -> str:
    message = f"hello, {name}"
    return message.upper() if upper else message


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="small greeting CLI")
    parser.add_argument("name")
    parser.add_argument("--upper", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(build_message(args.name, args.upper))


if __name__ == "__main__":
    main()
