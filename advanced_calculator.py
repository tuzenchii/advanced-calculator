print("Advanced Calculator 1.0 (Basic)")
name = input("Let's begin. What is your name? ")
if name.lower() == "tre'von":
    print("Oh it's the creator! Let's work.")
elif name.lower() == "kirsten":
    print("Oh lala. The wife! Ready to begin? I doubt I know anything you don't.")
else:
    print(f"Hello, {name}! Let's do some calculations.")

running = True #sets the variable running to True to start the loop.
while True: #identifying the loop for later.
    first_number = float(input("Enter the first number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    second_number = float(input("Enter the second number: "))

    if operation == "+":
        result = first_number + second_number
        print(f"{result}")
    elif operation == "-":
        result = first_number - second_number
        print(f"{result}")
    elif operation == "*":
        result = first_number * second_number
        print(f"{result}")
    elif operation == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error: Division by zero is not allowed."
    else:
        result = "Error: Invalid operation."

    exit_input = input("Exit or go again? (exit/go again): ")
    if exit_input.lower() == "exit":
        print("Goodbye!")
        running = False
        break #breaks the loop and ends the program due to the user inputting "exit".
    elif exit_input.lower() == "go again":
        running = True #continues the loop and allows the user to perform another calculation.