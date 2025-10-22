filename = input("enter the filename:")
try:
    with open(filename,'r') as file:
        text = file.read()

    words = text.split()
    clean_words = [word.strip('.,!?()[]{}":;')
                   for word in words]
    unique_words = sorted(set(clean_words),
                          key = str.lower)
    for word in unique_words:
        print(word)
except FileNotFoundError:
    print("file not found, please check the file name and try again!")
