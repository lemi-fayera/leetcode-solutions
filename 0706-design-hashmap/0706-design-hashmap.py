class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        # Check if key already exists
        for pair in self.map[index]:
            if pair[0] == key:
                pair[1] = value
                return

        # Key doesn't exist, so add it
        self.map[index].append([key, value])

    def get(self, key: int) -> int:
        index = key % self.size

        for pair in self.map[index]:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key: int) -> None:
        index = key % self.size

        for i, pair in enumerate(self.map[index]):
            if pair[0] == key:
                self.map[index].pop(i)
                return
