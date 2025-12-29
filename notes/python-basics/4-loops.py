programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)


for char in 'soukayna':
    print(char)
'''
 nested loops:
The outer loop will iterate through each category in the categories list.
 For each category, the inner loop will iterate through each food in
 the foods list. Here is the result that will be printed to the console:
'''

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']


for category in categories :
    for food in foods:
        print(category,food)



# secret_number=3
# guess=0
# while guess !=secret_number:
#     guess=int(input('guess the number between (1-5)'))
#     if guess!=secret_number:
#        print('wrong try again')
# print('you got it ')


developer_names = ['Jess','Merrinda' , 'Tom','soukayna','Naomi','jessica']

for developer in developer_names:
    if developer == 'Naomi':
        break
    elif developer=='Tom':
        continue
    print(developer)


words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")


