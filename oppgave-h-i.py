#h) Lag en funksjon som lagrer ei liste med avtaler til ei tekstfil. Tenk over hva som vil være et
#fornuftig format for ei slik tekstfil.
import csv
import numpy

#eksempel??
avtaleheader = ['tittel','sted','starttidpunk','varighet']
avtale1 = ['Forelesning','UIS','2022-09-16 13:15:00','45minutter']
with open('avtaleliste.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(avtaleheader)
    writer.writerow(avtale1)

