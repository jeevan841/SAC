def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n= int(input("Enter n:"))
print(f"{n}th term in the fibonacci series is:",fibonacci(n))
