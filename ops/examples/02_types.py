def describe(value: object) -> str:
    return f"value={value!r}, type={type(value).__name__}"


def main() -> None:
    values = ["python", 3.11, True, None]
    for value in values:
        print(describe(value))


if __name__ == "__main__":
    main()
