# Strings ---------------------------------------
basicString = 'String1'
basicString1 = "String2"
multilineString = '''Multiline string. Template Literal'''
multilineString1 = """Multiline string. Template literal"""

# If a string has has quotes, use the opposite type of quotes to denote string to avoid errors.
speechStrin = 'Reggies Says, "What about quote"'

# Python Indexing Operator (same as lists) - [startIdx:endIdx]
greet = 'Hello, World!'

print(greet[0]) # indexing a single char
print(greet[0:5]) # Print a sliced substring from index 0 - 5
print(greet[3:]) #Print everythin from 3 index to the end
print(greet * 3) # repeat string with * multiplication operator
print(greet + " smell ya later") # concatenate with + operator
print(greet.lower())
print(greet.replace('l', '@')) # replace one substring with another
print(greet.upper())
print(greet.split('l')) # removes delimiter when run
print(len(greet)) # len function

# Lists ---------------------------------------
animals = ['emu', 'squirrel', 'cat']
# use the python indexing operator to access elements of an list
print(animals[2])
print(animals[1])


# Lists ---------------------------------------
# Index operator - [start : stop : step]
animals = ['emu', 'squirrel', 'cat']
# use the python indexing operator to access elements of an list
print(animals[2])
print(animals[1])

bool = [True, False, True, True]
mixed = [1, "String", True, [1, 2, 4]]
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # mixed data type
# Indexing starts at 0
# [start : stop(not inclusivee) : step]

print(nums[2:9:3]) # start at 2nd index : stop at 9th index : step by 3s
print(nums[9::-1]) # negative step make a list count backwards
print(nums[3::2]) # counts from 3 index to the end by 2s
print(nums[:5]) #start at the begging and count to the 5

# 2d Lists
num2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Accessing 2d lists
print(num2[1][2]) # 6
print(num2[0][2]) # 3




# Strings ---------------------------------------
basicString = 'String1'
basicString1 = "String2"
multilineString = '''Multiline string. Template Literal'''
multilineString1 = """Multiline string. Template literal"""

# If a string has has quotes, use the opposite type of quotes to denote string to avoid errors.
speechString = 'Reggies Says, "What about quote"'

# Python Indexing Operator (same as lists) - [startIdx:endIdx]
greet = 'Hello, World!'
# Turning string into a list 
print(list(speechString))
# print(greet[0]) # indexing a single char
# print(greet[0:5]) # Print a sliced substring from index 0 - 5
# print(greet[3:]) #Print everythin from 3 index to the end
# print(greet * 3) # repeat string with * multiplication operator
# print(greet + " smell ya later") # concatenate with + operator
# print(greet.lower())
# print(greet.replace('l', '@')) # replace one substring with another
# print(greet.upper())
# print(greet.split('l')) # removes delimiter when run
# print(len(greet)) # len function

# print(type(str(13))) # now a string
# print(type(13)) # integer

# print(type(str(13.13)))
# print(type(13.13))


# # Lists ---------------------------------------
# # Index operator - [start : stop : step]
animals = ['emu', 'squirrel', 'cat']
# # use the python indexing operator to access elements of an list
# print(animals[2])
# print(animals[1])

# bool = [True, False, True, True]
# mixed = [1, "String", True, [1, 2, 4]]
# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # mixed data type
# # Indexing starts at 0
# # [start : stop(not inclusivee) : step]

# print(nums[2:9:3]) # start at 2nd index : stop at 9th index : step by 3s
# print(nums[9::-1]) # negative step make a list count backwards
# print(nums[3::2]) # counts from 3 index to the end by 2s
# print(nums[:5]) #start at the begging and count to the 5

# # 2d Lists
# num2 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # Accessing 2d lists
# print(num2[1][2]) # 6
# print(num2[0][2]) # 3

# # Turning string into a list 
# print(list(speechString))

# Modifying elements from array using [] notation
# reference array, then index number and edit as needed
print(animals)
animals[0] = "dog"

print(animals)

# adds single element
animals.append('deer')
print(animals)

# animals2 = ['bobcat', 'chipmunk', 'ferret']

# adds multielement, iterable
animals.extend(['bobcat', 'chipmunk', 'ferret'])

print(animals)