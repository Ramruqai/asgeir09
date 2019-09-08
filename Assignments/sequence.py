# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

# Make sure that you write up the algorithm before starting to code.
# Then implement the algorithm in Python. Put your algorihmic description as a comment in the program file.



n = int(input("Enter the length of the sequence: ")) # Do not change this line

first = 1
second = 2
third = 3
sequence = 0

if n >= 1 :
    print(first)
if n >= 2 :
    print(second)
if n >= 3 :
    print(third)
if n >= 4 :
    while n > 3 :
        sequence = first + second + third
        print(sequence)
        first = second
        second = third
        third = sequence
        n -= 1

