brojevi=[]

while True:
    unos=input("Unesi broj: ")
    if unos=='Done':
        break
    try:
        broj=float(unos)
        brojevi.append(broj)
    except ValueError:
        print("Nisi unio broj")

BrojUnesenihElemenata=len(brojevi)
SrednjaVrijednost=sum(brojevi)/len(brojevi)
MinimalnaVrijednost=min(brojevi)
MaksimalnaVrijednost=max(brojevi)

brojevi.sort()

print('Broj unesenih elemenata je: ',BrojUnesenihElemenata)
print('Srednja vrijednost elemenata je: ',SrednjaVrijednost)
print('Minimalna vrijednost elemenata je: ', MinimalnaVrijednost)
print('Maksimalna vrijednost elemenata je: ',MaksimalnaVrijednost)

print(brojevi)