# Module in Python
# Sind Libraries, die uns zusätzliche Funktionalität anbieten und meist auf eiN Thema zugeschnitten sind
# Bevor wir sie benutzen können müssen wir sie importieren und manchmal auch installieren

# Wie importiere ich Module in Python?

# from <ModulName> import <Namen der Funktionen/Klassen>/ * (Importiere alles)
# import <ModulName> => importiert auch alles

# from turtle import *
#
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
# Strg + / Kommentiert alles markierte aus

# import module04
# Wenn ich modul04 importiere, wird jede Zeile Code des Moduls eingelsen und ausgeführt

# print(__name__)


def countCase(string):
    lower = 0
    upper = 0
    special = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        else:
            special += 1
    print(f"Sonderzeichen/Zahlen: {special} | Groß: {upper} | Klein: {lower}")


def calcTax(price, tax):
    return price * tax

if __name__ == "__main__":
    print("Ich bin Modul05")
    print(__name__)
    print("Modul05 ist zu ende")


# Die Variable __name__ enthält den Namen einer Python-Datei
# Falls die Datei direkt ausgeführt wird ist __name__ immer __main__
# Falls ich die Datei importiere ist __name__ der tatsächliche Dateiname
