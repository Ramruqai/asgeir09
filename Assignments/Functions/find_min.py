# Write a function named find_min that takes two numbers as arguments and returns the minimum of the two.
# Also write a statement that calls the function using the given input as arguments.


# find_min function definition goes here
def min(a,b):
    min = a
    if b < min :
        min = b
    return min

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
# Call the function here
minimum = min(first, second)
print("Minimum: ", minimum)