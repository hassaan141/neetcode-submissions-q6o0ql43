import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # [1,2,4,6]

        out = []
        for i in range(len(nums)):
            
            pref = nums[:i]
            suff = nums[i+1:]

            total_pref = math.prod(pref)
            total_suff = math.prod(suff)
            

            out.append(total_pref * total_suff)

        print(out)
        return out