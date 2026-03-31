class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # [10,1,5,6,7,1]

        # [10, 20, 1, 5]
        
        # 1
        # n = 10
        # p = 0
        # 2
        # n = 10
        # p = 10
        # 3
        # n = 1
        # p = 10
        # 4
        # n = 10
        # p = 10

        minN = prices[0]
        profit = 0

        for i in prices:

            if i > minN:
                if i - minN > profit:
                    profit = i - minN


            elif i < minN:
                minN = i

        return profit