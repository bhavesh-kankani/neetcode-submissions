class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
        return list(res)