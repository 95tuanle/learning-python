# x = 10 / 0
# print(x)

# try:
#     x = 10 / 0
# except:
#     print("Well that didn't work!")

try:
    answer = input("What should I divide 10 by? ")
    num = int(answer)
    print(10 / num)
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero, silly.")
except ValueError as e:
    print(e)
    print("You must enter a number.")
finally:
    print("This will always run.")
