number = int(input("Введите число:"))
number = str(number)
number_length = len(number)
indices = range(number_length)

print(number + " = ", end="")
for i in indices:
    print(number[i] + " * " + str(10**(number_length - 1 - i)), end="")
    if i < number_length - 1:
        print(" + ", end="")