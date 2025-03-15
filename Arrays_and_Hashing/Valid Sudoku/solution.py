# 1. Create three default dictionary key: index, value: 3 sets to track numbers in:
#     Each Row
#     Each Column
#     Each 3*3 square --> What's the index(tuple) for this situation? EX: board[2,2] is in first grid(0, 0). board[2,5] is in second grid(0, 1). 
    
#         So index(tuple) can be (row // 3, col // 3) 
#         // means floor division operator   
#         It divides two numbers and rounds down to the nearest integer.

# 2. Loop through each cell in the 9*9 board:
#     If the cell contains '.'
#         skip to the next one.
#     Else: 
#         If Check wether the number is already in the row, column, or sub-grid:
#             return False 
#         Else: 
#             Add the number to the row, column, and 3*3 sub-grid

# 3. If we finish iterate through 9*9 grid: 
#     return True 


# Solution 
from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) 
        cols = defaultdict(set)
        grids = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                else:
                    if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grids[(r // 3, c // 3)]):
                        return False
                    else: 
                        rows[r].add(board[r][c])
                        cols[c].add(board[r][c])
                        grids[(r // 3, c // 3)].add(board[r][c])
        
        return True 
    
print(Solution().isValidSudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]])) #True 

print(Solution().isValidSudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]])) #False 


