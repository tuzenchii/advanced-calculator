print("Advanced Calculator 1.0 (Basic)")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
            continue
def calculator1(): 

    running = True 
    while running:

        valid_operation = True #sets the variable valid_operation to True to start the loop in case division by zero is attempted.
        first_number = get_number("Enter the first number: ")
        while True:
            try:
                operation = input("Enter an operation (+, -, *, /, %, pow): ")
                if operation not in ["+", "-", "*", "/", "%", "pow"]:
                    raise ValueError("Invalid operation. Please enter a valid operation.")
                break
            except ValueError:
                print("Error: Invalid operation. Please enter a valid operation.")
                continue
        second_number = get_number("Enter the second number: ")

            
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
        elif operation == "%":
            if second_number != 0:
                result = first_number % second_number
            else:
                print("Error: Not allowed.")
                valid_operation = False 
        elif operation == "pow":
            result = first_number ** second_number

        if valid_operation: #continues to print the result only if the operation was valid (not division by zero or invalid operation).
            print(f"{result:,g}")

        exit_input = input("Exit or go again? (Exit/Go Again): ")
        if exit_input.lower() == "exit":
            print(f"Goodbye! {first}!")
            running = False
            break

start = input("Are you ready to start? (Yes/No): ")
if start.lower() == "yes":
    name = input("Let's begin. What is your name? ").strip().title() #strips any whitespace and capitalizes the first letter of the name.( name = name.strip().title() )
    parts = name.split(" ") #splits the name into first and last name based on the space between them.
    first = parts[0] #assigns the first element of the list to the variable first.
    if first.lower() == "tre'von":
        print("Oh it's the creator! Let's work.")
    elif first.lower() == "kirsten":
        print("Oh lala. The wife! Ready to begin? I doubt I know anything you don't.")
    else:
        print(f"Hello, {first}! Let's do some calculations.")
    calculator1() #calls the calculator1 function to start the calculator program.
else:
    print("Weirdo.")