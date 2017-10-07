#!/usr/bin/python
'''
Write an efficient function that takes stock_prices_yesterday and returns the best profit
I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday
Example :  [10, 7, 5, 8, 11, 9] return 6 (buying for $5 and selling for $11)
'''
def get_max_profit(stock_prices):

    if len(stock_prices) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    min_price,max_profit = stock_prices[0],stock_prices[1] - stock_prices[0]
    for i in range(1,len(stock_prices)):
        max_profit = max(max_profit, abs(stock_prices[i]-min_price))
        min_price  = min(min_price, stock_prices[i])
    return max_profit


def get_max_profit1(stock_prices):

    if len(stock_prices) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    min_price,max_price = stock_prices[0],stock_prices[0]
    for i in range(1,len(stock_prices)):
        max_price = max(max_price, stock_prices[i])
        min_price  = min(min_price, stock_prices[i])

    print max_price
    print min_price
    return max_price-min_price

print(get_max_profit([165,151,150,143,122]))
print(get_max_profit([112,123,114,115,119,120,121,132,142]))
print(get_max_profit([10, 7, 5, 8, 11, 9]))

print(get_max_profit1([165,151,150,143,122]))


