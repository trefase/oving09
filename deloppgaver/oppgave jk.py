"""
Christoffer 24.10.22

"""

import pandas as pd


df = pd.read_csv('datafil.csv', sep=';', usecols=['tittel','sted','tidspunkt','varighet'])

def datoFilter(avtaleListe, dato):
   #return print(avtaleListe[avtaleListe['tidspunkt'] == dato])
   return print(avtaleListe[avtaleListe['tidspunkt'].str.contains(dato)])
 
datoFilter(avtaleListe=df,dato='2023')

