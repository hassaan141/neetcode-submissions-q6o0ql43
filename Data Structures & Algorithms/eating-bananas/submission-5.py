import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # needs to be 2

        # [1, 2, 3, 4, 5, 6, 7]
        #  l. m  r

        max_rate = max(piles)
        min_speed = max_rate

        l = 1
        r = max_rate

        while l<=r:

            m = (l + r) // 2
        
            total_hours = 0
            for j in piles:
                total_hours += math.ceil(j / m)
            print(total_hours)
            if total_hours <= h:
                min_speed = min(m, min_speed)
                r = m - 1
            elif total_hours > h:
                l = m + 1

        return min_speed

        
