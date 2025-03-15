## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:
 - _Can the input grid be empty?_ Yes, it can be empty. There is no element inside the grid.
 - _Can the numbers in the same row or column duplicate?_ No. If so, this is not a valid Sudoku board.
 - _Can the numbers be positive, negative, or both?_ No. 1-9
 - _Is there any requirement on time/space complexity?_ Yes, Time O(n^2), Spcae O(n^2)
 - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
 - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

### Example Test Cases:

- **Happy Case:**
 ```python
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: true
 ```

- **Edge Case:**
 ```python
 Input: board = [[all .],[all .]...]
 Output: true
 ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.

List ? 
Dictionary ? Yes! 
    Key : # of row, column, and grid 
    Value : We can create three sets to track the numbers that have already appeared in each row, column, and grid.


**Example Thought Process:**

## 🔑 Key Data Structure: Set()


---

## Plan (Pseudocode)

1. Create three default dictionary key: index, value: 3 sets to track numbers in:
    Each Row
    Each Column
    Each 3*3 square --> What's the index(tuple) for this situation? EX: board[2,2] is in first grid(0, 0). board[2,5] is in second grid(0, 1). 
    
        So index(tuple) can be (row // 3, col // 3) 
        // means floor division operator   
        It divides two numbers and rounds down to the nearest integer.

2. Loop through each cell in the 9*9 board:
    If the cell contains '.'
        skip to the next one.
    Else: 
        If Check wether the number is already in the row, column, or sub-grid:
            return False 
        Else: 
            Add the number to the row, column, and 3*3 sub-grid

3. If we finish iterate through 9*9 grid: 
    return True 

---

## Implement (Write the actual code)



---

## Review

- Carefully review your implementation by checking:
 - Correctness of variable naming.
 - Constraints handling.
 - Edge cases coverage (negative numbers, duplicates, sorted order).

---

## Evaluate

- Time Complexity: 
- Space Complexity: 

---

## Optimize

---

## Evaluate (Self-assessment)

- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?

