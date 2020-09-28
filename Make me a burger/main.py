from random import randint
from datetime import datetime

ingredients = {'B': 2, 'C': 1.50, 'P': 3, 'V': 1.20, 'O': 0.5, 'M': 1}

print("----------MENU----------")
print("Select your ingredients: \n'B' stands for a piece of bun - $2 \n'C' stands for cheese - $1.50 \n'P' stands for "
      "patty "
      "- $3 \n'V' stands for veggies - $1.20 \n'O' stands for onions - $0.50 \n'M' stands for mushroom - $1")
print("------------------------")

total_price = 0
counter_buns = 0
selected_ingredients = []
available_ingredients = []

for key, value in ingredients.items():
    available_ingredients.append(key)

while True:
    customer_input = input("Select ingredient: ").upper()

    if customer_input in available_ingredients:
        selected_ingredients.append(customer_input)

        # Calculate total price
        for key, value in ingredients.items():
            if customer_input == key:
                total_price += value

        # Count total buns, minimum two
        if customer_input == "B":
            counter_buns += 1

        print("Your ingredients: {}, Total Price: ${}".format(selected_ingredients, total_price))
        print("BUNS: " + str(counter_buns))

    elif customer_input == "Q":
        if total_price < 5:
            print("ERROR: Minimum amount must be $5")

        if counter_buns < 2:
            print("ERROR: Minimum 2 buns")

        elif total_price >= 5 and counter_buns >= 2:
            print("ORDER CONFIRMED")
            print("---------RECEIPT---------")
            print("Your order number is {}".format(str(randint(1, 200))))
            print("Selected ingredients: {}".format(str(selected_ingredients)))
            print("TOTAL: ${}, DATE: {}".format(str(total_price), str(datetime.now())))
            print("-------------------------")
            break

    else:
        print("ERROR: Ingredient does not exist")



