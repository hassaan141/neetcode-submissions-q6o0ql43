class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # 2,20,4,10,3,4

        if len(nums) == 0:
            return 0
        
        set_nums = set(nums)
        consec = 1

        for i in nums:
            
            if i-1 in set_nums:
                continue
            else:
                temp = i
                temp_consec = 1
                while temp+1 in set_nums:
                    temp_consec += 1
                    temp += 1
                
                print(f"{temp_consec} for {i}")
                consec = max(temp_consec, consec)

        return consec  


        