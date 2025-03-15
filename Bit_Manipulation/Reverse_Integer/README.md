## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:
 - _Can the input integer be empty?_ No, it must be an integer -2^31 <= x <= 2^31 - 1.
 - _Can the numbers be positive, negative, or both?_ Both
 - _Is there any requirement on time/space complexity?_ Yes, Time O(logX), Spcae O(1)
 - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
 - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

### Example Test Cases:

- **Happy Case:**

 ```python
 Input: x = 1234
 Output: 4321
 ```

- **Edge Case:**
 ```python
 Input: x = 12345
 Output: 0 
 ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.

We can use string slicing to reverse the integer.
string[start index(default 0) : end index(length) : -1]


**Example Thought Process:**

## 🔑 Key Data Structure:



---

## Plan (Pseudocode)

function reverse(x):
    result = 0
    
    # Step 1: Convert number to string and reverse it
    if x is negative:
        remove '-' from x
        convert from integer to string 
        reverse the remaining digits
        convert back to integer and add '-' sign
    else:
        convert to string
        reverse the digits directly and convert back to integer
    
    # Step 2: Check if result is within 32-bit range
    if result is out of [-2^31, 2^31 - 1] range:
        return 0
    
    return result



---

## Implement (Write the actual code)



---

## Review

- Carefully review your implementation by checking:
 - Correctness of variable naming.
 - Constraints handling.
 - Edge cases coverage (negative numbers, duplicates, sorted order).

---

## Evaluate

- Time Complexity: for a number x, there are logx(base is ten) digits. O(logX)
- Space Complexity: O(1) We only use extra X to store variable.

---

## Optimize

---

## Evaluate (Self-assessment)

- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?

