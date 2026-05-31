def unique_sorted(items: list[str]) -> list[str]:
    return sorted(set(items))


def count_by_name(items: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def main() -> None:
    services = ["nginx", "terraform", "ansible", "nginx"]
    print(unique_sorted(services))
    print(count_by_name(services))


if __name__ == "__main__":
    main()
