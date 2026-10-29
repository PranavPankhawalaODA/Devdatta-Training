from collections import Counter, defaultdict
from collections.abc import Iterable


def top_users_per_day(
    events: Iterable[tuple[str, str]], limit: int = 5
) -> dict[str, list[tuple[str, int]]]:
    """Return each day's most active users as (user_id, event_count) pairs.

    Each input event is a (day, user_id) pair. Ties are ordered by user ID.
    """
    if limit < 0:
        raise ValueError("limit must not be negative")

    counts_by_day: dict[str, Counter[str]] = defaultdict(Counter)
    for day, user_id in events:
        counts_by_day[day][user_id] += 1

    return {
        day: sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]
        for day, counts in sorted(counts_by_day.items())
    }


def main() -> None:
    events = [
        ("2026-10-28", "alice"),
        ("2026-10-28", "bob"),
        ("2026-10-28", "alice"),
        ("2026-10-29", "bob"),
        ("2026-10-29", "carol"),
        ("2026-10-29", "bob"),
    ]
    print(top_users_per_day(events))


if __name__ == "__main__":
    main()
