class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4, -1, -1, 0, 1, 2]        

        nums.sort()
        out = []

        for i in range(0, len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1
            inside_out = []

            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l = l + 1
                elif total > 0:
                    r = r - 1
                elif total == 0:
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while  nums[l] == nums[l -1] and l < r:
                        l += 1
                    
        return out
            






