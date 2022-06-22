
import math
    
   
def optimal_change (price, tendered):
    change = []
    diff = tendered - price
    if diff <= 0:
       return "no change"
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
            diff = diff % 20
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
            diff = diff % .25
            if diff // .10 > 1:
                dimes = diff // .1
                dimes = math.trunc(dimes)
                change.append(f'{dimes} dimes')
            elif diff // .1 ==1:
                change.append('1 dime')
            diff = diff % .1
            diff=round(diff,2)
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
   #make the change list into an array.  If the legnth of change list is greater than one, break off the last element 
   # to add 'and' before returning it. else return the list.                     
    if len(change)>1:
        last_change= str (change[-1])
        change= change[:-1] 
        change_string =  ', '.join(change)
        return f"The optimal change for an item that costs ${price} with an amount paid of ${tendered} is {change_string}, and {last_change}."          
    else: 
        change_string =  ', '.join(change)
        return f"The optimal change for an item that costs ${price} with an amount paid of ${tendered} is {change_string}."          


