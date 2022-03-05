def add(a, b):
    print(f"{a} + {b} = {a+b}\n")
    return a+b

def subtract(a, b):
    print(f"{a} - {b} = {a-b}\n")
    return a-b

def multiply(a, b):
    print(f"{a} x {b} = {a*b}")
    return a*b

def divide(a, b):
    print(f"{a} / {b} = {a+b}\n")
    return a/b

def floor(a, b):
    print(f"{a} // {b} = {a // b}\n")
    return a//b

def modulus(a, b):
    print(f"{a} % {b} = {a % b}\n")
    return a%b

def exponent(a, b):
    print(f"{a} ** {b} = {a ** b}\n")
    return a**b



print("Lets do some maths functions!\n")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
shoe_size = floor(10, 3)
blindness = modulus(10, 3)
speed = exponent(2, 500)


print(f"\n\nAge = {age}, Height = {height}, Weight = {weight}, IQ = {iq}, Shoe Size = {shoe_size}, Blindness = {blindness}, Speed = {speed}")