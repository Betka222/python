import random
from math import floor

def bubble(pole):
    delka=len(pole)-1        #délka pole (-1 proto, že indexy zaèínají od 0 a ne od 1) 
    srovnano = False         #pole není srovnáno, dokud si to neovìøíme
    while not srovnano:      #dokud nebude srovnáno, budeme ho projíždìt timhle cyklem 
        srovnano = True      #když se nic nestane, znamená to, že je srovnáno a cyklus se nebude opakovat
        for i in range (0,delka):  #pracujeme s celým øetìzcem, tedy s indexy od 0 do délky pole
            if  pole[i]>pole[i+1]: #pokud je èíslo vìtší než následující, tak je prohodíme
                a=pole.pop(i+1)    #menší èíslo se odebere z øetìzce a uloží pod promìnou a 
                pole.insert(i,a)   #èíslo uložené pod promìnou a vložíme na místo vìtšího èísla
                srovnano=False     #nìco jsme prohodili, znamená to tedy, že si nemùžeme být jistí zda je øetìzec srovnaný

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
