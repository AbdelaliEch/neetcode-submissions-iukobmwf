class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (l + r) // 2
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[middle] == target:
                return middle

            if nums[middle] > nums[l]: # middle is in left sorted half
                if target > nums[middle]:
                    # go right
                    l = middle + 1
                else:
                    if target < nums[l]:
                        # go right
                        l = middle + 1
                    elif target > nums[l]:
                        # go left
                        r = middle - 1

            else: # middle is in right sorted half
                if target < nums[middle]:
                    # go left
                    r = middle - 1
                else:
                    if target < nums[r]:
                        # go right
                        l = middle + 1
                    elif target > nums[r]:
                        # go left
                        r = middle - 1
        return -1


# the array is sorted but rotated
# so it means that it has two sorted halfs, we need to figure out which half to search
# if the middle is greater than the left, then the middle is in the left sorted half, 
# else it is in right sorted half

# now if we are in left sorted half, and target in greater than middle, that means target can't be from [l, m]
# but if target is less than middle, it can be in both halfs, we can compare with left,
# if target is less than left, then it is in right side
# and if it is greater than left, then it is in the left side


# now if we were in right sorted half, and target is less than middle, that means target is in left half