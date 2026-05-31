import random
generate_no = random.randint(1,100)
while True:
    try:
        
        guess_no = int(input("make a guess between 1 and 100"))
        if guess_no > generate_no:
            print("too high guess again")
        elif guess_no < generate_no:
            print("too low guess again")
        elif guess_no == generate_no:
            print("congratulation you got it!")
            break
    except ValueError:    
        print("error")

