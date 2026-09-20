class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zeroes = 1, 0
        for x in nums:
            if x == 0:
                zeroes += 1
            else:
                product *= x
        if zeroes >= 2:
            return [0]*len(nums)
        elif zeroes == 1:
            res = []
            for x in nums:
                if x == 0:
                    res.append(product)
                else:
                    res.append(0)
            return res
        else:
            return [product//x for x in nums]