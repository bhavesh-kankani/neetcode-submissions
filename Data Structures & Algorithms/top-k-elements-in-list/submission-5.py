class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for x in nums:
            hashmap[x] += 1
        maxi = max(hashmap.values())
        array = [[] for _ in range(maxi+1)]
        for x in hashmap:
            array[hashmap[x]].append(x)
        res = []
        i = maxi
        while k > 0:
            res.extend(array[i])
            k -= len(array[i])
            i -= 1
        return res

