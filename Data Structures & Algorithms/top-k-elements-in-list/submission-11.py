class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # [1, 2, 2, 3, 3, 3]    2/3

        out = []
        d = {}

        for num in nums:

            if num not in d:
                d[num] = 1
            else:
                d[num] = d[num] + 1
        
        print(d.items())
        a = sorted(d.items(), key=lambda item: item[1])

        for i in range(k):
            out.append(a[-i-1][0])
        
        return out
            


        return [7]
