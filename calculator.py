def calculator(number1, number2, operator):
    """
        This function will allow to make calculations
    """
    #"+" operator will perform addition
    if operator == "+":
        result = number1 + number2
    #else if "-" operator used, then subtraction performed
    elif operator == "-":
        result = number1 - number2
    #else if "*" operator used, multiplication will be performed
    elif operator == "*":
        result = number1 * number2
    #else if "/" operator is used, division performed
    elif operator == "/":
        #return false if num2 is 0 as result wont exist
        if number2 == 0:
            return False
        else:
            result = number1 / number2
    #perform integral division with "//" operator
    elif operator == "//":
        if number2 == 0:
            return False
        else:
            result = number1 // number2
    # else perform power operation with "**" operator
    elif operator == "**":
        result = number1 ** number2
    else:
        return False
    #print(result)
    #return result


def parse_input():
    """
    get the text of user input and parse the text.
    This function splits user input into number1, number2, and operator.
    passes variables to calculator() function.
    """
    text = input("Enter equation: ")
    number1, number2, operator = text.split()
    number1 = float(number1)
    number2 = float(number2)
    return calculator(number1, number2, operator)
