import random

def versionOne():
    user_input = ""
    point_count = 0
    while user_input != "EXIT":
        random_number = random.randint(1, 11)
        while (user_input != random_number):
            user_input = input("Input a number and I'll tell you if you're hot or cold: ")
            try:
                user_input = int(user_input)
                if user_input > random_number:
                    print("you're too high")
                elif user_input < random_number:
                    print("you're too low")
                else:
                    print("you got it right!")
                    point_count += 1
            except ValueError:
                if user_input.upper() == "EXIT":
                    user_input = user_input.upper()
                    break
                else:
                    print("you need to input a number or type \"exit\"!")
    print("you got {} points".format(point_count))

def versionTwo():
    user_input = ""
    point_count = 0
    random_number = random.randint(1,11)
    while user_input != "EXIT":
        user_input = input("Input a number and I'll tell you if you're hot or cold: ")
        try:
            user_input = int(user_input)
            if user_input > random_number:
                print("you're too high")
            elif user_input < random_number:
                print("you're too low")
            else:
                print("you got it right!")
                point_count += 1
                random_number = random.randint(1,11)
        except ValueError:
            if user_input.upper() == "EXIT":
                user_input = user_input.upper()
                break
            else:
                print("you need to inpute a number or type \"exit\"!")

versionOne()
versionTwo()