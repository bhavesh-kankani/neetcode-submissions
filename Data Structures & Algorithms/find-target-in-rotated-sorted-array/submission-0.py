class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        min_element = low
        low, high = 0, len(nums)-1
        def binary_search(nums, low, high):
            while low <= high:
                mid = (low + high)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        
        left = binary_search(nums, low, min_element)
        if left != -1: return left
        right = binary_search(nums, min_element, high)
        if right != -1: return right
        return -1
        