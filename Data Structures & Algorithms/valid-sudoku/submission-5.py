class Solution:
    
    def box_index(self, i, j):
        return i//3*3 + j//3

        # if 0<=i<=2 and 0<=j<=2:
        #     return 0
        # elif 0<=i<=2 and 3<=j<=5:
        #     return 1
        # elif 0<=i<=2 and 6<=j<=8:
        #     return 2
        # elif 3<=i<=5 and 0<=j<=2:
        #     return 3
        # elif 3<=i<=5 and 3<=j<=5:
        #     return 4
        # elif 3<=i<=5 and 6<=j<=8:
        #     return 5
        # elif 6<=i<=8 and 0<=j<=2:
        #     return 6
        # elif 6<=i<=8 and 3<=j<=5:
        #     return 7
        # elif 6<=i<=8 and 6<=j<=8:
        #     return 8
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        dicts_lst = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dicts_boxes = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        for i, row in enumerate(board):
            my_dict_row = {}

            for j, cell in enumerate(row):
                if cell.isdigit():
                    bx_index = self.box_index(i, j)

                    if cell in my_dict_row or cell in dicts_lst[j] or cell in dicts_boxes[bx_index]:
                        # print(dicts_lst)
                        # print(my_dict_row)
                        return False
                    else:
                        dicts_boxes[bx_index][cell] = (i, j)
                        dicts_lst[j][cell] = (i, j)
                        my_dict_row[cell] = (i, j)
        return True



# time: O(n**2), n: rows, m: columns
# space: O(n**2)
        



