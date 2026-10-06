class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = {timestamp: value}
        else:
            self.hashmap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        timestamps = list(self.hashmap[key].keys())
        l, h = 0, len(timestamps)-1
        while l <= h:
            m = (l + h)//2
            if timestamps[m] == timestamp:
                return self.hashmap[key][timestamps[m]]
            elif timestamps[m] < timestamp:
                l = m + 1
            else:
                h = m - 1
        if h >= 0: return self.hashmap[key][timestamps[h]]
        return ""
        
        
