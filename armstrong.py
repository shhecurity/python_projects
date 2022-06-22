def find_armstrong_numbers(numbers):
    armstrong= []
    for num in numbers:
        exponent=len(str(num))
        sum=0
        temp=num 
        while temp>0:
            digit= temp%10
            sum+=digit**exponent
            temp//=10
        if num == sum:
            armstrong.append(num)
    return armstrong

print(find_armstrong_numbers(list(range(0, 999))))