def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b

# Calling the function
result = add_numbers(5, 3)
print(f"The sum is: {result}")
print(add_numbers.__doc__)
