def f(number, even):
    num_str = str(number)
    
    total_sum = 0
    
    for char in num_str:
        digit = int(char)  
        
        if even:
            if digit % 2 == 0:
                total_sum += digit
        else:
            if digit % 2 != 0:
                total_sum += digit
    
    return total_sum

print(f(3124, True))   
print(f(3124, False))  
print(f(20576, False)) 
print(f(20576, True))  
print(f(13115, True))  