## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:
 - _Can the input array be empty?_ Yes
 - _Can the numbers in the array duplicate?_ Yes, definitely
 - _Can the numbers be positive, negative, or both?_ Both
 - _Is there any requirement on time/space complexity?_ Yes, Time O(n), Spcae O(n)
 - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
 - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

### Example Test Cases:

- **Happy Case:**

 ```python
Input: nums = [1, -1, 2, 0]
Output: 4
 ```

- **Edge Case:**
 ```python
 Input: nums = []
 Output: 0
 ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.

Array : One possible solution is using sorted(), and iterate from the index 0 to the end to check the length of longest consecutive sequence.  However, sorted() will cost O(nlogn) time.

So, another possible solution is using Set().


**Example Thought Process and dry run with Happy case and Edge case:**

## 🔑 Key Data Structure: Set()


---

## Plan (Pseudocode)

Input: nums = [1, -1, 2, 0]
Output: 4

0. if len(nums) == 0: return 0 

1. Convert the nums array into a set for fast lookups. set = {1, -1, 2, 0} O(n) time, O(n) space
2. Initialize res = 0 to keep track of the longest sequence. res = 0 
3. Loop through each number in the numSet: O(n) time
    Check if it's a starting number (i-1 is not in the set)
    if it's a starting number:
        set leng = 1, leng = 1 
        While loop: Keep finding the following consecutive integer inside the set, untill we can't find it. (i + leng inside the set) We don't do this while loop for every single element inside the nums. So the time complexity is not O(n^2)
            leng += 1, leng = 4
        res = max(res, leng) 
    else:
        continue 
4. return res 


Dry run: 
1. Happy case 
2. Edge case (add step 0)

Time : O(n)
Space : O(n)

---

## Implement (Write the actual code)


```python

from typing import List

class Solution:
    def longestCSeq(self, nums: List[int] ) -> int:
        if len(nums) == 0: 
            return 0 
        
        numSet = set(nums)
        res = 0 

        for num in numSet:
            if (num - 1) in numSet:
                continue
            else:
                leng = 1 
                while (num + leng) in numSet:
                    leng += 1 
                res = max(res, leng)
        
        return res 

```

---

## Review

- Carefully review your implementation by checking:
 - Correctness of variable naming.
 - Constraints handling.
 - Edge cases coverage (negative numbers, duplicates, sorted order).

---

## Evaluate

- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Optimize

---

## Evaluate (Self-assessment)

- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?

