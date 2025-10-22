f = open("thetest.txt", "w")
f.write("always bumblee...")
f.close()

f = open("thetest.txt")
print(f.read())
