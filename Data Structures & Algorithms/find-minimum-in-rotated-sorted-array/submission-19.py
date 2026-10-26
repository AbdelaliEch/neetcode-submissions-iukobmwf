class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            # if middle is in the right sorted array, so min is either in the middle or to the left of the middle
            if nums[middle] < nums[right]:
                right = middle
            # else, min is in the right sorted array
            else:
                left = middle + 1
        return nums[middle]
# time: O(logn)
# space: O(1)




# now we need some if statements that will determine where the minimum is: to the right or to the left?
# the array is divided into two sorted halves


# [3 4 5 6 1 2] = [3 4 5 6] [1 2]
# middle is 5


