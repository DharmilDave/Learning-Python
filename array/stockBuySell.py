def max_profit(stocks_price):
    min_price = min(stocks_price)
    index_of_min = stocks_price.index(min(stocks_price))
    temp_arr = stocks_price[index_of_min:len(stocks_price)+1]
    max_price = max(temp_arr)
    answer = max_price - min_price
    return answer


a = [7, 1, 5, 6, 2, 4]

print(max_profit(a))
