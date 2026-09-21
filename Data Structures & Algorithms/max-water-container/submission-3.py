class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        left_max, right_max = 0, 0
        final_res = 0
        while l < r:
            base = r-l

            left_max = max(left_max, heights[l])
            right_max = max(right_max, heights[r])
            
            if heights[l] < heights[r]:
                res = base * heights[l]
                l += 1
            else:
                res = base * heights[r]
                r -= 1
            final_res = max(final_res, res)
        return final_res

