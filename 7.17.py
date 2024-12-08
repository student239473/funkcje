def f(palindrome):
    normalized = ''.join(char.lower() for char in palindrome if char.isalnum())
    
    return normalized == normalized[::-1]

print(f("radar"))       
print(f("12-11-21"))     
print(f("book"))         