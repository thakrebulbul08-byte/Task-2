while True:
    a = input("Enter first number (or C to clear): ")

    if a.lower() == "c":
        print("Cleared!")
        continue

    try:
        a = float(a)
        op = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            print("Result:", a / b if b != 0 else "Cannot divide by zero")
        else:
            print("Invalid operator")

    except ValueError:
        print("Please enter valid numbers.")