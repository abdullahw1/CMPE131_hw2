def multiply_list(list):
    """
        function that will multiply elements in a list
        
        Parameter
        ---------
        list : list
        
        Returns
        -------
        product : int 
        
     """
    result = 1
    for i in list:
        if type(i)==int:
            result = result * i
        else:
            return False

    return result
