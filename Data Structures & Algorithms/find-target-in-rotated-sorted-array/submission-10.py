class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
            # we are in left sorted half, because break point not reached yet
                if target > nums[m]:
                # left half is sorted, so it will surely be to the right
                    l = m + 1
                elif target < nums[m]:
                # it can be to the right, or at the sorted right half
                # nums[l] is the minimum of the sorted left half, so
                    if target > nums[l]:
                        r = m - 1
                    elif target < nums[l]:
                        l = m + 1
                    else:
                        return l
                else:
                    return m
            else:
            # we are in right sorted half, because break point is already reached
                if target < nums[m]:
                # right half is sorted, so it surely be to the left
                    r = m - 1
                elif target > nums[m]:
                # nums[r] is the max of the right sorted half
                    if target > nums[r]:
                        r = m - 1
                    elif target < nums[r]:
                        l = m + 1
                    else:
                        return r
                else:
                        return m
        return l if target == nums[l] else -1

