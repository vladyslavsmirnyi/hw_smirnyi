import math


def find_flat(flat_number, flats_per_floor, floors_count):
    flats_per_entrance = flats_per_floor * floors_count
    entrance_number = math.ceil(flat_number / flats_per_entrance)
    floor_number = math.ceil((flat_number - flats_per_entrance * (entrance_number - 1)) / flats_per_floor)
    return entrance_number, floor_number

entrance, floor = find_flat(27, 3, 9)
print("Подъезд:", entrance, "этаж:", floor)

entrance, floor = find_flat(54, 3, 9)
print("Подъезд:", entrance, "этаж:", floor)

entrance, floor = find_flat(123545, 25, 50)
print("Подъезд:", entrance, "этаж:", floor)