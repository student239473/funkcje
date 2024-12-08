def sum_digits(number):
    number = abs(number)
    digits = str(number)
    total = sum(int(digit) for digit in digits)
    return total

any_number = int(input('Enter integer number: '))

result = sum_digits(any_number)

print(f'The sum of the digits in the number {any_number} is {result}')