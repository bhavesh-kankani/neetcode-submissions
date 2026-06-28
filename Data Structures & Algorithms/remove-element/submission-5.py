class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        i, j = 0, len(nums)-1

        while i <= j:
            if nums[i] == val:
                while nums[j] == val and j > i:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            i += 1
        return j+1
                