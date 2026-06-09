class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        i, j = 0, len(heights) - 1
        while i < j:
            width = j - i
            height = min(heights[i], heights[j])
            amount = width * height
            max_amount = max(amount, max_amount)
            # print(i, j, height, width, amount)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_amount

# [1,7,2,5,4,7,3,6]




# amount = height * width
# to increase the amount we need to increase height or width, we can't control height cuz it depends on the order list
# but we can control the width, the max width is between the first index and last index


# but we can't just move both i and j cuz we might miss some combinations like (i, j - 1) (i+1, j)
# so we need to move each of them based on some conditions

# and if we move i or j, the width gets lower

# should we maybe move the index that the min height, so we can find max height


