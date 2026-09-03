print("Advanced Calculator 1.0 (Basic)")
name = input("Let's begin. What is your name? ")
if name.lower() == "tre'von":
    print("Oh it's the creator! Let's work.")
elif name.lower() == "kirsten":
    print("Oh lala. The wife! Ready to begin? I doubt I know anything you don't.")
else:
    print(f"Hello, {name}! Let's do some calculations.")

running = True #sets the variable running to True to start the loop.
while running:
    valid_operation = True #sets the variable valid_operation to True to start the loop in case division by zero is attempted.

    first_number = float(input("Enter the first number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    second_number = float(input("Enter the second number: "))

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            print("Error: Division by zero is not allowed.")
            valid_operation = False 
    else:
        print("Error: Invalid operation.")
        valid_operation = False
        
    if valid_operation: #continues to print the result only if the operation was valid (not division by zero or invalid operation).
        print(f"{result:g}")

    exit_input = input("Exit or go again? (Exit/Go Again): ")
    if exit_input.lower() == "exit":
        print("Goodbye!")
        running = False
        break


