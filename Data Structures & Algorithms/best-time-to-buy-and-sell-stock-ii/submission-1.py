import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prices.append(-1)
        prev, buy = prices[0], prices[0]
        for curr in prices:
            if curr < prev:
                if prev - buy > 0:
                    profit += prev - buy
                buy = curr
            prev = curr
        return profit