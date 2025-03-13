# Solution 

class Solution:
    def reverseInt(self, x: int) -> int:
        res = 0 
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])
        
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res 
    

print(Solution().reverseInt(1234236467)) #0
print(Solution().reverseInt(1234))  #4321
print(Solution().reverseInt(-1234)) #-4321
