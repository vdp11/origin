class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """
        This method introduces the person.

        :return: A greeting message.
        :rtype: str
        """
        return f"Hello, my name is {self.name} and I am {self.age} years old."
