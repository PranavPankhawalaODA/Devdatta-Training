def most_frequent(items):
    if not items:
        return None

    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1

    return max(counts, key=lambda item: counts[item])


def main():
    while True:
        line = input("Enter items separated by spaces (blank to quit): ").strip()
        if not line:
            break

        items = line.split()
        answer = most_frequent(items)
        print("Most frequent:", answer)


if __name__ == "__main__":
    main()
