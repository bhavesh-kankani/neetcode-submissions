class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)
        ans = high
        while low <= high:
            mid = (low + high)//2
            summ = nums[0]
            partitions = 1
            for i in range(1, len(nums)):
                if summ + nums[i] <= mid:
                    summ += nums[i]
                else:
                    partitions += 1
                    summ = nums[i]
            if partitions > k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
            