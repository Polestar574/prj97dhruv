import random

random_number= random.randint(1,9)
chances=5
username=input("what is your Username")
print("Hello",username+",",)
question=input("Let's play a game or not? [Y/N]")
if question == "n":
    print("oh..okay")
if question == "y":
    print("I'm Thinking Of A Number Between 1 & 9")
    guess = int(input("Have a Guess :"))
if guess > random_number:
        print("Guess Lower...")
if guess < random_number:
        print("Guess Higher...")
 
while guess != random_number:
       chances += 5
guess = int(input("Try Again : "))
if guess <random_number:
            print("Guess Higher...")
if guess == random_number:
        print("You're Right! you win! The Number Was", random_number, "and it only",chances, "chances!")