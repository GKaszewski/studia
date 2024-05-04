n = int(input("podaj liczbe: "))
y = sum([x**2 for x in range(1, n+1)])
print(f'suma: {y}')