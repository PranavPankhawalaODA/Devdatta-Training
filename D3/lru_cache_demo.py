class _Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.previous: _Node | None = None
        self.next: _Node | None = None


class LRUCache:
    """Least-recently-used cache with O(1) get and put operations."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero")

        self.capacity = capacity
        self._nodes: dict[int, _Node] = {}
        self._most_recent = _Node(0, 0)
        self._least_recent = _Node(0, 0)
        self._most_recent.next = self._least_recent
        self._least_recent.previous = self._most_recent

    def _remove(self, node: _Node) -> None:
        previous = node.previous
        following = node.next
        if previous is None or following is None:
            raise RuntimeError("Cannot remove a detached cache node")
        previous.next = following
        following.previous = previous

    def _add_as_most_recent(self, node: _Node) -> None:
        following = self._most_recent.next
        if following is None:
            raise RuntimeError("Cache list is not initialized")
        node.previous = self._most_recent
        node.next = following
        self._most_recent.next = node
        following.previous = node

    def get(self, key: int) -> int | None:
        node = self._nodes.get(key)
        if node is None:
            return None

        self._remove(node)
        self._add_as_most_recent(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self._nodes.get(key)
        if node is not None:
            node.value = value
            self._remove(node)
            self._add_as_most_recent(node)
            return

        node = _Node(key, value)
        self._nodes[key] = node
        self._add_as_most_recent(node)

        if len(self._nodes) > self.capacity:
            least_recent = self._least_recent.previous
            if least_recent is None or least_recent is self._most_recent:
                raise RuntimeError("Cache list is not initialized")
            self._remove(least_recent)
            del self._nodes[least_recent.key]

    def items_most_recent_first(self) -> list[tuple[int, int]]:
        items: list[tuple[int, int]] = []
        node = self._most_recent.next
        while node is not None and node is not self._least_recent:
            items.append((node.key, node.value))
            node = node.next
        return items


def main() -> None:
    cache = LRUCache(capacity=2)
    cache.put(1, 10)
    cache.put(2, 20)
    print("After inserting 1 and 2 (MRU -> LRU):", cache.items_most_recent_first())

    print("Get key 1:", cache.get(1))
    print("After accessing 1:", cache.items_most_recent_first())

    cache.put(3, 30)
    print("After inserting 3 (key 2 is evicted):", cache.items_most_recent_first())
    print("Get evicted key 2:", cache.get(2))


if __name__ == "__main__":
    main()
