class RandomizedSet:

    def __init__(self):
        self.val = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        self.val[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        last_val = self.values[-1]
        id_to_remove = self.val[val]
        self.values[id_to_remove] = last_val
        self.val[last_val] = id_to_remove
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()