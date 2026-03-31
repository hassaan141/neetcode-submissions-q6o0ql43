class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(i, cres):

            if i == len(nums):
                res.append(cres[:]) 
                return

            backtrack(i + 1, cres)

            cres.append(nums[i])
            backtrack(i + 1, cres)
            cres.pop()

        backtrack(0, [])
        return res