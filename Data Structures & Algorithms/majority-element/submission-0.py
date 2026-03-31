class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        seen={}

        for i in nums:

            if i not in seen:
                seen[i] = 1
            else:
                seen[i] = seen[i] + 1
            
        maxOcc = max(seen.values())
        
        return next(k for k, v in seen.items() if v == maxOcc)
