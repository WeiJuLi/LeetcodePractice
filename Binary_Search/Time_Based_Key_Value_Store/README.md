## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:

 - _Is there any requirement on time/space complexity?_ Yes, You should aim for a solution with O(1) time for set(), O(logn) time for get(), and O(m * n) space, where n is the total number of values associated with a key, and m is the total number of keys.
 - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
 - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

### Example Test Cases:

- **Happy Case:**
 ```python
 {"lulu": [["sad", 1],["happy", 2],["happy", 5],["angry", 6]]} 
 Input: get("lulu", 2)
 Output: "happy"
 ```

- **Edge Case:**
 ```python
 Input: get("lulu", 7)
 Output: "angry"

 Input: get("cindy", 7) --> There is no such key.
 Output: ""

 Constraints: 1 <= key.length, value.length <= 100
  {"lulu": [["sad", 1],["happy", 2],["happy", 5],["angry", 6]], ["kevin"]:""} 
 Input: get("kevin", 7) 
 Output: This will not happen. If there is a key, then there must be at least a value for it. 
 ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.

Brute Force: Iterate through the whole array and check wether that timestamp is inside the array. --> O(n)
Binary search: O(logn) Timestamp is sorted, so we can try to use Binary Search.

**Example Thought Process:**

## 🔑 Key Data Structure or Algorithm: Binary search

---

## Plan (Pseudocode)


1. Create an empty dictionary keyStore to store key-value pairs with Timestamps.
keyStore = {key:[value, timestamp]}

2. Set function:
    If key is not in the keyStore, then initialize an empty list for it. 
    Append [value, timestamp] to keyStore[key]

3. Get function:
    Retrieve values for key, or an empty list if key does not exist.
    res = "" 
    two pointers, l and r 
    l = 0, r = len(values) - 1

    Binary Search While Loop: while l <= r
        m = (l + r) // 2 
        if values[m][1] == timestamp:
            return values[m][0]
        elif values[m][1] < timestamp: 
            l = m + 1 
            res = values[m][0] #In case, if there is no timestamp in values, then return the most recent value. 
        elif values[m][1] > timestamp:
            r = m - 1 
    return res 

### Dry run code : Happy case and Edge case 
### Time & Space Complexcity : 
Time O(logn) : where n is the total number of values associated with a key, and m is the total number of keys.
Space O(m * n) : for keyStore dictionary

---

## Implement (Write the actual code)

# Solution 

```python

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
