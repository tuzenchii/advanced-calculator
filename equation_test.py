def equation_test():
    equation = input("Enter an equation (e.g., 2 + 2): ")
    try:
        result = eval(equation)
        print(f"The result of the equation '{equation}' is: {result:,g}")
    except Exception as e:
        print(f"Error evaluating the equation: {e}")

equation_test()