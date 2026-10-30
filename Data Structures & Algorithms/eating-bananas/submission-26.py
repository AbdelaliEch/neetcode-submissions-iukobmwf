class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            middle = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / middle)

            # we need to increase k
            if hours > h:
                left = middle + 1
            # valid k, but let's check if there is a less one
            else:
                current_min = middle
                right = middle - 1
        return current_min

