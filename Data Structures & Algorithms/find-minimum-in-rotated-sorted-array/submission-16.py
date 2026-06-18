class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        current_min = float('inf')

        while l <= r:
            m = (l + r) // 2
            print(l, m, r)
            current_min = min(current_min, nums[m], nums[l], nums[r])
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m - 1
        # current_min = min(current_min, m, l, r)
        return current_min


# the array is rotated, so it is split into two sorted halves
# one half has the minimum


# the minimum is the number where the array stops going up

# so if middle is bigger than right, it means the point where array
# stops going up is not reached yet, so the min is on the right

# else it is already reached





# we'll use binary search
