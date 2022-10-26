# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 18:49:19 2022

@author: Henry
"""

from datetime import datetime
import numpy as np
import pandas as pd



#oppgave d)
#klasse for avtale 

class Avtale():
    def __init__(self, init_tittel = "", init_sted = "", init_starttidspunkt = datetime.now(), init_varighet = 0, init_kategori ="" ):
        self.tittel = init_tittel
        self.sted = init_sted
        self.starttidspunkt = init_starttidspunkt
        self.varighet = init_varighet
        self.kategori = init_kategori
        

#oppgave e)
#__str__

    def __str__(self):
        return f"{self.tittel}, {self.sted}, {self.starttidspunkt}, {self.varighet} min, {self.kategori}"
 

#oppgave f)
#funksjon ny avtale

liste=[]
dict_liste = dict()  

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
        bekreftet = input("Ja/Nei:")        
        if bekreftet == "Ja" or bekreftet =="ja":
           
            dict_liste[tittel]=Avtale(tittel,sted, starttidspunkt, varighet, kategori)
            liste.append(Avtale(tittel,sted, starttidspunkt, varighet, kategori))
            
            return(Avtale(tittel,sted, starttidspunkt, varighet, kategori))
            break
        else:
            print("Skriv avtalen på nytt.")
            continue
    
   
#test=ny_avtale()     
   
  
#oppgave g)
#funksjon skriver ut liste med avtale


#liste
def skriv_ut(x):
    print("Utskrift liste")
    for i in range(len(x)):
        print(i,x[i].tittel," - ",x[i])
        #print(i,x[i].tittel,x[i].kategori)

#skriv_ut(liste)


#dict
def skriv_ut_d(x):
    print("Utskrift liste")
    for i in (x):
        print(i,x[i])
        #print(i,x[i].varighet)
        
#skriv_ut_d(dict_liste)
