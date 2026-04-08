
"""

    - index is house
    - value is money in house
    - Cannot rob 2 adjacent houses, n-1 and n OR n and n + 1

    [                  ]

    ....    n-2   n-1   n 

    [ 2 , 9 , 8  , 3 ,  6 ]
             n-2  n-1   n 


    Ex 1: [  1     1      1     3  ]

    1   3.  1

    1   3

    if len(n) == 1
        return n
    if len(n) == 2:
        return max(n[0], n[1])
    
    n[i] = max(total[i - 2] + i , total[i - 1])

"""
        


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        total = [0] * len(nums)

        total[0] = nums[0]
        total[1] = max(total[0], nums[1])
        
        for i in range(2, len(nums)):

            total[i] = max(total[i-2] + nums[i], total[i-1])
            print(total)
        
        return total[-1]

        

        
