"""
everything in python is an object

Immutable and Mutable Types
Immutable Types: These types cannot change once declared, although you can point their variables at something new, which is called reassignment. They include integer, float, complex, boolean, string, tuple, range, and None.
Mutable Types: These types can change once declared. You can add, remove, or update their items. They include collection types such as list, set, and dictionary.

python is a dynamically typed language



"""
# common data types
my_integer_var = 10
print('Integer:', my_integer_var)
my_float_var = 4.50
print('Float:', my_float_var) # Float: 4.5
my_complex_var = 3 + 4j
print('Complex:', my_complex_var) # Complex: (3+4j)
my_string_var = 'hello'
print('String:', my_string_var) # String: hello
my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True
# set is an unordered of unique elements
my_set_var = {7, 5, 8}
print('Set:', my_set_var) 
#collection of key values
my_dictionary_var = {"name": "Alice", "age": 25}
print('Dictionary:', my_dictionary_var)
#immutable ordered collection
my_tuple_var = (7, 5, 8)
print('Tuple:', my_tuple_var) # Tuple: (7, 5, 8)
# Range: A sequence of numbers
my_range_var = range(5)
print(my_range_var) # range(0, 5)
# list mutable collection 
my_list = [22, 'Hello world', 3.14, True]
print(my_list) # [22, 'Hello world', 3.14, True]

# isinstance() checks if an element type is str or int etc
print(isinstance('Hello world', str)) # True
print(isinstance('John Doe', int)) # False


# Working with Strings

# Accessing Characters from Strings: You can access characters from strings by using bracket notation like this:
my_str = "Hello world"
print(my_str[0])  # H
print(my_str[6])  # w

# Escaping Strings: You can use a backslash (\) if your string contains quotes like this:
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
print(quote)

# String Concatenation: To concatenate strings, you can use the + operator like this:
#1 
developer = 'Jessica'
print('My name is ' + developer + '.') # My name is Jessica

# 2
greeting = 'My name is '
developer = 'Jessica.'

greeting += developer
print(greeting) # My name is Jessica.
# 3
developer = 'Jessica'
greeting = f'My name is {developer}.'
print(greeting) # My name is Jessica.
print (f"{developer} is a girl")

# String Slicing: This is when you can extract portions of a string. Here is the basic syntax:
message = 'Python is fun!'

print(message[0:6])  # Python
print(message[7:])  # is fun!
print(message[::2])  # Pto sfn   third parameter is step

# Getting the Length of a String: The len() function is used to return the number of the characters in the string:
developer = 'Jessica'

print(len(developer)) # 7

# in Operator: This returns a boolean that specifies whether the character or characters exist in the string or not:
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

# str.upper(): This returns a new string with all characters converted to uppercase:
print(developer.upper()) # JESSICA
print(developer.lower()) # jessica

# str.strip(): This returns a copy of the string with specified leading and trailing characters removed 
# (if no argument is passed to the method, it removes leading and trailing whitespace)
greets = 'hello world'
trimmed_my_str = greets.strip()
print(trimmed_my_str)  
# replace(): This returns a new string with all occurrences of the old string replaced by a new one.

replaced_my_str = greets.replace('hello', 'hi')
print(replaced_my_str)  # 'hi world'

# split(): This is used to split a string into a list using a specified separator.
# A separator is a string specifying where the split should happen.
dashed_name = 'example;dashed;name'
split_words = dashed_name.split(';')
print(split_words)  # ['example', 'dashed', 'name']

# join() from list->string
example_list = ['example', 'dashed', 'name']

joined_str = ' '.join(example_list)
print(joined_str)  # example dashed name

developer = 'Naomi'

result = developer.startswith('N')
print(result)  # True
result = developer.endswith('N')
print(result)  # False

# return the first occurence of a substring if not found -1
result = developer.find('n')
print(result)  # 0

# str.count(substring): This counts how many times a substring appears in a string:
city = 'Los Angeles'
print(city.count('e')) # 2


dessert = 'chocolate cake'
print(dessert.capitalize()) # Chocolate cake

dessert = 'chocolate cake'
print(dessert.isupper()) # False

dessert = 'chocolate cake'
print(dessert.islower()) # True

# str.title(): This returns a new string with the first letter of each word capitalized
city = 'los angeles'
print(city.title()) # Los Angeles

trans_table = str.maketrans('abc', '123')
print(trans_table) # {97: 49, 98: 50, 99: 51}

result = 'abcabc'.translate(trans_table)
print(result)  # 123123


# Common Operations used with Integers and Floats

int_1 = 56
int_2 = 12
float_1 = 5.4
float_2 = 12.0

# Addition

print('Integer Addition:', int_1 + int_2) # Integer Addition: 68
print('Float Addition:', float_1 + float_2) # Float Addition: 17.4

# Subtraction

print('Int Subtraction:', int_1 - int_2) # Int Subtraction: 44
print('Float Subtraction:',  float_2 - float_1) # Float Subtraction: 6.6

# Multiplication

print('Int Multiplication:', int_1 * int_2) # Int Multiplication: 672
print('Float Multiplication:', float_2 * float_1) # Float Multiplication: 64.80000000000001

# Division

print('Int Division:', int_1 / int_2) # Int Division: 4.666666666666667
print('Float Division:', float_2 / float_1) # Float Division: 2.222222222222222

# When you add a float and an integer, the result will be converted to a float like this:
int_1 = 56
float_1 = 5.4

print(int_1 + float_1) # 61.4


# Modulus Operator (%): This returns the remainder when a number is divided by another number:

int_1 = 56
int_2 = 12

print(int_1 % int_2) # 8


# Floor Division (//): This operator is used to divide two numbers and round down the result to the nearest whole number:

print(int_1 // int_2) # 4
# exponosiel
int_1 = 4
int_2 = 2
print(int_1 ** int_2) # 16

# float() Function: You can use this function to convert an integer to float.
num = 4

print(float(num)) # 4.0

num = 4.0

print(int(num)) # 4

num_1 = 3.4
num_2 = 7.7

print(round(num_1)) # 3
print(round(num_2)) # 8

num = -13
print(abs(num)) # 13


# bin() Function: This is used to convert an integer to its binary representation as a string:
num = 56
print(bin(num))  # 0b111000


# oct() Function: This is used to convert an integer to its octal representation as a string:
num = 56
print(oct(num))  # 0o70

# hex() Function: This is used to convert an integer to its hexadecimal representation as a string:
num = 56
print(hex(num))  # 0x38

# pow() Function: This is used to raise a number to the power of another:
result = pow(2, 3) 
print(result)  # 8


'''
Augmented Assignments
Definition: Augmented assignment combines a binary operation with an assignment 
in one step. It takes a variable, applies an operation to it with another value, and stores the result back into the same variable.
'''

# Addition assignment 
my_var = 10
my_var += 5

print(my_var) # 15

# Subtraction assignment
count = 14
count -= 3

print(count) # 11

# Multiplication assignment 
product = 65
product *= 7

print(product) # 455

# Division assignment 
price = 100
price /= 4

print(price) # 25.0

# Floor Division assignment 
total_pages = 23
total_pages //= 5

print(total_pages) # 4

# Modulus assignment 
bits = 35
bits %= 2

print(bits) # 1

# Exponentiation assignment 
power = 2
power **= 3

print(power) # 8



# Working with Functions


def get_sum(num_1, num_2):
    return num_1 + num_2

result = get_sum(3, 4) # function call
print(result) # 7

# If a function does not explicitly return a value, then the default return value is None:

# Common Built-in Functions
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0


# Scope in Python
# Local Scope: This is when a variable declared inside a function or class can only be accessed within that function or class.

def my_func():
    num = 10
    print(num)

# Enclosing Scope: This is when a function that's nested inside another function can access the variables of the function it's nested within.
def outer_func():
    msg = 'Hello there!'
    
    def inner_func():
        print(msg)
    inner_func()

print(outer_func()) # Hello there!



# Global Scope: This refers to variables that are declared outside any functions or classes which can be accessed from anywhere in the program.
tax = 0.70 

def get_total(subtotal):
    total = subtotal + (subtotal * tax)
    return total

print(get_total(100))  # 170.0


# Built-in Scope: Reserved names in Python for predefined functions, modules, keywords, and objects.

print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False


# Comparison Operators
# Equal (==): Checks if two values are equal:
print(3 == 4) # False
# Not equal (!=): Checks if two values are not equal:
print(3 != 4) # True
# Strictly greater than (>): Checks if one value is greater than another:
print(3 > 4) # False
# Strictly less than (<): Checks if one value is less than another:
print(3 < 4) # True
# Greater than or equal(>=): Checks if one value is greater than or equal to another:
print(3 >= 4) # False
# Less than or equal(<=): Checks if one value is less than or equal to another:
print(3 <= 4) # True



# Working with if, elif and else Statements
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child')  # You are a child


is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')

# Truthy and Falsy Values
'''
Definition: In Python, every value has an inherent boolean value, or a built-in sense of whether it should be treated as True or False
in a logical context. Many values are considered truthy, that is, 
they evaluate to True in a logical context. Others are falsy, meaning they evaluate to False. Here are some examples of falsy values:

examples of falsey 
None
False
Integer 0
Float 0.0
Empty strings


Working with the bool() Function
Definition: If you want to check whether a value is truthy or falsy, you can use the built-in bool() function. It explicitly converts a value
 to its boolean equivalent and returns True for truthy values and False for falsy values. Here are a few examples:
'''
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True


'''
Boolean Operators and Short-circuiting
Definition: These are special operators that allow you to combine multiple expressions to create more complex decision-making logic in your code.
 There are three Boolean operators in Python: and, or, and not.
and Operator: This operator takes two operands and returns the first operand if it is falsy, otherwise, it returns the second operand.
 Both operands
 must be truthy for an expression to result in a truthy value.
'''
is_citizen = True
age = 25

print(is_citizen and age) # 25


'''
or Operator: This operator returns the first operand if it is truthy, otherwise, it returns the second operand. An or expression results
 in a truthy 
value if at least one operand is truthy. Here is an example:
'''
age = 19
is_employed = False
print(age or is_employed) # 19


age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')