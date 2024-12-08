def f(x, y):
    total_sum = 0
    for num in range(x, y + 1):  
        if num % 6 == 0 and num % 4 != 0:
            total_sum += num
    return total_sum

print(f(1, 20))  
print(f(10, 30))  