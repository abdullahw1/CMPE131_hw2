def calculator(number1, number2, operator):
    """
        This function will allow to make calculations
    """
    # "+" operator will perform addition
    if operator == "+":
        print(number1 + number2)
    # else if "-" operator used, then subtraction performed
    elif operator == "-":
        print(number1 - number2)
    # else if "*" operator used, multiplication will be performed
    elif operator == "*":
        print(number1 * number2)
    # else if "/" operator is used, division performed
    elif operator == "/":
        # return false if num2 is 0 as result wont exist
        print(number1 / number2)
    # perform integral division with "//" operator
    elif operator == "//":
        print(number1 // number2)
    # else perform power operation with "**" operator
    elif operator == "**":
        print(number1 ** number2)


def parse_input():
    """
    gets user input and splits.
    This function splits user input into number1, number2, and operator.
    passes variables to calculator() function.
    """
    EquatOutout = input("Enter Equation: ")
    equat = EquatOutout.split()
    number1, operator, number2 = equat
    number1 = float(number1)
    number2 = float(number2)
    # pass user input to calculator() function
    print(calculator(number1, number2, operator))

parse_input()
