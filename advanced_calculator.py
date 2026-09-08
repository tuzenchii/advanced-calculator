print("Advanced Calculator 1.0 (Basic)")

def get_number(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
            continue
def calculate(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        if second_number != 0:
            return first_number / second_number
        else:
            print("Error: Division by zero is not allowed.")
            return None
    elif operation == "%":
        if second_number != 0:
            return first_number % second_number
        else:
            print("Error: Not allowed.")
            return None
    elif operation == "pow":
        return first_number ** second_number
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

        result = calculate(first_number, second_number, operation)

        if result is not None: #continues to print the result only if the operation was valid (not division by zero or invalid operation).
            print(f"{result:,g}")

        exit_input = input("Exit or go again? (Exit/Go Again): ")
        if exit_input.lower() == "exit":
            print(f"Goodbye, {first}!")
            running = False
            break
def equation():
    running = True
    while running:
        equation = input("Please enter your equation (ex. 2+2*(3-1)): ")
        try:
            result = eval(equation)
            print(f"{result:,g}")
        except Exception as error:
            print(f"Error. {error}")
            
        exit_input = input("Exit or go again? (Exit/Go Again): ")
        if exit_input.lower() == "exit":
            print(f"Goodbye, {first}!")
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
    method = input("What would you like to do? (Calculator/Equation): ")
    if method.lower() == "calculator":
        calculator1() #calls the calculator1 function to start the calculator program.
    elif method.lower() == "equation":
        equation() #calls the equation function to start the equation evaluator.
    else:
        print("Invalid option.")
else:
    print("Weirdo.")