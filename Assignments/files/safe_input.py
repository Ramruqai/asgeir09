# Here is the definition of safe_input. It should contain this exception:
def safe_input(safe_input, a_type):
    while True:
        try:
            change = a_type(input(safe_input))
            return change
        except ValueError:
            print("Error: please enter a value of", a_type)

# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))


