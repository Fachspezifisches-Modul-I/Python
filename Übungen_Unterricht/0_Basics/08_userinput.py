# Eingabe für Anwendende ermöglichen


alter = 49

if (alter >=18):
    'Du bist voll und jährig!'

# Durch Usereingaben wird es dynamisch

# eingabe = input('Gib mal was ein: ')
# 
# if (int(eingabe) >=18):
#     print('Du bist voll und jährig!')
# else:
#     print('Du bist zu jung')
# 
# print(eingabe)


while True:
    eingabe = input('Gib mal was ein: ')
    
    # Überprüfe, ob die Eingabe eine Zahl ist
    ist_zahl = True
    for char in eingabe:
        if char < '0' or char > '9':  # Überprüfe, ob jedes Zeichen zwischen '0' und '9' liegt
            ist_zahl = False
            break
    
    if ist_zahl:
        # Eingabe ist eine Zahl, Schleife verlassen
        if int(eingabe) >= 18:
            print('Du bist volljährig!')
        else:
            print('Du bist zu jung')
        break
    else:
        # Eingabe ist keine Zahl, Hinweis ausgeben und Schleife fortsetzen
        print("Bitte gib eine Zahl ein!")

print(eingabe)
