
def amount(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid input.")
def calculate():
    print(f"{currency_amount:,g} {start} is equal to {result:,g} USD.")

while True:
    start = input("What are we converting to USD? (Enter currency code): ").strip().upper()

    if start not in ["JPY", "YEN", "CNY", "YUAN"]:
        print("Invalid currency code.")
        continue

    if start in ["JPY", "YEN"]:
        currency_amount = amount(f"Enter the amount in {start}: ")
        result = float(currency_amount) * 0.0063
        calculate()
        break

    if start in ["CNY", "YUAN"]:
        currency_amount = amount(f"Enter the amount in {start}: ")
        result = float(currency_amount) * 0.15
        calculate()
        break
