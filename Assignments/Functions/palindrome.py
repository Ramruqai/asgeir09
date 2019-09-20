# palindrome function definition goes here
def palindrome(string):
    string2 = ""
    for char in string:
        if char.isalnum():
            string2 = string2 + char
    if string2 == string2[len(string2)::-1] :
        return "is a palindrome."
    else:
        return "is not a palindrome."






in_str = input("Enter a string: ")

# call the function and print out the appropriate message
print('"'+ in_str +'"',palindrome(in_str))