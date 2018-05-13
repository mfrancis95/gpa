from sys import argv

grade_values = {
    'a': 4.0,
    'a-': 3.67,
    'b+': 3.33,
    'b': 3.0,
    'b-': 2.67,
    'c+': 2.33,
    'c': 2,
    'c-': 1.67,
    'd+': 1.33,
    'd': 1,
    'd-': 0.67,
    'f': 0
}
total_credits = 0
total_points = 0

for grade in map(lambda grade: grade.split(':'), argv[1:]):
    grade.append(3.0)
    total_credits += float(grade[1])
    total_points += grade_values[grade[0]] * float(grade[1])

print('{0:.2f}'.format(total_points / total_credits))