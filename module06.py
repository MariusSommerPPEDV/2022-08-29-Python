# Filehandling mit Python am Beispiel von Textdateien:
from os.path import exists
# Hier wird aus dem Package OS und dem Modul Path die Funktion "exists" imporitert


def createFile():
    fileName = input("Gib den Dateinamen ein:\n")
    # input() gibt uns die Möglichkeit Eingaben vom User in der Konsole abzufragen
    # Datei erstellen:
    # Syntax von open:
    # open("Dateipfad", "modus")
    # w - writing Überschreibt vorhandenes
    # a - append
    # r - read
    # x - create
    # r+ - read & write
    # w+ - read & write, aber überschreibt die vorhandene Datei
    if not exists(fileName):
        open(fileName, "x")
    else:
        print("Datei wurde nicht erstellt, da sie bereits existiert")
    # Wollen nur die Datei erstellen
    return fileName


def openFile(fileName):
    validValues = ["a", "r", "w"]
    choice = ""
    print("Wähle einen Modus um die Datei zu öffnen:\n(a)ppend\n(r)ead\n(w)rite")
    choice = input().lower()
    while choice not in validValues:
        choice = input("Ungültige Wahl. Bitte a, r oder w auswählen.\n").lower()
    return open(fileName, choice), choice
    # Können in Python auch mehrere Werte zurückgeben lassen, wenn wir sie mit Komma trennen


def writeText(file):
    text = "\n" + input("Was soll in die Datei geschrieben werden?\n")
    file.write(text)


def readText(file):
    # Methoden um aus einer Datei zu lesen:
    # read(bytes) - liest so viele Bytes ein
    # readline() - liest eine Zeile ein
    # readlines() - liest alle Zeilen ein
    text = file.readlines()
    print("Inhalt der Datei:")
    for line in text:
        print(line)


def main():
    print(exists(".\\module06.py"))  # Hier sind zwei Backslashes,
    # weil \ der Escape-Character ist um Sonderzeichen darzustellen
    fileName = createFile()
    file, choice = openFile(fileName)
    if choice == "r":
        # pass wird übersprungen
        readText(file)
    else:
        writeText(file)


if __name__ == '__main__':
    main()
