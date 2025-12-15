from coffee_data import *
import time

def admin_panel(machine_state):
    attempts = 0
    while attempts < 3:
        
        password = 1234
        password_prompt = int(input("Please input your admin password:\n"))
        
        if password_prompt == password and attempts < 3:
            admin_input = input(
            "Welcome Admin, what would you like to do? off/refill/resources"
            ).lower()

            if admin_input == "off":
               machine_state = False

            if admin_input == "resources":
                get_resources()

            if admin_input == "refill":
                pass
        else:
            attempts += 1

# def machine_off():
#     return False

def get_resources():
    for item in resources:
        resource_output = f"{item}: {resources[item]}\n"
        print(resource_output)


def process_payment(pennies, 
                    nickels, 
                    dimes, 
                    quarters, 
                    user_choice):
    drink_cost = MENU[user_choice]["cost"]
    total = (pennies * .01) + (nickels * .05) + (dimes * .1) + (quarters * .25)
    change = total - drink_cost
    if total < drink_cost:
        return False, total, change
    else:    
        profit + drink_cost
        return True, total, change


def make_coffee(user_choice):
    for item, amount in MENU[user_choice]["ingredients"].items():
        resources[item] -= amount


machine_state = True

while machine_state:

    user_choice = input(
        "What would you like to drink (espresso/latte/cappuccino):\n"
        ).lower()

    if user_choice == "admin":
        admin_panel(machine_state)
    
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
        success, total, change = process_payment(
            pennies, 
            nickels, 
            dimes, 
            quarters, 
            user_choice
            )
        
        if success:
            print(f"Making your {user_choice} now!")
            make_coffee(user_choice)
            time.sleep(5)
        else:
            print(
                f'Insufficient funds —\n{user_choice} costs:'
                f' ${MENU[user_choice]["cost"]:.2f}\n'
                f'You inserted:\n${total:.2f}'
            )