class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        sum = nums[r]
        ans = float("inf")
        while r < len(nums):
            if sum >= target:
                ans = min(ans, r-l+1)
                print(sum, l, r)
                sum -= nums[l]
                l += 1
            else:
                r += 1
                if r >= len(nums):
                    break
                sum += nums[r]
                
        if sum >= target:
            ans = min(ans, r-l)
        return ans if ans < float("inf") else 0