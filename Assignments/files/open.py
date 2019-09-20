def open_file(filename):
    file_object = open(filename, "r")
    return file_object

def read_file(file_object):
    for line in file_object:
        line = line.strip()
        line = line.replace(" ", "")
        print(line, end="")

def main():
    file_object = open_file("test.txt")
    read_file(file_object)

main()