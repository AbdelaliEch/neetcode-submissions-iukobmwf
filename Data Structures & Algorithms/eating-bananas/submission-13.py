class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_p = max(piles)
        current_min = max_p

        l, r = 1, max_p
        while l <= r:
            m = (l + r) // 2
            
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/m)
            
            print(l, m, r, current_min, total_hours)

            if total_hours <= h:
                r = m - 1
                current_min = m
            else:
                l = m + 1

        return l


# complexity: O(nlog(m)) O(1)           


# we need to find the minimum eating rate such that
# all the piles will be finished in less than h hours


# i guess the brute force solution would be start from the max
# pile and go down

# which is O(max(piles))