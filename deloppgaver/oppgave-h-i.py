import csv

#dict for avtaler
avtaler = {}





#testavtale
test1 = Avtale('forelesning', 'norge', '2023-01-01', 45, 'diverse')
test2 = Avtale('asd', 'norge', '2023-01-01', 45, 'diverse')


avtaler[test1.__dict__.get('tittel')] = test1.__dict__.get('sted'),test1.__dict__.get('varighet')
avtaler[test2.__dict__.get('tittel')] = test2.__dict__.get('sted'),test2.__dict__.get('varighet')

#print (test123.__dict__.values())
print (avtaler)

#funksjon som skriver avtaler til fil
def skrivavtale():
    with open("myfile", 'w') as f: 
        w = csv.writer(f)
        for row in avtaler.items():
            w.writerow(row)

