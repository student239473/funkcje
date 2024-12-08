def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f'{hours:02}:{minutes:02}'
    elif time_format == '12':
        suffix = 'am' if hours < 12 else 'pm'
        display_hour = hours % 12
        if display_hour == 0:
            display_hour = 12 
        return f'{display_hour}:{minutes:02}{suffix}'

print(time_string(15, 38, '24'))  
print(time_string(8, 3, '24'))    
print(time_string(0, 5, '24'))    
print(time_string(11, 15, '12')) 
print(time_string(0, 7, '12'))    
print(time_string(7, 30, '12'))   
print(time_string(12, 46, '12'))  
print(time_string(13, 10, '12'))  
print(time_string(19, 2, '12'))   