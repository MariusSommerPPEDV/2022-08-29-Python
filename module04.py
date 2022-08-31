# Functions

# Ein Code-Block, der nur ausgeführt wird wenn wir ihn aufrufen
# Beispiele, len(), print()
# len(Paramter)
# Print(Parameter1, Parameter2...., ParameterN)

# Wir können auch eigenen Funktionen definieren
# Funktionen erlauben wiederverwendbarkeit, also sparen wir uns Arbeit
# Erleichtern das Testen
# Verbessern die Organisation des Codes
# Wie definiere ich Funktionen in Python?
# Syntax:
# def NameDerFunktion(Optional: Paramter):
#   Code_Block
# NameDerFunktion() => Aufrufen ohne Parameter
# NameDerFunktion("Test") => Aufrufen mit Parameter

def greeter():
    print("Hello World")


greeter()
greeter()


# Funktionen ohne Parameter können nicht mit Parametern ausgeführt werden
# Funktion mit Parameter definieren:


def greetPerson(personName):
    print(f"Hello {personName}")


greetPerson("Max")
greetPerson(12)
# greetPerson() Fehler, da ich einen Parameter übergeben muss

print(greetPerson("test"))  # None, da kein Rückgabewert definiert wurde
print(greetPerson)  # function at ....


# Rückgabewerte in eine Funktion einbauen:


def addNumber(numberOne, numberTwo):
    return numberOne + numberTwo


addNumber(12, 14)  # Macht effektiv nichts, da wir uns den Rückgabewert nicht "merken"
result = addNumber(12, 14)
print(result)
print(addNumber(15, 12))
print(addNumber("test", "hallo"))


# Default Werte
# Eignet sich z.B. wenn einer der beiden Parameter optional sein soll


def addNumberDefault(numberOne, numberTwo=0):
    return numberOne + numberTwo


print(addNumberDefault(12))  # Kann jetzt mit nur einem Paramter aufgerufen werden

result = addNumberDefault("Test", "test")
print(result)

# Alle normal definierten Parameter in Python sind automatisch auch Keywords

result = addNumberDefault(numberTwo=50, numberOne=24)
print(result)

# Parameter in Python können direkt befüllt werden, wenn wir ihren Namen gefolgt von einem = schreiben

# result = addNumberDefault(numberTwo=25)  Fehler, da numberOne nicht befüllt wurde
print(result)


def sumNumbers(*numbers):  # Der Stern vor dem Parameter-Namen muss nur in de Klammern bei der Definition stehen
    result = 0
    for number in numbers:  # Hier kann ich einfach den Namen des Parameters verwenden
        result += number
    return result


print(sumNumbers(12, 5, 1, 7, 42312, 542, 21))
print(sumNumbers(12))
print(sumNumbers(52, 63, 87, 95))

myTuple = tuple(range(1, 11))
myList = list(range(1, 11))

# sumNumbers(myTuple) Geht nicht, da die Funktion einzelne Werte erwartet
print(sumNumbers(*myTuple))  # unpacking Operator
print(sumNumbers(*myList))  # Packt die Liste/Tupel in einzelne Werte aus und übergibt sie der Funktion


def spellWord(*word):
    for character in word:
        print(character)


spellWord("test")
spellWord(*"test")

# Unpacking funktioniert mit jeder Indexbasierten Collection
# Der *-Operator kann auch zum "einpacken" verwendet werden

(a, b, *c, d) = (1, 2, 3, 4, 5, 6)
print(a)
print(d)
print(c)


# Wenn wir einen * vor eine Variable setzen kann sie zu einer Liste umgewandelt werden,
# wenn es mehr Werte als Variablen gibt

# greetPerson(personName="test", middleName="blabla", lastName="blabal")

# Wir können in Python auch arbitrary Kewyword Arguments verwenden, also eine unbestimmte Anzahl von übergebenen
# Keywords


def greetGuests(**guests):
    for key in guests:
        print(f"Hello {guests[key]}")


greetGuests(guest1="Max", guest2="Volker", guest3="Paul", guest4="Lukas", xyz="Marius", tata=60)

testDict = {"guest1": "Max", "guest2": "Volker", "guest3": "Paul", "guest4": "Lukas", "xyz": "Marius", "tata": 60,
            "Fertig": True}

greetGuests(**testDict)


def printDict(**keywords):
    for key, value in keywords.items():
        print(f"Schlüssel:{key} | Wert:{value}")


printDict(**testDict)


# Arbitrary Arguments, Arbitrary Keywordarguments, Positonals und Default-Paramter können beliebig vermischt werden
# valueTwo kann nur durch Keyword befüllt werden, da alle vorherigen Werte in das Tupel "test" gepackt werden

def mixedFunc(valueOne, *test, valueTwo=123, **kwords):
    print("valueOne:", valueOne)
    print("*test", *test)
    print("valueTwo:", valueTwo)
    print("**kwords:", kwords)


mixedFunc("test", "bla", "test2", 3, 5, 6)
mixedFunc("Hallo Welt",  1, 2, 3, 4, 5, 6, valueTwo="Bye World", test2="hallo", test3="TEST", test4=50)

# Es kann auch die verwendung von positional Arguments erzwungen werden:
# Wenn ich einen / nach einer Reihe von Parametern setze werden diese positional-only
# d.h. sie können nicht mehr per keyword befüllt werden


def multiply(numOne, numTwo, /, param3):
    print(param3)
    return numOne * numTwo


print(multiply(213, 245, param3="Test"))


# Übung 1:
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# Und uns die größte dieser Zahlen zurückgibt


def returnMax(*numbers):
    max = numbers[0]
    for num in numbers:
        if max < num:
            max = num
    return max


print(returnMax(150, 125, 100, 75, 750))
print(returnMax(750))
print(returnMax(-150, -125, -100, -75, -750))

# Übung 2:
# Wir wollen eine Funktion erstellen, die einen String als Paramter erhält
# Die Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht
# Bonus: Die Funktion soll zusätzlich zählen wie viele Sonderzeichen(Nummern inkludiert) enthalten sind und das
# ebenfalls ausgeben
# Sonderzeichen: 4 | Groß: 3 | Klein: 12


def countCase(string):
    lower = 0
    upper = 0
    special = 0
    for char in string:
        if char.lower() == char.upper():
            special += 1
        elif char == char.lower():
            lower += 1
        else:
            upper += 1
    print(f"Sonderzeichen: {special} | Groß: {upper} | Klein: {lower}")

# Schönere Variante:


def countCaseAlternative(string):
    lower = 0
    upper = 0
    special = 0
    for char in string:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        else:
            special += 1
    print(f"Sonderzeichen: {special} | Groß: {upper} | Klein: {lower}")

print(__name__)