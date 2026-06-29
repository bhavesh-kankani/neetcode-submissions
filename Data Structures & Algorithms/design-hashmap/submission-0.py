class MyHashMap:

    def __init__(self):
        self.hash = [[]]*10

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            for i in range(len(self.hash[key%10])):
                if self.hash[key%10][i][0] == key:
                    self.hash[key%10][i][1] = value
                    break
        else:
            self.hash[key%10].append([key, value])

    def get(self, key: int) -> int:
        for x in self.hash[key%10]:
            if x[0] == key:
                return x[1]
        return -1

    def remove(self, key: int) -> None:
        value = self.get(key)
        if value != -1:
            self.hash[key%10].remove([key, value])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)