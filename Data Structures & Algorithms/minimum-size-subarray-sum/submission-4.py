import sys
from itertools import accumulate
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        prefix = list(accumulate(nums))
        ans = sys.maxsize
        while r < len(nums) and prefix[r] < target:
            r += 1
        if r < len(nums) and prefix[r] >= target:
            ans = min(ans, r+1)
        print(ans)
        while r < len(nums) and l < len(nums):
            if prefix[r] - prefix[l] >= target:
                ans = min(ans, r-l)
                l += 1
            else:
                r += 1
        if ans < sys.maxsize:
            return ans
        else:
            return 0