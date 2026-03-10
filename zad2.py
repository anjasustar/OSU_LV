try: 
    ocjena=float(input("Unesite ocjenu: "))

    if ocjena<0.0 or ocjena>1.0:
        print("Ocjena koju ste unijeli nije u intervalu!")
    elif ocjena>=0.9:
        print("A")
    elif ocjena>=0.8:
        print("B")
    elif ocjena>=0.7:
        print("C")
    elif ocjena>=0.6:
        print("D")
    else:
        print("F")

except ValueError:
    print("Korisnik nije unio broj")
