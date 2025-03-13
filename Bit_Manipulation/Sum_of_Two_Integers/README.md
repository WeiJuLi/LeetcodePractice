# Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the + and - operators.

## 📖 Understand

### 📌 Step-by-step Process:

- **Read the question out loud**.
- **Clarify the following details**:
  - _Can the input integers be empty?_ No, they can't be empty.
  - _Can the numbers be positive, negative, or both?_ Both
  - _Is there any requirement on time/space complexity?_ Yes, Time O(1), Spcae O(1)
  - _Can I use Python to solve the problem or are there any languages you prefer me to use?_ Python is preferred
  - _Do you want me to write pseudocode first or just code the result out?_ I'll write pseudocode first

### Example Test Cases:

- **Happy Case:**

  ```python
  Input:  a = 1, b = 1
  Output: 2 
  ```

- **Edge Case:**
  ```python
  Input: a = -10, b = 0
  Output: -10 
  ```

---

## Match

Identify suitable **Data Structures** or **Algorithms** if you're stuck.


**Example Thought Process:**

## 🔑 Key Data Structure:

- 

---

## Plan (Pseudocode)
![Sum of Two Integers](https://github.com/WeiJuLi/LeetcodePractice/blob/main/Bit_Manipulation/Sum_of_Two_Integers/sumoftwoint.jpeg)
1. use XOR(^) does addition without carry
2. AND(&) + Left Shift(<<) finds carry
3. Repeat until no carry(b=0)
    a = (a ^ b) & mask
    b = ((a & b) << 1 ) & mask 

mask = 0xFFFFFFFF
👉 Keeps numbers within 32-bit range

0xFFFFFFFF (binary: 1111 1111 1111 1111 1111 1111 1111 1111)
It ensures only the last 32 bits are kept, preventing Python from using unlimited precision.

max_int = 0x7FFFFFFF
👉 Helps detect negative numbers in 32-bit

0x7FFFFFFF (binary: 0111 1111 1111 1111 1111 1111 1111 1111)
Largest 32-bit positive number (2147483647).


How to deal with Positive and Negative number?
In a 32-bit binary number:

Range: 

Positive numbers: 0 to 2147483647 (0x00000000 to 0x7FFFFFFF)
Negative numbers: -1 to -2147483648 (0xFFFFFFFF to 0x80000000)
How to tell if it's positive or negative?

If the first (leftmost) bit is 0, it's a positive number.
If the first bit is 1, it's a negative number (using two’s complement representation).

In a 32-bit system, numbers are stored as binary:

Positive numbers are stored normally.
Negative numbers are stored using two’s complement:
Flip all the bits (1 → 0, 0 → 1).
Add 1 to the result.
For example:

```python
       5  =  0000 0000 0000 0000 0000 0000 0000 0101
  max_int =  1111 1111 1111 1111 1111 1111 1111 1111   (flip : 5 ^ mask)
5^max_int =  1111 1111 1111 1111 1111 1111 1111 1010
      -5  =  1111 1111 1111 1111 1111 1111 1111 1011   (add 1)
```

---

## Implement (Write the actual code)

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            # Addition without carry 
            xor = (a ^ b) & mask 
            carry = ((a & b) << 1) & mask 
            a = xor 
            b = carry 

        return a if a <= max_int else ~(a ^ mask)
```

---

## Review

- Carefully review your implementation by checking:
  - Correctness of variable naming.
  - Constraints handling.
  - Edge cases coverage (negative numbers, duplicates, sorted order).

---

## Evaluate

- Time Complexity: O(32) -> O(1) Runs at most 32 times because b shifts left, limited to 32 bits.
- Space Complexity: O(1), because we only use several variables.

---

## Optimize

---

## Evaluate (Self-assessment)

- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?
