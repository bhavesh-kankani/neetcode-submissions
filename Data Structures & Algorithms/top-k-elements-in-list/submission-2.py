class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for x in nums:
            count[x] += 1
        max_frequency = max(count.values())
        buckets = [[] for _ in range(max_frequency+1)]
        for x in count:
            buckets[count[x]].append(x)
        res = []
        for i in range(max_frequency, 0, -1):
            if k == 0:
                return res
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                k -= 1
        return res