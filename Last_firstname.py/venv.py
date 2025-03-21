# main.py

# List
fruits = ['apple', 'strawberry', 'banana', 'kiwi']
print(fruits)

# Dictionary
fruit_colors = {'apple': 'red', 'strawberry': 'white', 'banana': 'green', 'kiwi': 'golden'}
print(fruit_colors)

# Add an item
fruits.append('orange')
print(fruits)

# Remove item
fruits.remove('banana')

# Sort list
fruits.sort()
print(fruits)

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])
print(matrix[0][2])
print(matrix[2][0])

# Keys and values
keys = fruit_colors.keys()
values = fruit_colors.values()
print(keys)
print(values)

# Update dictionary
fruit_colors['apple'] = 'green'
print(values)

# get()
print(fruit_colors.get('orange', 'Not found'))
fruit_colors['orange'] = 'blood orange'
fruit_colors.update({'grapes': 'purple'})
print(fruit_colors)
