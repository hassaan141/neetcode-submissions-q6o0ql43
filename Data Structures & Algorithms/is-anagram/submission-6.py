class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = {}
        a = {}
        for x in s:
            if x not in d:
                d[x] = 1
            else: 
                d[x] = d[x] + 1

        for x in t:
            if x not in a:
                a[x] = 1
            else: 
                a[x] = a[x] + 1
        
        if a == d:
            return True
        else:
            return False
