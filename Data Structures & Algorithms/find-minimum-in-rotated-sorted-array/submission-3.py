class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0 
        r = len(nums) - 1

        while l<=r:

            m = (l + r) // 2
            print(nums[m])

            if nums[l] <= nums[r]:
                return nums[l]

            if l + 1 == r:
                return nums[r]
            elif nums[l] > nums[m]:
                r = m 
            elif nums[l] < nums[m]:
                l = m 
    


