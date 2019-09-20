def open_file(filename):
    file_object = open(filename, "r")
    return file_object

def read_file(file_object):
    longest = ""
    for lines in file_object:
        lines = lines.strip()
        if len(lines) > len(longest):
            longest = lines
    print("Longest word is '" + longest +"' of length", len(longest))

#def find_longest(word):


def main():
    file_object = open_file(input("Enter filename: "))
    read_file(file_object)


main()