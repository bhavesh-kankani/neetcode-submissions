class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        l, r = 0, n-1
        left = right = 0
        while l < r:
            left = max(left, height[l])
            right = max(right, height[r])
            if left < right:
                ans += (left - height[l])
                l += 1
            else:
                ans += (right - height[r])
                r -= 1
        return ans