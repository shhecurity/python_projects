# args = arguments, aka parameters, for functions/methods
#kwargs = keyword arguments

# def my_fun_function(a,b):
#     print(a)
#     print(b)
    

# x = 'hello'
# y='world'
# my_fun_function(x,y)
    
    #with default params:
def my_fun_function(first = "",second="", third = 'something'):
    print(first)
    print(second)
    print(third)
    

# x = 'hello'
# y='world'
# z='and Zivs'
# my_fun_function(x,y,z)

foods = {
    "first": 'watermelon',
    "second": 'ice cream',
    "third": 'hamburgers'   
}
# **foods =>( "i" = 'watermelon") ("j" = 'ice cream') ("k" = 'hamburgers')
# my_fun_function(foods["i"], foods["j"], foods["k"])

my_fun_function(**foods)
# my_fun_function(second='ice cream', third='hamburgers', first='watermelon')