def basic_calculator():
    print("Welcome to the Basic Calculator!")

    # Step 1: Ask for the first number
    num1 = float(input("Enter the first number: "))

    # Step 2: Ask for the second number
    num2 = float(input("Enter the second number: "))

    # Step 3: Ask for the mathematical operation
    operation = input("Enter an operation (+, -, *, /): ").strip()

    # Step 4 & 5: Check the operation and perform calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Step 6: Handle division carefully
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operation entered!")
        return

    # Step 7: Display the result
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    basic_calculator()
