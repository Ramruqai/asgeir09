# Design an algorithm that finds the maximum positive integer input by a user.  The user repeatedly inputs numbers until a negative value is entered.
# adding a change to test git.


max_int = 0

while True:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int < 0 :
        break
    elif num_int > max_int :
        max_int = num_int
    continue
print("The maximum is", max_int)    # Do not change this line