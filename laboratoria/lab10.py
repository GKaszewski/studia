l = []
for i in range(10):
    liczba = int(input("Podaj liczbe: "))
    l.append(liczba)

def check_if_first(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for liczba in l:
    if check_if_first(liczba):
        print(liczba)
