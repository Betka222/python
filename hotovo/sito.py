def hledani(mez):                #mez ur�uje konec mno�iny ve kter� prvo��sla hled�me
    prvocisla = []               #pr�zdn� pole, ��dn� prvo��sla jsme je�t� neobjevili
    for novy in range(2, mez):   #pro v�echna ��sla od 2 do meze (0 a 1 nejsou prvo��sla, to v� p�ece ka�dej :P)...
        je=True                  #...budeme p�edpokl�dat, �e jsou prvo��sla...
        for delitel in prvocisla: #...pokud se neuk�e...
              if novy % delitel == 0: #...�e jsou d�liteln� bezezbytku n�jak�m z prvo��sel
                 je=False             #pokud jsou, znamen� to �e se nejedn� o prvo��slo...
                 break                #...a my mu�eme proces ukon�it
        if je:                        #pokud ��slo ale pro�lo na�� d�l�c� zkou�kou...
           prvocisla.append(novy)     #p�id�me ho na �estn� vyslou�en� m�sto v seznamu prvo��sel
    return prvocisla

print(hledani(1000))                
       
      
       
def vyhazovani(strop):                      #zkusime opacnou cestu, m�sto n�boru do pr�zdn�ho seznamu...
    adepti = [i for i in range(2,strop+1)]  #budeme vyhazovat z v�choz�ho seznamu, kter� m� v�echna ��sla od 2 do stropu (1,0 nejsou prvo��sla, jak u� v�me z minula)
    for i in adepti:                        #ka�d� ��slo v adeptcech se stane deliteme 
        for j in adepti[adepti.index(i)+1:]: #a ��slo vedle nich v seznamu se stane d�lencem
            if j%i==0:                       #pokud delence vyd�l�me bezezbytku, bohu�el zkou�kou nepro�el...
                adepti.remove(j)             # ...a my ho mus�me krut� vyhodit a na pozici d�lence se dost�v� dal�� p�n na holen� �ekaj�c� v �ad�
           
    return adepti
print (vyhazovani(1000))
