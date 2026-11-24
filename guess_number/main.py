import random
secret_number = random.randint(1, 100)




guess = int(input("Guess a number between 1 and 100: "))


while guess != secret_number and guess > 0:
    if guess < secret_number:
        print("you guesed too low" , end =" ")
        guess = int(input("enter bigger number: "))
    elif guess > secret_number:
        print("your guesed too high" , end = " ")
        guess = int(input("enter smaller number: "))
    if guess == secret_number:
        print("you win" , secret_number)


