class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            check_row = []
            for grid in board[i]:
                if grid == ".":
                    continue
                else:
                    check_row.append(grid)
            if len(check_row) != len(set(check_row)):
                return False
            
        for col in range(len(board)):
            check_col=[]
            for row in range(len(board)):
                if board[row][col] == ".":
                    continue
                else:
                    check_col.append(board[row][col])
            if len(check_col) != len(set(check_col)):
                return False
            
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                check_box = []
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        if board[row][col] == ".":
                            continue
                        else:
                            check_box.append(board[row][col])
                if len(check_box) != len(set(check_box)):
                    return False


        
        return True



            

        