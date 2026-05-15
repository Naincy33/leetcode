""""You are given an array prices where prices[i] is the price of a stock on the i-th day.You want to maximize your profit by choosing:
One day to buy the stock, and
A different day in the future to sell it.
Return the maximum profit you can achieve.
If no profit is possible, return 0"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price = float('inf')  # initially infinite
        max_profit = 0            # initially zero

        for price in prices:
            # update minimum price if a smaller price is found
            if price < min_price:
                min_price = price
            else:
                # calculate current profit
                profit = price - min_price
                # update max profit if this profit is higher
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit
obj = Solution()

# Example 1
prices1 = [7, 1, 5, 3, 6, 4]
print("Max Profit (Example 1):", obj.maxProfit(prices1))  # Output: 5

# Example 2
prices2 = [7, 6, 4, 3, 1]
print("Max Profit (Example 2):", obj.maxProfit(prices2))  # Output: 0