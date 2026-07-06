# Using sort to solve
import sys
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        last_min = -sys.maxsize
        final_res = 0
        res = 0
        for x in nums:
            if last_min == x-1:
                res += 1
            elif last_min == x:
                continue
            else:
                final_res = max(res, final_res)
                res = 1
            last_min = x
        final_res = max(res, final_res)
        return final_res