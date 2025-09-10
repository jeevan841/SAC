import math
def quadratic_roots(a,b,c):
    D = b**2 - 4*a*c
    if D > 0:
        root1 = (-b + math.sprt(D))/(2*a)
        root2 = (-b - math.sprt(D))/(2*a)
        return "Real and Distinct", (root1, ropot2)
    elif D == 0:
        root = -b /(2*a)
        return "Real and Equal", (root,)
    else:
        real = -b / (2*a)
        imag = math.sqrt(abs(D)) / (2*a)
        return "Imaginary", (f"{real}+{imag}j",f"{real}-{imag}j")
a= float(input("enter coefficient a:"))
b= float(input("enter coefficient b:"))
c= float(input("enter coefficient c:"))
nature, roots = quadratic_roots(a,b,c)
print("Nature of roots:", nature)
print("Roots:",roots)
