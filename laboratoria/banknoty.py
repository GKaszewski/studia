nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
kwota = float(input("Podaj kwotę:"))

def wydaj_banknoty(kwota):
    banknoty = {}
    pozostala_kwota = kwota
    for nominal in nominaly:
        if pozostala_kwota <= 0: 
            break
        ile = pozostala_kwota // nominal
        if ile > 0:
            banknoty[nominal] = int(ile)
        pozostala_kwota = round(pozostala_kwota - (nominal * ile), 2)
    return banknoty


print(wydaj_banknoty(kwota))
