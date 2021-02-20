def process_line(line):
    numbers = list(map(int, line.split()))
    fizz = numbers[0]
    buzz = numbers[1]
    number = numbers[2]
    count_loop(fizz, buzz, number)
    print()


def count_loop(fizz, buzz, number):
    counter = 1
    while counter <= number:
        count_single(fizz, buzz, counter)
        counter += 1


def count_single(fizz, buzz, counter):
    if is_multiple(counter, fizz) and is_multiple(counter, buzz):
        print("FB", end=" ")
    elif is_multiple(counter, fizz):
        print("F", end=" ")
    elif is_multiple(counter, buzz):
        print("B", end=" ")
    else:
        print(counter, end=" ")


def is_multiple(a, b):
    return a % b == 0


f = open('numbers_fizz_buzz.txt')
for s in f:
    process_line(s)
