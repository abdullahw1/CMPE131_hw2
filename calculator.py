def calculator(number1,number2,operator):
    # "+" operator will perform addition
    if operator=="+":
        print(number1+number2)
    # else if "-" operator used, then subtraction performed
    elif operator=="-":
        print(number1-number2)
    # else if "*" operator used, multiplication will be performed
    elif operator=="*":
        print(number1*number2)
    # else if "/" operator is used, division performed
    elif operator=="/":
        print(number1/number2)
    # else if operator is "//",then perform integer division and print result
    elif operator=="//":
        #return false if num2 is 0 as result wont exist
        if number2 == 0:
            return False
        else:
            print(number1//number2)

    # else perform power operation with "**" operator
    elif operator=="**":
        print(number1**number2)
    # else return False
    else:
        return False

# input_output() function
def parse_input():
    number1 = 0.0
    number2 = 0.0
    print("Enter equation: ")
    text = input()
    # split text into three variables by " ", So that we can get the data
    strList = text.split(" ")
    # prevent system get error when user input wrong text
    try:
        number1 = float(strList[0])
        number2 = float(strList[2])
    except ValueError:
        return False
    calculator(number1, number2, strList[1])
