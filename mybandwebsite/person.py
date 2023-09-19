class Person:
    def __init__(self, name, age):
        """
        Initialize a Person object.

        :param name: The name of the person.
        :type name: str
        :param age: The age of the person.
        :type age: int
        """
        self.name = name
        self.age = age

    def introduce(self):
        """
        This method introduces the person.

        :return: A greeting message.
        :rtype: str
        """
        return f"Hello, my name is {self.name} and I am {self.age} years old."
