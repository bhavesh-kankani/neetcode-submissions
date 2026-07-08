from itertools import accumulate
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = list(accumulate(nums))
        counter = defaultdict(int)
        ans = 0
        for x in pre_sum:
            if x == k:
                ans += 1
            if x-k in counter:
                ans += counter[x-k]
            counter[x] += 1
        return ans