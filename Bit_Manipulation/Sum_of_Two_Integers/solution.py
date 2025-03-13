#Solution


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
            

    
#Test cases

print(Solution().getSum(1, 2)) #3
print(Solution().getSum(0, 0)) #0
print(Solution().getSum(-10, -20)) #-30
