# def pierwsza(n):
#     if n < 2:
#         return False
#     i = 2
#     while i*i <= n:
#         print(f'i: {i}, n: {n}')
#         if n % i == 0:
#             return False
#         i += 1
#     return True

# print(pierwsza(30))


# a = [1,2,3,4,5,6]
# min_wartosc = min(a)
# indeks_min = a.index(min_wartosc)'

"dddf".split("d")
['d','d','df']

def silnia(n):
    if n==0:
        return 1
    return n * silnia(n-1)


f = open("tekst.txt", "a")
liczby = [int(x) for x in f.read().split(" ")]
srednia = sum(liczby)/len(liczby)
print(srednia)
f.close()