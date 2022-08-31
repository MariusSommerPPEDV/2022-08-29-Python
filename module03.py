import time

# Kontrollstrukturen

# if-Anweisungen
# Werden meistens in Kombination mit den logischen Operatoren benutzt

# Vergelichsoperatoren:
# < - Kleiner als
# <= Kleiner gleich
# > größer als
# >= größer gleich
# == Prüft ob die Werte gleich sind

# Logische Operatoren
# and - und, beide Bedingungen müssen wahr, alternativ &
# or - oder, eine der beiden Bedingungen muss wahr sein, alternativ |
# not - nicht, negiert die Bedingung
# is - ist identisch, vergleicht nicht die Werte sondern die Adresse im Speicherplatz
# in - prüft ob das Element links vom in im Objekt rechts von in enthalten ist

# if-Anweisung
# Prüft die BEdingung rechts vom if, in dem if es in einen Boolean umwandelt
# Falls True zurückgegeben wird, steigt Python in den if-Block rein

a = 200
b = 20

# if Bedingung:
#       Code-Block

if a < b:
    print("a ist kleiner")  # Wird nur ausgeführt, falls a kleiner als b ist
elif a == b:
    print("a und b sind gleich groß")
else:
    print("a ist größer als b")  # Wird ausgeführt wenn der if-Block davor False ist

# else
# Wird ausgeführt falls der vorherige if Block False ist
# Kann nicht ohne vorheriges if oder elif stehen

# elif
# Syntax: elif Bedingung:
#       Code-Block
# elif wird nur geprüft, falls das if davor False ergeben hat
# Ansonsten wird es ignoriert

c = 100

# Bei mehreren if-Statements hintereinander wird jedes geprüft

if c > 100:
    print("c ist größer als 100")
if c > 90:
    print("c ist größer als 90")
if c > 80:
    print("c ist größer als 80")
if c > 70:
    print("c ist größer als 70")
else:
    print("c ist kleiner als 70")

# Mit elif

if c > 100:
    print("c ist größer als 100")
elif c > 90:
    print("c ist größer als 90")
elif c > 80:
    print("c ist größer als 80")
elif c > 70:
    print("c ist größer als 70")
else:
    print("c ist kleiner als 70")

# Elif wird nur geprüft, falls das vorherige if oder elif False war

# Verschachtelte if Blöcke

if a > b:
    print(a, "ist größer als", b)
    if a % 2 == 0:
        print(a, "ist gerade")  # Der Codeblock muss auch wieder eingerückt werden
    else:
        print(a, "ist ungerade")

# Kurzschreibweise if
# Kann auch auf eine Zeile geschrieben werden

if a > b: print("ist größer")

# Kurzschreibweise if und else
print("a ist kleiner") if a < b else print("a ist größer als b")

# Ternary
a = 20
# if, elif und else auf einer Zeile
print("a ist größer als b") if a > b else print("a ist so groß wie b") if a == b else print("a ist kleiner als b")
# Kürzer, aber schwerer zu lesen

# for Schleife
# verhält sich wie eine for each Schleife in anderen Sprachen
# Funktioniert mit iterierbaren Objekten, also z.B: range, list, set usw.
# Syntax:
# for PlatzhalterFürDasElement in IterierbareObjekt

for character in "Hallo Welt":
    print(character.lower())

numList = list(range(0, 16))

for number in numList:
    # f-String
    # f steht für formatted String
    # x = 10
    # f"Der Wert von x: {x}"
    # => Der Wert von x: 10
    print(f"Number hat gerade den Wert: {number}")
    print(f"{number}^2 = {number * number}")
    if number % 2 == 0:
        print(f"{number} ist gerade")
    else:
        print(f"{number} ist ungerade")

# Mit continue und break können wir die Schleife nochmal genauer steuern
# Man kann die Schleife sogar mit einem else kombinieren

evenList = []

for number in numList:
    if number % 2 == 0:
        evenList.append(number)
    elif number == 5:
        continue  # Überspringt die derzeitige iteration
    elif number == 15:
        break  # Bricht die Schleife ab
    else:
        print(f"{number} ist ungerade und wird nicht hinzugefügt")
else:  # Das else wird nur ausgeführt, wenn die Schleife vollständig ausgeführt wurde, also ohne break
    print(evenList)

# FizzBuzz
# 1. Schleife schreiben, die von 0 bis inklusive 100 hochzählt
# 2. Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
# Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# 1
# 2
# Fizz
#  4
# Buzz
# ...
# 14
# FizzBuzz


for i in range(0, 101):
    answ = ""
    if i == 0:
        print(i)
        continue
    if i % 3 == 0:
        answ += "Fizz"
    if i % 5 == 0:
        answ += "Buzz"
    if answ:
        print(answ)
    else:
        print(i)


# print('\n'.join('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or str(i) for i in range(1, 101)))
#  http://michaeljgilliland.blogspot.com/

# List-Comprehension

evenNumbers = [number for number in range(0, 101) if number % 2 == 0]
print(evenNumbers)

# Syntax:
# newList = [expression for identifier in iterierbaresObjekt Bedingung ]
allNumbers = [number - 15 for number in range(0,101)]
print(allNumbers)

testList = ["test" for number in range(2, 6)]
print(testList)

# Die Expression wird in die neue Liste gepackt, wenn bei der Bedingung des identifiers True zurückgegeben wird
# Wenn wir keine Bedingung haben, wird die Expression für jedes Element des Iterierbaren Objektes hinzugefügt

testList2 = ["even" for number in range(0, 11) if number % 2 == 0]
print(testList2)

testList3 = ["even" if number % 2 == 0 else "odd" for number in range(0, 11)]
print(testList3)

nameList = ["Adrian", "Arthur", "Bob", "Xavier"]
newList = [name.upper() for name in nameList if "a" in name[0].lower()]
print(newList)

# neueVariable = [Wert der in die neue Liste gepackt wird for Variable in Liste/Set if Bedingung die eintreten muss]
# Es kann auch der Identifier der for-Schleife verwendet werden, wenn wir die Werte unverändert übernehmen wollen
# Übung zur List-Comprehension
# Schreibe eine List-Comprehension die nur Zahlen aus einer Range von 1 bis inklusive 30 in die neue Liste packt,
# falls die Zahl durch 6 teilbar ist
# Bevor die Zahl in die neue Liste gepackt wird, soll sie um 12 erhöht werden

excerciseList = [number + 12 for number in range(1, 31) if number % 6 == 0]

print(excerciseList)

excerciseList.clear()

for number in range(1, 31):
    if number % 6 == 0:
        excerciseList.append(number + 12)

print(excerciseList)

# while-Schleife

# Benötigen eine Endbedingung
# Benötigen meistens einen Zähler
# Der Zähler muss außerhalb der while Schleife definiert werden

# Syntax:
# while Bedingung:
#   Code-Block
# Optional: else:
#   Code-Block

i = 1

while i < 11:
    print(i)
    i += 1
else:
    print(f"i ist jetzt {i}")


while True:
    print(i)
    i += 10
    if i > 250:
        break

# Verschachtelte for-Schleife:

# Beispiel: Stoppuhr
# Bevor die Minute hochtickt, müssen die Sekunden einmal eine volkommenen Umdrehung hinter sich gebracht haben

# for minute in range(0, 3): # DIe äußere Schleife zählt erst weiter, wenn die innere einmal fertig ist
#     for second in range(0, 60):
#         time.sleep(1)
#         print(f"{minute}:{second}")

# Übung:
# Erstelle eine Schleife die das kleine Einmaleins von 1 bis 10 berechnet, und jeden einzelnen
# Schritt in der Konsole ausgibt
# "1 x 1 = 1"
#.. "10 x 10 = 100"

for i in range(1, 11):
    print(f"{i}'er Einmaleins:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

# Match-Case
test = "Goodbye"

# Syntax:
# match Variable:
    # case Bedingung:
    # Code-Block
    # case _:
    # Default Block
    # In Kombi mit if wird er als guard betitelt


match test:
    case "Hello World":
        print("Goodbye World")
    case "Goodbye World":
        print("Hello World")
    case _ if len(test) > 11:
        print("Langer Satz")
    case _:
        print("Keine der vorherigen Fälle trat ein")
