# Ich bin ein Kommentar
# Merhzeilige Kommentare exisitieren nicht, also muss vor jeder Zeile das # Zeichen gesetzt werden

# Wie werden Variablen definiert?
# identifier = value

# Alle Variablen sind dynamisch, das heißt ihre Datentypen können sich ändern
# In Python gibt es keine Konstanten, d.h. jede Variable kann verändert werden

# Datentypen in Python

# Primitive

# Integer
# Ganzzahlen, egal ob positiv oder negativ
# Es gibt an sich keinen Integeroverflow, d.h. die Integer können unbegrenzt groß sein

myInteger = 5

# Float
# Gleitkommazahlen, immer mit . und nicht mit ,

myFloat = 25.75

# String
# Textfolge, wird mit "" oder mit '' definiert

myString = "Max Mustermann"

# Methoden des Strings
# Methoden sind Funktionen, die zu einem Objekt gehören

# string.count("Ausdruck")
# Gibt einen Integer zurück, der sagt wie oft der Ausdruck im String vorkommt
# Ist case-sensitive

myString.count("n")

## Exkurs: print("")
# Print gint in seine Parameter in der Konsole aus

print(myString.count("m"))
# Strg + Shift + F10 führt die gerade geöffnete Python Datei aus

# string.lower()
# Gibt einen neuen String zurück, der komplett kleingeschrieben ist
print(myString.lower())
print(myString)  # Ist trotzdem groß geschrieben, da der bestehende String nicht verändert wird
myLowerString = myString.lower()
print(myLowerString)

# Man kann Methoden auch hintereinanderreihen, wenn es sich weiterhin um den selben Datentypen handelt

print(myString.lower().count("m"))  # Funktioniert, da lower einen String zurückgibt und count eine String-Methode ist
# print(myString.count("n").lower()) Geht nicht, da count einen int zurückgibt und lower() eine String-Methode ist

# string.upper()
# Gibt einen neuen String zurück der komplett aus Großbuchstaben bestehet

print(myString.upper())

# myString.isupper()/islower()
# Gibt einen Boolean zurück, der aussagt ob der String groß oder klein ist

print(myString.isupper())
print(myString.islower())

# Geben beide False zurück, da der ganze String geprüft wird
# Wir können über den Index einzelene Zeichen im String ansprechen
# Der Index beginnt bei 0 und Endet bei der Länge des Strings - 1
# Benutzung Identifier[Index]

print(myString[0])  # Gibt den ersten Buchstaben zurück
# Gibt auch einen String zurück
print(myString[0].isupper())

# Exkurs: len(Variable)
# Gibt die Länge der Variable an
# Funktioniert nur bei Variablen mit Index

print(myString[len(myString) - 1])  # Ruft den letzten Buchstaben auf, da len die Länge des Strings zurückgibt
print(myString[len(myString) - 1].islower())

print(myString[-1])  # Gibt auch den letzten Buchstaben des Strings zurück
# Mit - fangen wir von hinten an zu zählen

# string.isalpha()
# Prüft ob ein String nur aus Buchstaben besteht und gibt dementsprechend True oder False zurück

print(myString.isalpha())  # False, da ein Leerzeichen enthalten ist

# string.isnumeric()
# Prüft ob der String nur aus Zahlen besteht und gibt dementsprechend True oder False zurück

print(myString.isnumeric())  # False, da der String nicht nur aus Zahlen besteht

# string.isalnum()
# Prüft ob der String nur aus Zahlen und Buchstaben besteht

print(myString.isalnum())  # False, da ein Leerzeichen dabei ist

# Booleans
# Datentyp, der entweder True oder False sein kann
# Häufig für Schleifen und ifs benutzt

myBool = True

# complex
# Komplexe Zahlen
# j steht für den imaginären Teil

myComplex = 5 + 12j

# Arithmetische Operatoren in Python
# + Addition
# - Subtraktion
# / Division
# * Multiplikation
# % Modulus
# Division mit Rest
# ** Potenzierung
# // Ganzzahldivision, schneidet die Kommazahlen ab, falls welche im Ergebnis wären

# List
# Kann mehrere Werte in einer Variable speichern
# Verfügt über Index
# Ist veränderbar, d.h. es können neue Elemente hinzugefügt werden oder bestehende entfernt werden
# Duplikate sind erlaubt
# Es können mehrere verschiedene Datentypen enthalten sein

myList = [1, 2, 3, 4, True, "test"]
print(myList)

# Kann auch auf einzelne Werte zugreifen mittels Index

print(myList[4])

# Kann auch von einem Startpunkt bis zu einem bestimmten Endpunkt wiedergeben lassen
print(myList[2:5])
# Beginnt bei Index 2 und endet vor Index 5 => [3, 4, True]

# Von Startpunkt bis zum Ende der Liste/Strings
print(myList[3:])

# Kann auch wieder von hinten zählen lassen
print(myList[-3:-1])

# Empfehlung Datentypen nicht zu mischen

# list(iterierbares Objekt)
myStringList = list(myString)  # Wandelt den String in eine Liste um, jedes Zeichen wird ein Element in der Liste
print(myStringList)
print(myStringList[1])
print(myString[1])

# Methoden der Liste

# list.append()
# Fügt ein oder mehr Elemente an das Ende der Liste an
myList.append("test")
print(myList)
myList.append(myList)  # FÜgt die ganze Liste als ein Element an das Ende der Liste an
print(myList)
print(myList[-1][
          3])  # Bei verschachtelten Listen müssen wir zwei eckige Klammern setzen um einzelne ELmente der inneren Liste anzusprechen
print(myList[-1])

# Können auch Elemente aus der Liste entfernen
# Haben dafür drei Möglichkeiten

# list.pop(Index)
# Entfernt das Element an der Indexposition und gibt es zurück
print(myList.pop(7))
print(myList)

# list.remove(wert)
# Entfernt den angebenen Wert aus der Liste an der ersten gefundenen Position
print(myList.remove("test"))  # Gibt None aus, da es keinen Rückgabewert hat
print(myList)

# list.clear()
# Leert die Liste
# Keine Rückgabe
myList.clear()
print(myList)  # => [], da die Liste jetzt leer ist

# list.extend(Objekt mit index)
# Fügt die einzelnen Elemente des Objekts an die Liste an
myList.extend(myString)  # Fügt jedes Zeichen als einzelnes Item an die Liste an
print(myList)

# list.insert(Index, Wert)
# Fügt den neuen Wert an der gewünschten Position hinzu
myList.insert(2, "test")
print(myList)

# list.count(wert)
# Zählt wie oft der Wert in der Liste vorkommt
print(myList.count("n"))

# list.index(Wert)
# Gibt die Indexpositon des ersten auftretens des Wertes zurück
print(myList.index("M"))
# Man kann auch einen anderen Startpunkt angeben
print(myList.index("M", 1))
print(myList[5])

# list.reverse()
# Dreht die Reihenfolge der Liste um
myList.reverse()
print(myList)

# list.sort()
# Sortiert die Liste standartmäßig Alphanumerisch absteigend
myList.sort()
print(myList)

# Tuple
# Verhalten sich ähnlich wie listen
# Sind nicht veränderbar
# Wir können nicht direkt neue Elemente hinzufügen oder bestehende entfernen
# Duplikate sind erlaubt
# Kann verscheidene Datentypen halten
# Verfügt über Index
# Können auch verschachtelt sein

myTuple = (1, 2, 3, 4, 5, "blabla")
print(myTuple)
print(myTuple[2:4])

# Methoden der Tupel:

# tuple.count(Wert)
# Gibt uns einen Integer zurück, der uns sagt wie oft der gesuchte WErt im Tupel enthalten ist

# tuple.index(Wert)
# Gibt uns den Index des ersten Auftretens des gesuchten Elementes zurück


# Workaround um Werte im Tupel zu verändern
myTuple = list(myTuple)
myTuple[1] = 230
myTuple = tuple(myTuple)

print(myTuple)

# Kombinieren von Tupeln

tupleA = (1, 2)
tupleB = (3, 4)

tupleC = tupleA + tupleB
print(tupleC)

# Unpacking
# Löst iterierbare Objekte in ihre einzelnen Elemente auf und weist sie einer Variable zu
# Es müssen genau so viele Variablen wie Werte in dem iterierbaren Objekt sein
testList = [2, 3, 4, 5, 7, 8, 9]

# (a, b, c, d) = testList Geht nicht, da die Testliste zu lang ist
(a, b, c, d) = tupleC
print(a)
print(d)

a = tupleC[0]
print(a)

# Range
# Nichtveränderbare Sequenz von Integern
# Werden häufig in Listen oder Tupel umgewandelt

# Syntax:
# range(100) Erstellt eine Sequenz bestehend aus 100 Integern
# beginnend bei 0 und endet bei 99
# Endzahl ist nie enthalten
# range(startzahl, endzahl)
# Startzahl ist inkludiert
# range(1, 100) 1 - 99
# range(0, 101, 5) Fängt bei 0 an und zählt in 5er Schritten hoch bis 100
myRange = range(0, 101, 5)
print(myRange)
print(list(myRange))

# Sets
# Können mehrere Werte halten
# Können verscheiden Datentypen halten
# Duplikate sind nicht möglich
# Sets sind ungeordnet, sie verfügen über keinen Index
# Es können neue Werte hinzugefügt werden und bestehende entfernt werden, aber enthaltenne Werte können nicht verändert werden

mySet = {1, 2, 3, 4, 5}
print(mySet)

# Neue Elemente zum Set hinzufügen
# set.add(Element) fügt das Element am Ende des Sets hinzu

mySet.add(6)
print(mySet)

# Bestehende Entfernen
# set.pop()
# Entfernt das erste Element aus dem Set

print(mySet.pop())
print(mySet.pop())

# Nützlich wenn wir eine Liste oder ein Tupel mit DUplikaten in eine Liste/tupel mit einzigartigen Werten umwandeln wollen

testList = [1, 1, 1, 2, 3, 4, 4, 4, 5]
print(testList)
testList = set(testList)
testList = list(testList)
print(testList)

# Dictionaries
# Sind Key: Value Paare
# Sind geordnet
# Sind veränderbar
# Key-Duplikate sind nicht erlaubt

myCar = {
    "Brand": "Audi",
    "Model": "A3",
    "Year": 2017
}

print(myCar)  # Gibt das ganze Objekt zurück
print(myCar["Year"])  # Gibt nur den Values des Keys "Year" zurück

# Wert ändern
myCar["Year"] = 2019
print(myCar)

myCar.update({"Year": 2021})
print(myCar)

# Neuen Wert hinzufügen
myCar["Wheels"] = 4
print(myCar)
# Alternativ:
myCar.update({"Wheels": 4})
print(myCar)

# Neuen Wert hinzufügen, falls er noch nicht existiert:
# dictionary.setdefault("key", Value)
# Falls der Eintrag bereits existiert, wird der derzeitige Wert des Keys zurückgegeben

print(myCar.setdefault("Wheels", 8))  # Gibt 4 zurück, da der Key bereits existiert
print(myCar.setdefault("FuelUsage", 8))  # Gibt 8 zurück und erstellt den Key mit dem Wert
print(myCar)

# Methode um Value auszulesen
print(myCar.get("Model"))

# dictionary.items()
# Gibt alle Key:Value Paare als Tupel zurück

print(myCar.items())

# dicitonary.keys()
# Gibt die Keys als Liste zurück
print(myCar.keys())

# dictionary.values()
# GIbt Values als Liste zurück
print(myCar.values())

# dictionary.popitem()
# Entfernt das letzte Key:Value Paar und gibt es als Tupel zurück
print(myCar.popitem())
print(myCar.popitem())

# dictionary.pop("key")
# Entfernt das angegebene Key:Value Paar
# Gibt den Value des Keys zurück
print(myCar.pop("Brand"))
print(myCar)

# 1. Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
# Kombiniere die drei Listen in eine ganze Liste und schließe Duplikate aus

# 2. Erstelle einen String und wandele ihn in eine Liste um, dabei soll jedes einzelene Zeichen ein Element der Liste werden

# 3. Lasse eine Liste erstellen die bei 0 beginnt und alle geraden Zahlen bis 20 enthält
# Nicht selbst schreiben, sondern Python machen lassen


# Übung 1:
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
list4 = list1 + list2 + list3
list4 = list(set(list4))
print(list4)

# Übung2:
myStringExcercise = "Hello World"
excerciseList = []
excerciseList.extend(myStringExcercise)
print(excerciseList)

# Übung 3:
excerciseRange = range(0,21, 2)
excerciseRange = list(excerciseRange)
print(excerciseRange)