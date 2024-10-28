'''
Quartett sollmer machen
'''

'''
Array wird benötigt

# Was ist ein Queartett Kartenspiel
Meist 32 Karten in Gruppen je 4 Karten

Wie ist eine Karte definiert?
Die Karte beinhaltet meist ein Bild des Objektes
Titel/Name
Gruppenzugehörigkeit
Eigenschaften die auf allen Karten identisch sind
Meist 5 - 6 verschiedene Eigenschaften


Future Expansion
Kartendatenbank zu erstellung eigener Decks

'''

class QuartettSpiel():
    def __init__(self, *eigenschafts_namen):
        self.card_deck = []
        self.eigenschafts_namen = eigenschafts_namen


class QuartettKarte():

    eigenschaften_liste = None

    def __init__(self, bildle, *arguments):
        self.eigenschaften_liste = arguments
        self.image = bildle



a = None
a = 1
print(a)
class IntegerVariable():

    def __init__(self, value):
        self.a = value

a = IntegerVariable(1)
print(a)
