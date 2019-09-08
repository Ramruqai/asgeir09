# Problem solved by Ásgeir Atlason - asgeir09@ru.is
# Write a Python program that:
# Finds and prints all positive two digit numbers whose square of the sum of its digits is equal to the number.
# Finds and prints all positive numbers < 100 with exactly 10 divisors.
# Each number, fulfilling the above conditions, found by the program is printed out in a separate line.

# Your program should have the name numbers.py
# Make sure you think about and write down an algorithm for the problem before you start coding!

#Finds and prints all positive two digit numbers whose square of the sum of its digits is equal to the number.
for number in range(10,100) :
    if (number % 10 + number//10)**2 == number :
        print(number)

#Finds and prints all positive numbers < 100 with exactly 10 divisors.
count = 0
for num in range(1,100) : #Loops through all positive numbers from 1 to 99.
    if count == 10 : #If number has 10 divisors, print the number.
        print(number_10)
    count = 0
    number_10 = num
    for divisor in range(1, num+1) : #Counts divisors of a number.
        if num % divisor == 0 :
            count += 1