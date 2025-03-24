## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:
 - _Can the input list be empty?_ Yes
 - _Can the input binary tree uncompleted?_ Yes
 - _Can the numbers in the array duplicate?_ No. Every element should be distinct.
 - _Can the numbers be positive, negative, or both?_ Both
 - _Is there any requirement on time/space complexity?_ 
    Yes, O(n) time and O(n) space, where n is the number of nodes in the tree
 - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ 
    Python is preferred
 - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

### Example Test Cases:

- **Happy Case:**
 ```python
 Input: nums = [1, 2, 3, 4] 
       1
      / \
     2   3
    /
   4

 Output: 
       1
      / \
     3   2
          \
           4
 ```

- **Edge Case:**
 ```python
 Input: nums = [] 
 Output: 
 ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.

DFS : 
DFS (Depth-First Search) is an algorithm that explores as far as possible along each branch of a tree or graph. Once it finishes exploring one branch, it backtracks and continues with other branches.

BFS :
BFS (Breadth-First Search) is an algorithm that traverses a tree or graph level by level from the root, using a queue to visit nodes in order.

**Example Thought Process:**

## 🔑 Key Data Structure or Algorithm: DFS, BFS

---

## Plan (Pseudocode)



### Dry run code : Happy case and Edge case 
### Time & Space Complexcity : 


---

## Implement (Write the actual code)

# Solution 

```python

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
- Space Complexity: O(n)

---

## Optimize

---

## Evaluate (Self-assessment)

- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?
