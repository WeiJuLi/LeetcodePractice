## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:
  - _Can the input list be empty?_ is it possible? No, because 1 <= strs.length <= 1000
  - _Can the element inside the input list be empty?_ Yes, because 0 <= strs[i].length <= 100.
  - _Is there any requirement on time/space complexity?_ O(m\*n) time, O(m) space where m is the number of strings and n is the length of the longest string.
  - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
  - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first
- **Write down key rules clearly**: e.g., distinct integers, ascending order.

### Example Test Cases:

- **Happy Case:**

  ```python
  Input: strs = [“bear”, “reab”, “real”]
  Output: [[“bear”, “reab”], [“real”]]
  ```

- **Edge Case1:**

  ```python
  Input: strs = [""] Empty string is an anagram of itself.
  Output: [[""]]
  ```

- **Edge Case2:**

  ```python
  Input: strs = [“a”]
  Output: [[“a”]]
  ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**?
- Is a **Set** helpful?
- Consider a **Hashtable (Dictionary)**

1. How to group anagrams inside a sub list? There must be a same key from them to be grouped together.
2. Frequency of characters can be the same key.

Dict: key = char, value = occurence. --> Dictionary is mutable and it can't be key.
List: index= the order of English character , value = occurence. [2,3] A = 2, B = 3.
--> List is mutable as well, so we need to convert List into Tuple.

3. Key: tuple(List), Value: []

## 🔑 Key Data Structure:

- List, Tuple, and Dictionary.

---

## Plan (Pseudocode)

1. Create an empty dictionary `groups`
2. Loop through each word in the input list:
   a. Create a list of size 26, filled with zeros
   b. For each character in the word: - Convert the character to an index (e.g., 'a' = 0, 'b' = 1, ..., 'z' = 25) - Increase the count at that index
   c. Convert the list into a tuple (to use as a dictionary key)
   d. Add the word to `groups[key]`
3. Return all grouped anagrams as a list of lists

### Check:

1. Does it fit the Edge case? 
2. Can we exist first? Yes, 不處理也可以。

---

## Implement (Write the actual code)

```python
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            freq = [0] * 26 
            for j in i:
                freq[ord(j) - ord('a')] += 1 
            groups[tuple(freq)].append(i)
        
        return list(groups.values())
```

---

## Review

- Carefully review your implementation by checking:
  - Correctness of variable naming.
  - Constraints handling.
  - Edge cases coverage (negative numbers, duplicates, sorted order).

---

## Evaluate

- Time Complexity: O(m * n), We use a nested for loop inside the function. 
m is the number of strings and n is the length of the longest string.

- Space Complexity: O(m * n). 

Step 1: Space for Keys
Each key in the dictionary is a tuple of size 26 (since we use a letter count).
Since there are at most m unique keys (one per word in the worst case), this part takes O(m) space.

Step 2:
We store m words inside the dictionary and the length of longest string is n. O(m * n).

Step 3: Space for Output
The final result list(res.values()) stores all words again.
Since it contains m words, each of length up to n, it also takes O(m * n) space.

---

## Optimize

- 另有一個實際比理論更快的範例，需要花時間研究python List and sorted
- https://leetcode.com/problems/group-anagrams/solutions/6509694/beats-98-with-python3/?envType=study-plan-v2&envId=top-interview-150

---

## Evaluate (Self-assessment)

- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?
