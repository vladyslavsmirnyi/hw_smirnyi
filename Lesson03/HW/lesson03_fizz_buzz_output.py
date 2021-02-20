# Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
# Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите.

# for - переберает все элементы того что мы напсали после in
# и записывает нам в переменную, которую мы записали после for

# split - Разбивает строку по разделителю и создает список. По умолчанию разделитель - пробел
# int - целое число
# map - применяет переданную ей функцию к списку


f = open('numbers_fizz_buzz.txt')
f2 = open('file_hw.txt', 'w')


for s in f:
    numbers = list(s.split())
    fizz = int(numbers[0])
    buzz = int(numbers[1])
    number = int(numbers[2])

    counter = 1
    while counter <= number:
        if counter % fizz == 0 and counter % buzz == 0:
             f2.write("FB")
        elif counter % fizz == 0:
            f2.write("F")
        elif counter % buzz == 0:
            f2.write("B")
        else:
            f2.write(str(counter))
        counter += 1
    f2.write('\n')

f2.close()




