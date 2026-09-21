class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]*len(height)
        maxi = 0
        for i in range(len(height)):
            if height[i] > maxi:
                left_max[i] = height[i]
                maxi = height[i]
            else:
                left_max[i] = maxi
        right_max = [0]*len(height)
        maxi = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > maxi:
                right_max[i] = height[i]
                maxi = height[i]
            else:
                right_max[i] = maxi
        ans = 0
        for i in range(len(height)):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans