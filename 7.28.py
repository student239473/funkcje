def f(dice):
    max_streak = 1  
    current_streak = 1  
    
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_streak += 1
        else:
            current_streak = 1
        
        if current_streak > max_streak:
            max_streak = current_streak
    
    return max_streak

print(f("5233165554211")) 
print(f("2133"))  