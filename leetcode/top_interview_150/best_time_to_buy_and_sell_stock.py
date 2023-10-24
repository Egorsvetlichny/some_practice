# task 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        sorted_list = sorted(prices, reverse=True)
        if prices == sorted_list:
            return 0
        else:
            min_price = prices[0]
            max_profit = 0

            for price in prices:
                if min_price >= price:
                    min_price = price
                elif price - min_price > max_profit:
                    max_profit = price - min_price

        return max_profit


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    prices = [7, 1, 5, 3, 6, 4]
    assert solution.maxProfit(prices) == 5

    # test case 2
    prices = [7, 6, 4, 3, 1]
    assert solution.maxProfit(prices) == 0
