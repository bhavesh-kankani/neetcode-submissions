class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for a in range(len(nums)):
            tar = target - nums[a]
            for b in range(a+1, len(nums)):
                c, d = b+1, len(nums)-1
                while c < d:
                    curr_sum = nums[b] + nums[c] + nums[d]
                    if curr_sum > tar:
                        d -= 1
                    elif curr_sum < tar:
                        c += 1
                    else:
                        ans.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1
        return list(ans)