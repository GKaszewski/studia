m = n = ""
while not m.isdigit() or not n.isdigit():
    m = input('Podaj pierwsza liczbe: ')
    n = input('Podaj druga liczbe: ')
m = int(m)
n = int(n)
d = []
for i in range(1, min(m,n)+1):
    if m % i == 0 and n % i == 0:
        print(i)
        d.append(i)

print(f'najwiekszy wspolny dzielnik: {max(d)}')

# i = 1 
# while i <= min(m,n):
#     if m % i == 0 and n % i == 0:
#         print(i)
#         d.append(i)
#     i += 1

# print(f'ilosc dzielnikow: {len(d)}, najwiekszy wspolny dzielnik: {max(d)}')

def nwd(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
    print(f'nwd: {a}'.title())
    return a

nwd(m,n)
