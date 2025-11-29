# Secret number is set manually
secret_number = 17
max_attempts = 5
attempt = 1
guessed = False

print("Welcome to the Number Guessing Game...!")
print("Guess the number between 1 and 25.")
print("You have", max_attempts, "attempts.")

while attempt <= max_attempts:
    user_guess = input("Attempt " + str(attempt) + ": Enter your guess: ")
    guess = int(user_guess)

    if guess == secret_number:
        print(" Correct! You guessed the number in", attempt, "attempts.")
        guessed = True
        attempt = max_attempts + 1  
    elif guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(" Invalid input.")

    attempt = attempt + 1

# After the loop
if guessed == False:
    print(" You didn't guess the number. It was:",secret_number)
