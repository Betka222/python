def hledani(mez):                #mez urèuje konec množiny ve které prvoèísla hledáme
    prvocisla = []               #prázdné pole, žádná prvoèísla jsme ještì neobjevili
    for novy in range(2, mez):   #pro všechna èísla od 2 do meze (0 a 1 nejsou prvoèísla, to ví pøece každej :P)...
        je=True                  #...budeme pøedpokládat, že jsou prvoèísla...
        for delitel in prvocisla: #...pokud se neukáže...
              if novy % delitel == 0: #...že jsou dìlitelný bezezbytku nìjakým z prvoèísel
                 je=False             #pokud jsou, znamená to že se nejedná o prvoèíslo...
                 break                #...a my mužeme proces ukonèit
        if je:                        #pokud èíslo ale prošlo naší dìlící zkouškou...
           prvocisla.append(novy)     #pøidáme ho na èestnì vysloužené místo v seznamu prvoèísel
    return prvocisla

print(hledani(1000))                
       
      
       
def vyhazovani(strop):                      #zkusime opacnou cestu, místo náboru do prázdného seznamu...
    adepti = [i for i in range(2,strop+1)]  #budeme vyhazovat z výchozího seznamu, který má všechna èísla od 2 do stropu (1,0 nejsou prvoèísla, jak už víme z minula)
    for i in adepti:                        #každý èíslo v adeptcech se stane deliteme 
        for j in adepti[adepti.index(i)+1:]: #a èíslo vedle nich v seznamu se stane dìlencem
            if j%i==0:                       #pokud delence vydìlíme bezezbytku, bohužel zkouškou neprošel...
                adepti.remove(j)             # ...a my ho musíme krutì vyhodit a na pozici dìlence se dostává další pán na holení èekající v øadì
           
    return adepti
print (vyhazovani(1000))
