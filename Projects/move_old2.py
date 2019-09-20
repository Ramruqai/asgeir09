#draws the string with "o" in position specified by parameters given.
def draw(position):
    string = ""
    for i in range(1, 11):
        if i == position:
            string = string + "o"
        else:
            string = string + "x"
    return string


position = int(input("Input a position between 1 and 10: "))
print(draw(position))
print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")

MAX_L_VALUE = 1
MAX_R_VALUE = 10

#Main program, moves "o" according to user input.
while True:
    move = input("Input your choice: ")
    if move == "l":
        position -= 1
        #Check for illegal position of "o"
        if position < MAX_L_VALUE:
            position = MAX_L_VALUE
        print(draw(position))
    elif move == "r":
        position += 1
        #Check for illegal position of "o"
        if position > MAX_R_VALUE:
            position = MAX_R_VALUE
        print(draw(position))
    else:
        print(draw(position))
        break