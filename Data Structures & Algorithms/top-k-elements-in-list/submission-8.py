class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        out = []

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1
        
        a = list(d.items())
        c = sorted(a, key=lambda x: x[1])

        for i in range(k):
            
            b = c.pop()

            out.append(b[0])
        
        return out



        


    