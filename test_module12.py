import unittest
from unittest import TestCase
# Hier wird das unittest modul importiert


# Die Testklasse selber muss vom TestCase erben
from module12 import randomClass


class TestRandomClass(TestCase):
    # Hier definiere ich einen bestimmten Testfall
    # Wir gehen nach dem Schema Arrange, Act, Assert vor
    def test_randomClass(self):
        # Arrange und Act in diesem Fall
        # Da wir den Constructor testen und somit der act teil des arrange ist
        instance = randomClass(25, 50, 40)
        # Assert
        # Wir wollen, dass instance nicht none ist
        self.assertIsNotNone(instance, "Die Variable instance wurde nicht richtig erstellt")
        # instance muss eine Instanz von randomClass sein
        self.assertIsInstance(instance, randomClass, "instance ist keine Instanz der Klasse randomClass")

    def test_area(self):
        # Hier wollen wir nun die Methode area testen

        # Arrange
        instance = randomClass(25, 50, 40)
        expectedResult = 75

        # Act
        # Wir weisen den Wert der Aktion einer Variablen zu
        result = instance.area()

        #Assert
        # Wir stellen Behauptungen auf und hoffen, dass sie erfüllt werden
        self.assertEqual(result, expectedResult, "Die Methode area hat ein falsches Ergebnis geliefert")
        self.assertIsInstance(result, int, "Das Ergebnis ist kein integer")


if __name__ == "__main__":
    unittest.main()
    # Führt den Test durch
