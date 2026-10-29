def merge_sorted(a: list[float], b: list[float]) -> list[float]:
    i = j = 0
    merged: list[float] = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


def is_sorted(values: list[float]) -> bool:
    return all(values[k] <= values[k + 1] for k in range(len(values) - 1))


def parse_numbers(text: str) -> list[float]:
    nums = [float(x) for x in text.split()]
    return [int(n) if n.is_integer() else n for n in nums]

def read_sorted_list(prompt: str) -> list[float]:
    while True:
        try:
            values = parse_numbers(input(prompt))
        except ValueError:
            print("Please enter numbers only, separated by spaces.")
            continue
        if not is_sorted(values):
            print("That list is not sorted in ascending order. Try again.")
            continue
        return values

def main() -> None:
    first = read_sorted_list("First sorted list: ")
    second = read_sorted_list("Second sorted list: ")
    print("Merged:", merge_sorted(first, second))

if __name__ == "__main__":
    main()
 