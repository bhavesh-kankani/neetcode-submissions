class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for x in nums:
            if x != 0:
                product *= x
            else:
                zero_count += 1
        output = [0 for _ in range(len(nums))]
        if zero_count >= 2:
            return output
        
        for i in range(len(nums)):
            if nums[i] == 0:
                output[i] = product
            else:
                if zero_count == 1:
                    output[i] = 0
                else:
                    output[i] = product//nums[i]
        return output