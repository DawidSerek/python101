#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/05_oceny_02.py

"""
	ZADANIE
    Napisz program, który umożliwia wprowadzanie nazw przedmiotów oraz ocen
    z wybranego przedmiotu.
"""

# importujemy funkcje z modułu ocenyfun zapisanego w pliku ocenyfun.py
def drukuj(co,kom="Sekwencja zawiera: "):
    print kom
    for i in co:
        print i,

przedmioty = set(['polski','angielski']) #definicja zbioru
drukuj(przedmioty, "Lista przedmiotów zawiera: ")

print "\nAby przerwać wprowadzanie przedmiotów, naciśnij Enter."
while True:
    przedmiot = raw_input("Podaj nazwę przedmiotu: ")
    if len(przedmiot):
        if przedmiot in przedmioty: #czy przedmiot jest w zbiorze?
            print "Ten przedmiot już mamy :-)"
        przedmioty.add(przedmiot) #dodaj przedmiot do zbioru
    else:
        drukuj(przedmioty,"\nTwoje przedmioty: ")
        przedmiot = raw_input("\nZ którego przedmiotu wprowadzisz oceny? ")
        if przedmiot not in przedmioty: #jeżeli przedmiotu nie ma w zbiorze
            print "Brak takiego przedmiotu, możesz go dodać."
        else:
            break # wyjście z pętli

oceny = [] # pusta lista ocen
ocena = None # zmienna sterująca pętlą i do pobierania ocen
print "\nAby przerwać wprowadzanie ocen, podaj 0 (zero)."

while not ocena:
	try:
		ocena = int(raw_input("Podaj ocenę (1-6): "))
		if (ocena > 0 and ocena < 7):
			oceny.append(float(ocena))
		elif ocena == 0:
			break
		else:
			print "Błędna ocena."
		ocena = None
	except ValueError:
		print "Błędne dane!"

drukuj(oceny,przedmiot.capitalize()+" - wprowadzone oceny: ")
