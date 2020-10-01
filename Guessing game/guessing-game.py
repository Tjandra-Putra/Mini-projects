from random import randint

total_guesses = 0
number_generator = randint(0, 10)

while True:
    user_input = int(input(">>>"))

    if user_input > number_generator:
        print("Guess lower!")
        total_guesses += 1

    elif user_input < number_generator:
        print("Guess higher!")
        total_guesses += 1

    else:
        print("You guessed the number! The number is {} \nYour total guesses is {}".format(str(number_generator), str(total_guesses)))
 

