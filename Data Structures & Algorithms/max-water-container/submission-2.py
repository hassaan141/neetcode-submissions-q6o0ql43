class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # [1,7,2,5,4,7,3,6]
        max_area = 0
        l = 0
        r = len(heights) - 1

        while l<=r:
            
            base = r - l
            height = min(heights[l], heights[r])
            area = height * base
            
            if area>max_area:
                max_area = area
            elif heights[l] == min(heights[l], heights[r]):
                l = l + 1
            else:
                r = r - 1

        
        return max_area