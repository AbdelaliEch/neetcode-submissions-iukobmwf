class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        current_min = float('inf')
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            
            if hours > h:
                left = mid + 1
            else:
                current_min = mid
                right = mid - 1
        return current_min