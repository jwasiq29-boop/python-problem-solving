import random
secret_number = random.randint(1, 100)

def guess_number():
    guess = int(input("Guess a number between 1 _100: "))
    if guess <= 0:
        while True:
            print("Plase enter the postive number" , end =" ")
            guess = int(input("Guess a postive number plase: "))
            if guess > 0:
                break
    return guess

def guess_check():
    check = guess_number()

    while check != secret_number:
        if check < secret_number:
            check = int(input("your number is smaller, enter bigger number: "))
        elif check > secret_number:
            check = int(input("your number is bigger, enter smaller number: "))
        if check == secret_number:
            return "you win" , secret_number
        
print(guess_check())

