def maxProfit(prices: List[int]) -> int:
        s_min, s_max = 10001, 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < s_min:
                s_min = prices[i]
                s_max = 0
            elif prices[i] > s_max:
                s_max = prices[i]
            if max_profit < s_max - s_min:
                max_profit = s_max - s_min
        return max_profit