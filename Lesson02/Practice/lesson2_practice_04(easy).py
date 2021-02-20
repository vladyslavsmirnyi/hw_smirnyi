number = int(input("Введите число:"))

max_rank = 1
while number // max_rank > 0:
    max_rank *= 10

print(str(number) + " = ", end="")
rank = max_rank
while rank > 1:
    rank_value = (number % rank - number % (rank // 10)) // (rank // 10)
    print(str(rank_value) + " * " + str(rank // 10), end="")
    if rank > 10:
        print(" + ", end="")
    rank //= 10
