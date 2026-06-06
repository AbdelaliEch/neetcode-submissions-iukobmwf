class Solution:
    def getBoxIndex(self, i, j):
        return (i // 3) * 3 + (j // 3)
    
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols_sets_dict = defaultdict(set)
        boxes_sets_dict = defaultdict(set)

        for i, row in enumerate(board):
            row_set = set()
            for j, col in enumerate(row):
                if not col.isdigit():
                    continue
                box_index = self.getBoxIndex(i, j)
                if col in row_set or col in cols_sets_dict[j] or col in boxes_sets_dict[box_index]:
                    return False
                row_set.add(col)
                cols_sets_dict[j].add(col)
                boxes_sets_dict[box_index].add(col)

        return True

# complexity: O(n**2) O(n**2)


# in 1st square: 0<=i<=2 and 0<=j<=2    0 = 0 + 0
# in 2nd square: 0<=i<=2 and 3<=j<=5    1 = 0 + 1
# in 3rd square: 0<=i<=2 and 6<=j<=8    2 = 0 + 2

# in 4th square: 3<=i<=5 and 0<=j<=2    3 = 3 + 0 
# in 5th square: 3<=i<=5 and 3<=j<=5    4 = 3 + 1
# in 6th square: 3<=i<=5 and 6<=j<=8    5 = 3 + 2

# in 7th square: 6<=i<=8 and 0<=j<=2    6 = 6 + 0
# in 8th square: 6<=i<=8 and 3<=j<=5    7 = 6 + 1
# in 9th square: 6<=i<=8 and 6<=j<=8    8 = 6 + 2
 