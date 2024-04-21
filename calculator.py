start = input("What would you like to use? (add/a, subtract/s, multiply/m, divide/d, fractionalize/f, exponents/e?, pie/n) ")

if start == "a":
    x = float(input("What's x? "))
    y = float(input("What's y? "))

    z = (x + y)
    print(z)

elif start == "s":
    x = float(input("What's x? "))
    y = float(input("What's y? "))

    z = (x - y)
    print(z)

elif start == "m":
    x = float(input("What's x? "))
    y = float(input("What's y? "))

    z = (x * y)
    print(z)

elif start == "d":
    x = float(input("What's x? "))
    y = float(input("What's y? "))

    z = (x / y)
    print(z)

elif start == "e":
    def expm():
        x = int(input("What's x? "))
        print(f"x squared is, {square(x)}")

    def square(n):
        return n * n

    expm()

elif start == "f":
    numerator = int(input("What is numerator? "))
    denominator = int(input("What is denominator? "))

    print(f"{numerator} / {denominator}")

elif start == "n":
    print("pie or π is 3.14159")
else:
    print("Bro enter the right value/error in program.")
