# Exercise 1
students = ['jack', 'john', 'jim', 'kim', 'kevin', 'kerry']
#print(students[1])
#print(students[len(students)-1])


# Exercise 2
foods = ('pizza', 'apples', 'sushi', 'tacos', 'burgers', 'pasta')
#for food in foods:
#    print(f'{food} is a good food')

# Exercise 3
#last_two = slice(len(foods)-2, len(foods))
#print(foods[last_two])

#  Exercise 4
#home_town = {
#    'city': 'South Bend',
#    'state': 'Indiana',
#    'population': 102037 
#}
#print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Exercise 5
#for key in home_town:
#    print(f'{key} = {home_town[key]}')

# Exercise 6
#cohort = []
#for student in students:
#    i = students.index(student)
#    cohort.append({
#        'student': student,
#        'fav_food': foods[i]
#    })
#for c in cohort:
#    print(c)

# Exercise 7
#awesome_students = []
#for student in students:
#    awesome_students.append(f'{student} is awesome!')
#
#for awe_stu in awesome_students:
#    print(awe_stu)

# Exercise 8
for food in foods:
   if food.find('a') > 0:
       print(food)