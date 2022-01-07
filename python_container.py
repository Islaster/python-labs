# Exercise 1
students = ['jack', 'john', 'jim', 'kim', 'kevin', 'kerry']
print(students[1])
print(students[len(students)-1])


# Exercise 2
foods = ('pizza', 'apples', 'sushi', 'tacos', 'burgers', 'pasta')
for food in foods:
    print(f'{food} is a good food')
# Exercise 3
last_two = slice(len(foods)-2, len(foods))
print(foods[last_two])
  