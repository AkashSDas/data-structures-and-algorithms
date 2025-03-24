class TimeMap:

    def __init__(self):
        self.store: dict[str, list[tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key):
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        info = self.store.get(key)

        if not info:
            return ""

        start = 0
        end = len(info) - 1
        result = ""

        while start <= end:
            mid = start + (end - start) // 2
            item = info[mid]

            if item[1] <= timestamp:
                result = item[0]
                start = mid + 1
            else:
                end = mid - 1

        return result
