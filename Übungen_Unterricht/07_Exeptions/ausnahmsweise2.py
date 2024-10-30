from random import randint


class Zahlenratespiel():

    def __init__(self, start=1, ende=100):
        self.start = start
        self.ende = ende
        self.gemerkte_nummer = randint(start, ende)

    def is_nan(self, value: str) -> bool:
        try:
            int(value)
            return False
        except Exception as e:
            print(e)
            return True

    def is_nan_classic_foreach(self, value: str) -> bool:
        # value muss zeichenweise iteriert werden
        # mir ord() wird in Python der Ascii-Wert eines Zeichens zurückgegeben
        for char in value:
            if ord(char) < 48 or ord(char) > 57:
                return True
        return False

    def is_nan_classic(self, value: str) -> bool:
        # value muss zeichenweise iteriert werden
        # mir ord() wird in Python der Ascii-Wert eines Zeichens zurückgegeben
        for i in range(len(value)):
            if ord(value[i]) < 48 or ord(value[i]) > 57:
                return True
        return False

    def mein_tipp(self, tipp):
        if tipp is None or tipp == '':
            raise Exception('Null- oder Leerwert als Tipp!')

        if tipp < self.start or tipp > self.ende:
            raise ValueError(f'Die Grenzen liegen zwischen {self.start} \
                               und {self.ende}.')

        if tipp < self.gemerkte_nummer:
            return 1
        elif tipp > self.gemerkte_nummer:
            return -1
        return 0

zrs = Zahlenratespiel()

print(zrs.is_nan_classic('42a'))