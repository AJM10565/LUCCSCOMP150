"""
ATM/Shipping Cost Lab


"""


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



    pass


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
    pass


if __name__ == "__main__":
    print("Welcome to the ATM/ Shipping Cost Lab")
    """ Uncomment one of these to run that program"""
    # atm_lab()
    # shipping_cost()
