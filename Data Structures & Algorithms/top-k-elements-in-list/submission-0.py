class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]] += 1
        tmp = []
        for x in hashmap:
            tmp.append((x, hashmap[x]))
        tmp.sort(key = lambda x: x[1], reverse = True)
        return [tmp[i][0] for i in range(k)]