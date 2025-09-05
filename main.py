MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO 1 : print report
# TODO 2 : check resources sufficiency
# TODO 3 : process coins
# TODO 4 : check transaction successful
# TODO 5: make coffee
want_coffee = True
money = 0
while want_coffee:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").strip()
    total = 0
    def report():
        print(f"Water : {resources["water"]}ml")
        print(f"Milk : {resources["milk"]}ml")
        print(f"Coffee : {resources["coffee"]}g")
        print(f"Money : ${money}")
    if user_input == "off":
        want_coffee = False
    elif user_input == "report":
        report()
    elif user_input in MENU:
        money += MENU[user_input]["cost"]
        for i in MENU[user_input]["ingredients"]:
            if resources["water"] < MENU[user_input]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
                want_coffee = False
            elif resources["coffee"] < MENU[user_input]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
                want_coffee = False
            elif "milk" in MENU[user_input]["ingredients"]:
                if resources["milk"] < MENU[user_input]["ingredients"]["milk"]:
                    print("Sorry there is not enough milk.")
                    want_coffee = False
        resources["water"] = resources["water"] - MENU[user_input]["ingredients"]["water"]
        if "milk" in MENU[user_input]["ingredients"]:
            resources["milk"] = resources["milk"] - MENU[user_input]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[user_input]["ingredients"]["coffee"]
        def process_coins():
            print("Please insert coins.")
            quarter = int(input("how many quarters?: "))
            dime = int(input("how many dimes?: "))
            nickle = int(input("how many nickles?: "))
            penny = int(input("how many pennies?: "))
            return quarter, dime, nickle, penny
        quarters, dimes, nickles, pennies = process_coins()
        total += 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
        total_1 = round(total, 2)
        change = total_1 - MENU[user_input]["cost"]
        change = round(change, 2)
        if total_1 < MENU[user_input]["cost"]:
            print("Sorry that's not enough. Money refunded.")
        else:
            if total_1 > MENU[user_input]["cost"]:
                print(f"Here is ${change} dollars in change.")
                print(f"Here is your {user_input}. Enjoy!")


