class Solution:
    def maxProfit(self, prices: list[int]) -> int: 
        cheapest = prices[0]
        best_profit = 0
        for x in prices:
            if x < cheapest:
                cheapest = x
            if x - cheapest > best_profit:
                best_profit = x - cheapest
        return best_profit
            
            

                

            
            
        

        
