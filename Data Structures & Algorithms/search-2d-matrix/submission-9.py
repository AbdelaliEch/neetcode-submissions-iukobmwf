class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1, r1 = 0, len(matrix) - 1
        
        while l1 <= r1:
            m1 = (l1 + r1) // 2
            print(l1, m1, r1)
            if target > matrix[m1][-1]:
                l1 = m1 + 1
            elif target < matrix[m1][0]:
                r1 = m1 - 1
            else:
                lst = matrix[m1]
                print(lst)
                l2, r2 = 0, len(lst) - 1
                while l2 <= r2:
                    m2 = (l2 + r2) // 2
                    if target > lst[m2]:
                        l2 = m2 + 1
                    elif target < lst[m2]:
                        r2 = m2 - 1
                    else:
                        return True
                return False
        return False

# complexity: O(log(m) + log(n)) = O(log(m*n)) O(1)
