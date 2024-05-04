i = 1
n = int(input("podaj liczbe: "))
print(f"podzielniki {n} to: ")
while i <= n:
    if n % i == 0:
        print(i, end=', ')
    i += 1

print('\na parzyste to: ')

i = 1
while i <= n:
    if n%i == 0 and (i % 2 == 0):
        print(i, end=', ') 
    i += 1

