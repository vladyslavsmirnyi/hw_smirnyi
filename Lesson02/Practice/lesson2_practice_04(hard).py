import math

number = int(input("Введите число:"))

max_rank_power = math.floor(math.log(number, 10)) + 1

print(str(number) + " = ", end="")
for rank_power in range(max_rank_power, 0, -1):
    rank = 10**rank_power
    rank_value = (number % rank - number % (rank // 10)) // (rank // 10)
    print(str(rank_value) + " * " + str(rank // 10), end="")
    if rank_power > 1:
        print(" + ", end="")
