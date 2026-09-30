class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        ans = high

        while low <= high:
            mid = (low + high)//2
            total_days = 1
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight > mid:
                    total_days += 1
                    curr_weight = 0
                curr_weight += weight
            if total_days <= days:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans