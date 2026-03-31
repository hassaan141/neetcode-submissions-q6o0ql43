class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        out = {}
        for i in strs:

            a = {}

            for j in i:
                if j not in a:
                    a[j] = 1
                else:
                    a[j] = a[j] +  1
            
            a_tuple = tuple(sorted(a.items()))
            print(a.items())
            print(sorted(a.items()))
            print(a_tuple)
            
            if a_tuple not in out:
                out[a_tuple] = [i]
            else:
                incomplete_list = out[a_tuple]
                incomplete_list.append(i)
                out[a_tuple] = incomplete_list

        final=[]
        for i in out.values():
            final.append(i)
        
        return final