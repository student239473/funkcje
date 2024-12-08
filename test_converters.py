import converters

def test_converters():
    print('### Test converters')
    print(f'Three meters is {converters.m_to_cm(3)}cm')  
    
    print(f'532cm is {converters.cm_to_m(532)}m')  
    
    print(f'50cm is {converters.cm_to_inches(50)} inches')  
    
    print(f'5 feet 10 inches is {converters.ft_inch_to_cm(5, 10)} cm') 

if __name__ == "__main__":
    test_converters()