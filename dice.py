import random
while True:

    message=input("roll the dice (y/n)")
    if message == "y":
        dice1 = random.randint(1,6 )
        dice2 = random.randint(1,6 )
        print(f'({dice1},{dice2})')
    elif message == "n":
       print("thank you")
       break
    else:
        print("invalid choice")

  