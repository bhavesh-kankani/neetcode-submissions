class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        # right smaller at every index
        right = [n]*n
        stack = [-1]
        for idx in range(n-1, -1, -1):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[idx]:
                stack.pop()
            if stack[-1] != -1 and heights[stack[-1]] < heights[idx]:
                right[idx] = stack[-1]
            stack.append(idx)
        
        # left smaller at every index
        left = [-1]*n
        stack = [-1]
        for idx in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[idx]:
                stack.pop()
            if stack[-1] != -1 and heights[stack[-1]] < heights[idx]:
                left[idx] = stack[-1]
            stack.append(idx)
        ans = 0
        for idx in range(n):
            ans = max(ans, heights[idx] * (right[idx]-1 - left[idx]) )
        return ans
