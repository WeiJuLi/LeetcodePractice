## Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Arrays, Hashing
Content: 
- Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
- You may assume that each input would have exactly one solution, and you may not use the same element twice.
- You can return the answer in any order.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - *Can the input list be empty?* is it possible? No
  - *Will the numbers in the array duplicate?* Yes
  - *Can the numbers be positive, negative, or both?* Both
  - *Is there any requirement on time/space complexity?* O(n), O(n)
  - *Can I use Python to solve the problem or are there any languages you prefer me to use?* Python is preferred
  - *Do you want me to write pseudocode first or just code the result out?* I'll write pseudocode first
- **Write down key rules clearly**: e.g., distinct integers, ascending order.

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: nums = [-10, 0, 1], target = -10
  Output: [0, 1]
  ```

- **Edge Case1:**
  ```python
  Input: nums = [1, 1, 1], target = 2
  Output: [0, 1] or [1, 2]  # If multiple valid pairs exist
  ```

- **Edge Case2:**
  ```python
  Input: nums = [1, 1], target = 2
  Output: [0, 1] can not be [0, 0]  
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Usually sequential and O(n) for lookups.
- Is a **Set** helpful? No, we can't store index inside the set.
- Consider a **Hashtable (Dictionary)** Yes, we can find a key inside a Hashtable within O(1) time.

**Example Thought Process:**
- Using a List, checking existence is O(n) → inefficient.
- Hashtable provides O(1) lookup → ideal for this problem.

## 🔑 Key Data Structure:
- Hashtable (dictionary): stores numbers as keys, and their indices as values for O(1) lookups.

---

## Plan (Pseudocode)

1. create a dictionary to store all elements inside the input list. Key: char, Value: index.
2. for loop: store all of them
3. for loop: iterate through the whole list
      find = target - nums[i]
      if find in dictionary and index of find != current index i:
        return [i, index of find]
      
### Check:

1. Does it fit the Edge case? No, we have to check wether the index of find != current index 
2. Can we exist first?

---

## Implement (Write the actual code)

```python
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumD = {}
        for index, value in enumerate(nums):
            twoSumD[value] = index 

        for i, num in enumerate(nums):
            find = target - nums[i]
            if find in twoSumD and i != twoSumD[find]:
                return [i, twoSumD[find]]
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

- We can store and find the difference at the same time. The difference is target - nums[i].
- twoSumD; Key: number, Value: index 

- for index, num in enumerate(nums):
    find = target - nums[index] 
    if find in twoSumD:
      return [twoSumD[find], index]
    else:
      twoSumD[num] = index  

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?

