def check_if_first(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input("podaj liczbe:"))
if check_if_first(n):
    print(f'{n} jest pierwsza')
else:
    print(f'{n} nie jest pierwsza')