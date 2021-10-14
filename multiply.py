def multiply_list(list):
    product = 1
    for x in list:
        if type(x)==int:
            product = product * x
        else:
            return False

    return product
