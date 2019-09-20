# Write a Python program for the Scrambled Words project on page 340 in the textbook. Submit a program file called scrambled_words.py.

# The input to your program is a name of a file consisting of one word (possibly with a punctuation attached to it) in each line.  
# The output of your program is a sequence of scrambled words (one space between words) followed by one new line at the end.

# When scrambling a word, use the following rules:

# The first and last letter in each word are unscrambled.
# If a punctuation is attached to a word (e.g. problem.), the punctuation is left untouched and does not count as the final unscrambled letter 
# (in the sequence problem. the letter m is the last letter that should not be scrambled). 
# When checking for punctuation letters, use string.punctuation (see page 253 in the textbook).
# Otherwise, the letters between the first and the last letter of a word should be scrambled by swapping adjacent letters (starting from the left).
# In your solution, you should only use material from chapters 0-6 in the textbook.  
# This means, for example, that lists cannot be used.

# It goes without saying, that readability is of prime importance in your solution.


# accept user input "filename"
# open and read file


def open_file(filename):
    file_object = open(filename, "r")
    return file_object

def read_file(file_object):
    for line in file_object:
        line = line.strip()
        line_len = len(line)
        counter = 0
        if line_len <= 3:
            print(line)
        else:
            for ch in line:
                if counter == 0:
                    new_line = ch
                if counter == (line_len-1) and line_len % 2 == 0:
                    new_line = new_line + ch
                if counter == (line_len-1) and line_len % 2 == 1:
                    new_line = new_line + move + ch
                elif counter % 2 == 1:
                    move = ch
                elif counter % 2 == 0 and counter != 0:
                    new_line = new_line + ch + move

                counter += 1
            print(new_line)
        #print(line, end="")

def write_file(file_object):
    create_file = open(user_input("Enter new file name: "), "w")
    for line in file_object:
        line = line.strip()
        print(line, file=create_file)

def user_input(promt):
    user_input = (input(promt))
    return user_input

def change_type(input, a_type):
    var = a_type(input)
    return var







def main():
    file_object = open_file(user_input("Enter filename: "))
    read_file(file_object)
    #write_file(file_object)

    file_object.close()



main()