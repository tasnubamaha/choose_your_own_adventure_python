name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirty road. It has come to an end and you can go left or right. Which way would you like to go? "
).lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across. Type 'walk' to walk around and 'swim' "
                   "to swim across: ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross it or head back? Type 'cross' to "
                   "cross the bridge or 'back' to head back: ").lower()
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them? Type 'yes' to talk and "
                       "'no' to ignore: ").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignored the stranger and you lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")
