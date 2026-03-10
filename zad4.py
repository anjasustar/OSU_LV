import string

fhand=open('song.txt')
sadrzaj=fhand.read()

SadrzajBezZnakova=sadrzaj.translate(str.maketrans('','',string.punctuation)).lower()
rijeci=SadrzajBezZnakova.split()

rjecnik={}

for r in rijeci:
    rjecnik[r]=rjecnik.get(r,0)+1

JedinstveneRijeci=[]

for kljuc in rjecnik:
    if rjecnik[kljuc]==1:
        JedinstveneRijeci.append(kljuc)

BrojJedinstvenihRijeci=len(JedinstveneRijeci)
print('Broj jedinstvenih rijeci je: ', BrojJedinstvenihRijeci)
print(JedinstveneRijeci)

fhand.close()