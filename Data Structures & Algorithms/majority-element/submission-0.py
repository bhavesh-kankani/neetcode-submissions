class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for x in nums:
            d[x] += 1
        ans = nums[0]
        count = 1
        for x in d:
            if d[x] > count:
                ans = x
                count = d[x]
        return ans