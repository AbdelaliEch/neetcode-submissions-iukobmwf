class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        left = max_profit = 0
        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
            if prices[right] < prices[left]:
                left = right
        return max_profit



# we are looking for max profit
# so we are looking for lowest buying price and highest selling price, as long as selling price is in front of buying price not before

# if we loop through the array, we are going forward, so we will eventually meet the highest price
# for the min we will leave it behind us, so we need to store it