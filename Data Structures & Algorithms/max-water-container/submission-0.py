class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # [1,7,2,5,4,7,3,6]

        l = 0
        r = len(heights)-1

        max_water = 0

        while r>l:
            minH = min(heights[l], heights[r])
            bottom = r - l

            temp_max = bottom * minH
            if temp_max > max_water:
                max_water = temp_max

            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l +=1
        print(max_water)
        return max_water

        