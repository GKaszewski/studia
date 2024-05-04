#--------------------- 2 zadanie --------------------
from math import sqrt

def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    
    pierwiastek = int(sqrt(n)) + 1
    for dzielnik in range(3, pierwiastek, 2):
        if n % dzielnik == 0:
            return False
    return True

#albo
def czy_pierwsza_druga_wersja(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    

f = open(r'liczby.txt', 'r') 
dane = f.readlines()
for liczba in dane:
    if czy_pierwsza(int(liczba)):
        print(liczba)
f.close()



# liczby = []
# for liczba_tekst in dane:
#     nasza_liczba = int(liczba_tekst)
#     liczby.append(nasza_liczba)

# for liczba in liczby:
#     if czy_pierwsza(liczba):
#         print(liczba)


#--------------------- 3 zadanie --------------------

def ile_mniejszych_do_kwadratu(n):
    mniejsze = []
    for i in range(1, n):
        if i**2 < n:
            mniejsze.append(i)
    print(mniejsze)
    return len(mniejsze)

n = int(input("Podaj n:"))
print(ile_mniejszych_do_kwadratu(n))

#--------------------- 4 zadanie --------------------

def odwroc_liste(lista):
    lista.reverse()
    return lista

lista = [1,2,3,4,5,6,7,8]
print(odwroc_liste(lista))
