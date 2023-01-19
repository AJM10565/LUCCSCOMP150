"""
Truth Table

ATM/Shipping Cost Lab


"""


def truth_table():
    """ Print a truth table
    A | B | A and B | A or B |A and !B |!A and B | !(A and B)| etc
    T | T | ??????? |??????? |
    T | F | ??????? |??????? |
    F | T | ??????? |??????? |
    F | F | ??????? |??????? |

    """
    A = "A"
    B = "B"
    row = f'{A} | {B} | {"A and B"} | {"A or B"} |'
    print(row)
    A = True
    B = True
    row = f'{A} | {B} | {A and B} | {A or B} |'
    print(row)
    B = False
    row = f'{A} | {B} | {A and B} | {A or B} |'
    print(row)
    A = False
    B = True
    row = f'{A} | {B} | {A and B} | {A or B} |'
    print(row)
    B = False
    row = f'{A} | {B} | {A and B} | {A or B} |'
    print(row)


def current_day():
    """ Print the current day month and year
    example: "Today is Day: 16, Month 1, Year: 2023"

    """

    from datetime import date

    today = date.today()

    # dd/mm/YY
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    print(f"Today is Day: {day}, Month {month}, Year: {year}")


def atm_lab():
    """In this lab, you will be creating a program that simulates an ATM machine.
     Your program should start by prompting the user to select one of three options: withdraw, view, or deposit.

    ~If the user selects 'withdraw,' your program should prompt the user to enter an amount to withdraw.
    ~If the user has enough money in their account, your program should subtract the entered amount from
    the user's account balance and print the new balance. If the user does not have enough money in their account,
    your program should print an error message.
    ~If the user selects 'view,' your program should simply print the user's current account balance.
    ~If the user selects 'deposit,' your program should prompt the user to enter an amount to deposit. Your program should then add the entered amount to the user's account balance and print the new balance.
    You should consider using variables to store the user's account balance and the amount entered by the user. Your program should also include appropriate error handling for cases where the user enters an invalid option or an invalid amount.

    Your program should be able to handle multiple transactions and should keep track of the account balance after each transaction. Be sure to use proper syntax and indentation in your code, and include comments to explain your logic.
    """
    print("Welcome to ATM v0.1")
    balance = 100
    app_is_running = True
    while app_is_running:
        command = input("""Would you like to:
                        'view': View your current balance
                        'deposit': add money to your account
                        'withdraw': remove money from your account
                        'exit': close the app
                        """)
        valid_commands = ['view', 'deposit', 'withdraw', 'exit']
        if command not in valid_commands:
            print("You entered: {command}, which is not a valid input")
        elif command == 'view':
            print("You have a balance of ${balance}")
        elif command == 'deposit':
            amount_to_deposit = input("How much would you like to deposit")
            amount_to_deposit_as_integer = int(amount_to_deposit)
            if amount_to_deposit_as_integer >= 0:
                balance = balance + amount_to_deposit_as_integer
            else:
                print("You can only deposit positive amounts of money to the atm machine")
        elif command == 'withdraw':
            amount_to_withdraw = input("How much would you like to withdraw")
            amount_to_withdraw_as_integer = int(amount_to_withdraw)
            if amount_to_withdraw_as_integer >= balance:
                balance = balance - amount_to_withdraw_as_integer
                print(f"After withdrawing {amount_to_withdraw_as_integer}, Your new balance is: {balance} ")
            else:
                """ Not enough money in the account"""
                print(f"""
                You only have {balance} money in your account, 
                which is less than {amount_to_withdraw_as_integer}
                """)
        else:
            """ here we know tha the command has to be 'exit', as its the last option"""
            app_is_running = False
        if app_is_running:
            pass
        else:
            return


def shipping_cost():
    """
    In this lab, you will be creating a program that calculates the cost to ship a package.
    Your program should start by prompting the user to enter the weight of the package in pounds
    and the distance the package will travel in miles.

    Your program should then use the entered weight and distance to calculate the shipping cost. You should assume that
    the cost to ship a package is $0.25 per pound and $0.10 per mile.

    You should also allow the user to specify a specific route (e.g. Chicago to New York) and have the program
    calculate the cost based on a known distance for that route.

    Additionally, you should consider adding a feature that allows the user to select a shipping method
    (e.g. standard, express, overnight) and adjust the shipping cost accordingly.

    Your program should be able to handle multiple package shipments and should print the total cost of each shipment.
    Be sure to use proper syntax and indentation in your code, and include comments to explain your logic.

    """
    print("Welcome to the Shipping Cost Calculator App")
    item_weight = 0
    distance_to_travel = 0
    app_is_running = True
    while app_is_running:
        while item_weight == 0:
            response_weight_in_pounds = int(input("How much does your package weight in lbs?"))
            if not response_weight_in_pounds > 0:
                print("The package cannot weight 0 or less lbs")
            else:
                item_weight = response_weight_in_pounds
        while distance_to_travel == 0:
            response_distance_to_travel = int(input("How far must your package be shipped in miles?"))
            if not response_distance_to_travel > 0:
                print("The package must travel at least 0 miles")
            else:
                distance_to_travel = response_distance_to_travel
        cost_to_ship = (distance_to_travel * 0.1) + (item_weight * 0.25)
        print(
            f"It will cost {cost_to_ship} to deliver a package weighing {item_weight}lbs a distance of {distance_to_travel} miles.")
        go_again = input("Would you like to calculate another shipment? enter yes, otherwise have a nice day")
        if go_again == 'yes':
            pass
        else:
            app_is_running = False


if __name__ == "__main__":
    print("Welcome to the ATM/ Shipping Cost Lab")
    """ Uncomment one of these to run that program"""
    # truth_table()
    # current_day()
    # atm_lab()
    # shipping_cost()
