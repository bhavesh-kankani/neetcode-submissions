class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        mid = (low + high)//2
        while low < high:
            if nums[low] < nums[high]:
                return nums[low]
            mid = (low + high)//2
            if nums[low] <= nums[mid]:
                low = mid + 1
            elif nums[low] > nums[mid]:
                high = mid
        return nums[high]