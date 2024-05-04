from math import sqrt
numbers = list(map(float, input("Wprowadz liczby oddziel je spacja: ").split(' ')))
average = sum(numbers) / len(numbers)
std_deviation = 0
std_parts = []
for n in numbers:
    part = (n - average)**2
    std_parts.append(part)
n = len(numbers)
std_deviation = sqrt( (sum(std_parts) * 1/(n*(n-1))) )
print(f'Srednia: {average}, odchylenie standardowe: {std_deviation}')
