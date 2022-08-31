# Vertiefung Klassen


class Lebewesen:

    def __init__(self, age, species):
        self.age = age
        self.species = species

    def __str__(self):  # WIrd immer aufgerufen, wenn wir unser Objekt als String darstellen wollen
        return f"Ich bin ein Lebewesen der Spezies {self.species} und ich bin {self.age} Jare alt."

    def aging(self):
        self.age += 1


amoeba = Lebewesen(1, "ameoba")

print(amoeba)  # Gibt bis jetzt nur den Speicherpunkt aus und zu welcher Klasse es gehört
print(f"EIn Objekt: {amoeba.age} {amoeba.species}")
amoeba.aging()
print(amoeba)


# Vererbung
# Bei der Vererbung sind runde Klammern zwingen nötig, da ich in die runden Klammern die Basisklasse eintrage
# Hund ist eine Subklasse von Lebewesen
# Subklasse = Klasse, die von einer anderen erbt
class Hund(Lebewesen):
    # Alle Eigenschaften und Methoden der Basisklasse sind automatisch vorhanden
    def __init__(self, age, breed, name):
        super().__init__(age, "dog")
        # super() ruft die Basisklasse auf, .__init__() ruft den Konstruktor der Basisklasse auf
        # Hier übergeben wir alle Parameter, die die Basisklasse bereits abdeckt
        # Wir können auch einige Parameter fix übergeben, wie in diesem Fall dog
        # Zusätzliche neue Parameter können nicht der Basisklasse übergeben werden, sondern müssen vom Constructor der
        # Kindsklasse selbst gehandelt werden
        self.breed = breed
        self.name = name

    def __str__(self):
        # Hier überschreiben wir die Methode __str__ der Basisklasse
        return super().__str__() + f" Ich bin ein {self.breed} und mein Name ist {self.name}"

    def bark(self):  # Die neue Methode gibt es nur für die Klasse Hund
        print("Wuff wuff")


lessie = Hund(3, "collie", "lessie")
lessie.bark()
print(lessie)
lessie.aging()
print(lessie)


# Typisierung und Docstrings
# Es kann auch von Subklassen geerbt werden
class Collie(Hund):
    # Typeannotation
    # Wir hängen hinter einem Parameter einen : an und nach dem Doppelpunkt geben wir den Typen an
    # Sind allerdings nur Empfehlungen und werden nicht erzwungen
    def __init__(self, age: int, name: str):
        super().__init__(age, "collie", name)

    # Typisierung bei Rückgabe
    # -> Typ
    # Wird vor den Doppelpunkten der Methode gesetzt
    # Docstrings
    # Ein Docstring beschreibt die Methode/Klasse
    # Wird definiert durch """
    # Direkt nach der Definitionszeile
    def rescue(self, test: str, test2: int) -> str:
        """
        Eine Methode um Menschen zu retten
        :param test: Ein teststring
        :param test2: Ein testint
        :return: Ein kurzer Satz
        """
        return "Kind wurde gerettet"


lessie2 = Collie("test", 12)  # Funktioniert, aber Pycharm weist darauf hin, dass ein anderer Typ erwartet wird
print(lessie2)
print(lessie2.rescue("test", 2))


# Übung:
# Erstelle eine Klasse Fahrzeug erstellen
# Sie soll über die Props:
# Motorstatus: bool
# maximale Geschwindigket: int
# derzeitige Geschwindigkeit: int
# Sie soll die __str__ Methode implementieren
# Sie soll eine beschleunigungs Methode implementieren, diese akzeptiert einen Parameter, die neue Geschwindigkeit
# Wenn die neue Geschwindigkeit <= maximale Geschwindigkeit ist, soll die derzeitige Geschwindigkeit angepasst werden

class Fahrzeug:
    def __init__(self, motorstatus: bool, maxSpeed: int, currentSpeed: int):
        self.motorstatus = motorstatus
        self.maxSpeed = maxSpeed
        self.currentSpeed = currentSpeed

    def __str__(self):
        return f"Ein Fahrzeug. Derzeitige Geschwindigkeit: {self.currentSpeed}. Maximale Geschwindigkeit: {self.maxSpeed}."

    def accelerate(self, newSpeed: int):
        if newSpeed <= self.maxSpeed:
            self.currentSpeed = newSpeed
        else:
            print("So schnell gehts nicht")


car = Fahrzeug(True, 200, 0)
print(car)
car.accelerate(150)
car.accelerate(250)
print(car)

