# Python3 program for union() function

set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {7, 8, 9, 10}

# Using union function
print("set1 U set2 : ", set1.union(set2))
print("set1 U set2 U set3 :", set1.union(set2, set3))
# Without using union function
print("set1 U set2 : ", set1 | set2)
print("set1 U set2 U set3 :", set1 | set2 | set3)


# Find algorithm in Python
word = 'geeks for geeks'

# returns first occurrence of Substring
result = word.find('geeks')
print("Substring 'geeks' found at index:", result)

result = word.find('for')
print("Substring 'for ' found at index:", result)

# How to use find()
if word.find('pawan') != -1:
    print("Contains given substring ")
else:
    print("Doesn't contains given substring")
