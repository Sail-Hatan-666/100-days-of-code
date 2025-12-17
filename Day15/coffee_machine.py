from coffee_data import *
import coffee_data
# import time


def admin_panel():
    attempts = 0
    while attempts < 3:

        password = 1234
        password_prompt = int(input("Please input your admin password:\n"))
        
        if password_prompt == password and attempts < 3:
            admin_input = input(
            "Welcome Admin, what would you like to do? off/refill/resources: \n"
            ).lower()
            if admin_input == "off":
                state = False
                return state
            if admin_input == "resources":
                return resources
            if admin_input == "refill":
                pass
        else:
            attempts += 1


def get_resources():
    for item in resources:
        print(f"{item}: {resources[item]}")


def process_payment(user_choice,
                    pennies, 
                    nickels, 
                    dimes, 
                    quarters 
                    ):
    drink_cost = MENU[user_choice]["cost"]
    total = (pennies * .01) + (nickels * .05) + (dimes * .1) + (quarters * .25)
    change = total - drink_cost
    if total < drink_cost:
        return False, total, change
    else:
        return True, total, change


def make_coffee(user_choice):
    global profit
    ingredients = MENU[user_choice]["ingredients"]
    for ingredient, value in ingredients.items():
        if resources[ingredient] < value:
            return f"We are out of {ingredient}, please contact the admin to refill."
        else:
            resources[ingredient] -= value
            profit += MENU[user_choice]["cost"]


machine_state = True

while machine_state:

    user_choice = input(
        "What would you like to drink (espresso/latte/cappuccino):\n"
        ).lower()

    if user_choice == "admin":        
        admin_choice = admin_panel()
        if not admin_choice:
            machine_state = False
        if admin_choice == resources:
            # ingredient_value = get_resources()
            get_resources()
            print(f"profit: ${coffee_data.profit:.2f}")
            # print(profit)
            
    
    if user_choice in MENU:
        print(
            f'You ordered a {user_choice}, that will be '
            f'${MENU[user_choice]["cost"]:.2f}.\n'
            f'Please insert your payment.'
            )
        pennies = int(input("How many pennies?:\n"))
        nickels = int(input("How many nickels?:\n"))
        dimes = int(input("How many dimes?:\n"))
        quarters = int(input("How many quarters?:\n"))

        # Splits the return value of process_payment into usable integers
        success, total, change= process_payment(
            user_choice,
            pennies, 
            nickels, 
            dimes, 
            quarters
            )
        if success:
            print(f"Making your {user_choice} now!")
            make_coffee(user_choice)
            # time.sleep(2)
        else:
            print(
                f'Insufficient funds —\n{user_choice} costs:'
                f' ${MENU[user_choice]["cost"]:.2f}\n'
                f'Refunding:\n${total:.2f}'
            )