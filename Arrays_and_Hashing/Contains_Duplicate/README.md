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
  - _Can the input list be empty?_ Yes, it can be empty.
  - _Can the numbers in the array duplicate?_ Yes, definitely
  - _Can the numbers be positive, negative, or both?_ Both
  - _Is there any requirement on time/space complexity?_ Yes, Time O(n), Spcae O(n)
  - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
  - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

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

- var length, this var will store the length of this array.
  put every integer inside a set(), all elements inside this set() should be unique.
  We can check whether the length of the set and the length of the variable length are the same. If they are the same, then there's no duplicate integer inside this array. However, if they are different, then there must be duplicate integers in the input.

**Example Thought Process:**

## 🔑 Key Data Structure:

- Set

---

## Plan (Pseudocode)

1. create a set and put every numbers inside of it
2. return (len(nums) != len(setNums))

---

## Implement (Write the actual code)

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        return (len(nums) != len(setNums))

```

---

## Review

- Carefully review your implementation by checking:
  - Correctness of variable naming.
  - Constraints handling.
  - Edge cases coverage (negative numbers, duplicates, sorted order).

---

## Evaluate

- Time Complexity: O(n), because I store every single element into the setNums.
- Space Complexity: O(n), because I use a set to store n elements.

---

## Optimize

---

## Evaluate (Self-assessment)

- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?
