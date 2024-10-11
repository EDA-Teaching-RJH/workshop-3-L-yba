print("lets play a guessing game")
import random

secret_number = random.randint(0,10)

number = int(input("Guess the number"))
if number==secret_number:
    print("correct")
elif number<secret_number:
    print("Too low")
elif number>secret_number:
    print("Too high")
