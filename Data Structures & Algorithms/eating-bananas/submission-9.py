import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        """
        have:
            piles = [1, 4, 3, 2]
            piles[i] is the amount of bananas in that pile
            h is the number of hours you have to eat
        
        want:    
            the minimum k is the banana eating speed
        
        example:

            piles = [1, 4, 3, 2] h = 9

            if speed is 1 b/h then takes 10 hour NOT GOOD
            if speed is 2b/h then takes 6 hours
            We can at if our eating speed is more than the bananas in the pile, we still take 1 hour
            
            max eating speed will be the max(piles)

            binary search from 1 to max(piles)

            [1, 2, 3, 4]

            max_eating_speed = 4

         
       """    
        min_eat_speed = math.inf

        max_eating_speed = max(piles)

        l = 1
        r = max_eating_speed

        while l <= r:

            m = l + ((r - l) // 2)
            print(f"m is {m}")

            total_hours = 0 
            for i in piles:
                total_hours += math.ceil(i / m)
            
            print(f"total hours is {total_hours}")
            if total_hours > h:
                l = m + 1
            elif total_hours <= h:
                r = m - 1
                min_eat_speed = min(min_eat_speed, m)

        
        return min_eat_speed

                

            









        