from collections import deque
from threading import Lock
from time import monotonic
from typing import Callable


class PerUserRateLimiter:
    """Allow at most ``max_requests`` per user in a rolling time window."""

    def __init__(
        self,
        max_requests: int,
        window_seconds: float,
        clock: Callable[[], float] = monotonic,
    ) -> None:
        if max_requests <= 0:
            raise ValueError("max_requests must be greater than zero")
        if window_seconds <= 0:
            raise ValueError("window_seconds must be greater than zero")

        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._clock = clock
        self._requests: dict[str, deque[float]] = {}
        self._lock = Lock()

    def allow_request(self, user_id: str) -> bool:
        """Return whether this user's request is within the configured limit."""
        with self._lock:
            now = self._clock()
            cutoff = now - self.window_seconds
            timestamps = self._requests.setdefault(user_id, deque())
            while timestamps and timestamps[0] <= cutoff:
                timestamps.popleft()

            if len(timestamps) >= self.max_requests:
                return False

            timestamps.append(now)
            return True


def main() -> None:
    limiter = PerUserRateLimiter(max_requests=2, window_seconds=60)
    print(limiter.allow_request("alice"))  # True
    print(limiter.allow_request("alice"))  # True
    print(limiter.allow_request("alice"))  # False
    print(limiter.allow_request("bob"))  # True; limits are per user


if __name__ == "__main__":
    main()
