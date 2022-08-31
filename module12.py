# Einfache Unittests
# Python kommt mit seinem eignene Testframework
# unittest

# Ein Unittest ist ein Test, der einzelne Funktionen oder Teilbereiche testet
# Ein Integrationtest testet das gesamte Programm


class randomClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return self.a + self.b


def greeter(name):
    return "Hello " + name