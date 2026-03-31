# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         d = {}
#         a = {}
#         for x in s:
#             if x not in d:
#                 d[x] = 1
#             else: 
#                 d[x] = d[x] + 1

#         for x in t:
#             if x not in a:
#                 a[x] = 1
#             else: 
#                 a[x] = a[x] + 1
        
#         if a == d:
#             return True
#         else:
#             return False



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        d = {}
        f = {}

        for i in s:
            if i not in d:
                d[i] = 1
            
            else: 
                d[i] = d[i] + 1

        for i in t:
            if i not in f:
                f[i] = 1
            
            else: 
                f[i] = f[i] + 1
        
        if d == f:
            return True
        else:
            return False

        































