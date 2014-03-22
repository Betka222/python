import random
from math import floor
  
def quick(pole):
        if ( len(pole)==0 or len(pole)==1 ):    # pokud je pole pr�zdn� nebo se skl�d� jen z jednoho �lenu, nem� cenu ho �adit
            return pole
       
        delka = len(pole)-1   #d�lka pole (-1 proto, �e indexy za��naj� od 0 a ne od 1)
        piv = delka;          #v�choz� hodnota pivota, kde se nach�z� pivot na za��tku p�ed porovn�v�n�m
        pivot = pole[delka]   #pivot nebude n�hodn� ��slo ale v�dy posledn� v poli
        p=0                   #prom�nn� p bude pozd�ji ur�ovat index
        h=0                   #prom�nn� h funguje jako po��tadlo - zat�m jsme nic nepo��tali, proto nastaven� na nule
       
        while h<delka:  # pokud jsme je�t� nesrovnali k pivotovi tolik ��sel, kolik jich v poli je, srovn�vejme d�l
           if pole[p]<=pivot: # pokud je ��slo na indexu p (za��n�me s 0- tedy na za��tku pole) men�� nebo rovn� pivotovi...
              a=pole.pop(p)   #...tak si ho uloz do prom�nn� a, z�rove� ho odeber....
              pole.insert(0,a)#...a prdni ho na za��tek pole 
              p+=1 #mus� nav��it p o jedna, aby si p��t� znova neporovn�val ��slo co si hodil na za��tek pole minul�m krokem v jednom z minul�ch kolech
              h+=1 #porovnali jsme dal�� ��slo, p�ipo�teme si to tedy na na�em po��tadle
               
           if pole[p]>pivot: # pokud je ale ��slo v�t�� ne� pivot...
              b=pole.pop(p)  #...popniho ven...
              pole.insert(delka,b) #...a hod na konec seznamu
              h+=1   #srovnali jsme dal�� ��slo, tak abychom nezapomn�li, hned to p�ipo�tem na na�em po��tadle
              piv-=1 #pivot n�m t�m p�dem ale utek ze sv� v�choz� pozice o jedno do leva tedy do m�nusov� oblasti, kdy� v�ch�z�me z 0
             
        pole[piv+1:] = quick(pole[piv+1:]) #pole si rozd�l�me na ��st od pivota do konce...
        pole[0:piv] = quick(pole[0:piv])   #...a na ��st od 0 do pivota...
                                           #a ob� pole znovu projedeme funkc� quick :)
        return pole
 
pole = [42, 42, 15, 1, 58, 17, 36, 85, 5, 1, 7, 3]
 
 
print("Pole obsahovalo: \n")    
print(pole)
print("Ted obsahuje: \n")
print(quick(pole))