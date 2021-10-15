import time
"""
    function to calculate time to run a function
    
    parameters
    ----------
    function : function
    
    Returns
    --------
    test : float
"""

def calculate_time(function):
    def timer():
        startTime = time.time()
        function()
        end = time.time()
        print(f"Total time", (end - startTime))
    return timer

def test():
    time.sleep(2)

test = calculate_time(test)
test()
