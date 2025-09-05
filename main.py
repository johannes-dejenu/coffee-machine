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
user_input = input("What would you like? (espresso/latte/cappuccino): ").strip()
money = 0
def report():
    print(f"Water : {resources["water"]}ml")
    print(f"Milk : {resources["milk"]}ml")
    print(f"Coffee : {resources["coffee"]}g")
    print(f"Money : ${money}")
if user_input == "report":
    report()
if user_input in MENU:
    for i in MENU["latte"]["ingredients"]:
        if resources["water"] < MENU[user_input]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["milk"] < MENU[user_input]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < MENU[user_input]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
def process_coins():
    print("Please insert coins.")
    quarters = input("how many quarters?: ")
    dimes = input("how many dimes?: ")
    nickles = input("how many nickles?: ")
    pennies = input("how many pennies?: ")
    return quarters, dimes, nickles, pennies
