


from datetime import datetime
import pandas as pd
import csv


dict_liste = dict()  
liste=[]


#Klasse for ny avtale 
class Avtale():
    def __init__(self, init_tittel = "", init_sted = "", init_starttidspunkt = datetime.now(), init_varighet = 0, init_kategori ="" ):
        self.tittel = init_tittel
        self.sted = init_sted
        self.starttidspunkt = init_starttidspunkt
        self.varighet = init_varighet
        self.kategori = init_kategori
        
#Avtale streng __str__
    def __str__(self):
        return f"{self.tittel}, {self.sted}, {self.starttidspunkt}, {self.varighet} min, {self.kategori}"


#filterfunksjon for liste, aktuell liste (avtale_liste), kolonne som skal letes i (kolonne) og søkestreng (lete_streng).
#burde gjerne lage felles public dataframe!!
#exceptionhandling!
def liste_filter(avtale_liste):
    gyldige_kolonner = ["tittel", "sted", "starttidspunkt", "varighet", "kategori"]  
    kolonne = input("Hvilken kolonne ønsker du å lete i? %s:"%(gyldige_kolonner))
    lete_streng = input('Hva leter du etter?: ')
    
    data_frame = pd.DataFrame(columns = ['tittel','sted','starttidspunkt','varighet','kategori'])
    for i in avtale_liste:
        df = pd.DataFrame([[i.tittel, i.sted, str(i.starttidspunkt), i.varighet, i.kategori]], columns=('tittel','sted','starttidspunkt','varighet','kategori'))
        data_frame = data_frame.append([df], ignore_index=True)
    try: 
        data_frame[data_frame['%s'%(kolonne)].str.contains(lete_streng)]
    except:
        print("\nSøket ga ingen resultater.\n")
    else:
        return print("Søkeresultat som inneholder '%s': \n"%(lete_streng),data_frame[data_frame['%s'%(kolonne)].str.contains(lete_streng)])


            
#Torbjørn fix og fjern kommentar
def avtaler_fra_fil():
    print("Du har valgt: 1: Skriv inn avtaler fra fil")
    fortsette_tilbake = input("Hvis du vil fortsette, trykk ENTER, hvis du vil gå tilbake, tast 0")
    if fortsette_tilbake == "0":
        hovedmeny(1)
    else:
        pass
    print("Denne funksjonen skriver inn avtalene til en ny fil") #erstatt denne linjen med funksjonen
    #global dict_liste 
    #dict_liste.clear() # slett den eksisterende listen
    with open('avtaler.csv', 'r') as csv_file:
        reader = csv.reader(csv_file,delimiter=';')
        dict_liste = dict(reader)
def avtaler_til_fil():
    print("Du har valgt: 2: Skriv avtalene til fil")
    fortsette_tilbake = input("Hvis du vil fortsette, trykk ENTER, hvis du vil gå tilbake, tast 0")
    if fortsette_tilbake == "0":
        hovedmeny(1)
    else:
        pass
    print("Denne funksjonen skriver avtalene til fil")#Erstatt denne linjen med funksjonen
    with open('avtaler.csv', 'a',newline='') as csv_file:  # appender csv filen, endre til w hvis den skal overskrives
        writer = csv.writer(csv_file,delimiter =";")
        for key, value in dict_liste.items():
            writer.writerow([key,value])
def ny_avtale():
    print("Du har valgt: 3: Skriv inn en ny avtale")
    fortsette_tilbake = input("For å fortsette, trykk ENTER, hvis du ønsker å gå tilbake til hovedmenyen, tast 0 :")
    if fortsette_tilbake == "0":
        hovedmeny(1)
    else:
        pass
        bekreftet = "" 
        while bekreftet != "Ja":
            tittel = input("Ny avtale\nOppgi tittel:")
            sted = input("Oppgi sted:")
            print("Oppgi tidpunkt(ÅÅÅÅ-MM-DD TT:MM:SS):")
            starttidspunkt = ""

            while starttidspunkt == "":
                try:
                    starttidspunkt = datetime(int(input("ÅÅÅÅ:")),int(input("MM:")),int(input("DD:")),int(input("TT:")),int(input("MM:")))                
                    if starttidspunkt < datetime.now():
                        print("Dato utgått! Vennligst oppgi på nytt.")
                        starttidspunkt = ""
                except ValueError:
                    print("Ikke en gyldig dato!")

            varighet = input("Oppgi varighet:")
            while varighet != type(int):
                try:
                    varighet = int(varighet)
                    break
                except ValueError:
                    print("Ikke et gyldig tall!")
                    varighet = input("Oppgi varighet:")

            kategori = input("Oppgi kategori:")


            print("Bekreft ", Avtale(tittel,sted, starttidspunkt, varighet, kategori))
            bekreftet = input("Ja/Nei:").casefold()        
            if "ja" in bekreftet:

                dict_liste[tittel]=Avtale(tittel,sted, starttidspunkt, varighet, kategori)
                liste.append(Avtale(tittel,sted, starttidspunkt, varighet, kategori))

                return(Avtale(tittel,sted, starttidspunkt, varighet, kategori))
                break
            else:
                print("Skriv avtalen på nytt.")
                continue    
    
    
    
    
    
    
def skriv_ut_alle_avtaler():
    print("Du har valgt: 4: Skriv ut alle avtalene")
    fortsette_tilbake = input("For å fortsette, tast 1, hvis du ønsker å gå tilbake til hovedmenyen, tast 0 :")
    if fortsette_tilbake == "0":
        hovedmeny()
    else:
        pass
        df_liste = pd.DataFrame(columns = ['tittel','sted','starttidspunkt','varighet','kategori'])  
        for i in liste:
            df = pd.DataFrame([[i.tittel,i.sted,str(i.starttidspunkt),i.varighet,i.kategori]], columns=('tittel','sted','starttidspunkt','varighet','kategori'))
            df_liste = df_liste.append([df], ignore_index=True)

        print("Utskrift liste")
        print(df_liste)    
    
    
    
    
    
    print("Denne funksjonen skriver ut alle avtalene")#erstatt denne linjen med funksjonen
def slette_avtale():
    print("Du har valgt: 5: Slette en avtale")
    fortsette_tilbake = input("For å fortsette, trykk ENTER, hvis du ønsker å gå tilbake til hovedmenyen, tast 0 :")
    if fortsette_tilbake == 1:
        hovedmeny()
    else:
        pass
    print("Denne funksjonen sletter en avtale")#erstatt denne linjen med funksjonen
def redigere_avtale():
    print("Du har valgt: 6: Redigere en avtale")
    fortsette_tilbake = input("For å fortsette, trykk ENTER, hvis du ønsker å gå tilbake til hovedmenyen, tast 0 :")
    if fortsette_tilbake == 1:
        hovedmeny()
    else:
        pass
    print("denne funksjonen redigerer en avtale")#erstatt denne linjen med funksjonen
def hovedmeny(start):                 
    while start == 1:
        print("1: Les inn avtaler fra fil")
        print("2: Skriv avtalene til fil")
        print("3: Skriv inn en ny avtale")
        print("4: Skriv ut alle avtalene")
        print("5: Slette en avtale")
        print("6: Redigere en avtale")
        print("0: Jeg vil avslutte")
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
            print("Ugyldig svar, vennligst bruk 1-6")
hovedmeny(1)
        
