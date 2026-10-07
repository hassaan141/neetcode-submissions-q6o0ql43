class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        out = {}

        for strr in strs:
            
            sorted_strr = "".join(sorted(strr))
            if sorted_strr not in out:
                out[sorted_strr] = [strr]
            elif sorted_strr in out:
                out[sorted_strr].append(strr)
        
        res = []
        for i in out.values():
            res.append(i)
        
        return res



        