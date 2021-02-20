
print('Let`s find to odd number and chek devision by 3 and 5')
number = int(input('enter a number: '))

if number % 2 != 0 and number % 3 == 0 and  number % 5 == 0:
    print('This number we are searching for')
else:
    print('This number is wrong')