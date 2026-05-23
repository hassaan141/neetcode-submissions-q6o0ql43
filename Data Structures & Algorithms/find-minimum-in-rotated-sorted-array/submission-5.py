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

        mini = nums[l]

        while l<= r:

            if nums[l] <= nums[r]:
                mini = min(mini, nums[l])
                break

            m = l + ((r-l)//2)
            mini = min(nums[m], mini)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1 
        
        return mini

