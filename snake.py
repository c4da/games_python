# -*- coding: utf-8 -*-
"""
Created on Tue May 2 22:46:07 2016

@author: MCA

Python 3.6

Simple snake game.
"""
import pygame, sys, time, random
from pygame.locals import *

pygame.init() #inicializace knihovny pygame
taktovaciFrekvence = pygame.time.Clock() #nastaveni rychlosti hry
#nastaveni zobrazovaci plochy hry

herniPlocha = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Had s malinou') #popis okna

#definovani barev
cervenaBarva = pygame.Color(255, 0, 0)
cernaBarva = pygame.Color(0, 0, 0)
bilaBarva = pygame.Color(255, 255, 255)
sedaBarva = pygame.Color(150, 150, 150)

#pomocne promenne - list
polohaHada = [100, 100]
castiHada = [[100, 100], [80, 100], [60, 100]]
polohaMaliny = [300, 300]
malinaVyrostla = 1

smer = 'doprava' #urcuje smer hada po zapnuti - dokud hrac nestiskne klavesu ktera by prepsala hodnotu zmeny smeru
zmenaSmeru = smer

#definovani funkce konec hry

def konecHry():
	konecHryPismo = pygame.font.Font('freesansbold.ttf', 72)
	konecHryPlocha = konecHryPismo.render('Konec hry', True, sedaBarva)
	konecHryObd = konecHryPlocha.get_rect()
	konecHryObd.midtop = (320, 10)
	herniPlocha.blit(konecHryPlocha, konecHryObd)
	pygame.display.flip()
	time.sleep(5)
	pygame.quit() #ukonceni knihovny pygame
	sys.exit() #ukonceni prostredi python
	
#fce vypise na obrazovku text konec hry - velkymi  pismeny
#pozastavi cinnost programu na 5s
#pote ukonci knihovnu pygame i samotne prostredi python

#hlavni cast programu - pod cyklem while - dokud had nezemre
while True:
     #rychlost hry
 taktovaciFrekvence.tick(50)
    #predepsan nekonecny cyklus, ktery lze ukoncit pouze fci konecHry
    #hodnota true je vzdy pravdiva - program nic nevyhodnocuje
    #smycka kontroluje udalosti pygame, jako stisknuti klaves

 for event in pygame.event.get():
     #smycka overuje zda uziv stiskl klavesu
     if event.type == QUIT:
           pygame.quit()
           sys.exit()
     elif event.type == KEYDOWN: 

         if event.key == K_RIGHT or event.key == ord('d'):
              zmenaSmeru = 'doprava'
         if event.key == K_LEFT or event.key == ord('a'):
              zmenaSmeru = 'doleva'
         if event.key == K_UP or event.key == ord('w'):
              zmenaSmeru = 'nahoru'
         if event.key == K_DOWN or event.key == ord('s'):
              zmenaSmeru = 'dolu' 
         if event.key == K_ESCAPE:
              pygame.event.post(pygame.event.Event(QUIT))
     #podminka dodrzeni spravne zmeny smeru - had se nesmi kousnout
         if zmenaSmeru == 'doprava' and not smer == 'doleva':
            smer = zmenaSmeru
         if zmenaSmeru == 'doleva' and not smer == 'doprava':
            smer = zmenaSmeru
         if zmenaSmeru == 'nahoru' and not smer == 'dolu':
              smer = zmenaSmeru
         if zmenaSmeru == 'dolu' and not smer == 'nahoru':
            smer = zmenaSmeru
         #jeden segment nebo blok meri 20 px (ctverec)
         if smer == 'doprava':
            polohaHada[0] += 20
            castiHada.insert(0, list(polohaHada))
         if smer == 'doleva':
            polohaHada[0] -= 20
            castiHada.insert(0, list(polohaHada))
         if smer == 'nahoru':
            polohaHada[1] -= 20
            castiHada.insert(0, list(polohaHada))
         if smer == 'dolu':
            polohaHada[1] += 20
            castiHada.insert(0, list(polohaHada))
 #cislo v [] je poloha v listu
 #[0] osa X, [1] osa Y
 #zajisteni rustu tela hada
          
 #instrukce insert vlozi do seznamu castiHada novou hodnotu:aktualni pozici hada
 #pokud interpret pythonu dosahne tohoto radku zvysi pokazde delku hadova tela o jeden segment
 #a umisti jej na aktualni polohu hlavy
 #rust hada by se vsak mel dit pouze po snezeni maliny, jinak by had rostl neustale
         if polohaHada[0] == polohaMaliny [0] and polohaHada[1] == polohaMaliny[1]:
             malinaVyrostla = 0 #vygeneruje malinu, resp nevygeneruje
         else:
        #     pass
             castiHada.pop()
 #telo hada neustale roste, ale pokud had nenarazi na malinu je hodnota seznamu prikazem pop smazana
 #pop vrati ze seznamu nejstarsi hodnotu a zaroven ji odebere takze se seznam o jednu polozku zkrati
 #pop uzira ocas a vytvari iluzi pohybu hada
 #diky prikazu else se pop provede pouze pokud zustane malina nesnedena
 #pokud se podminka polohy hlavy hada = poloze maliny prikaz pop se neprovede
 
 #generovani maliny v pripade, ze byla puvodni malina snedena
         if malinaVyrostla == 0:
             x = random.randrange(1, 32)
             y = random.randrange(1, 24)
             polohaMaliny = [int(x*20), int(y*20)]
             malinaVyrostla = 1
 #malina snedena = malinaVyrostla = 0, podminka if kontroluje zda byla malina snedena
 #modul random byl importovan na zacatku programu
 
 #kod uvedeny vyse se oznacuje jako respawning (generovani)
 
         herniPlocha.fill(cernaBarva)
         for poloha in castiHada:
           pygame.draw.rect(herniPlocha, bilaBarva, Rect(poloha[0], poloha[1], 20, 20)) #vykresleni tela hada bilou barvou
           pygame.draw.rect(herniPlocha,cervenaBarva, Rect(polohaMaliny[0], polohaMaliny[1], 20, 20)) #vykresleni maliny
           pygame.display.flip() #bez teto instrukce nebude pro hrace nic viditelne, prikaz aktualizuje obrazovku
         
         #pravidla hry
         if polohaHada[0] > 600:
         	konecHry()
         if polohaHada[1] > 400:
         	konecHry()
         #konec hry v pripade narazu do okraje hraci plochy
         
         for teloHada in castiHada[1:]:
          if polohaHada[0] == teloHada[0] and polohaHada[1] == teloHada[1]:
           konecHry()
 #for prochazi vsechny polohy casti hada od druhe polozky seznamu az po jeho konec
 #pritom je porovnava s akt polohou hlavy
 #je nutne porovnavat az od druhe polozky protoze prvni polozka je vzdy poloha hlavy
 #pri porovnavani polohy od prvni polozky by tak hra skoncila okamzite
 

 	
 	
 	