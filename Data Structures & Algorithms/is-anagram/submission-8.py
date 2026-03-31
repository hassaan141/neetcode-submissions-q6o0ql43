class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        set_s, set_t = {}, {}


        #rrr
        for i in range(len(s)):

            if s[i] not in set_s:
                set_s[s[i]] = 1
            elif s[i] in set_s:
                set_s[s[i]] += 1

            if t[i] not in set_t:
                set_t[t[i]] = 1
            elif t[i] in set_t:
                set_t[t[i]] += 1

        if set_t == set_s:
            return True
        else:
            return False

        
        