#Valid Anagram

Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Topic: Arrays, Hashing
Content: 
- Given two strings s and t, return true if t is an anagram of s, and false otherwise.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
    - *Can the strings be empty?* No
    - *Can the strings be of different lengths?* Yes
    - *Can the strings contain special characters?* No
    - *Can I use Python to solve the problem or are there any languages you prefer me to use?* Python is preferred
    - *Do you want me to write pseudocode first or just code the result out?* I'll write pseudocode first

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: s = "anagram", t = "nagaram"
  Output: true
  ```

- **Edge Case:**
  ```python
  Input: s = "rat", t = "car"
  Output: false
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Usually sequential and O(n) for lookups.
- Is a **Set** helpful? Fast lookups, but unordered.
- Consider a **Hashtable (Dictionary)** for O(1) lookups.

---

## Plan (Pseudocode)
## 🔑 Key Data Structure:
- Hashtable (dictionary): stores characters as keys and their frequencies as values for O(1) lookups.

**Example Thought Process:**
- Using a List, checking existence is O(n) → inefficient.
- Hashtable provides O(1) lookup → ideal for this problem.

1. Create two dictionaries (`s_map` and `t_map`) to store character frequencies.
2. Iterate through string `s`:
    - If character exists in `s_map`, increment count.
    - If not, add character with count 1.
3. Iterate through string `t`:
    - If character exists in `t_map`, increment count.
    - If not, add character with count 1.
4. Compare dictionaries:
    - If identical, return `True`.
    - If different, return `False`.

### Pseudocode Example:
```python
Process:
    Initialize empty dictionaries s_map and t_map
    
    FOR each character in string s:
        IF character exists in s_map:
            Increment count by 1
        ELSE:
            Add character with count 1
            
    FOR each character in string t:
        IF character exists in t_map:
            Increment count by 1
        ELSE:
            Add character with count 1
            
    IF s_map equals t_map:
        RETURN true
    ELSE:
        RETURN false
---

## Implement
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}  
        
        for char in s:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1
                
        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1     
                
        return s_map == t_map
```
---

## Review
- Time Complexity: O(n), because I iterate through the strings once 
- Space Complexity: O(n), because I use two dictionaries to store the characters and their frequencies

---

## Optimize
- I can optimize the space complexity by using a single dictionary to store the characters and their frequencies
---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?     