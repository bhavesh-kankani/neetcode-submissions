import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high
        while low <= high:
            mid = (low + high)//2
            s = 0
            for bana in piles:
                s += math.ceil(bana/mid)
            if s <= h:
                high = mid - 1
                ans = min(ans, mid)
            else:
                low = mid + 1
        return ans
