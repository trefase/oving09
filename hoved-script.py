


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
 





#funksjon ny avtale - avtalen havner i liste og dictionary som objekt
def ny_avtale():
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



   
#Valg av funksjoner som skriver ut liste med avtale, dataframe er mest oversiktlig
#Funksjon som skriver dictionary til csv fil 
def avtaler_til_fil():
    with open('avtaler.csv', 'a',newline='') as csv_file:  # appender csv filen, endre til w hvis den skal overskrives
        writer = csv.writer(csv_file,delimiter =";")
        for key, value in dict_liste.items():
            writer.writerow([key,value])
#Funksjon som leser csv fil til dictionary  
def avtaler_fra_fil():
    #global dict_liste 
    #dict_liste.clear() # slett den eksisterende listen
    with open('avtaler.csv', 'r') as csv_file:
        reader = csv.reader(csv_file,delimiter=';')
        dict_liste = dict(reader)
         

#Skriver ut liste - indeks og avtalestreng 
def skriv_ut_liste(liste):
    print("Utskrift liste")
    for i in range(len(liste)):
        print(i,liste[i].tittel," - ",liste[i].__str__())

#Skriver ut dictionary - indeks og avtalestreng 
def skriv_ut_dict(dict_):
    print("Utskrift liste")
    for i in (dict_):
        print(i," - ",dict_[i])

#Generere dataframe fra liste og skriver denne ut 
def skriv_ut_alle_avtaler():
    df_liste = pd.DataFrame(columns = ['tittel','sted','starttidspunkt','varighet','kategori'])
    for i in liste:
        df = pd.DataFrame([[i.tittel,i.sted,str(i.starttidspunkt),i.varighet,i.kategori]], columns=('tittel','sted','starttidspunkt','varighet','kategori'))
        df_liste = df_liste.append([df], ignore_index=True)
       
    print("Utskrift liste")
    print(df_liste)


            
            
            

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