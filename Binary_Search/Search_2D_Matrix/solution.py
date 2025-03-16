# Solution 
from typing import List

class Solution:
    def twoDBS(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows * cols - 1) 

        while l <= r:
            middle = (l + r) // 2 
            # l = 0, r = 11, middle = 5 
            # Convert middle index into 2D cooridinates 
            # if middle = 5(start from index 0), row = 3, col = 4.
            # matrix[1][1] 5 // 4 = 1, 5 % 4 = 1 

            row = middle // cols  
            col = middle % cols  

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = middle - 1 
            else: 
                l = middle + 1 
        return False 

print(Solution().twoDBS([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 12))
print(Solution().twoDBS([[1]], 1))
