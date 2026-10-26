class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right= 1, max(piles)
        while left <= right:
            middle = (left + right) // 2 
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / middle)

            if hours > h:
                left = middle + 1
            else:
                current_min = middle
                right = middle - 1
        return current_min 
        
# time: O(nlogm) with n length of piles and m max of piles 
# space: O(1)




