class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            middle = (low + high) // 2
            eq_result = sum(math.ceil(p/middle) for p in piles)
            if eq_result > h:
                low = middle + 1
            elif eq_result <= h:
                res = middle 
                high = middle - 1
        return res
        
        # x = 1
        # while x <= max(piles):
        #     eq_result = sum(math.ceil(p/x) for p in piles)
        #     if eq_result <= h:
        #         return x
        #     x+=1




