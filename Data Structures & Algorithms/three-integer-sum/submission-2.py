class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            target = -nums[i]
            s = set()
            for j in range(i+1, len(nums)):
                third = target - nums[j]
                if third in s:
                    ans.add(tuple(sorted((nums[i], nums[j], third))))
                s.add(nums[j])
        return list(ans)