class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        
        # s1 = "abc", s2 = "lecabee"
        #                   l r
        l = 0
        r = len(s1) - 1 

        d1 = {}
        for i in s1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] = d1[i] + 1
        

        while r != len(s2):

            sub = s2[l:r+1]
            
            d2 = {}

            for i in sub:
                if i not in d2:
                    d2[i] = 1
                else:
                    d2[i] = d2[i] + 1 
            
            if d1 == d2:
                return True
            else:
                l += 1
                r += 1

        
        return False

        