def total_function(quantity, price):
    """
    This function calculates the total revenue from ticket sales.

    :param quantity: The total quantity of tickets ordered from the band website.
    :type quantity: int

    :param price: The price of each ticket ordered from the band website.
    :type price: int

    :return: The total revenue from ticket sales.
    :rtype: int
    """
    total_revenue = quantity * price
    return total_revenue

# Example usage:
revenue = total_function(3, 5)
print(revenue)  # This will print 15


