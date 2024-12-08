def f(detector):
    people_in_room = 0  

    for action in detector:
        if action == '+':
            people_in_room += 1
        elif action == '-':
            people_in_room -= 1
        
        if people_in_room >= 3:
            return True
    
    return False

print(f("+-+++-+---"))  
print(f("+-+-+-+-"))    
print(f("+-++-+--"))    
print(f("+-++-++-+---")) 