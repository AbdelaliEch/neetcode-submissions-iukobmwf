class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        low, high= 1, max(piles)
        while low <= high:
            middle = (low + high) // 2
            eq_result = sum(math.ceil(p/middle) for p in piles)
            if eq_result > h:
                low = middle + 1
            else:
                res = middle 
                high = middle - 1
        return res
        


