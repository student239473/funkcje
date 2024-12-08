def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False

    first_three_digits = [int(digit) for digit in product_code[:3]]
    fourth_digit = int(product_code[3])
    
    sum_of_first_three = sum(first_three_digits)
    
    remainder = sum_of_first_three % 7
    
    return remainder == fourth_digit

print(f("1082"))  
print(f("2035"))  
print(f("1114"))  
print(f("7071"))  