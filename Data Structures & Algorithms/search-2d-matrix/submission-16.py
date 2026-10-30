class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_r, right_r = 0, len(matrix) - 1
        while left_r <= right_r:
            middle_r = (left_r + right_r) // 2
            if target > matrix[middle_r][-1]:
                left_r = middle_r + 1
            elif target < matrix[middle_r][0]:
                right_r = middle_r - 1
            else:
                break
        else:
            return False

        row = matrix[middle_r]
        left, right = 0, len(row) - 1
        while left <= right:
            middle = (left + right) // 2
            if target > row[middle]:
                left = middle + 1
            elif target < row[middle]:
                right = middle - 1
            else:
                return True
        return False
        

