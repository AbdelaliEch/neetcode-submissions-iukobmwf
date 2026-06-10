class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = right = max_profit = 0

        current_min = prices[left]

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            max_profit = max(prices[right] - prices[left], max_profit)
            right += 1

        return max_profit

# complexity: O(n) O(1)

# left needs to always track current min
# right needs to just move and calculate


# to get the max profit, we need to buy low and sell high
# so buy at minimum
# so why not iterate thro
# [10,1,5,6,7,1]  