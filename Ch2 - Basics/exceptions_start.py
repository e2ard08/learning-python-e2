#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:


# TODO: Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together

# try:
#     x = 10 /0
# except:
#     print((" well that din't work!!"))



# TODO: You can also catch specific exceptions

try:
    answer = input( " what shoul I ivie 10 by ?")
    num = int (answer)
    print (10/num)
except ZeroDivisionError as e:
    print ("You can't divide by Zero!")
except ValueError as e:
    print ( " You don't give me a valid number!")
    print(e)
finally:
    print ( "This Code always runs")

