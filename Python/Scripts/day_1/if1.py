score = int(input('Enter score: '))

if score >= 80:
    grade = 'A'
else:
    if score >= 70:
        grade = 'B'
    else:
        grade = 'C'

print('\n\nGrade is: {}'.format(grade))
