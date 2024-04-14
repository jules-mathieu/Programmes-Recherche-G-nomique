# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 23:24:51 2024

@author: Jules
"""
###Ici nous cherchons à déterminer le brin inverse d'une séquence de nucléotide


##Proramme principal
deb = 0
fin = 0
ch = "atcgatgtctatgacgtatgctagctatggctagt"
res = ""
i=0

while i < len(ch):
    
    if ch[i] == "":
        fin = i
        str1 = ch[deb:fin]
        for j in range(len(str1)-1, -1, -1):
            res = res + str1[j]
        res += ""
        deb = len(res)
        
    if i == len(ch) - 1:
        fin = i+1
        str1 = ch[deb:fin]
        for j in range(len(str1)-1, -1, -1):
            res = res + str1[j]
    
    i=i+1
    
print(res)

    
        
    
            
        