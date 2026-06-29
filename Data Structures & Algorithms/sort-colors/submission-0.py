class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z, o, t = 0, 0, 0
        for x in nums:
            if x == 1:
                o += 1
            elif x == 2:
                t += 1
            elif x == 0:
                z += 1
        k = 0
        for i in range(z):
            nums[k] = 0
            k += 1
        for i in range(o):
            nums[k] = 1
            k += 1
        for i in range(t):
            nums[k] = 2
            k += 1
            