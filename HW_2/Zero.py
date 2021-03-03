


def zeros_not_for_heroes(number):
    if number == 0:
        return number
    while number % 10 == 0:
        number //= 10
    return number

print(zeros_not_for_heroes(20324200000))