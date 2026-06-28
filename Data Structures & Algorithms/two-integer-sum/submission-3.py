class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seta = {}
        for i in range(len(nums)):
            seta[nums[i]] = i
        for i in range(len(nums)):
            j = target - nums[i]
            if j in seta and i != seta[j]:
                return [i, seta[j]]