'''Copy contents of one file into another'''

source_file = input("Enter the name of the source file:")
destination _file = input("Enter the name of the destination file:")

try:
    with open(source_file, 'r') as src:
        content = src.read()

    with open(descrition_file, 'w') as dest:
        dest.write(content)

    printf"Contents of '{source_file}' have been copied to '{destination}'  ")
except FileNotFoundError:
    print("Source file not found. Please check the file name and try again!")
