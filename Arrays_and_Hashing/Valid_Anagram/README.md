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
  - _Can the strings be empty?_ Yes
  - _Can the strings be of different lengths?_ Yes
  - _Can the strings contain special characters?_ No, all characters are lowercase letters.
  - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
  - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first
  - _Time and space requirement?_ O(n + m) time, O(1)space

### Example Test Cases:

- **Happy Case:**

  ```python
  Input: s = "anagram", t = "nagaram"
  Output: true
  ```

- **Edge Case1:**

  ```python
  Input: s = "", t = ""
  Output: true
  ```

- **Edge Case2:**
  ```python
  Input: s = "ace", t = "acee"
  Output: false
  ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Is a **Set** helpful? Set can not store the frequenct of each letter.
- Consider a **Hashtable (Dictionary)** Yes, We can store the frequency for each character inside these two Hashtables. Key: character, Value: frequency.
- If they are the same, it means that these two strings are anagrams. However, if the two hashmaps are not the same, then the strings are definitely not anagrams.

- Can we exist early in certain cases to improve efficiency? Yes, If s and t have different length, then we can return False.

---

## Plan (Pseudocode)

## 🔑 Key Data Structure:

- Hashtable




### Pseudocode Example:

1. If len(s) != len(t): return False
2. Create two **default dictionaries** sDict, tDict 
3. for loop: store elements inside the dictionaries.
    for i in range(len(s)):
        sDict[s[i]] += 1 
        tDict[t[i]] += 1 

4. compare two dictionaries

## Implement
```python

````

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
