# Funktionen


def funktionsName():
    return 1


def funktionMitParameter(test):
    print(test)



funktionMitParameter("testasd123")

funktionMitParameter(test="Ich bin der Test-Parameter")


def positionalOnly(test, /):
    print(test, "der Parameter kann nicht mehr per Keyword befüllt werden")

# positionalOnly(test="aabasdasdasd")  Geht nicht als Keyword, da wir den / gesetzt haben


def arbitraryArguments(*arbitraryArguments):
    print(arbitraryArguments)
    print(type(arbitraryArguments))


arbitraryArguments(12, 4, 5, 6, 7, 8, 12313, 65)


def defaultParams(test=12):
    print(test)

defaultParams()


def arbitraryKwords(**kwargs):
    print(kwargs)


arbitraryKwords(test=124, tasd="adasda", klopasda=124)


# Classes

class Klasse:
    def __init__(self):
        self.test = "yes"

    def methode(self):
        print("Hallo aus der Klasse")


instanz = Klasse()

print(instanz.test)

instanz.methode()

