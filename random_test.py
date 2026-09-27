import random

# def list(prompt):
#     return input(prompt).split(",")

# choice = random.choice(list("What you thinking? "))
# print(choice)

list = input("Enter a list of numbers separated by commas: ").split(",")
print(random.choice(list))