class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns_sets = [set() for _ in range(len(board))]
        boxes_sets = [set() for _ in range(len(board))] 

        for i, row in enumerate(board):
            row_set = set()
            for j, cell in enumerate(row):
                box_index = (i // 3) * 3 + j // 3
                if not cell.isdigit():
                    continue
                if cell in row_set or cell in columns_sets[j] or cell in boxes_sets[box_index]:
                    print(cell, i, j)
                    return False
                row_set.add(cell)
                columns_sets[j].add(cell)
                boxes_sets[box_index].add(cell)
        return True


# how to get the index of the box from i, j
# 0<=i<=2 and 0<=j<=2  ==>  box_index = 0 = i // 3 * 3 + j // 3 = 0 + 0   
# 0<=i<=2 and 3<=j<=5  ==>  box_index = 1 = i // 3 * 3 + j // 3 = 0 + 1
# 0<=i<=2 and 6<=j<=8  ==>  box_index = 2 = i // 3 * 3 + j // 3 = 0 + 2

# 3<=i<=5 and 0<=j<=2  ==>  box_index = 3 = i // 3 * 3 + j // 3 = 3 + 0
# 3<=i<=5 and 3<=j<=5  ==>  box_index = 4 = i // 3 * 3 + j // 3 = 3 + 1
# 3<=i<=5 and 6<=j<=8  ==>  box_index = 5 = i // 3 * 3 + j // 3 = 3 + 2

# 6<=i<=8 and 0<=j<=2  ==>  box_index = 6 = 6 + 0 = i // 3 * 3 + j // 3 = 
# 6<=i<=8 and 3<=j<=5  ==>  box_index = 7 = 6 + 1 = i // 3 * 3 + j // 3
# 6<=i<=8 and 6<=j<=8  ==>  box_index = 8 = 6 + 2 = i // 3 * 3 + j // 3


