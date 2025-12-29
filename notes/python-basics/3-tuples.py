developer=('alice',34,'rust developper')
# tupes are immutable you cant update them

# developer[0]='soukayna';
# print(developer[1])

name="soukayna"
tuple_name=tuple(name)
if ('s'in tuple_name):
    print(True)

name,age,job=developer
print(name,age,job)
    
name,*details=developer
print(name,details)

#extracting with split
deserts=('cake','strawberry','cookies')
deserts.count('cake')#calculate how many time an item has appeared
         
crs=deserts[1:3]
print(type(crs)) #class tuple

# removing items from tuple isnt possible
# del deserts[0]

'''
So when might you use a tuple over a list?
If you need a dynamic collection of elements where you can add, 
remove and update elements, then you should use a list.
 If you know that you are working with a fixed and immutable
 collection of data, then you should use a tuple.
'''


# What Are Some Common Methods for Tuples?
programming_languages = ('Rust', 'Java', 'Python', 'C++','Java', 'Rust')
programming_languages.count('Rust')
programming_languages.index('Java',2)
# sort by length
sorted(programming_languages,key=len)
sorted(programming_languages,reverse=True)
# you can even add start and stop for index search if you want to
numbers=(13,2,5,8,94,7,45,5)
# numbers.sort()  because sort() cahnges in the origanal since tuple is immutable u can do that
# sorted() return a list from the tuple and sort them
print(type(sorted(numbers)))

