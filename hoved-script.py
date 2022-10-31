def slette_avtale():
    print(avtale_liste)
    valg = int(input("Hvilken avtale ønsker du å slette: "))
    
def redigere_avtale():
    print(avtale_liste)
    valg = int(input("Hvilken avtale ønsker du å redigere: "))


def hovedmeny():
    print("1: Les inn avtaler fra fil")
    print("2: Skriv avtalene til fil")
    print("3: Skriv inn en ny avtale")
    print("4: Skriv ut alle avtalene")
    print("5: Slette en avtale")
    print("6: Redigere en avtale")
    print("7: Jeg vil avslutte")
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
