from collections.abc import Iterable


def reconcile_ids(
    first_ids: Iterable[str], second_ids: Iterable[str]
) -> dict[str, list[str]]:
    """Split IDs into shared and list-specific groups in O(n + m) time.

    Results preserve the first occurrence order and contain each ID once.
    """
    first = list(dict.fromkeys(first_ids))
    second = list(dict.fromkeys(second_ids))
    first_set = set(first)
    second_set = set(second)

    return {
        "in_both": [item for item in first if item in second_set],
        "only_in_first": [item for item in first if item not in second_set],
        "only_in_second": [item for item in second if item not in first_set],
    }


def main() -> None:
    old_ids = ["u1", "u2", "u3", "u2"]
    new_ids = ["u2", "u3", "u4"]
    print(reconcile_ids(old_ids, new_ids))


if __name__ == "__main__":
    main()
