import random
def getlist(prompt):
    while True:
        try:
            user_input = input(prompt)
            items = [item.strip() for item in user_input.split(",") if item.strip()]
            if not items:
                raise ValueError("Error: No valid items entered.")
            return items
        except ValueError as e:
            print(e)
            
print("Randomly selected item: ", random.choice(getlist("What are you thinking about eating? (Enter items separated by commas): ")))
