def slette_avtale():
    print(avtale_liste)
    valg = int(input("Hvilken avtale ønsker du å slette: "))
    
def redigere_avtale():
    print(avtale_liste)
    valg = int(input("Hvilken avtale ønsker du å redigere: "))


def hovedmeny():
    print("Les inn avtaler fra fil")
    print("Skriv avtalene til fil")
    print("Skriv inn en ny avtale")
    print("Skriv ut alle avtalene")
    print("Slette en avtale")
    print("Redigere en avtale")
    print("Jeg vil avslutte")
    valg=int(input("velg et alternativ: "))
    if valg==1:
        avtaler_fra_fil()
    elif valg==2:
        avtaler_til_fil()
    elif valg ==3:
        ny_avtale()
    elif valg==4:
        skriv_ut_alle_avtaler()
    elif valg==5:
        slette_avtale()
    elif valg==6:
        redigere_avtale()
    elif valg==7:
        exit
    else:
        print("Ugyldig svar, vennligst bruk 1-7")
