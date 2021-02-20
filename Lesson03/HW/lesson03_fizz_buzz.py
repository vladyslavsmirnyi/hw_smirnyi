# Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
# Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите.


f = open('numbers_fizz_buzz.txt')
for s in f:
    numbers = list(map(int,s.split()))
    fizz = numbers[0]
    buzz = numbers[1]
    number = numbers[2]

    counter = 1
    while counter <= number:
        if counter % fizz == 0 and counter % buzz == 0:
            print("FB", end=" ")
        elif counter % fizz == 0:
            print("F", end=" ")
        elif counter % buzz == 0:
            print("B", end=" ")
        else:
            print(counter, end=" ")
        counter += 1
    print()


