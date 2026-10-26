class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        current_min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < current_min:
                current_min = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - current_min)
            # current_min = min(current_min, prices[i])
        return max_profit