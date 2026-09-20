class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        k = l
        while k <= r:
            while l < r and nums[l] == 0:
                l += 1
            while r > l and nums[r] == 2:
                r -= 1
            if nums[k] == 2:
                nums[r], nums[k] = nums[k], nums[r]
                r -= 1
            elif nums[k] == 0 and k > l:
                nums[k], nums[l] = nums[l], nums[k]
                l += 1
            else:
                k += 1
        

        