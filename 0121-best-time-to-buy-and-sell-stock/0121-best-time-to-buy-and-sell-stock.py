class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        lowest_buy_price = float("inf")

        for day in range(len(prices)-1):
            buy = prices[day]
            sell = prices[day+1]

            if buy < lowest_buy_price:
                lowest_buy_price = buy 

            profit = sell - lowest_buy_price

            if profit > max_profit:
                max_profit = profit

        return max_profit
        
        