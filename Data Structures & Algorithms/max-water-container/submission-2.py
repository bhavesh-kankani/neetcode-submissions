import sys
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        final_ans = 0
        while i < j:
            ans = (j-i) * min(heights[i], heights[j])
            final_ans = max(final_ans, ans)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return final_ans
