from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        l = r = 0
        ans = []
        while r < len(nums):
            if r-l+1 > k:
                l += 1
                ans.append(nums[d[0]])
            while d and d[0] < l:
                d.popleft()
            while d and nums[d[-1]] <= nums[r]:
                d.pop()
            d.append(r)
            r += 1
        ans.append(nums[d[0]])

            
            
        return ans
