file = open("test.txt", "r")
for line in file:
    semi_index = line.index(";")
    before_semi = line[:semi_index].split()
    after_semi = line[semi_index + 1:].split()

    quotient = int(after_semi[0])
    remainder = int(after_semi[1])

    numbers = list(map(int, before_semi))
    numbers_sum = sum(numbers)
    true_quotient = numbers_sum // len(numbers)
    true_remainder = numbers_sum % len(numbers)

    # :-1 чтобы убрать перенос строки в конце
    print(line[:-1], end=" ")
    print(quotient == true_quotient and remainder == true_remainder)