def calculator(number1, number2, operator):
    """
        This function will allow to make calculations
    """
    #"+" operator will perform addition
    if operator == "+":
        print(number1 + number2)
    #else if "-" operator used, then subtraction performed
    elif operator == "-":
        print(number1 - number2)
    #else if "*" operator used, multiplication will be performed
    elif operator == "*":
        print(number1 * number2)
    #else if "/" operator is used, division performed
    elif operator == "/":
        #return false if num2 is 0 as result wont exist
        print(number1 / number2)
    #perform integral division with "//" operator
    elif operator == "//":
        print(number1 // number2)
    # else perform power operation with "**" operator
    elif operator == "**":
        print(number1 ** number2)
        
  def parse_input():
    """
    get the text of user input and parse the text.
    This function splits user input into number1, number2, and operator.
    passes variables to calculator() function.
    """
    num1 =  float (input("Enter 1st number: "))
	num2 = float (input ("Enter 2nd number: "))
	operator = input ("Operator: ")
    # pass user input to calculator() function
	calculator(num1, num2, operator)

parse_input()

    

