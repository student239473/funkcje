import range_utils  

number = int(input("A number: "))

x = 2
y = 15

is_in_range = range_utils.is_within_range(number, x, y)

if is_in_range:
    print(f"Number {number} in the range <{x},{y}>: yes")
else:
    print(f"Number {number} in the range <{x},{y}>: no")