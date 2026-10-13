class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4, -1, -1, 0, 1, 2]        

        nums.sort()
        out = set()

        for i in range(0, len(nums)-1):

            l = i + 1
            r = len(nums) - 1

            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l = l + 1
                elif total > 0:
                    r = r - 1
                elif total == 0:
                    out.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
            
                    
        return [list(tupple) for tupple in out]
            
