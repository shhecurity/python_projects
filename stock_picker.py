# take in list
#must buy before sell
#buy low, sell high
#can only buy and sell once
#return list of index of low buy, high sell in list
    

# def picker(prices):
#     max_profit = 0 #float("-inf")#or 0 
#     buy_sell_days = [0, 0]
    
#     for first_day, first_price, in enumerate(prices):
#         for second_day, second_price, in enumerate(prices):
#             if second_day <= first_day: continue
#             if second_price - first_price > max_profit:
#                 max_profit = second_price - first_price
#                 buy_sell_days = [first_day, second_day]
#     return buy_sell_days
#     #print('max profit:',max_profit)
            
# # print(picker([1,2,4]))

##above code is O n**2

def picker(prices):
    max_profit = 0 #float("-inf")#or 0 
    days = [0, 0]
    lowest_day = 0
    
    for current_day, current_price in enumerate(prices):
        if current_price <prices[lowest_day]:
            lowest_day = current_day
        if current_price - prices[lowest_day] > max_profit:
                max_profit = current_price - prices[lowest_day]
                days = [lowest_day, current_day]
    print(days)
    return days
    #print('max profit:',max_profit)