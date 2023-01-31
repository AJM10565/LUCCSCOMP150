def problem1():
    """
    Given: A = False, B = True, C = False
    Solve:
    a=B and C
    b=B or C
    c=not A and B
    d=(A and B) or not C
    e=not B and not (A or C)
    f=B and not C
    g=not A or not C
    h=not (A and B) and C
    i=A or not (B and C)
    j=not A or B and C
    """
    # ok so
    A = False
    B = True
    C = False

    a = B and C
    print(f"a: {B and C = }")
    b = B or C
    print(f"b: {B or C = }")
    c = not A and B
    print(f"c: {not A and B = }")
    d = (A and B) or not C
    print(f"d: {(A and B) or not C = }")
    e = not B and not (A or C)
    print(f"e: {not B and not (A or C) = }")
    f = B and not C
    print(f"f: {B and not C = }")
    g = not A or not C
    print(f"g: {not A or not C = }")
    h = not (A and B) and C
    print(f"h: {not (A and B) and C = }")
    i = A or not (B and C)
    print(f"i: {A or not (B and C) = }")
    j = not A or B and C
    print(f"j: {not A or B and C = }")
    for expression in [a, b, c, d, e, f, g, h, i, j]:
        print(f"{expression}")


def problem2():
    """
    Type()
    for
    a=27.98
    b=“Words” and 29
    c=918273645
    d=[4,7,11,26]
    e={“list”:[”23”,”24”,”25”]}
    f=“Numbers are our Friends!”
    g=“17”
    h=“False”
    i=9.5
    j=[1,2,3]
    k={'key': 'value'}
    l="True"
    """
    a = 27.98
    b = "Words" and 29
    c = 918273645
    d = [4, 7, 11, 26]
    e = {"list": ["23", "24", "25"]}
    f = "Numbers are our Friends!"
    g = "17"
    h = "False"
    i = 9.5
    j = [1, 2, 3]
    k = {'key': 'value'}
    l = "True"
    for value in [a, b, c, d, e, f, g, h, i, j, k, l]:
        print(type(value))


def problem3():
    """
    and
    _and
    var
    var1
    1var
    My-name
    your name
    COLOR
    myVar
    _myVar
    my_var
    my-var
    my var
    123
    """
    # and = 1
    print("and is not legal, it is a reserved word")
    _and = 1
    print(f"{_and=} is fine")
    var = 1
    print(f"{var=} is fine")
    var1 = 1
    print(f"{var1=} is fine")
    # 1var = 1
    print("1var is not legal, names can't start with numbers")
    # My-name = 1
    print("My-name is not legal, cannot use - in names")
    # your name = 1
    print("'your name' is not legal, cannot use ' ' space in names")
    COLOR = 1
    print(f"{COLOR=} is fine, although in general most names should be lowercase, by convention we reserve fully upper"
          f"case names for constants, and class names should start with an uppercase character")
    myVar = 1
    print(f"{myVar=} is fine")
    _myVar = 1
    print(f"{_myVar=} is fine")
    my_var = 1
    print(f"{my_var=} is fine")
    # my-var =1
    print("my-var is not legal, cannot use - in names")
    # my var =1
    print("'my var' is not legal, cannot use ' ' space in names")
    # 123 =1
    print(f"Error cannot assign to literal, also names cannot just be an integer or start with a number")


def problem4():
    """
    Your solution to problem 4 goes here. Here's problem statement as a reference:
    Greet the User with user input:
    - Write a program that prompts the user for their name and then greets them by name.
    - Your program should use the input function to get the user's name as a string.
    - You should then use the print function to greet the user by name.
    """
    user_entered_name = input("What is your name: ")
    greeting = f"Greetings {user_entered_name}"
    print(greeting)

    # Alternatively: in a single line
    print(f'Greetings {input("What is your name: ")}')

    """ Comments on the general solution:
    1) We used 2 python built-in's "input" and "print"
    2) input is used to get a value from the console, which in this case is a string, so there's no additional 
    conversion required
    3) print shows a message to the console. We stored that message in a variable called 'greeting', so that 
    someone who reads the code knows the purpose of the string
    4) An alternative solution is given that uses only 1 line of code to complete the task. 
    Is this easier to understand?
    Or does it make it harder to understand, when everything is on the same line of code?
    """


def problem5():
    """
    Your solution to problem 5 goes here. Here's problem statement as a reference:
    Temperature conversion
    - Write a program that converts temperatures from Fahrenheit to Celsius.
    - Your program should prompt the user for a temperature in Fahrenheit.
    - You should then use the appropriate formula to convert the temperature to Celsius.
    - Your program should print the temperature in Celsius to the user.
    """
    print("This application converts temperatures from Fahrenheit to Celsius")
    temperature_in_fahrenheit: float = float(input("What is the temperature in Fahrenheit: "))
    # Source for the conversion: https://www.nist.gov/pml/owm/si-units-temperature
    # See table labeled: Temperature Conversion (Exact)
    # °C = (°F - 32) / 1.8
    temperature_in_celsius: float = (temperature_in_fahrenheit - 32) / 1.8
    response = f"{temperature_in_fahrenheit}°F is the same as {temperature_in_celsius:.2}°C"
    print(response)
    """ Comments on the general solution:
    1) We printed a message at the start of the application letting the user know the purpose of the tool they are 
    using. This can be useful if there are multiple pieces of code that can be executed from a single file, such as in
    this homework assignment. 
    2) We also used the float() function, which converts strings into their float representation for arithmetic
    **Remember a float in python is the name of the kind of number that includes decimal values**
    3) We use a .gov reference for the temperature conversion, and it shows a cleaner formula, than the traditional 
    C = (F - 32) * (5/9)
    4) We use the ° symbol to add flair to our printed output, rather than the word degrees.
    5) We also repeat back the input, so that everything is encapsulated on a single line
    6) We also use format specifiers to limit the total number of decimal places in the case of a non-repeating infinite 
    decimal number: https://peps.python.org/pep-0498/#format-specifiers
    7) There's actually a whole language out there for specifying the format of output, which is beyond the scope of what
    we're going to cover in this course, but if you're interested, please check out: 
    https://docs.python.org/3.6/library/string.html#formatspec
    """


def problem6():
    """
    Your solution to problem 6 goes here. Here's problem statement as a reference:
    Odd or Even
    - Write a program that determines whether a number is odd or even.
    - Your program should prompt the user for a number.
    - You should then use an if statement to check whether the number is odd or even.
    - Your program should print "odd" if the number is odd and "even" if the number is even.
    """
    print("This application determines if a number is odd or even")
    number: int = int(input("What is the number: "))
    if number % 2 == 0:
        print(f"The number: {number} is even.")
    else:
        print(f"The number: {number} is odd.")

    # Alternatively
    print("This application determines if a number is odd or even")
    number = int(input("What is the number: "))
    odd_or_even = "odd"
    if number % 2 == 0:
        odd_or_even = "even"
    print(f"The number: {number} is {odd_or_even}.")

    """ Comments on the general solution:
    1) The property of a number being even or odd can only apply to integers by definition, the test is to see if the
    number divided by 2 has a remainder. If it does, then the number is odd, otherwise, the number is even.
    2) The solution to the problem requires the use of process-control tools
    3) In the case of this problem, the tools used are "if" and "else"
    4) In the first case, we use if and else and we print the response according to the result of the control flow
    5) In the alternate solution, we can simplify the number of checks, because we know that there are onlu 2 cases:
    even or odd. We assume the number is odd, check if it's even, and then we print the message with the result. The 
    benefit of this strategy is that we only need a single print statement. This technique of only using a single print
    statement can be useful when you're reading long portions of code, with functions that call other functions, and
    it can be confusing if the function ends in too many different places, thousands of lines from each other. So its
    worth exposing students to this strategy here, when the stakes aren't so high. In event, both solutions are
    acceptable.
    """


def problem7():
    """
    Your solution to problem 7 goes here. Here's problem statement as a reference:
    Circle Area Calculator
    - Write a program that calculates the area of a circle.
    - The formula for calculating the area of a circle is pi * radius^2.
    - Your program should prompt the user for the radius of the circle.
    - You should then use the appropriate formula to calculate the area of the circle.
    - Your program should print the result of the calculation.
    """
    print("This application calculates the area of a circle if the user gives a value for the radius")
    radius = float(input("What is the radius of the circle: "))
    pi = 3.14159  # this is an approximation of pi
    area = pi * radius * radius
    print(f"A circle with radius: {radius} units will have an area of {area} units.")

    # alternate solution
    print("This application calculates the area of a circle if the user gives a value for the radius")
    radius = float(input("What is the radius of the circle: "))
    pi = 3.14159  # this is an approximation of pi
    area = pi * (radius ** 2)
    print(f"A circle with radius: {radius} units will have an area of {area} units.")

    # alternate solution
    import math
    print("This application calculates the area of a circle if the user gives a value for the radius")
    radius = float(input("What is the radius of the circle: "))
    pi = math.pi  # this is a more exact version of pi, useful when you need the extra digits or when precision matters
    area = pi * (radius ** 2)
    print(f"A circle with radius: {radius} units will have an area of {area} units.")

    """ Comments on the general solution:
    1) This problem is very similar to problem5, we take a value, process it with math, and then return another value
    2) When the problem is low-stakes, we can just use a value for pi with a few digits
    3) This problem was an opportunity to show case the exponentiation syntax (**), but we could also solve by 
    multiplying by the radius twice. 
    4) When we need more digits of pi, python has a module called math, that we can import. The math module includes a 
    bunch of functions and constants that are useful when doing arithmetic and other kinds of operations
    Note: When we use a constant defined by another module, we don't add "()" to the end of the call.
    This is different from when we use date() later on in the homework.
    """


def problem8():
    """
    Your solution to problem 8 goes here. Here's problem statement as a reference:
    Greeting Generator
    - Write a program that generates a greeting based on the time of day.
    - Your program should prompt the user for the current time in hours (from 0 to 23).
    - If the time is from 0 to 11, your program should print "Good morning."
    - If the time is from 12 to 17, your program should print "Good afternoon."
    - If the time is from 18 to 23, your program should print "Good evening."
    - Be sure to use proper syntax and punctuation in your program.
    """

    time_of_day = int(input("What is the current time in hours(0 to 23): "))
    if 0 <= time_of_day <= 11:
        print("Good morning.")
    elif 12 <= time_of_day <= 17:
        print("Good afternoon.")
    else:
        print("Good evening.")

    # alternate solution

    time_of_day = int(input("What is the current time in hours(0 to 23): "))
    if 0 <= time_of_day < 12:
        print("Good morning.")
    elif 11 < time_of_day < 18:
        print("Good afternoon.")
    else:
        print("Good evening.")

    # alternate solution

    time_of_day = int(input("What is the current time in hours(0 to 23): "))
    if time_of_day in range(0, 12):
        print("Good morning.")
    elif time_of_day in range(12, 18):
        print("Good afternoon.")
    else:
        print("Good evening.")

    """ Comments on the general solution:
    1) This solution deals with an application that has 3 different outputs, we use if, elif, and else to determine the 
    correct statement to print.
    2) The first solution uses the logical operators "<=" less than or equal to, in order to make the determination
    The benefit of this operator is that the numbers for the various outputs are the same as in the problem statement
    3) The second solution adds in the addition of the "<" less than operator, which can add clarity to the code, but
    requires a translation of numbers in order to get the code to function as specified (the upper boundary needs to be 
    one more than in the previous case)
    4) In the last solution, we do-away with logical operators, and instead ask, is the number in a range. The benefit
    to this solution is that we perform a single check for each conditional so its easier to read.
    """


def problem9():
    """
    Your solution to problem 9 goes here. Here's problem statement as a reference:
    Write a program that calculates a person's age in years, months, and days.
    - Your program should prompt the user for their birth year, birth month, and birth day.
    - You should then use the current date to calculate the user's age in years, months, and days.
    - Your program should print the user's age in the following format: "Your age is X years, Y months, and Z days."
    - Be sure to use proper syntax and punctuation in your program.
    """
    import calendar
    from datetime import date, timedelta

    # Get today's date
    today = date.today()

    # Get birth_date from user input
    birth_day = int(input(f"Enter your birth day: "))
    birth_month = int(input(f"Enter your birth month: "))
    birth_year = int(input(f"Enter your birth year: "))

    # Create birth_date object
    birth_date = date(birth_year, birth_month, birth_day)

    # Calculate age by subtracting birth_date from today's date
    age = today - birth_date

    # Check if birthday has already occurred this year
    if birth_date.replace(year=today.year) > today:
        age = age - timedelta(days=365)
        # If birth year is a leap year, subtract one more day from age
        if calendar.isleap(birth_year):
            age = age - timedelta(days=1)

    # Lists for number of days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if current year is a leap year
    if calendar.isleap(today.year):
        days_in_month = days_in_month_leap

    # Calculate the number of days, months and years
    months = age.days // 30
    days = age.days % 30
    years = 0

    # Increment years and decrement months until months is less than 12
    while months >= 12:
        months -= 12
        years += 1

    # Increment months and decrement days until days is less than days in current month
    while days > days_in_month[months]:
        days -= days_in_month[months]
        months += 1
        if months >= 12:
            months -= 12
            years += 1

    # Print age in years, months, and days
    print(f"Your age is {years} years, {months} months, and {days} days.")
    """ Comments on the general solution:
    1) The code first imports the calendar and datetime modules, and gets today's date using the date.today() function.
    2) Then it prompts the user to enter their birth day, month, and year, and creates a date object for the birth date
     using the inputted values.
    3) It then calculates the age by subtracting the birth date from today's date, and checks if the birthday has
     already occurred this year. If it has not, it subtracts one year from the age.
    4) It also creates two lists for the number of days in each month, one for a regular year and one for a leap year,
     and checks if the current year is a leap year to decide which list to use.
    5) It then calculates the number of days, months, and years in the age using integer division and modulus operators,
     and adjusts the values until they are in the correct range (months less than 12, days less than days in current month).
    6) Finally, it prints the age in years, months, and days.
    """


def problem10():
    """
    Your solution to problem 10 goes here. Here's problem statement as a reference:
    Rock, Paper, Scissors Game
    - Write a program that allows two players to play the rock, paper, scissors game.
    - Your program should prompt each player for their choice (rock, paper, or scissors).
    - You should then determine the winner of the game based on the following rules:
      - Rock beats scissors.
      - Scissors beats paper.
      - Paper beats rock.
    - Your program should print the winner of the game.
    - If the players choose the same option, your program should print, "It's a tie!"
    - Be sure to use proper syntax and punctuation in your program.
    """
    player1_choice_is_good = False
    valid_choices = ["rock", "paper", "scissors"]
    player1_choice = ""
    while player1_choice_is_good:
        player1_choice = input("please choose (rock, paper, or scissors): ")
        if player1_choice.lower() in valid_choices:
            player1_choice = player1_choice.lower()
            player1_choice_is_good = True

    player2_choice = ""
    player2_choice_is_good = False
    while player2_choice_is_good:
        player2_choice = input("please choose (rock, paper, or scissors): ")
        if player2_choice.lower() in valid_choices:
            player2_choice = player2_choice.lower()
            player2_choice_is_good = True

    if player1_choice == player2_choice:
        print("It's a tie!")
    elif (player1_choice == "paper" and player2_choice == "rock") or (
            player1_choice == "scissors" and player2_choice == "paper") or (
            player1_choice == "rock" and player2_choice == "scissors"):
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")

    """ Comments on the general solution:
    1) It is a well known fact that users don't tend to follow the rules, and will try and break software whenever 
    possible. While not strictly required, it can be useful to add input handling to verify the input is what you 
    expect. This will be useful for solving homework #2.
    2) This solution deals with an application that has 3 different outputs, we use if, elif, and else to determine the 
    correct statement to print.
    3) The first output corresponds to the case where the answers are the same
    4) The second output corresponds to the cases when player1 wins
    5) The last output corresponds to the cases when player2 wins
    """


if __name__ == "__main__":
    print("Welcome to Homework")
    """ Uncomment one of these to run/test that problem"""
    problem1()
    problem2()
    problem3()
    # problem4()
    # problem5()
    # problem6()
    # problem7()
    # problem8()
    # problem9()
    # problem10()
