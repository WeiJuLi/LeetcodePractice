## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:
 - _Can the input list be empty?_ No, it can not be empty.
 - _Can the numbers in the array duplicate?_ No. Every element should be sorted in ascending order.
 - _Can the numbers be positive, negative, or both?_ Both
 - _Is there any requirement on time/space complexity?_ Yes, Time O(logn) 
 - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
 - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

### Example Test Cases:

- **Happy Case:**
 ```python
 Input: nums = [3, 4, 1, 2] 
 Output: 1
 ```

- **Edge Case:**
 ```python
 Input: nums = [0] 
 Output: 0

 if len(nums) == 1: return nums[0] is the smallest 
 ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.

Brute Force: Iterate through the whole list and find the smallest --> O(n)
Binary search: O(logn)

[3,4,5,1,2] nums[middle] = 5, nums[r] = 2. 
We find that nums[middle] > nums[r] so smallest number must in the right half. 
We find that nums[middle] < nums[r] so smallest number must in the left half. 

**Example Thought Process:**

## 🔑 Key Data Structure or Algorithm: Binary search

---
## Plan (Pseudocode)

0. If len(nums) == 1: return nums[0] is the smallest 
1. Initialize l, r pointers. l = 0, r = len(nums) - 1 
2. While loop: l < r (最後再判斷，是l <= r還是l < r) O(logn)
    middle = (l + r) // 2 
    if nums[middle] < nums[r], the minimum must be in the left half, so set r = middle (Can not be middle - 1, which might out of bound)
    Otherwise, the minimum must be in the right half, so let l = middle + 1. #nums[m] must bigger than nums[m + 1]
3. While l == r, return nums[l]

### Dry run code : Happy case and Edge case 
### Time & Space Complexcity : 
Time O(logn): Since binary search divides the search space in half at each step, the number of steps required to find the target is approximately log₂(n).

Space O(1)
---

## Implement (Write the actual code)

# Solution 

```python
from typing import List

class Solution:
    def minBinary(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        l, r = 0 , len(nums) - 1
        while l < r:
            m = (l + r) // 2 
            if nums[m] < nums[r]:
                r = m #nums[m - 1] might out of bound
            else: #nums[m] >= nums[r]
                l = m + 1 #nums[m] must bigger than nums[m + 1]
        return nums[l]
    

print(Solution().minBinary([1])) #1
print(Solution().minBinary([3,4,1,2])) #1
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