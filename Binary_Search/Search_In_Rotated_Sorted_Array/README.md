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
 Input: nums = [5, 6, 1, 2, 3, 4] target = 4 
 Output: 5
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
Binary search: O(logn) We can only use binary search when the list is sorted.

Input: nums = [5, 6, 1, 2, 3, 4] target = 4 
 l = 0, r = 5, m = 2 
 There are at most two sorted sequence at both left and right side of nums[m]

 Input: nums = [6, 1, 2, 3, 4, 5] target = 4 
 l = 0, r = 5, m = 2 
 There is only sorted sequence at the right side of nums[m]

 Conclusion : At least, we can find one sorted sequence at the right or left side of nums[m]


**Example Thought Process:**

## 🔑 Key Data Structure or Algorithm: Binary search

---

## Plan (Pseudocode)

 1. create two pointers. l = 0, r = len(nums) - 1 
 2. While loop: keep narrowing the search range untill l > r 
    middle = (l + r) // 2 
    if target == nums[m] return m

    3. Find the sorted sequence to do binary search

    4. nums[m] <= nums[r] : the right side of nums[m] is sorted

        if target is not betweeb nums[m] and nums[n] : the target might at the left half r = m - 1 
        else: l = m + 1 

    5. nums[m] > nums[r] : the left side of nums[m] is sorted 

        if target is not between nums[l] and nums[m] : the target might at the right half. l = m + 1 
        else: r = m - 1 

3. while l > r and can't find the target 
return - 1 


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
    def searchRotate(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        while l <= r:
            m = (l + r) // 2 

            if nums[m] == target:
                return m

            if nums[m] <= nums[r]: #right half is sorted 
                if nums[m] < target <= nums[r]:
                    l = m + 1 
                else:
                    r = m - 1 
            
            else : #left half is sorted 
                if nums[l] <= target < nums[m]:
                    r = m - 1 
                else: 
                    l = m + 1 
        return -1 
    

print(Solution().searchRotate([0], 1)) #-1
print(Solution().searchRotate([6,1,3,5], 3)) #2

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
