from coffee_data import *
import time


def admin_panel(profit):
    attempts = 0
    while attempts < 3:

        authorized_user = "ryan"
        password = 1234
        username = input("Please enter your username:\n")
        password_prompt = int(input("Please input your password:\n"))
        
        if username == authorized_user and password_prompt == password and attempts < 3:
            logged_in = True
            while logged_in:
                admin_input = input(
                "Welcome Admin, what would you like to do? off/refill/resources/exit: \n"
                ).lower()
                if admin_input == "off":
                    return "off"
                elif admin_input == "resources":
                        for item in resources:
                            print(f"{item}: {resources[item]}ml")
                        print(f"profit: ${profit:.2f}")
                elif admin_input == "refill":
                    resources["water"] = 300
                    resources["milk"] = 200
                    resources["coffee"] = 100
                elif admin_input == "exit":
                    return "exit"
        else:
            attempts += 1


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
    ingredients = MENU[user_choice]["ingredients"]
    for ingredient, value in ingredients.items():
        if resources[ingredient] < value:
            return False
        else:
            resources[ingredient] -= value
            return True


machine_state = True

while machine_state:
    user_choice = input(
        "What would you like to drink (espresso/latte/cappuccino):\n"
        ).lower()

    if user_choice == "admin":
        status = admin_panel(profit)  
        if status == "off":
            machine_state = False
        elif status == "exit":
            continue   
    
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

        # Splits the return value of process_payment() into usable integers
        approved, total, change = process_payment(
            user_choice,
            pennies, 
            nickels, 
            dimes, 
            quarters
            )
        if approved:
            success = make_coffee(user_choice)
            if success:
                profit += MENU[user_choice]["cost"]
                print(f"Making your {user_choice} now!")
                time.sleep(2)
                print(
                    f"Dispensing change:\n${change:.2f}\n"
                    f"Please enjoy your drink!"
                    )
            else:
                print(
                    f"Insufficient ingredients, please contact the Admin\n"
                    f"Refunding:\n${total:.2f}"
                    )
                
        else:
            print(
                f'Insufficient funds —\n{user_choice} costs:'
                f' ${MENU[user_choice]["cost"]:.2f}\n'
                f'Refunding:\n${total:.2f}'
            )
    else:
        print("Invalid drink option...")