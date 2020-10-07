from random import randint

# Random Password Generator
first_pin = randint(0, 9)
second_pin = randint(0, 9)
third_pin = randint(0, 9)

password = str(first_pin) + str(second_pin) + str(third_pin)

for number in range(1000):
    number += 1
    formatted_number = f"{number:03}"
    print(formatted_number)

    if formatted_number == password:
        print("The Password is {}".format(formatted_number))
        break

