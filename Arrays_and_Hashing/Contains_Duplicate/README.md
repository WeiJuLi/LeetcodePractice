# Contains Duplicate

Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Topic: Arrays, Hashing
Content: 
- Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
    - *Can the input list be empty?* is it possible? No
    - *Can the numbers in the array duplicate?* Yes, definitely
    - *Can the numbers be positive, negative, or both?* Both
    - *Is there any requirement on time/space complexity?* No
    - *Can I use Python to solve the problem or are there any languages you prefer me to use?* Python is preferred
    - *Do you want me to write pseudocode first or just code the result out?* I'll write pseudocode first   

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: nums = [1, 2, 3, 1]
  Output: true
  ```           

- **Edge Case:**
  ```python
  Input: nums = [1, 2, 3, 4]
  Output: false
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

1. Create a dictionary (`nums_map`) to store numbers as keys, and their indices as values for O(1) lookups.
2. Iterate through `nums`:
    - Check if the current number exists in the dictionary.
    - If it does, return `True`.
    - If it doesn't, add the number to the dictionary.
3. If no duplicates are found, return `False`.

---

## Implement (Write the actual code)

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for n in nums:
            if n in nums_map:
                return True
            nums_map[n] = n
        return False
```

---

## Review
- Carefully review your implementation by checking:
    - Correctness of variable naming.
    - Constraints handling.
    - Edge cases coverage (negative numbers, duplicates, sorted order).

---

## Evaluate
- Time Complexity: O(n), because I iterate the nums list once
- Space Complexity: O(n), because I use a dictionary to store the number I checked and its Index

---

## Optimize

- I can optimize the space complexity by using a list to store the result instead of a dictionary  

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve? 