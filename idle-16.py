s = input("Enter a string:")

rev = ''
for ch in s:
    rev = ch + rev

if s == rev:
    print("PAlindrome")
else:
    print("not PAlindrome")
