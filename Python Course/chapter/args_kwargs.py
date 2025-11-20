#*args
def funarg(*argss):
    total = 0
    for num in argss:
        total += num
    return total
print(funarg(1,2,3)) #output: 6
# print(funarg(10,20,30,40)) #output: 100

#**kwargs
# def fnum1(**f_num):
#     for key, value in f_num.items():
#         print(f"{key}: {value}")
# fnum1(name="hello", age=25, city="Pune", Town="Manjari")

# Output: 
# name: hello
# age: 25
# city: Pune
# Town: Manjari

# *args&*kwargs used in same function
# def process_details(arg1, *args2, **arg3):
#     print(f"Fixed Arguments: -> {arg1}")
#     print(f"Positiinal Arguments: -> {args2}")
#     print(f"Keyword Arguments: -> {arg3}")
# process_details("Rajan", 1,1,2,3,4, name="Prashant", age=32, City="Pune", Town="Manjari")

#example
# def mufun(*kids):
#     print("The youngest chiks is " + kids[0])
# mufun("hello","rajan","prisha")

# def fun1(great, *names):
#     for name in names:
#         print(great, name)
# fun1("","Rajan","How","are", "you.")

####### Example1 #####
# def fun_total(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# print(fun_total(1,2,3,4,5,6))
# print(fun_total(10,20,30,40))
# print(fun_total(6))

####### Example2: Finding the maximum numbers #####
# def my_fun(*numbers):
#     if len(numbers) == 0:
#         return None
#     max_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num
# print(my_fun(3,7,2,9,1))
# def funn(*kids):
#     print("The Youngest child is " + kids[2]) ##why + was used here
#     print("Type: ", type(kids))
# funn("Prisha", "Rajan", "Tiwari")
    


# def myfun(*number1):
#     if len(number1) == 0:
#         return None
#     max_num = number1[0]
#     for num in number1:
#         if num > max_num:
#             max_num = num
#     return max_num

# print(myfun(3,10,98,32,0, 12, -1))

####### Example2: Finding the minmum numbers #####
# def funf(*numbers):
#     if len(numbers) == 0:
#         return None
#     min_num = numbers[0]
#     for num in numbers:
#         if num < min_num:
#             min_num = num
#         return min_num
# print(funf(87, 0, -12, 90))

# class Number:
#     def __init__(self, value):
#        self.value = value
# x = Number(21)
# y = Number(42)
# min(x, y)
# # Traceback (most recent call last):
# # TypeError: '<' not supported between instances of 'Number' and 'Number'
# max(x, y)
# Traceback (most recent call last):
# TypeError: '>' not supported between instances of 'Number' and 'Number'
