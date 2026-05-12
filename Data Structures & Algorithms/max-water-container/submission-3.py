class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_volume = 0

        l = 0
        r = len(heights) - 1


        while l < r:

            width = r-l
            height = min(heights[r], heights[l])
            volume = width * height

            max_volume = max(max_volume, volume)

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_volume


        