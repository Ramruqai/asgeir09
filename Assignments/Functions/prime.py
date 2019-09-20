# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
# Write a function named is_prime that takes an integer argument and returns True if the number is prime and False otherwise. 
# (Assume that the argument is an integer greater than 1, i.e. no need to check for erroneous input.)

# Also write code that calls the function and prints out a message saying that the given number is a prime or not.

# Example input/output:


# is_prime function definition goes here
def prime(number):
    prime = True
    for x in range(2,number):
        if number % x == 0:
            prime = False
    if prime == True :
        return " is a prime"
    else :
        return "is not a prime"
        



num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
print(num, prime(num))