# def divide(x, y):
#     # x = int(input("Enter the X value in Interger: "))
#     # y = int(input("Enter the y value in interger: "))
#     try: 
#         x = int(input("Enter the X value: "))
#         y = int(input("Enter the y value: "))
#         result = x // y
#         print("Your Answer is ", result)
#     except ZeroDivisionError:
#         print("Sorry! You are dividing by Zero")
# divide(3, 2)
# divide(3, 0)
# ##################################################################
# # Python code to illustrate working of try()  
# def divide(x, y): 
#     try: 
#         # Floor Division : Gives only Fractional
#         # Part as Answer 
#         result = x // y 
#         print("Yeah ! Your answer is :", result) 
#     except ZeroDivisionError: 
#         print("Sorry ! You are dividing by zero ") 
  
# # Look at parameters and note the working of Program 
# divide(3, 2) 
# divide(3, 0)
# ##################################################################
# try:
#     # print(x)
#     print("Datbase Connected Susscees Fully")
# except NameError:
#     print("Something Went Wrong")
# finally:
#     print("Nothing Went Wrong")
 ##################################################################
# try:
#     x = int(input("Enter a number: "))
#     result = 10 // x
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# ##################################################################
# def divide(x, y):
#     try:
#         result = x // y 
#     except ZeroDivisionError:
#         print("Sorry! U r dividing by Zero")
#     else:    
#         print("Your Answer is: ", result)
#     finally:
#         print("This is always executed")
# divide(3, 2)
# divide(3, 0)
# ##################################################################
x = 7
if not type(x) is int:
    raise TypeError("Only integers are allowed")
import demo
# ##################################################################