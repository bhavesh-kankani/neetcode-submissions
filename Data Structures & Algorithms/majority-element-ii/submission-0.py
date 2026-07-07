class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        for x in nums:
            counter[x] += 1
        return [x for x in counter if counter[x] > len(nums)//3]