
def replace(string_1, old_substr_1, new_substr_1, count):
    len_old_string = len(old_substr_1)
    index = string_1.find(old_substr_1)
    counter = 0
    while index > -1 and counter < count:
        string_1 = string_1[:index] + new_substr_1 + string_1[index + len_old_string:]
        index = string_1.find(old_substr_1, index + len(new_substr_1))
        counter += 1
    return string_1

print('aaaabbaaabbaaaa'.replace('aa', 'a', 4))
print(replace('aaaabbaaabbaaaa','aa', 'a', 4))