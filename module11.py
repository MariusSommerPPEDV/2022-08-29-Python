# Einfache Datenbankanbindung

# Benutzen hierfür sqlite3


# Für größere Sachen:
# https://www.sqlalchemy.org/

# müssen dafür das sqlite3 modul importieren

import sqlite3

# Verbindungsherstellung
connection = sqlite3.connect("kurs.db")
# connection = sqlite3.connect(":memory:") erstellt eine In-Memory Datenbank

# Erzeugt einen Cursor, der zwischen unserem Server und unserem Code "dolemtscht"
cursor = connection.cursor()

# Mit dem Cursor können wir direkt Befehle auf dem Server ausführen

# Dafür benutzen wir die Methode execute des Cursors
cursor.execute("create table if not exists testtable(id integer primary key, name text)")
# Hier erstellen wir eine neue Tabelle, falls diese noch nicht existiert

id = int(input("Id eingeben:"))
name = input("Namen eingeben:")
# Wir fragen nach den Werten, die eingetragen werden sollen

# NUn fügen wir das in die neue Tabelle ein
cursor.execute("Insert into testtable(id, name) values(?, ?)", (id, name))
# Sqlite erwartet immer Tupel, also müssen wir unsere variabeln verpacken
# Selbst bei einem einzigen Wert, der übergeben wird, will sqlite ein Tupel: (id,)

# damit die daten wirklich gespeichert werden, müssen die Daten commited werden
# commit() ist eine Methode der Connection und nicht des Cursors
connection.commit()

# Daten abfragen funktioniert ähnlich wie das einfügen neuer Daten
cursor.execute("select * from testtable")

# print(cursor)  sagt nur cursor objekt

# Bevor wir die Daten anschauen können müssen wir sie "fetchen"
# Dafür gibt es 3 verschiedene Methoden beim Cursor Objekt
# cursor.fetchall() Nimmt sich alle Zeilen aus der Abfrage und packt sie in eine Liste
# cursor.fetchmany(anzahlAnZeilen) Hier können wir sagen wie viele Zeilen geholt werden sollen
# cursor.fetchone() Nimmt sich eine Zeile raus
# Der Cursor merkt sich die aktuelle Position
# D.h. wenn ihc als erstes cursor.fetch() aufrufe befinde ich mich nun in Zeile 2

rowOne = cursor.fetchone()
rowMany = cursor.fetchmany(3)
rowAll = cursor.fetchall()

print("Zeile 1: ", rowOne)
print("Zeile 2-4: ", rowMany)
print("Restlichen Zeilen: ", rowAll)

# Nachdem wir mit der Datenbank fertig sind, sollten wir sie wieder schließen
connection.close()
