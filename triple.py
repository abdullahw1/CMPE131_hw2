def tripler(function):
    """
        This functon will use  decorator to call
        function to call given function 3 times.

        Parameters
        ----------
        function : function
            runs in decorator
    """
    def decorator():
        function()
        function()
        function()
    return decorator
@tripler

def test():
    print("test")
test()
