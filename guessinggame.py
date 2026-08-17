import random
secreat_number = random.randint(1,100)
attempt = 0
while True:
    guess = int(input("Guess number between 1 to 100:"))
    attempt=attempt+1
    if guess<secreat_number:
        print("too low!")
    elif guess>secreat_number:
        print("too high!")
    else:
        print("correct")
        print("you guessed in ",attempt,"attempts")
        break

