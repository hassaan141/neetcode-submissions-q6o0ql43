class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited = {}

        for i, v in enumerate(nums):
            
            check = target - v

            if check in visited:
                return [visited[check], i]
            else:
                visited[v] = i


            




        