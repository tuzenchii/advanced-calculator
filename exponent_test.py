def exponent(base, exponent):
    return base ** exponent

base = float(input("Enter the base number: "))
exponent_value = float(input("Enter the exponent: "))
result = exponent(base, exponent_value)
print(f"{base:,g} raised to the power of {exponent_value:,g} is: {result:,g}")

