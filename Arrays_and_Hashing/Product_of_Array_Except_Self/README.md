## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:
 - _Can the input list be empty?_ No
 - _Can the numbers in the array duplicate?_ Yes, definitely
 - _Can the numbers be positive, negative, or both?_ Both
 - _Is there any requirement on time/space complexity?_ Yes, Time O(n), Spcae O(n)
 - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
 - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

### Example Test Cases:

- **Happy Case:**

 ```python
Input: nums = [1, -1, 2, 0]
Output: [0, 0, 0, -2]
 ```

- **Edge Case:**
 ```python
 Input: nums = [0, 0]
 Output: [0, 0]
 ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.

Prefix and Suffix

Prefix = []
Suffix = []
Res = []

Input: nums = [1, -1, 2, 0]
Output: [0, 0, 0, -2]

Prefix = [1, Prefix[0] * nums[0], Prefix[1] * nums[1]......]

**Example Thought Process:**

## 🔑 Key Data Structure:



---

## Plan (Pseudocode)



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

- Time Complexity: 
- Space Complexity: 

---

## Optimize

---

## Evaluate (Self-assessment)

- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?

