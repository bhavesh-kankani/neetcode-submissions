class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1], [1]
        for x in nums:
            prefix.append(x*prefix[-1])
        for i in range(len(nums)-1, -1, -1):
            suffix.append(nums[i]*suffix[-1])
        print(prefix, suffix)
        output = []
        for i in range(len(nums)): 
            if i == 0:
                output.append(suffix[len(nums)-1])
            elif i == len(nums)-1:
                output.append(prefix[i])
            else:
                output.append(prefix[i]*suffix[len(nums)-1-i])
        return output
