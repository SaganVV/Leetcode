class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof =0 
        min_price = prices[0]
        for i, el1 in enumerate(prices[1::]):
            if el1 < min_price:
                min_price = el1
            else:
                profit = el1-min_price
                if profit > max_prof:
                    max_prof = profit
        return max_prof
