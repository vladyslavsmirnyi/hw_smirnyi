d = {'Vlad': [6,7,8,8,7], 'Oleg': [8,9,8,9,10], 'Roman': [8,9,7,8,9], 'Ignat': [1,4,2,5,2],'Vasya': [4,5,6,2,6] }
max_average = -1
min_average = float('inf')

print('Students: ')
for c in d:
    average = sum(d[c]) / len(d[c])
    print(c,'average score:',average)
    if average > max_average:
        max_average = average
        max_average_name = c
    if average < min_average:
        min_average = average
        min_average_name = c
print('')
print('The best student -',max_average_name + ',','average score: ',max_average)
print('The worst student -',min_average_name + ',','average score: ',min_average)