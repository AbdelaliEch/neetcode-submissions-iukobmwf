class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = max(piles)
                
        # while k > 0:
        #     hours = 0
        #     for pile in piles:
        #         hours += math.ceil(pile / k)
        #     if hours > h:
        #         return k + 1
        #     k -= 1    

        left, right, current_k = 1, max(piles), max(piles)
        while left <= right:
            middle = (left + right) // 2 
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / middle)
            
            # print(left, middle, right, hours, h)

            if hours > h:
                left = middle + 1
            else:
                current_min = middle
                right = middle - 1
        return current_min 


        
# time: O(n*m) with n length of piles and m max of piles 
# space: O(1)




