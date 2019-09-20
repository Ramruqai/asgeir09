# The Fibonacci sequence is: 1, 1, 2, 3, 5, 8, 13, ...

# Write a function, fibo, to print the first N numbers of the Fibonacci sequence.  
# There should be one space between the elements.

# Also write a statement to call fibo.
# Your function definition goes here
def fib(n):
    if n == 1:
        fib = "1"
    if n == 2:
        fib = "1 1"
    if n > 2 :
        fib1 = 1
        fib2 = 1
        fib = "1 1"
        while n > 2:
            fib3 = fib1 + fib2
            fib = fib + " " +str(fib3)
            fib1 = fib2
            fib2 = fib3
            n -= 1
    return fib   


n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here        
print(fib(n))