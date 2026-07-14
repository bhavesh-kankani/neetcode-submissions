import sys
from itertools import accumulate
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        current_sum = 0
        min_len = sys.maxsize
        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum >= target:
                min_len = min(min_len, r-l+1)
                current_sum -= nums[l]
                l += 1
        return min_len if min_len < sys.maxsize else 0