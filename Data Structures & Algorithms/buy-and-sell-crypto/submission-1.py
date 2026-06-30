class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        """
        1. 
        min 10

        2.

        min 1 


        3.
        min 1 
        diff 4 

        4. 
        min 1 
        diff 5 

        5. 
        min 1 
        diff 4 

        6. 

        10,1,5,6,7,1

           b.    s

        """

        min_val = prices[0]
        max_profit = 0

        for r in range(1, len(prices)):

            if prices[r] < min_val:
                min_val = prices[r]

            else:
                max_profit = max(prices[r] - min_val, max_profit)


        return max_profit

        