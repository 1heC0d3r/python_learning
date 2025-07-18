while True:
    calculationToPerform = (input("Enter the operation: ")).strip()
    if calculationToPerform.lower() == "sqrt":
        a = int(input("Enter the number: "))
    else:
        a, b = int(input("Enter the first number: ")), int(input("Enter the second number: "))
    if calculationToPerform == "+":
        print(a + b)
    elif calculationToPerform == "-":
        print(a - b)
    elif calculationToPerform == "*":
        print(a * b)
    elif calculationToPerform == "/":
        if b == 0:
            print("Division by zero is not accepted")
            continue
        else:
            print(a / b)
    elif calculationToPerform == "%":
        print(a % b)
    elif calculationToPerform == "**":
        print(a ** b)
    elif calculationToPerform.lower() == "sqrt":
        if a < 0:
            print("Negative number is not accepted")
        else:
            print(a ** 0.5)
    elif calculationToPerform == "//":
        print(a // b)
    else:
        print("Please enter a valid operation")
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != "y":
        break
    else:
        continue