n = int(input("Podaj dla ilu liczb policzyc srednia: "))
l = []
for i in range(n):
    liczba = int(input("Podaj liczbe: "))
    l.append(liczba)

# srednia = sum(l) / n
# print(f'srednia: {srednia}')

srednia = 0
suma = 0 
for i in l:
    suma += i
srednia = suma / n
print(f'srednia: {srednia}')