'''
Problem solved by Ásgeir Atlason asgeir09@ru.is
Write a program, move.py, which asks the user for the position of a virtual character on the x-axis in a coordinate system 
and then allows the user to move the virtual character to the right or left, indicated by the characters 'r'  or 'l'.
The user should be able to move the virtual character as often as he/she wishes, but if the input is neither 'r' nor 'l' the program quits.
Instructions for the user are written out at the beginning, but the position of the virtual character (denoted by 'o') is shown in each iteration.

The valid range on the x-axis, which the virtual character can traverse, is from 1 to 10 and you can assume that at the beginning the user inputs a number in this range.
If the virtual character is positioned at either end of the range it will not move when the user tries to move it out of the range.

In your solution, you should only use methods/material discussed in the first five chapters in the textbook.
This means, for example, that you are not allowed to use lists.
Make sure that your code is very readable (see, for example, this thread). 

Note the following:
The numbers 1 and 10, which signify the range, should be implemented as constants. In Python, a constant is a variable whose value will not change in the program.
It is a good rule to use capital letters for naming constants.
You must use functions in your implementation. It is fine that your main program contains the loop, but the body of the loop should, in most part, be a series of function calls.
Example input/output is below.  Your output should be exactly the same.
Example input/output:
'''

MAX_L_VALUE = 1
MAX_R_VALUE = 10

def draw(position):
    ''' draws the string with "o" in position specified by parameters given. '''
    string = ""
    for i in range(MAX_L_VALUE, MAX_R_VALUE+1):
        if i == position:
            string = string + "o"
        else:
            string = string + "x"
    return string

def check(position):
    ''' Returns number if it is within the parameters of constants, otherwise give closest legal value. '''
    if position > MAX_R_VALUE:
        return MAX_R_VALUE
    elif position < MAX_L_VALUE:
        return MAX_L_VALUE
    else:
        return position

#User input and print inscructions for user.
position = int(input("Input a position between 1 and 10: "))
position = check(position)
print(draw(position))
print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")

while True:
    '''Main program, moves "o" according to user input. '''
    move = input("Input your choice: ")
    if move == "l":
        position -= 1
        position = check(position)
        print(draw(position))
    elif move == "r":
        position += 1 
        position = check(position)
        print(draw(position))
    else:
        position = check(position)
        print(draw(position))
        break