

string = input(f"Enter a string: ")

def longest_string(string_1):
    substring = ''
    result = ''
    for char in string_1:
        if char == ' ':
            if len(substring) > len(result):
                result = substring
            substring = ''
        else:
            substring += char
    else:
        if len(substring) > len(result):
            result = substring
        return result

print(longest_string(string))