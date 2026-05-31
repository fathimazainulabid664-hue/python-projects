import random
while True:
    emojies = {"r":"🪨","p":"📜","s":"✂️"}
    choices = ["r","p","s"]
    user_choice = input("rock papper or scissor (r/p/s)")

    if user_choice not in choices:
        print("error")
        continue
    computer_choice = random.choice(choices)

    print(f"you choose {emojies[user_choice]}")
    print(f"computer choosed {emojies[computer_choice]}")

    if (user_choice == "r" and computer_choice == "s") or \
    (user_choice == "s" and computer_choice == "p") or \
    (user_choice == "p" and computer_choice == "r"):
        print("you won")
    elif (user_choice == computer_choice):
        print("tie")
    else:
        print("you lose")        
    should_continue = input("should continue or not (y/n)")
    if should_continue == "n":
        break