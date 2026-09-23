class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        l = r = 0
        ans = []
        while r < len(nums):
            if r-l+1 > k:
                l += 1
            while d and nums[r] > nums[d[-1]]:
                d.pop()
            d.append(r)
            r += 1
            while d[0] < l:
                d.popleft()
            if r-l >= k:
                ans.append(nums[d[0]])
        return ans