class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = []
        sell = []

        for price in prices:
            # Buy: use the best sell profit from two days ago
            if not sell:
                buy.append(-price)
            else:
                prev_sell = sell[-2] if len(sell) >= 2 else 0
                buy.append(max(buy[-1] if buy else -price,
                               prev_sell - price))

            # Sell: use the best available buy
            if buy:
                sell.append(max(sell[-1] if sell else 0,
                                buy[-1] + price))

        return sell[-1] if sell else 0