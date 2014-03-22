import random
from math import floor

def bubble(pole):
    delka=len(pole)-1        #d�lka pole (-1 proto, �e indexy za��naj� od 0 a ne od 1) 
    srovnano = False         #pole nen� srovn�no, dokud si to neov���me
    while not srovnano:      #dokud nebude srovn�no, budeme ho proj�d�t timhle cyklem 
        srovnano = True      #kdy� se nic nestane, znamen� to, �e je srovn�no a cyklus se nebude opakovat
        for i in range (0,delka):  #pracujeme s cel�m �et�zcem, tedy s indexy od 0 do d�lky pole
            if  pole[i]>pole[i+1]: #pokud je ��slo v�t�� ne� n�sleduj�c�, tak je prohod�me
                a=pole.pop(i+1)    #men�� ��slo se odebere z �et�zce a ulo�� pod prom�nou a 
                pole.insert(i,a)   #��slo ulo�en� pod prom�nou a vlo��me na m�sto v�t��ho ��sla
                srovnano=False     #n�co jsme prohodili, znamen� to tedy, �e si nem��eme b�t jist� zda je �et�zec srovnan�

    return pole

pole = [42, 42, 15, 1, 58, 17, 36, 85, 5, 1, 7, 3]
nahodny_pole = [int(floor(100*random.random())) for _ in xrange(300)]   

print("Pole obsahovalo: \n")    
print(pole)
print("Ted obsahuje: \n")
print(bubble(pole))

print("Nahodny pole obsahovalo: \n")    
print(nahodny_pole)
print("Ted obsahuje: \n")
print(bubble(nahodny_pole))
