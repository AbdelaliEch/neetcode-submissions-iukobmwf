class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        
        while i <= j:
            middle = (i + j) // 2
            if target < matrix[middle][0]:
                # left side
                j = middle - 1
                if j < 0:
                    return False
            elif target > matrix[middle][-1]:
                # right side
                i = middle + 1
                if i >= len(matrix):
                    return False
            else:
                # inside list
                list_found = matrix[middle]
                inner_i = 0
                inner_j = len(list_found) - 1
                while inner_i <= inner_j:
                    inner_middle = (inner_i + inner_j) // 2
                    if target < list_found[inner_middle]:
                        inner_j = inner_middle - 1
                    elif target > list_found[inner_middle]:
                        inner_i = inner_middle + 1
                    else:
                        return True
                return False
        return False

# time: O(log(m * n))
# space: O(1)

# Outer binary search → log(m)
# You have m rows. Each iteration you cut the rows in half. That's classic binary search → log(m).
# Inner binary search → log(n)
# Once you found the row, it has n elements. You binary search inside it, cutting in half each time → log(n).
# Total → log(m) + log(n)
# You do one then the other, so you just add them. Not multiply, not nested — strictly sequential. Outer finishes → inner starts.



