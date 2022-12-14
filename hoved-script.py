from datetime import datetime
import pandas as pd
import csv
import tkinter
from tkinter import filedialog
import os


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


#filterfunksjon for liste
def liste_filter(avtale_liste):
    gyldige_kolonner = ["tittel", "sted", "starttidspunkt", "varighet", "kategori"]
    gyldige_kolonner_print = ["1. Tittel", "2. Sted", "3. Starttidspunkt", "4. Varighet", "5. Kategori"]
    print("Hvilken kolonne ønsker du å lete i?")
    print('\n'.join(gyldige_kolonner_print))
    while True:
        try:
            kolonne = int(input('Skriv inn valg [1-6]: '))
            if kolonne < 1 or kolonne > 5:
                raise ValueError
        except ValueError:
            print('Velg en gyldig kategori')
        else:
            lete_streng = str(input('Hva leter du etter?: '))
            data_frame = pd.DataFrame(columns = ['tittel','sted','starttidspunkt','varighet','kategori'])
            for i in avtale_liste:
                df = pd.DataFrame([[i.tittel, i.sted, str(i.starttidspunkt), i.varighet, i.kategori]], columns=('tittel','sted','starttidspunkt','varighet','kategori'))
                data_frame = data_frame.append([df], ignore_index=True)
            return print("Søkeresultat som inneholder '%s': \n"%(lete_streng),data_frame[data_frame['%s'%(gyldige_kolonner[kolonne-1])].str.contains(lete_streng)])           
    
    


        
def avtaler_fra_fil():
    print("Du har valgt: 1: Skriv inn avtaler fra fil")
    fortsette_tilbake = input("Hvis du vil fortsette, trykk ENTER, hvis du vil gå tilbake, tast 0")
    if fortsette_tilbake == "0":
        hovedmeny(1)
    else:
        pass
        tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
        filnavn = filedialog.askopenfilename()
        global dict_liste
        #dict_liste.clear() # slett den eksisterende listen
        with open(filnavn, 'r') as csv_file:
            reader = csv.reader(csv_file,delimiter=';')
            dict_liste = dict(reader)
        print ("Lest følgende avtaler fra fil: ")
        for i in (dict_liste):
            print(i," - ",dict_liste[i])
        input("For å gå tilbake til hovedmenyen, trykk ENTER")
        hovedmeny(1)
def avtaler_til_fil():
    print("Du har valgt: 2: Skriv avtalene til fil")
    fortsette_tilbake = input("Hvis du vil fortsette, trykk ENTER, hvis du vil gå tilbake, tast 0")
    if fortsette_tilbake == "0":
        hovedmeny(1)
    else:
        pass
        with open('avtaler.csv', 'a',newline='') as csv_file: # appender csv filen, endre til w hvis den skal overskrives
            writer = csv.writer(csv_file,delimiter =";")
            for key, value in dict_liste.items():
                writer.writerow([key,value])
            print ("Skrevet følgende avtaler til fil: ")
            for i in (dict_liste):
                print(i," - ",dict_liste[i])
    input("For å gå tilbake til hovedmenyen, trykk ENTER")
    hovedmeny(1)
    
def ny_avtale():
    bekreftet = "" 
    while bekreftet != "Ja":
            tittel = input("Rediger avtale\nOppgi tittel:")
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
                
    input("For å gå tilbake til hovedmenyen, trykk ENTER")
    hovedmeny(1)
    
def ny_avtale_til_meny():
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
                
        input("For å gå tilbake til hovedmenyen, trykk ENTER")#han som har lagd den my flytte denne på riktig plass, finner ikke ut av det
    
    
    
    
    
    
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
        input("For å gå tilbake til hovedmenyen, trykk ENTER")
        hovedmeny(1)   
    
    
    
    
    
    
    
def slette_avtale():
    print("Du har valgt: 5: Slette en avtale")
    fortsette_tilbake = input("For å fortsette, trykk ENTER, hvis du ønsker å gå tilbake til hovedmenyen, tast 0 :")
    if fortsette_tilbake == 1:
        hovedmeny(1)
    else:
        pass
    global liste
    for i in range(len(liste)):
        print(i,liste[i].tittel," - ",liste[i].__str__())
    indeks = int(input("Hvilken avtale vil du slette: "))
    del liste[indeks]
    input("Avtale slettet, trykk ENTER for å gå tilbake til hovedmenyen")

    hovedmeny(1)
    
    
def redigere_avtale():
    print("Du har valgt: 6: Redigere en avtale")
    fortsette_tilbake = input("For å fortsette, trykk ENTER, hvis du ønsker å gå tilbake til hovedmenyen, tast 0 :")
    if fortsette_tilbake == "0":
        hovedmeny(1)
    else:
        pass
    global liste
    for i in range(len(liste)):
        print(i,liste[i].tittel," - ",liste[i].__str__())
    indeks = int(input("Hvilken avtale vil du redigere?"))
    ny = ny_avtale()
    #if hva == 1:
        #ny = input("Hva vil du redigere til: ")
        #liste[int(indeks)].tittel
    liste = liste[:indeks]+[ny]
    input("Avtale redigert, trykk ENTER for å gå tilbake til hovedmenyen")
    hovedmeny(1)

def hovedmeny(start):
    os.system('cls')                 
    while start == 1:
        print("1: Les inn avtaler fra fil")
        print("2: Skriv avtalene til fil")
        print("3: Skriv inn en ny avtale")
        print("4: Skriv ut alle avtalene")
        print("5: Slette en avtale")
        print("6: Redigere en avtale")
        print("7: Søke i avtaler")
        print("0: Jeg vil avslutte")
        valg=int(input("Velg et alternativ: "))
        if valg==1:
            avtaler_fra_fil()
        elif valg==2:
            avtaler_til_fil()
        elif valg ==3:
            ny_avtale_til_meny()
        elif valg==4:
            skriv_ut_alle_avtaler()
        elif valg==5:
            slette_avtale()
        elif valg==6:
            redigere_avtale()
        elif valg==7:
            liste_filter(liste)
        else:
            print("Ugyldig svar, vennligst bruk 1-6")
hovedmeny(1)
