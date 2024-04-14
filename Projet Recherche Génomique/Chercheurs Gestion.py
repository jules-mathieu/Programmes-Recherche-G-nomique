# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:39:47 2024

@author: Jules
"""
##L'obectif est de recenser les chercheurs d'une équipe de recherche en génomique. 
##Sont recensés leur nom, prénom, et sur quels projets ils travaillent   


##Fonctions
class Chercheur(object):
    def __init__(self, nom, prenom, projet):
        self.nom=nom
        self.prenom=prenom
        self.projet=projet
        
    def setProjet(self, unage):
        self.projet=unage
        
    def setName(self, nom):
        self.nom = nom
    
    def toString(self):
        str2 = f"Nom du Chercheur : {self.nom}, prenom: {self.prenom}, projet: {self.projet}, "
        return(str2)
    
    
class Service(object):
    
    def __init__(self):
        self.liste = []
       
    def toString(self):
        chaine = ""
        for elem in self.liste:
            chaine += elem.toString()
        return(chaine)
    
    def add(self, Chercheur):
        self.liste.append(Chercheur)
        

##Programme principal
ch1 = Chercheur("Marc", "Jean", "Analyse de données genomiques")
ch2 = Chercheur("Martin", "Pierre", " Fonction des génomes microbiens")
ch3 = Chercheur("Tom", "Norroy", "Génomique évolutive et adaptation")
service = Service()

ch1.setProjet("Génomique évolutive et adaptation")
ch2.setName("Jacques")
service.add(ch1)
service.add(ch2)
service.add(ch3)

print(service.toString())

