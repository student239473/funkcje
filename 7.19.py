from collections import Counter

def f(number):
    num_str = str(number)
    
    digit_count = Counter(num_str)
    
    repeated_sum = 0
    
    for digit, count in digit_count.items():
        if count > 1: 
            repeated_sum += int(digit) * (count - 1)  
    
    return repeated_sum

print(f(1027))       
print(f(230335))     
print(f(513553007))