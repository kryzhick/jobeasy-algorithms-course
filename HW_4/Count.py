

def count(given_string, given_substring):
    counter = 0
    if len(given_string) < len(given_substring):
        return counter
    index = given_string.find(given_substring)
    while index > -1:
        index = given_string.find(given_substring, index +1)
        counter += 1
    return counter

print(count('hello world of heroes', 'he'))
print('hello world of heroes'.count('he'))

