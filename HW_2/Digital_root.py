from HW_1_sum import sum_of_digit

def digital_root(number):
  while number > 9:
      number = sum_of_digit(number)
  return number

print(digital_root(132189))