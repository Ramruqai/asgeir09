# Write a function that takes an integer as an argument
#  and returns True if the number is within the range 1 to 555 
# (not inclusive, i.e. neither 1 nor 555 are in range).


# Also write a statement that calls the function with the given input as an argument.
# Example input/output:

# The function definition goes here
def in_range(number):
    if number > 1 and number < 555: 
        return " is in range."
    else:
        return " is outside the range!"


num = int(input("Enter a number: "))

# You call the function here
print(num, in_range(num))