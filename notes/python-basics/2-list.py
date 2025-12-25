'''
Docstring for notes.python-basics.2-list
The list data type is an ordered sequence of elements that can be comprised of strings, numbers, or even other lists.
 Lists are mutable and use zero-based indexing, meaning that the first element of the list is at index zero.
'''
cities = ['Los Angeles', 'London', 'Tokyo']
cities[0]
cities[-1]#to access last element

# Another way to create a list is to use the list() constructor. The list() constructor is used to convert an iterable into a list like this:
name='soukayna'
letters=list(name)
countletters=len(name)
print(letters)
print(countletters)


# If you wanted to update a value at a particular index, you can do something like this:

programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

# If you want to remove an element from a list you can use the del keyword like this:
del programming_languages[0]
print(programming_languages)

# Sometimes it is helpful to check if an element is inside the list. To do that, you can use the in keyword like this:
print('c++' in programming_languages)

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2][1])

# Unpacking values from a list is a technique used
#  to assign values from a list to new variables. Here is an example of unpacking a developer list into new variables called name, age and job.

character=['soukayna',25,'developper']
name,age,job=character
print(name,age,job)


developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']


desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie']
print(desserts[::2])


# What Are Some Common Methods Used for Lists?
# add in the end of the list
numbers = [1, 2, 3, 4, 5]
list1=[7,8,9]
numbers.append(6)
numbers.append(list1)
print(numbers) # [1, 2, 3, 4, 5, 6]
# extend() add list element in another list
numbers.extend(list1)
print(numbers)
# insert() to add an element to a specific index
numbers.insert(11,10)
print(numbers)
# remove() take the elemnt as argument and deletes the first instance not all of them
list2=[1,2,3,4,5,5]
list2.remove(5)
print(list2)
# pop() will remove all instances of the elemetnin the argument , if you dont specify the elemetn removes the last item in the list
# clear( ) empties the list
list2.clear()

number = [19, 2, 35, 1, 67, 41]
number.sort()
print(number) # [1, 2, 19, 35, 41, 67]

numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

# In contrast to the sort() method, there
#  is the sorted() function which works for any iterable and returns a new sorted list instead of modifying the original list. For example:
print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]

# The next method we will take a look at is the reverse() method. This method, will reverse a list of elements in place like this:
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()
print(numbers) # [1, 2, 3, 4, 5, 6]


# The last method we will take a look at is the index method. This is used to find the first index where 
# an element can be found in a list. Here is an example of using the index method to find the language 'Java' in a programming_languages list:

programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1