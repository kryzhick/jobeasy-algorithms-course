from HW_1_sum import sum_of_digit

def digital_root_rec(num):
    if num < 10:
        return num
    return digital_root_rec(sum_of_digit(num))

print(digital_root_rec(121212))

