# #example of using *args function
# def printArgsFunctionParameters(name, *args):
#     print(type(args))
#     for arg in args:
#         print(arg)

# printArgsFunctionParameters('Paul Smith', 5, 'Bazinga', True, 5.14, [1, True])

# #example of using **kwargs function
# def printKwargsFunctionParameters(**kwargs):
#     print(type(kwargs))
#     if kwargs['name']:
#         print(kwargs['name'])
#     if kwargs['num']:
#         print(kwargs['num'])
    
# printKwargsFunctionParameters(name = 'Sam', num = 18, access = False, petName = 'Baki')

# #some exercises
# def isUppercase(word):
#     if word[0] == word[0].upper():
#         print(True)
#     else:
#         print(False)

# isUppercase(input())

# def printName(first_name = '', last_name = ''):
#     if first_name and last_name:
#         print(first_name + ' ' + last_name)
#     else:
#         print('No name passed in')

# printName()
# printName('Lana')
# printName('Lana', 'Kowalski')

# #example of using ternary operator
# def isFive(num):
#     const = 5
#     return True if num == const else False

# print(isFive(5))
# print(isFive(7))

# # changing list item values by index
# sports = [ "baseball", "football", "hockey", "basketball" ]
# def change(aList):
#     aList[ 0 ] = "soccer"
# print(id(sports))
# print(f"Before Altering: {sports}")
# change(sports)
# print(id(sports))
# print(f"After Altering: {sports}")

# names = ['Bob', 'Rich', 'Amanda']
# def changeValue(aList, value, index):
#     aList[index] = value

# print(names)
# changeValue(names, 'Robert', 0)
# print(names)

