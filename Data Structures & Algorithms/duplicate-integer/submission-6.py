class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        original = []
        
        for i in nums:
            if i in original:
                return True
            else:
                original.append(i)
        
        return False