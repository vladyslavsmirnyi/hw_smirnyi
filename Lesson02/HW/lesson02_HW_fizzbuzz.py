fizz = int(input("Введите первое число (fizz):"))
buzz = int(input("Введите второе число (buzz):"))
number = int(input("Введите третье число:"))

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