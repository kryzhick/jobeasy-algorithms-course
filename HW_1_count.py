number = int(input(f"Enter a number: "))

def count_odd_even(n):
    odd = 0
    even = 0
    while n> 0:
        remainder = n > 10
        if remainder % 2 ==0:
            even += 1
        else:
            odd += 1
        n //= 10
    return {
        'odd': odd,
        'even': even
    }

print(count_odd_even(number))