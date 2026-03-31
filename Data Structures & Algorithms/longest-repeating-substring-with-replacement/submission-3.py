class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        d = {}
        m = 0
        for i, v in enumerate(s):
            
            window_len = i - l + 1
            if v not in d: 
                d[v] = 1
            elif v in d:
                d[v] +=  1
            
            # if window_len - max(d.values()) == k:
            #     m = max(m, window_len)
            if window_len - max(d.values()) > k:
                d[s[l]] -= 1 
                l += 1
                
            else:
                m = max(m, window_len)


        return m 



        


        