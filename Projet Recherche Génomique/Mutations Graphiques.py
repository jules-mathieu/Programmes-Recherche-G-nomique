# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:36:09 2024

@author: Jules
"""
##On cherche ici à afficher des graphiques d'analyse du nombre mutations en cours du temps

##Importations
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


##Fonctions
class Générateur(object):
    def __init__(self, nb):
        self.nb = nb
        self.X = np.empty(self.nb)
        self.Y = np.empty(self.nb)
        
    def générer(self):
        self.X = np.linspace(0,2,self.nb)
        self.Y = 2*self.X + 0.5*(1-2*np.random.rand(self.nb)) - 1.0
        
    def afficher(self):
        print(self.X)
        print(self.Y)
        
    def afficherGraphiquePoints(self):
         plt.plot(self.X, self.Y, '+')
         plt.title("Mutations cumulées en fonction du temps - Courbe")
         plt.xlabel("Temps")
         plt.ylabel("Valeur")
         plt.show()
         
    def afficherGraphiqueLignes(self):
        plt.plot(self.X, self.Y,)
        plt.title("Position en fonction du temps")
        plt.xlabel("Temps")
        plt.ylabel("Nombre de mutations")
        plt.show()
        
    def enregistrerCSV(self, file):
        np.savetxt(file, np.array([self.X,self.Y]).transpose())
    

class Analyseur(object):
    def __init__(self, file):
        self.X, self.Y = np.loadtxt(file, unpack = True)
        self.min =0 
        self.max = 0
        self.mean = 0
        
    def afficherSynthese(self):
        self.mean = np.mean(self.Y)
        self.min = np.min(self.Y)
        self.max = np.max(self.Y)
        print((f'min: {self.min}, max: {self.max}, moy: {self.mean}'))
        
    def afficherRegression(self):
        self.X = (np.array(self.X)).reshape(-1, 1)
        myreg = LinearRegression()
        myreg = myreg.fit(self.X, self.Y)
        plt.plot(self.X, self.Y, '+')
        plt.plot(self.X,myreg.predict(self.X),"-r")
        plt.title("Mutations cumulées en fonction du temps - Regression")
        plt.xlabel("Temps")
        plt.ylabel("Nombre de mutations")
        plt.show()
    
        
##Programme principal        
nuage1 = Générateur(50)
nuage1.générer()
nuage1.afficherGraphiqueLignes()
nuage1.enregistrerCSV('C:/Users/Jules/Desktop/M1/Programmation/mutations.txt')

analyse = Analyseur('C:/Users/Jules/Desktop/M1/Programmation/mutations.txt')
analyse.afficherSynthese()
analyse.afficherRegression()


       
    
        
    

         
    
