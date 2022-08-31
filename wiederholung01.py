# Datentypen

# Primitiven
# String - Zeichenfolgen
# Integer - Ganzzahlen
# Float - Gleitkommazahlen
# Boolean - Boolesche Werte also Wahr/Falsch, True/False
# Complex - Komplexe Zahlen

# Collections
# List - []
# Set - {}
# Tuple - ()
# Range - Range()
# Dictionary - {"key": "value"}

# Kontrollstrukturen
# if, elif und else
# match
# for
# while

myList = [1, 2, 3, 4, 5]

for i in myList:
    print(i)

o = 0

while o < len(myList):
    print(myList[o])
    o += 1


test = "Hallo"
greetings = ["Hallo", "Hello", "Hi"]

match test:
    case 3 | 4:
        # Bei match geht es nur mit | und nicht mit or
        print("Test ist 3 oder 4")
    # case "Hallo" | "Hello" | "Hi":
    #     print("test ist eine Begrüßung")
    case "Hallo" if len(test) > 3:
        # Kann auch mit einem expliziten Fall verknüpft werden
        print("test ist Hallo und länger als 3")
    case _ if test in greetings:
        # Wenn ich den default case mit einem if Verbinde, spricht man von einem guard
        print("test ist eine Begrüßung")
    case _ if test in myList:
        print("test ist eine Zahl")
    case _:
        print("Ich werde ausgeführt, falls keiner der vorherigen Fälle eintrat")

for character in test:
    match character:
        case "a":
            print("Ist a")


# List-Comprehension
# Erlaubt es mir schnell eine neue Liste aus einem bestehendem iterierbaren Objekt zu erstellen, kann mit Bedingungen verknüpft werden
# Ich kann auch den Wert davor verändern

doubledMyList = [number * 2 for number in myList]
print(doubledMyList)
oddDoubledList = [number * 2 for number in myList if number % 2 != 0]
print(oddDoubledList)

# Übung neue String Liste
myWordList = ["Test", "Beta", "Hallo", "Bye", "Tschüss"]
# Schreibe eine List-Comprehension, die aus myWordList eine neue Liste erstellt, die aber nur aus Wörtern besteht die länger
# als 4 Zeichen sind
# Und alle Elemente in der neuen Liste sollen komplett großgeschrieben sein

newWordList = [word.upper() for word in myWordList if len(word) > 4]
print(newWordList)

# List-Comprehension mit if und else

fruits = ["apple", "cherry", "banana", "kiwi"]

myFavouriteFruits = [fruit if fruit != "kiwi" else "pear" for fruit in fruits]
print(fruits)
print(myFavouriteFruits)
# Falls wir mit if und else arbeiten müssen die Bedingungen vor der for Schleife stehen
# Alternativ kann man immer eine normale for Schleife benutzen

altList = []
for fruit in fruits:
    if fruit != "kiwi":
        altList.append(fruit)
    else:
        altList.append("pear")

print(altList)

