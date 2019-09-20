my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
#print("The binary of", my_int, "is", bin_str)

bin_str = ""
quotient = my_int

if my_int == 0:
    bin_str = 0
else:
    while quotient > 0:
        my_bit = quotient % 2
        quotient = quotient // 2
        bin_str = str(my_bit) + bin_str
    
print("The binary of", my_int, "is", bin_str)