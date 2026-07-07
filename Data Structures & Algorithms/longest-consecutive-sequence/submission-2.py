#Optimal solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        final_res = 0
        res = 0
        for x in s:
            if x-1 in s:
                continue
            else:
                while x in s:
                    res += 1
                    x += 1
                final_res = max(final_res, res)
                res = 0
        final_res = max(final_res, res)
        return final_res