import random
from math import floor
  
def quick(pole):
        if ( len(pole)==0 or len(pole)==1 ):    # pokud je pole prázdné nebo se skládá jen z jednoho èlenu, nemá cenu ho øadit
            return pole
       
        delka = len(pole)-1   #délka pole (-1 proto, že indexy zaèínají od 0 a ne od 1)
        piv = delka;          #výchozí hodnota pivota, kde se nachází pivot na zaèátku pøed porovnáváním
        pivot = pole[delka]   #pivot nebude náhodné èíslo ale vždy poslední v poli
        p=0                   #promìnná p bude pozdìji urèovat index
        h=0                   #promìnná h funguje jako poèítadlo - zatím jsme nic nepoèítali, proto nastavené na nule
       
        while h<delka:  # pokud jsme ještì nesrovnali k pivotovi tolik èísel, kolik jich v poli je, srovnávejme dál
           if pole[p]<=pivot: # pokud je èíslo na indexu p (zaèínáme s 0- tedy na zaèátku pole) menší nebo rovný pivotovi...
              a=pole.pop(p)   #...tak si ho uloz do promìnné a, zároveò ho odeber....
              pole.insert(0,a)#...a prdni ho na zaèátek pole 
              p+=1 #musíš navýšit p o jedna, aby si pøíštì znova neporovnával èíslo co si hodil na zaèátek pole minulým krokem v jednom z minulých kolech
              h+=1 #porovnali jsme další èíslo, pøipoèteme si to tedy na našem poèítadle
               
           if pole[p]>pivot: # pokud je ale èíslo vìtší než pivot...
              b=pole.pop(p)  #...popniho ven...
              pole.insert(delka,b) #...a hod na konec seznamu
              h+=1   #srovnali jsme další èíslo, tak abychom nezapomnìli, hned to pøipoètem na našem poèítadle
              piv-=1 #pivot nám tím pádem ale utek ze své výchozí pozice o jedno do leva tedy do mínusové oblasti, když výcházíme z 0
             
        pole[piv+1:] = quick(pole[piv+1:]) #pole si rozdìlíme na èást od pivota do konce...
        pole[0:piv] = quick(pole[0:piv])   #...a na èást od 0 do pivota...
                                           #a obì pole znovu projedeme funkcí quick :)
        return pole
 
pole = [42, 42, 15, 1, 58, 17, 36, 85, 5, 1, 7, 3]
 
 
print("Pole obsahovalo: \n")    
print(pole)
print("Ted obsahuje: \n")
print(quick(pole))