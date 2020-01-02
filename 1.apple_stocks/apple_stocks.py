def get_max_profit(stock_prices: list) -> list:

    max_profit, min_price = float("-inf"), stock_prices[0]

    if len(stock_prices) <= 2:
        raise ValueError("It Requires 2 numbers to calculate the best profit!")

    for price in range(1, len(stock_prices)):
        current_price = stock_prices[price]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)
    return max_profit
