class RandomizedSet:

    def __init__(self):
        self.dictionary = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dictionary:
            return False
        self.dictionary[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dictionary:
            position = self.dictionary[val]
            last_num = self.list[-1]
            self.list[position] = last_num
            self.list.pop()
            self.dictionary[last_num] = position
            del self.dictionary[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()