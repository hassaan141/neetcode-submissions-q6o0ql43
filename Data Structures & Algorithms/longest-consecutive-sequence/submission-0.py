class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ret = []
        s = set(nums)
        # [2, 3, 4, 5, 10, 20]
        for i in s:
            if (i -1) in s:
                continue
            else:
                temp = [i]
                idx = i
                while (idx + 1) in s:
                    idx +=1
                    temp.append(idx)
                
                if len(temp) > len(ret):
                    ret = temp
                
        return len(ret)



        