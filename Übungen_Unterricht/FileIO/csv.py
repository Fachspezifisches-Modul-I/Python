'''
Datei einlesen
'''

datei_objekt = open('Übungen_Unterricht/FileIO/res/einkaufsliste_comma.csv', encoding="utf-8")
print(datei_objekt)
zeilen = datei_objekt.readlines()

print(len(zeilen))

for zeile in zeilen:
    print(zeile)
