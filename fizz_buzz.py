#write a program that returns the numbers from 1 to 100, but for multiples of 3 return "Fizz" instead of the number and for multiples of 5 return "Buzz" instead of the number.  For numbers that are multiples of both three and five, return "FizzBuzz" instead of the number.
def fizzbuzz():
    nums=[]
    for i in range(1,101):
        if i % 3==0 and i %5==0:
            nums.append('Fizzbuzz')
        elif i % 3==0:
            nums.append('Fizz')
        elif i % 5 == 0:
            nums.append('Buzz')
        else:
            nums.append(i)

    return nums

    