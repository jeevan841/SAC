def add(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b!= 0:
        return a / b
    else:
        return "Error! Division by Zero."

print("Simple Calculator")
a = int(input("Enter first number: "))
b = int(input("Enter secound number:"))

print("Addition:", add(a,b))
print("subtraction:", subtraction(a,b))
print("multiply:", multiply(a,b))
print("divide:",divide(a,b))
