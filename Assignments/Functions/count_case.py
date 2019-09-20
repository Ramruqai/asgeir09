# Write a function named count_case that takes a string as an argument 
# and returns the count of upper case 
# and lower case characters 
# in the string (in that order). 

# Also write a statement that calls the function with the given input as an argument.

def upper(string) :
    count = 0
    for a in string:
        if (a.isupper()) == True: 
            count += 1
    return count

def lower(string) :
    count = 0
    for a in string:
        if (a.islower()) == True: 
            count += 1
    return count

# Your function definition goes here

user_input = input("Enter a string: ")

# Call the function here
print("Upper case count: ", upper(user_input))
print("Lower case count: ", lower(user_input))