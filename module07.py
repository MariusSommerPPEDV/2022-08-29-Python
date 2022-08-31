# Klassen in Python

# Objekte
# Eigentlich ist alles in Python ein Objekt
# type(variable/wert) gibt eine String zurück der uns sagt um welchen Typen es sich
# bei der Variable handelt
print(type(12))  # => class int, Objekt der Klasse Integer

# isinstance(variable, klasse)
print(isinstance("test", str))  # => True, da "test" eine Instanz der Klasse str ist

# Klasse
# Eine Klasse ist eine Art Blaupause, es definiert was ein Objekt der Klasse ausmacht
# Was das Objekt z.B. können muss

# Instanz
# Die tatsächliche Ausprägung des Objektes

# Wie definiere ich eine eigene Klasse in Python?
# Wir benutzen das Keyword class


class Table:
    # Um unsere Klasse sinnvoll zu initialisieren, sollten wir ihr einen Constructor geben
    def __init__(self, fuesse, ablageflaeche):
        # __init__ entspricht dem Construcotr andere Sprachen und wird immer aufgerufen
        # wenn wir eine neue Instanz der Klasse initialisieren
        print("Init von Table wurde aufgerufen")
        self.feet = fuesse
        self.area = ablageflaeche

    def polish(self):
        # Methoden werden wie Funktion definiert, sind aber im Klassenkörper
        # und haben als ersten Parameter immer self
        print("Tisch wurde poliert.")


schreibtisch = Table(4, 400)
kuechentisch = Table(2, 250)
print(schreibtisch)
print(type(schreibtisch))
print(isinstance(schreibtisch, Table))

# In Python können Instanzen neue Attribute (Properties) erhalten
# schreibtisch.name = "Günther"
# Dynamic Props sollten vermieden werden
# print(schreibtisch.name)

# Wie greife ich auf Props zu?
print(schreibtisch.area)
print(kuechentisch.feet)

# Wie rufe ich eine Methode auf?
schreibtisch.polish()
