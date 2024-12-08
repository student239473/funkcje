import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

area_input = triangle_area(a, b, c)
print(f'The area of a triangle with sides {a}, {b}, and {c} is {area_input:.2f}')

area1 = triangle_area(3, 4, 5)
print(f'The area of a triangle with sides 3, 4, 5 is {area1:.2f}')

area2 = triangle_area(5, 12, 13)
print(f'The area of a triangle with sides 5, 12, 13 is {area2:.2f}')

area3 = triangle_area(7, 24, 25)
print(f'The area of a triangle with sides 7, 24, 25 is {area3:.2f}')