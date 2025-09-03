a=int(input("enter your first number:"))
b=int(input("enter your secound number:"))
c=int(input("enter your third number:"))

if a==b==c:
    print("all the three numbers are equal")
elif a>=b and a>=c:
    print(f"{a} is the greatest no.")
elif b>=a and b>=c:
    print(f"{b} is the greatest no.")
else:
    print(f"{c} is the greatest no.")
