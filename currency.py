

start = input("What are we converting to USD? (Enter currency code): ").strip().upper()
if start == "JPY":
    amount = input(f"Enter the amount in {start}: ")
    result = float(amount) * 0.0063


print(f"{amount} {start} is equal to {result} USD.")