import random

user_input = ''
while user_input != "exit":
    user_input = input("Decide what you want, press A for 4, B for 6 sided dice, c for 12 sided, d for 20 sided enter to roll, type exit to stop the program: ")
    user_input = user_input.lower()
    dice_dict = {
        "a": 4,
        "b": 6,
        "c": 12,
        "d": 20,
        "e": 30,
        "f": 100
    }
    if user_input in dice_dict:
        print(random.randint(1, dice_dict[user_input]))
    elif user_input != "exit":
        print("no")
