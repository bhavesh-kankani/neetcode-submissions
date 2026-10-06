class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        l, h = 0, len(self.hashmap[key])-1
        while l <= h:
            m = (l + h)//2
            if self.hashmap[key][m][0] == timestamp:
                return self.hashmap[key][m][1]
            elif self.hashmap[key][m][0] < timestamp:
                l = m + 1
            else:
                h = m - 1
        if h >= 0: return self.hashmap[key][h][1]
        return ""
        
        
