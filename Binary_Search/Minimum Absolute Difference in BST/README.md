## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:
 - _Can the input list be empty?_ No, we will given a root.
 - _Can the numbers in the array duplicate?_ No. Every element should be distinct. Because by definition, a Binary Search Tree (BST) does not have duplicate values — each node’s left child must have a strictly smaller value, and each right child must have a strictly greater value.
 - _Can the numbers be positive, negative, or both?_ Both
 - _Is there any requirement on time/space complexity?_ Yes, 
 - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
 - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

### Example Test Cases:

- **Happy Case:**
 ```python

 ```

- **Edge Case:**
 ```python

 ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.

### Why DFS??
In a BST, in-order DFS gives values in sorted order.
Once the values are sorted, we only need to compare adjacent values to find the smallest difference.
DFS (especially in-order) helps us visit nodes in order from smallest to largest.

### Why not BFS??
BFS goes level by level.
The values are not sorted in BFS order.
So we would have to collect all values, sort them, and then compare — which takes extra time and memory.

BST has a special property: in-order traversal gives sorted values.
We can just do in-order traversal and compare adjacent values to get the minimum difference.

To implement this, we can use:

1. Iteration : More memory-efficient and no stack overflow problem 
2. Recursion : Can cause stack overflow if recursion depth is too deep (e.g., very unbalanced trees)

Which one is better? 


**Example Thought Process:**

## 🔑 Key Data Structure or Algorithm: Binary search

---

## Plan (Pseudocode)

In-order DFS 有個共通點：
1. 先left (middle也屬於left)
2. 計算minDiff
3. 再right 

### DFS Resursion 
Set prev as None and minDiff as infinity

Define a recursive inorder(node) function:

If node is None, return

Recursively call inorder(node.left)

If prev is not None, update minDiff = min(minDiff, node.val - prev)

Set prev = node.val

Recursively call inorder(node.right)

Call inorder(root)

Return minDiff

### DFS Iteration 

![photo](https://github.com/WeiJuLi/LeetcodePractice/blob/main/Binary_Search/Minimum Absolute Difference in BST/DFS_iter.jpg)

Initialize variables:

cur as the root node (current node pointer)
stack as an empty list (to simulate recursion for in-order traversal)
minDiff as a large number (e.g., 100000) to store the minimum difference
prev as a very small number (e.g., -100000) to store the previous node's value during traversal

While stack is not empty or cur is not null:

While cur is not null:

Push cur onto the stack

Move cur to its left child

Pop a node from the stack, assign it to node

Update minDiff as the minimum of minDiff and (node.val - prev)

Update prev to node.val

Move cur to the right child of node

After traversal, return minDiff as the result


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
