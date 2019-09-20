def start_graphic(number):
    #Draw the first graphic
    start_graphic = "oxxxxxxxxx"
    for i in range(1,number):
        start_graphic = "x" + start_graphic
    return start_graphic[0:10]

def left(draw_graphic):
    #Move the "o" to the left
    draw_graphic = draw_graphic + "x"
    return draw_graphic[1:11]

def right(draw_graphic):
    #Move the "o" to the right
    draw_graphic = "x" + draw_graphic
    return draw_graphic[0:10]

#user input
start_pos = 0
while start_pos < 1 or start_pos > 10:
    start_pos = int(input("Input a position between 1 and 10: "))

#draw the initial graphic and user instructions
draw_graphic = start_graphic(start_pos)
print(draw_graphic)
print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")

#run program until invalid input
while True:
    move = input("Input your choice: ")
    #move left
    if move == "l":
        draw_graphic = left(draw_graphic)
        #check for left boundary
        if draw_graphic == "xxxxxxxxxx" :
            draw_graphic = "oxxxxxxxxx"
            print(draw_graphic)
        else:    
            print(draw_graphic)
    #move right
    elif move == "r":
        draw_graphic = right(draw_graphic)
        #check for right boundary
        if draw_graphic == "xxxxxxxxxx" :
            draw_graphic = "xxxxxxxxxo"
            print(draw_graphic)
        else:    
            print(draw_graphic)
    #invalid input: end program
    else:
        print(draw_graphic)
        break

