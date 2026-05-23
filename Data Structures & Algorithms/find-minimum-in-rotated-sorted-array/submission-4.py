class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
        Given
            nums = [3, 4, 5, 6, 1, 2].       [5, 6, 1, 2].    [6, 1, 2].  [6, 1]
                    l.    m        r          l. m     r       l. m. r     l. r

                   [5, 6, 1, 2, 3, 4]

                    l.    m        r 

                    [6, 1, 2, 3, 4, 5]
                    l.     m        r 
        Want
            min(nums)

        """
        
        l = 0
        r = len(nums) - 1

        if nums[l] <= nums[r]:
            return nums[l]

        while l<= r:

            m = l + ((r-l)//2)

            if l + 1 == r:
                return nums[r]
            elif nums[l] > nums[m]:
                r = m
            elif nums[r] < nums[m]:
                l = m        

