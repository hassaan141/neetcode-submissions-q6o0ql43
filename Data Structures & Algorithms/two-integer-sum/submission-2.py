class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i, value in enumerate(nums):
            
            sec = target - value
            if sec in d:
                return [d[sec], i]
                
            d[value] = i

# {
#     3: 0,

# }
        