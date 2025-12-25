"""
Docstring for notes.python-basics.pyhon
What is Python?
Introduction: Python is a general-purpose programming language known for its simplicity and ease of use. Python is used in many fields like data science and machine learning, web development, scripting and automation, embedded systems and IoT, and much more.
Common Use Cases: Python is used in data science, machine learning, web development, cybersecurity, automation and microcomputers like the Raspberry Pi and MicroPython-compatible boards.
"""


"""
Variables
Declaring Variables: To declare a variable, you start with the variable name followed by the assignment operator (=) and then the value. This can be a number, string, boolean, etc. Here are some examples:
Naming Conventions for Variables: Here are the naming conventions you should use for variables

Variable names can only start with a letter or an underscore (_), not a number.
Variable names can only contain alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
Variable names are case-sensitive — age, Age, and AGE are all considered unique.
Variable names cannot be one of Python s reserved keywords such as if, class, or def.
Variables names with multiple words are separated by underscores. Ex. snake_case.
"""

"""
Immutable and Mutable Types
Immutable Types: These types cannot change once declared, although you can point their variables at something new, which is called reassignment. They include integer, float, complex, boolean, string, tuple, range, and None.
Mutable Types: These types can change once declared. You can add, remove, or update their items. They include collection types such as list, set, and dictionary.
type() Function: To see the type for a variable, you can use the type() function like this:
"""

print(isinstance('Hello world', str)) # True
print(isinstance('John Doe', int)) # False

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w

print(my_str[-1])  # d
print(my_str[-2]) # l