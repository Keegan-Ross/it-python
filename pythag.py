import math
from banner import banner

banner("PYTHAGOREAN CALCULATOR", "Keegan Ross")

print("We will help you find the missing side of a right triangle. The lengths of the two legs are 'a' and 'b', and the length of the hypotenuse is 'c'.")

print("Please enter the length of each side, or leave it blank if you don't know.")
a=0
b=0
c=0
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a==0:
    z = c * c
    y = b * b
    x = z - y
    a = math.sqrt(x)
    print(f"Your missing side is a and it's length is {a}")
elif b==0:
    z = c * c
    x = a * a
    y = z - x
    b = math.sqrt(y)
    print(f"Your missing side is b and it's length is {b}")
elif c==0:
    x = a * a
    y = b * b
    z = x + y
    c = math.sqrt(z)
    print(f"Your missing side is c and it's length is {c}")