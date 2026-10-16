class Solution:
    def findMin(self, nums: List[int]) -> int:

        """


        1. 3 4 5 6 1 2 

           l   m     r   

        2. 3 4 5 6 1 2 

                 l m r

        3. 3 4 5 6 1 2 
                 l r 
                 m
                 
        4. 3 4 5 6 1 2 


        
        """

        l, r = 0, len(nums) - 1


        while l < r:
            
            m = l + (r-l) //2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
        return nums[l]

        