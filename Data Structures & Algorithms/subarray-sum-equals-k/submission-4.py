class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        prefix = list(accumulate(nums))
        ans = 0
        for x in prefix:
            if x-k in hashmap:
                ans += hashmap[x-k]
            if x-k == 0:
                ans += 1
            hashmap[x] += 1
        return ans
            