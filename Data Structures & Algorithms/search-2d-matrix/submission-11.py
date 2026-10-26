class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        
        while left <= right:
            middle = (left + right) // 2
            print(left, middle, right)
            if target > matrix[middle][-1]:
                left = middle + 1
            elif target < matrix[middle][0]:
                right = middle - 1
            else:
                break
        else:
            return False

        middle_matrix = matrix[middle]
        left, right = 0, len(middle_matrix) - 1
        while left <= right:
            middle = (left + right) // 2
            if target > middle_matrix[middle]:
                left = middle + 1
            elif target < middle_matrix[middle]:
                right = middle - 1
            else:
                return True
        else:
            return False

# [1,2,4,8] [10,11,12,13] [14,20,30,40]