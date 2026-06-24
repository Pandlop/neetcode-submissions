class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            hash_row = set()
            hash_col = set()
            hash_square = set()

            square_i = int((i / 3)*3)
            for j in range(len(board)):
                row_val = board[i][j]
                col_val = board[j][i]
                square_val = board[(i//3)*3 + j//3][(i%3)*3 + j%3]

                if row_val != "." and row_val in hash_row:       return False
                if col_val != "." and col_val in hash_col:       return False
                if square_val != "." and square_val in hash_square: return False

                hash_row.add(row_val)
                hash_col.add(col_val)
                hash_square.add(square_val)
            
        return True

                
        