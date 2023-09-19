# example_script.py

def greet(name):
    """
    This function greets the user with a personalized message.

    :param name: The name of the user.
    :type name: str

    :return: A greeting message.
    :rtype: str
    """
    greeting = f"Hello, {name}! Welcome to our program."
    return greeting

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)
