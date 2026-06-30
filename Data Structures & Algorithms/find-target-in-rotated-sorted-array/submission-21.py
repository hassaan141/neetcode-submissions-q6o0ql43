class Solution:
    def search(self, nums: List[int], target: int) -> int:



        """
        nums [3, 4, 5, 6, 1, 2]
        target: number that you have to find    [5, 6, 1, 2, 3, 4]
                                                 l.    m.       r
        [3, 4, 5, 6, 1, 2].    t = 1/4
         l     m        r
         

        [3, 5, 6, 0, 1, 2].     
        l.     m.       r


        """
        
        l, r = 0, len(nums) - 1

        while l <= r: 

            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]:
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else:

                if nums[r] >= target and target >= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            
        
        return -1


        # l, r = 0, len(nums) -1
        
        # while l<=r:

        #     m = l + ((r - l) //2)

        #     if target == nums[m]:
        #         return m
        #     elif nums[l] <= nums[m]:
        #         if nums[l] <= target and target < nums[m]:
        #             r = m - 1
        #         else:
        #             l = m + 1

        #     elif nums[r] > nums[m]:
        #         if nums[m] < target and target <= nums[r]:
        #             l = m + 1
        #         else:
        #             r = m - 1 

        
        # return -1


        