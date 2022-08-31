import module05  # Mit einfachem import Statement muss ich den Namen des Moduls vor den Funktionsnamen hängen
from helper import sayHello, greetPerson # Hier sage ich explizit welche FUnktionen/Klassen importiert werden
# from helper import * , importiert alle Funktionen/Klassen direkt in die Datei, macht es schwieriger zum Nachvollziehen
# woher etwas kommt

# Module-Searchpath
# 1. Existiert in dem Ausführungsordner(da wo die ausgeführte Python Datei liegt) ein Modul mit diesem Namen
# 2. PYTHONPATH, Ordner in dem Python selbst installiert ist, inkludiert alle Python Integrierten Libraries
# 3. Liste an Ordnern, die wir bei der Installation von Python zusätzlich konfiguriert haben
# Wenn nach Punkt 3 nichts gefunden wird => ModuleNotFoundError
# Mit dem sys Module können wir die Suchpfade anzeigen lassen
# sys.path => Liste, die die einzelnen Suchpfade enthält

import sys
import pandas

def main():
    print("Ich werde direkt ausgeführt")
    module05.countCase("Test 123 Test")
    print(module05.calcTax(1000, 0.19))
    sayHello()
    greetPerson("Max Mustermann")
    for location in sys.path:
        print(location)  # Gibt die einzelnen Ordner in der Konsole aus, in denen Python nach einem Modul sucht

# Snippet in Pycharm:
# main => Tab

# Wie installiere ich ein zusätzliches Modul?
# 1. Entweder per Terminal:
# pip install <PackageName>
# 2. Über den Python Packages Tab in Pycharm



if __name__ == "__main__":
    main()

