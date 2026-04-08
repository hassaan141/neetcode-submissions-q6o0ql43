"""
       
    1. 2. 3  5. 8. 13
 .  __ __ __ __ __ __ 

"""




class Solution:
    def climbStairs(self, n: int) -> int:

        a, b = 1, 2

        if n == a:
            return a
        if n == b:
            return b

        for _ in range(2, n):

            temp = b
            b = a + b
            a = temp
        
        return b
    


    
