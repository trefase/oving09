"""
Christoffer 24.10.22

"""

import pandas as pd


datafil = pd.read_csv('datafil.csv', sep=';', usecols=['tittel','sted','tidspunkt','varighet'])

def dato_filter(avtale_liste, dato):
   #return print(avtaleListe[avtaleListe['tidspunkt'] == dato])
   return print(avtale_liste[avtale_liste['tidspunkt'].str.contains(dato)])
 
dato_filter(avtale_liste=datafil,dato='2023')

