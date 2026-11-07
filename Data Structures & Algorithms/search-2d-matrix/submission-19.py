class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_m, right_m = 0, len(matrix) - 1
        while left_m <= right_m:
            mid_m = (left_m + right_m) // 2

            if target > matrix[mid_m][-1]:
                left_m = mid_m + 1
            elif target < matrix[mid_m][0]:
                right_m = mid_m - 1
            else:
                break
        else:
            return False
        
        lst = matrix[mid_m]
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2

            if target > lst[mid]:
                left = mid + 1
            elif target < lst[mid]:
                right = mid - 1
            else:
                return True
        return False

# time: O(logn + logm) = O(logmn) with m number of rows and n number of columns
# space: O(1)