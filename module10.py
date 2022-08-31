# Fehlerbehandlung in Python

def doStuff(test):
    print(test)


# doStuff()  # So würde unser Programm eifnach abstürzen

# Wir können in Python aber auch Fehler abfangen und behandeln

# Das funktioniert mit dem try-Block

try:
    doStuff("test")
    # Der try-Block kann nicht alleine stehen
    # Wir brauchen immer zusätzlich einen except oder finally Block, oder beides
except Exception as e:  # Hier erwarten wir jeglichen Fehler, speichern die Fehlermeldung als Variable e
    print(e)  # Hier lassen wir e ausgeben, falls ein Fehler auftritt
    print("Ich führe aber weiter aus")  # Und hier lassen wir etwas zusätzliches ausgeben, falls ein Fehler auftritt
    # Alles was im except Block steht wird nur ausgeführt, falls ein Fehler auftritt

# Wir sollten allerdings nicht einfach jegliche Art von Fehler erwarten
# Denn so behandeln wir jeden Fehler gleich egal was ist

# WIe gehe ich auf verschiedene Arten von Fehlern ein?


def divide(numOne, numTwo):
    return numOne / numTwo

# divide(2, "zwei")  TypeError
# divide(2, 0)  ZeroDivisionError

try:
    numOne = int(input("Gib eine Zahl ein"))  # Hier fragen wir nach UserInput und wandeln ihn in eine Zahl um
    numTwo = int(input("Gib die zweite Zahl ein"))
    divide(numOne, numTwo)
except TypeError as e:  # Hier wird nur der TypeError erwartet, alle anderen Exceptions führen zum Absturz
    print("Unerwarteter Typ wurde übergeben")
    print(f"Type von NumOne: {type(numOne)} | Type von NumTwo: {type(numTwo)}")
except ValueError as e:
    print("Es können nur Zahlen übergeben werden")
    print(e)
except ZeroDivisionError as e:
    print("Es kann nicht durch 0 geteilt werden. numTwo wurde auf 1 geändert")
    divide(numOne, 1)
except Exception as e:  # Hier fangen wir alle anderne nicht behandelten Fehler ab
    print("unerwartert Fehler")
    print(e)
# Zusätzlich zu try können wir else und finally Blöcke hinzufügen
else:  # Der else Block wird ausgeführt, falls alles ohne Fehler durchlief
    print("Programm wurde erfolgreich ausgeführt")
    print(divide(numOne, numTwo))
# Abschließend gibt es noch den finally Block
finally:
    # Der finally Block wird immer ausgeführt, egal ob es fehler gab oder nicht
    print("Ich werde immer ausgeführt")


# while True:
#     try:
#         numOne = int(input("Gib eine Zahl \n"))  # Hier fragen wir nach UserInput und wandeln ihn in eine Zahl um
#         numTwo = int(input("Gib die zweite Zahl ein\n"))
#         divide(numOne, numTwo)
#     except TypeError as e:  # Hier wird nur der TypeError erwartet, alle anderen Exceptions führen zum Absturz
#         print("Unerwarteter Typ wurde übergeben")
#         print(f"Type von NumOne: {type(numOne)} | Type von NumTwo: {type(numTwo)}")
#     except ValueError as e:
#         print("Es können nur Zahlen übergeben werden")
#         print(e)
#     except ZeroDivisionError as e:
#         print("Es kann nicht durch 0 geteilt werden. numTwo wurde auf 1 geändert")
#         divide(numOne, 1)
#     except Exception as e:  # Hier fangen wir alle anderne nicht behandelten Fehler ab
#         print("unerwartert Fehler")
#         print(e)
#     # Zusätzlich zu try können wir else und finally Blöcke hinzufügen
#     else:  # Der else Block wird ausgeführt, falls alles ohne Fehler durchlief
#         print("Programm wurde erfolgreich ausgeführt")
#         print(divide(numOne, numTwo))
#     # Abschließend gibt es noch den finally Block
#     finally:
#         # Der finally Block wird immer ausgeführt, egal ob es fehler gab oder nicht
#         print("Ich werde immer ausgeführt")
#         choice = ""
#         while choice.lower() not in ["n", "j"]:
#             choice = input("Noch etwas berechnen? (J)a|(N)ein\n")
#             if choice.lower() == "n":
#                 exit()
#             elif choice.lower() == "j":
#                 break

# Eigene Fehlerarten erstellen
# Einfach Namen definieren und von Exception erben lassen
# Körper kann einfach pass enthalten
class CoffeeError(Exception):
    pass

# Mit dem Keyword raise können wir jederzeit Fehler ezwingen, egal ob vordefinierte oder eigene Fehlerklassen

coffee = 1
try:
    if coffee < 1:
        raise CoffeeError("Zu wenig Kaffee")
    # raise ValueError  ich kann auch vordefinierte Fehler erheben
except CoffeeError as e:
    print(e)
    print("Geh mal Kaffee holen")


