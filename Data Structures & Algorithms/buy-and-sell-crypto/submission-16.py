class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            max_profit = max(max_profit, prices[right] - prices[left])
            right += 1
        return max_profit

# time: O(n)
# space: O(1)