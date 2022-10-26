"""
Christoffer 24.10.22

"""

import pandas as pd


datafil = pd.read_csv('ressursfiler\datafil.csv', sep=';', usecols=['tittel','sted','tidspunkt','varighet'])

def dato_filter(avtale_liste, dato):
   #return print(avtaleListe[avtaleListe['tidspunkt'] == dato])
   return print(avtale_liste[avtale_liste['tidspunkt'].str.contains(dato)])
 
dato_filter(avtale_liste=datafil,dato='2023')

#Funksjon som leter etter en gitt streng (lete_streng) i en dataframe (avtale_liste). Søkefunksjonen er case-insensitive (str.casefold)
def tittel_filter(avtale_liste, lete_streng):
   avtale_liste['tittel'] = avtale_liste['tittel'].str.casefold()
   return print(avtale_liste[avtale_liste['tittel'].str.contains(lete_streng.casefold())])


tittel_filter(datafil,input('Hva leter du etter?: '))