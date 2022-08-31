# Lambdas und Decorators

# Lambdas sind eine Art der anonymen Funktione
# In anderne Sprachne oft auch als Pfeilfunktion bekannt =>
# In Python werden sie mit dem lambda Keyword definiert
# Sie benötigen nicht unbedingt einen Identifier
# Die Parameter, die sie erhalten werden nicht mit klammern geschrieben
# Sie dürfen nur eine Expression enthalten
# Sie brauchen kein return

# Beispiel einer Lambdafunktion:
import time

lambda numOne, numTwo: numTwo * numOne
# So sinnlos, da ich sie nicht aufrufen kann
multiplier = lambda numOne, numTwo: numOne * numTwo


# Selbe Funktion, aber ohne lambda Syntax
def multiply(numOne, numTwo):
    return numOne * numTwo


result = multiplier(5, 20)
print(result)
print(multiplier(numTwo=20, numOne=500))

# Können auch arbitrary Arguments und arbitrary Keyword arguments erhalten
lambdaMitArb = lambda *args: print(args)

lambdaMitArb(1, 2, 3, 4, 5, 6)

# lambdas dürfen kein while, for, return, continue oder break enthalten

# Werden häufig als Parameter für eine andere Funktion benutzt
# V.a. in Verbindung mit filter() und map()
# filter(Funktion die auf jedes Element der Liste der angewandt wird, liste die gefiltert wird)
# filter() gibt ein filter Objekt zurück
numberList = list(range(100))

# Wir wollen die numberList mittels filter und lambdas auf gerade Zahlen filtern
evenNumberList = list(filter(lambda num: num % 2 == 0, numberList))
# die filter Funktion iteriert über jedes Element der numberList und fügt das Element dann in die lambda Funktion ein
# Falls die Funktion True ergibt, wird das Element in das Filter-Objekt gepackt, andernfalls wird es ignoriert
# Es verändert die bestehende Liste nicht, sondern gibt ein komplett neues Filter Objekt zurück
print(evenNumberList)
print(filter(lambda num: num % 2 == 0, numberList))  # Gibt nur zurück, dass es sich um ein Filter Objekt handelt und wo


# es liegt


# Geht auch mit einer normalen Funktion anstelle von lambda
def isEven(number: int):
    return number % 2 == 0


# Diese Funktion kann auch als Parameter übergeben werden
# Wichtig ist dabei, dass die Funktion, dann ohne Klammern übergeben werden muss
# Da wir nur die Referenz auf die Funktion übergeben und sie nicht sofort ausführen wollen

altEvenList = list(filter(isEven, numberList))
print(altEvenList)


# Wie sieht das innerhalb der Funktion aus?
# Dafür erstellen wir unsere eigene Filterfunktion
def filterList(functionReference, listToFilter: list):
    filterdList = []
    for element in listToFilter:
        if functionReference(element):
            filterdList.append(element)
    return filterdList


myEvenList = filterList(isEven, numberList)
print("Ich bin mit unserer eigenen Funktion gefiltert worden.")
print(myEvenList)
print("Ich bin unsere eigenen Liste, aber diesmal mit Lambda")
print(filterList(lambda num: num % 2 == 0, numberList))

# Die Map Funktion
# Syntax: map(Funktion die auf jedes Element angewandt wird, iterierbares Objekt)
# Gibt ein Map objekt zurück
# Erwartet keinen booleschen Wert bei der Funktion
quadrupledList = map(lambda num: num * 4, numberList)
print(quadrupledList)  # Gibt nur zurück, dass es sich um ein Map Objekt handelt und wo es liegt
quadrupledList = list(quadrupledList)  # Hier wandeln wir das Objekt in eine Liste um
print(quadrupledList)  # Hier geben wir die Liste aus

# Decorators in Python
# Sind Funktionen, die das verhalten von anderen Funktion verändern
# Werden mit @decorator hinzugefügt
# def test():

# Auch Funktionen sind in Python einfach objekte

print(isEven)

# Funktionen können Variablen zugewiesen werden

test = isEven(3)  # SO wird das Ergebnis der FUnktion einer Variable zugewiesen
test2 = isEven  # Jetzt wurde eine Funktion einer Variable zugewiesen

# test2 verweist nun auf die isEven Funktion und kann auch aufgerufen werden kann

print(test2(3))  # Hier führe ich die referenzierte Funktion aus


# Dementsprechend können auch Funktionen erstellt werden, die andere Funktionen zurückgeben

# Decorator machen sich das zu Nutzen, sie führen erst ihr eigenes Verhalten aus und danach die dekorierte Funktion


# Eigener Decorator:
# Decorators erhalten als Parameter immer eine Funktion
def myDecorator(func):
    # Meistens enthalten sie eine weitere Funktion, einen sogenannten Wrapper
    def wrapper():
        print("Ich werde vor der Funktion ausgeführt")
        func()  # Hier wird die dekorierte Funktion ausgeführt
        print("Ich werde nach der Funktion ausgeführt")

    return wrapper  # Hier geben wir die nun dekorierte Funktion zurück


def sayHello():
    print("Hallo Welt")


decoratedSayHello = myDecorator(sayHello)  # Hier lasse ich isEven dekorieren

sayHello()
decoratedSayHello()


# Kurzfassung: Ein Decorator ist eine Funktion, die eine andere Funktion umschließt und ihre Verhalten anpasst

# Da diese Variante der decorators recht aufwendig ist wurde eine Kurzform eingeführt


@myDecorator
def sayBye():
    print("Bye World")


sayBye()


# Decorator mit Parametern
def doTwice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@doTwice
def tellResult(numberOne, numberTwo):
    print(numberOne + numberTwo)


tellResult(12, 56)
tellResult(numberOne=60, numberTwo=55)


# Weiteres Problem:
# Rückgabe einer dekorierten Funktion
@doTwice
def isOdd(number):
    return number % 2 != 0


result = isOdd(3)  # Wir erwarten True

print(result)  # Tatsächlich aber none, da mein wrapper keine Rückgabe hat


# Neuer Decorator mit return
def doTwiceReturn(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)  # Hier wird der Rückgabewert der referenzierten Funktion zurückgegeben
    return wrapper


@doTwiceReturn
def addNumbers(numOne, numTwo):
    return numOne + numTwo


result = addNumbers(59, 21)
print(result)

# Bei Klassen kommen Decorator z.B. zum Einsatz
# Decorator implementieren das verhalten von Gettern und Settern


class Square:
    def __init__(self, seitenlänge):
        self._seitenlänge = seitenlänge  # Unterstrich steht für "privates" Property

    @property  # Wird zum getter, ist also zum abrufen der Seitenlänge da
    def seitenlänge(self):
        print("Getter wird ausgeführt")
        return self._seitenlänge  # Geben das private Prop aus

    @seitenlänge.setter  # Wird verwendet wenn wir die Seitenlänge neu zuweisen
    def seitenlänge(self, neuerWert):
        print("Setter wird aufgerufen")
        self._seitenlänge = neuerWert

mySquare = Square(20)
mySquare.seitenlänge
mySquare.seitenlänge = 40
# mySquare._seitenlänge = 21  Geht trotzdem, da Python das Konzept von privaten Attributen nicht kennt
print(mySquare.seitenlänge)

# Decorators verändenr das Verhalten unserer eigenen Funktionen
# Meistens werden sie um nue Funktionen erweitert
# Wir erstellen nun eine Funktion, die misst wie lange eine FUnktion zum ausführen braucht

# Hier erstellen wir den decorator
def timeFunction(func):
    # Der Decorator muss immer eine Funktion zurückgeben
    # Und zwar die ursprüngliche FUnktion + das zusätzliche Verhalten des Decorators
    # Wir definieren nun den Wrapper, dieser verändert das ursprüngliche Verhalten
    def wrapper(*args, **kwargs):
        # Wir setzen uns nun einen Startzeitpunkt
        startTime = time.time()  # Gibt uns das derzeitige Datum + Uhrzeit zurück
        result = func(*args, **kwargs)  # Hier wird unsere ursprüngliche FUnktion ausgeführt
        endTime = time.time()  # Definiert den Endzeitpunkt
        return (endTime - startTime), result  # Gibt uns die Zeit in Sekunden, sowie unser Ergebnis zurück
    return wrapper


@timeFunction
def sumNumbers(*args):
    return sum(args)


print(sumNumbers(*range(100000000)))
print(sumNumbers(*range(1000)))

