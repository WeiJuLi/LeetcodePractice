# LeetCode Problem-Solving SOP (UMPIRE Method)

This SOP systematically guides you through solving coding interview problems using the **UMPIRE** method:

- **Understand**
- **Match**
- **Plan (Pseudocode)**
- **Implement**
- **Review**
- **Evaluate & Optimize**

---

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - **Constraints**: e.g., each number can only be used once.
  - **Empty input**: is it possible? (Usually no, according to constraints.)
  - **Number characteristics**: positive, negative, or both?
  - **Time/space complexity**: any specific requirements (e.g., O(n) time & O(n) space)?
  - **Preferred programming language**: clarify if Python or another language is preferred.
  - **Approach**: pseudocode first or direct coding?
- **Write down key rules clearly**: e.g., distinct integers, ascending order.

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: nums = [-10, 0, 1], target = -10
  Output: [0, 1]
  ```

- **Edge Case:**
  ```python
  Input: nums = [1, 1, 1], target = 2
  Output: [0, 1] or [1, 2]  # If multiple valid pairs exist
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Usually sequential and O(n) for lookups.
- Is a **Set** helpful? Fast lookups, but unordered.
- Consider a **Hashtable (Dictionary)** for O(1) lookups.

**Example Thought Process:**
- Using a List, checking existence is O(n) → inefficient.
- Hashtable provides O(1) lookup → ideal for this problem.

## 🔑 Key Data Structure:
- Hashtable (dictionary): stores numbers as keys, and their indices as values for O(1) lookups.

---

## Plan (Pseudocode)

1. Create a dictionary (`twoSum`) to store numbers as keys and their indices as values.
2. Iterate through `nums`:
    - Calculate the required number (`find = target - num`).
    - Check if `find` exists in the dictionary:
      - If found and indices differ, return both indices.

### Pseudocode Example:
```pseudo
initialize empty dictionary twoSum
for index, num in enumerate(nums):
    find = target - num
    if find exists in twoSum and index is not the same:
        return [twoSum[find], index]
    else:
        twoSum[num] = index
```

---

## Implement (Write the actual code)

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = {}  # store numbers and their indices

        for index, num in enumerate(nums):
            find = target - num
            if find in twoSum:
                return [twoSum[find], index]
            twoSum[num] = index
```

---

## Review
- Carefully review your implementation by checking:
  - Correctness of variable naming.
  - Constraints handling.
  - Edge cases coverage (negative numbers, duplicates, sorted order).

---

## Evaluate
- **Time Complexity**: O(n) – each element checked exactly once.
- **Space Complexity**: O(n) – storing each number in a hashtable.

---

## Optimize

- **Improved solution (One-Pass)**:
  - Iterate only once to enhance efficiency.

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNums = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dictNums:
                return [dictNums[diff], i]
            dictNums[n] = i
```

### Time & Space Optimization:
- **One-pass approach** ensures optimal:
  - Time Complexity: **O(n)**
  - Space Complexity: **O(n)**

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?

---

## 🎯 **Key Takeaways (學習要點)**
- UMPIRE method provides a systematic framework for solving problems.
- Always clarify problem constraints thoroughly.
- Use the most efficient data structures, particularly hashtables for quick lookups.
- Aim for a one-pass solution to optimize complexity.
