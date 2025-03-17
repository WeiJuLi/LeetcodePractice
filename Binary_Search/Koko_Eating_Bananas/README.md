## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:
k means our minimun bananas-per-hour eating rate
h means the maximun hours that we have to finish all bananas

 - _Can the input list be empty?_ No, it can not be empty.
 - _Can the numbers in the array duplicate?_ Yes
 - _Can the numbers be positive, negative, or both?_ positive only
 - _Is there any requirement on time/space complexity?_ Yes, Time O(nlogm), Space O(1) 
 n is the size of the input array, and m is the maximum value in the array.
 - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
 - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

### Example Test Cases:

- **Happy Case:**
 ```python
Input: piles = [1,4,3,2], h = 9
Output: 2
 ```

- **Edge Case:**
 ```python
 Input: piles = [1, 2] h = 2
 Output: 2 
 if len(piles) == h : return max(piles) 
 ```
---

## Match
Brute Force: 
Input: piles = [1,4,3,2], h = 9

We want to find the minumun k (per-eating rate).
K is between 1 to max(piles), inclusive.

If k = 4, then hours = 4 (which is smaller than 9)
If k = 3, then hours = 5 
If k = 2, then hours = 6 
If k = 1, then hours = 10 (exceeds h)

Minimun k is 2. 
Time : O(mn) 
N is the size of the input array, and M is the maximum value in the array.

The value of k (eating speed) is a number between 1 and max(piles), inclusive.
This range is an ordered numerical range, which makes it suitable for Binary Search to find the best answer.

Identify suitable **Data Structures** or **Algorithms** if you're stuck.



**Example Thought Process:**

## 🔑 Key Data Structure or Algorithm: Binary search

---

## Plan (Pseudocode)

1. If len(piles) == h : return max(piles) 
2. We need to create two pointers. l = 1, r = max(piles) 
3. While loop : keep narrowing our searching range. While l <= r: O(logm)
    4. a middle variable = (l + r) // 2 
    5. Calculate hours required with speed = middle 
    for loop: for each pile in piles: O(n)
        hours += ceil(pile / middle)
    6. Check if the total hours fir within h 
    If hours <= h:
        minK = middle # update minimum eating speed 
        r = middle - 1 # Try smaller speeds
    Else: 
        l = middle + 1 # Increase speed to reduce total hours

return minK

### Dry run code : Happy case and Edge case 
### Time & Space Complexcity : 
time O(logm) * O(n)
space O(1)


---

## Implement (Write the actual code)

# Solution 

```python
from typing import List
import math

class Solution:
    def koBana(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        l, r = 1, max(piles)
        minK = max(piles)

        while l <= r:
            middle = (l + r) // 2 
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / middle)
            if hours <= h:
                minK = min(minK, middle)
                r = middle - 1 
            else:
                l = middle + 1 
        return minK

            
print(Solution().koBana([1,4,3,2], 9)) #2 
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
