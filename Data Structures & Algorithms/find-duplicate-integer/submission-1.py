class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using hashset
        hashset = set()
        for num in nums:
            if num in hashset:
                return num
            hashset.add(num)
