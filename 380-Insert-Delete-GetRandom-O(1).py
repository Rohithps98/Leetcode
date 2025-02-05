import random
class RandomizedSet:

    def __init__(self):
        self.val = {}
        self.value = []

    def insert(self, val: int) -> bool:
        if val in self.val:
            return False
        self.val[val] = len(self.value)
        self.value.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val:
            return False
        last_val = self.value[-1]
        itr = self.val[val]
        self.value[itr] = last_val
        self.val[last_val] = itr
        self.value.pop()
        del self.val[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.value)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()