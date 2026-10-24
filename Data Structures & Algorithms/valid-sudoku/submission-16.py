class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns_sets = [set() for _ in range(len(board))]
        boxes_sets = [set() for _ in range(len(board))]
        for i, row in enumerate(board):
            row_set = set()
            for j, cell in enumerate(row):
                if not cell.isdigit():
                    continue
                box_index = i//3*3 + j//3    
                if cell in row_set or cell in columns_sets[j] or cell in boxes_sets[box_index]:
                    return False
                row_set.add(cell)
                columns_sets[j].add(cell)
                boxes_sets[box_index].add(cell)
        return True

# time: O(n**2)
# space: O(n**2)