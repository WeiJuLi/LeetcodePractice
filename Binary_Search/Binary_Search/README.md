## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:
 - _Can the input list be empty?_ No, it can not be empty.
 - _Can the numbers in the array duplicate?_ No. Every element should be distinct.
 - _Can the numbers be positive, negative, or both?_ Both
 - _Is there any requirement on time/space complexity?_ Yes, Time O(logn) 
 - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
 - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

### Example Test Cases:

- **Happy Case:**
 ```python
 Input: nums = [1, 2, 3, 4] target = 4 
 Output: 3 
 ```

- **Edge Case:**
 ```python
 Input: nums = [0] targte = 1
 Output: -1 
 ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.

Brute Force: Iterate through the whole array and check wether target is inside the array. --> O(n)
Binary search: O(logn)

**Example Thought Process:**

## 🔑 Key Data Structure or Algorithm:  Binary search

---

## Plan (Pseudocode)

1. Initialize two pointers, l and r.
    l at the start of the array (index 0)
    r at the end of the array (index length - 1)

2. Keep narrowing the range between l and r pointers, untill the index of l > r
    Find the middle index using floor division (l+r // 2)
    if target == nums[middle] return middle
    elif target < nums[middle]: move r to middle - 1 
    else: target > nums[middle] move l to middle + 1 

3. If the while loop ends, return -1. We can't find target inside this array.

### Dry run code : Happy case and Edge case 
### Time & Space Complexcity :  
O(logn) time - Since binary search divides the search space in half at each step, the number of steps required to find the target is approximately log₂(n).

O(1) Space 

---

## Implement (Write the actual code)

# Solution 

```python
from typing import List

class Solution:
    def biSearch(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 

        while l <= r:
            middle = (l + r) // 2 
            if target == nums[middle]:
                return middle 
            elif target < nums[middle]:
                r = middle - 1 
            else: 
                l = middle + 1 
        return -1 
    

print(Solution().biSearch([1, 2, 3, 4], 4)) #3
print(Solution().biSearch([1, 2, 3, 5], 4)) #-1
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

