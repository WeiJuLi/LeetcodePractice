## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:
 - _Can the input list be empty?_ No, because m and n should be between 1 and 100, inclusive. 
 - _Can the numbers in the array duplicate?_ Yes
 - _Can the numbers be positive, negative, or both?_ Both
 - _Is there any requirement on time/space complexity?_ Yes, Time O(logm*n) 
 - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
 - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

### Example Test Cases:

- **Happy Case:**
 ```python
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 12
Output: true
 ```

- **Edge Case:**
 ```python
Input: matrix = [[1, 1],[2, 2]], target = 1 # non-decreasing order with duplicated numbers
Output: true
 ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.

Brute Force: Flatten this 2D matrix into a 1D list of length m * n, and iterate through the whole list to check wether target is inside this 1D list. --> O(mn)

For a more efficient way, we can use Binary search to solve this problem.

Binary search: O(logn) Flatten this 2D matrix into a 1D list of length m * n and use Binary search to fond the target.

**Example Thought Process:**

## 🔑 Key Data Structure or Algorithm: Binary search

---

## Plan (Pseudocode)

1. Set two pointers. l = 0, r = rows * cols - 1
2. While l <= r, keep narrowing the search range:
    find the middle index using floor division
    convert the 1D index to 2D coordinates
    row = middle index // # of cols
    col = middle index % # of cols 
    check the middle: 
    if == target return True 
    if > target, move r to middle - 1
    if < target, move l ro middle + 1 
3. return False



### Dry run code : Happy case and Edge case 
### Time & Space Complexcity : O(logm*n) Flatten 2D matrix into 1D list and use binary search algorithm to solve this problem. 


---

## Implement (Write the actual code)

# Solution 

```python
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
```

---

## Review

- Carefully review your implementation by checking:
 - Correctness of variable naming.
 - Constraints handling.
 - Edge cases coverage (negative numbers, duplicates, sorted order).

---

## Evaluate

- Time Complexity: O(logn)
- Space Complexity: O(1)

---

## Optimize

---

## Evaluate (Self-assessment)

- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?
