#Aufgabe 1
#c)
#1.
#Um die funktion sqrt() zu verwenden muss man das Modul "math" importen
import math
print(math.sqrt(4))

#2.
#Die Wurzel einer negativen Zahl gibt einen "ValueError" aus
#'ValueError: math domain error'
#print(math.sqrt(-1))

#3.
#mysqrt using if: else:
print("\nAb jetzt läuft funktion mysqrt() mit if: else:")
def mysqrt(number):
    if number<0:
        return "mysqrt() funktioniert nicht für negative Zahlen, du Dussel!"
    else:
        return math.sqrt(number)
print(mysqrt(10))
print(mysqrt(-10))

#mysqrt using try: except:
print("\nAb hier läauft die funktion mysqrt() mit try: except:")
def mysqrt(number):
    try:
        return math.sqrt(number)
    except ValueError:
        return "mysqrt() funktioniert nicht für negative Zahlen, du Dussel!"

print(mysqrt(3))
print(mysqrt(-3))

#4.
#Der % ("modulo") Operator gibt den Rest einer Division aus.
#Bsp: 15 modulo 4 = 3 Weil 4*3=12 15-12=3 <- der Rest der Division
for i in range(-10,11):
    print("i =",i)
    print(i,"modulo 5 =", i%5)



#5.
#Man benutzt die drei Anführungszeichen um einen Text in mehr als einer Zeile
#auszugeben, die einzelnen Umbrüche werden jedoch beachtet!
#Funktioniert auch außerhalb einer Klammer.
#Außerdem kann man sie für multi line comments abusen.
#Sie werden, so lange man keine variable davor schreibt zwar dennoch als String
#behandelt, jedoch direkt garbage collected.
'''
Dieser String wird direkt garbage collected,
kann also theoretisch als multi line comment
abused werden.
'''

print('''Dieser Text
ragt über eine Teile hinaus
und man mann noch extra Anführungszeichen verwenden: "Hallo Welt!"''')
a='''Dies hier funktioniert
ebenfalls!'''
print(a)

#6.
#Eine "list" kann verschiedene datentypen sammeln, diese kann man auch nachträglich noch ändern
#und verschieben und hinzufügen.
#Ein "dict" ordnet einem "key" einen Wert hinzu.
#Der "key" muss ein unveränderlicher Datentyp sein.
#Wenn man mehrfach den selben key in einem dict verwendet wird nur der letzte(neuste)
#key verwendet, er überschreibt die alten.

test_list = ["Eine list", "ist eine Sammlung", "von (auch unterschiedlichen) Datentypen",
321, "Man kann die objekte in der Liste auch nachträglich ändern/verschieben"]
print(test_list)

test_dict = {"haus": "haus 1", "maus": "maus 2"}
print(test_dict.get("haus"))


#7.
#__init__ funktioiert als der Constructor
#wird benutzt um einer speziefischen Instanzierung der Klasse (neue) Werte
#zuzuschreiben ohne diese Werte für alle Instanzen der Klasse zuzuschreiben

class TestMe:
    def __init__(self, name, alter, job):
        self.n = name
        self.a = alter
        self.j = job

meineklasse = TestMe("Max Mustermann", 42, "Milchmann")
print(meineklasse.n, meineklasse.a, meineklasse.j)
