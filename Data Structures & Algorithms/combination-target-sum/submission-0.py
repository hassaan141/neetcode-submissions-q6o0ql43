class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(i, cres, total):

            if total == target:
                res.append(cres[:])
                return
            if i >= len(nums) or total > target:
                return
            
            #Dont
            backtrack(i + 1 , cres, total)

            # Do
            cres.append(nums[i])
            backtrack(i , cres, total + nums[i])
            cres.pop()
            
        backtrack(0, [], 0)
        return res
        


        

            