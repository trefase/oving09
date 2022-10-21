# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:36:24 2022

@author: Henry
"""


from datetime import datetime

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
        return f"Avtale: ({self.tittel}, {self.sted}, {self.starttidspunkt}, {self.varighet} min, {self.kategori})"
 



#for å teste   
bmw=Avtale("test","norge",datetime.now(),60, "bil")
print(Avtale.__str__(bmw))
     
