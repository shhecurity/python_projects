import math
    
denominations = [100, 50, 20, 10, 5, 1, .25, .10, .05, .01]
   
   
   
def optimal_change (tendered, price):
    change = []
    diff = tendered - price
    print(diff)
    if diff <= 0:
       change.append("no change")
       return change
    else:
            if  diff // 100 > 1:
                hundreds = diff // 100
                change.append(f"{hundreds} $100 bills")
            elif diff // 100 == 1:
                change.append("1 $100 bill")
            diff = diff%100
            if diff // 50 == 1:
                change.append("1 $50 bill")
            
            diff = diff%50
            if diff // 20 > 1:
                twenties = diff // 20
                twenties = math.trunc(twenties)
                change.append(f"{twenties} $20 bills")
            elif diff // 20 == 1:
                change.append('1 $20 bill')
            diff=round(diff,2)
            diff = diff % 20
            print(diff)
            if diff // 10 == 1:
                change.append("1 $10 bill")
            diff= diff % 10
            if diff // 5 == 1:
                change.append('1 $5 bill')
            diff = diff % 5
            if diff // 1 > 1:
                ones = diff // 1
                ones = math.trunc(ones)
                change.append(f"{ones} $1 bills")
            elif diff // 1 == 1:
                change.append("1 $1 bill")
            diff = diff % 1
            if diff // .25 > 1:
                quarters = diff // .25
                quarters = math.trunc(quarters)
                change.append(f"{quarters} quarters")
            elif diff // .25 ==1:
                change.append('1 quarter')
            print(diff)
            diff = diff % .25
            diff=round(diff,2)
            if diff // .10 > 1:
                dimes = diff // .1
                change.append(f'{dimes} dimes')
            elif diff // .1 ==1:
                change.append('1 dime')
            diff = diff % .1
            if diff // .05 == 1:
                change.append('1 nickel')
            diff = diff % .05
            diff=round(diff,2)
            if diff // .01 > 1:
                pennies = diff // .01
                pennies = math.trunc(pennies)
                change.append(f'{pennies} pennies' )
            elif diff // .01 == 1:
                change.append('1 penny')
                        
    if len(change)>1:
        last_change= str (change[-1])
        change= change[:-1] 
        change_string =  ', '.join(change)
        return f"The optimal change for an item that costs ${price} with an amount paid of ${tendered} is {change_string}, and {last_change}."          
    else: 
        change_string =  ', '.join(change)
        return f"The optimal change for an item that costs ${price} with an amount paid of ${tendered} is {change_string}."          

print (optimal_change(100,10))
print(optimal_change(100,20))

print(optimal_change(100,5))

print(optimal_change(100,50))

print(optimal_change(100,60))
   
print(optimal_change(5,1))
   
print(optimal_change(100,62.13))
print(optimal_change(1, .3))


print(optimal_change(100,49.49))