# Iteration 1
# print("Wilkommen in der Lotterie")
# 
# number1 = int(input('Bitte eine Zahl zwischen 1 und 49 eingeben: '))
# if number1 >= 1 and number1 <= 49:
#     number1
# else:
#     print("Keine Zahl von 1-49 eingegeben!")
#     print("Bitte vorgang wiederhohlen!")
# 
# number2 = int(input('Bitte eine Zahl zwischen 1 und 49 eingeben: '))
# if number2 >= 1 and number2 <= 49:
#     number2
# else:
#     print("Keine Zahl von 1-49 eingegeben!")
#     print("Bitte vorgang wiederhohlen!")
# 
# number3 = int(input('Bitte eine Zahl zwischen 1 und 49 eingeben: '))
# if number3 >= 1 and number1 <= 49:
#     number3
# else:
#     print("Keine Zahl von 1-49 eingegeben!")
#     print("Bitte vorgang wiederhohlen!")
# 
# if number1 == 3 and number2 == 27 and number3 == 40:
#     print("Herzlichen Glückwunsch,du hast die Lotterie gewonnen!")
# else:
#     print("Du hast leider verloren")




# Iteration 2
# print("Willkommen in der Lotterie")
# 
# # Liste für die Eingaben erstellen
# zahlen = []
# 
# # Schleife läuft, bis drei gültige Zahlen eingegeben wurden
# while len(zahlen) < 3:
#     number = int(input(f"Bitte Zahl {len(zahlen) + 1} zwischen 1 und 49 eingeben: "))
#     if 1 <= number <= 49:
#         zahlen.append(number)  # Zahl zur Liste hinzufügen, wenn sie gültig ist
#         print(f"Deine Zahl {len(zahlen)} ist {number}")
#     else:
#         print("Keine Zahl von 1-49 eingegeben!")
#         print("Bitte Vorgang wiederholen!")
# 
# Die gewonnenen Zahlen sind: 3, 27, 40
#     print("Herzlichen Glückwunsch, du hast die Lotterie gewonnen!")
# else:
#     print("Du hast leider verloren.")




# Iteration 3
print("Willkommen in der Lotterie")

# Liste für die Eingaben erstellen
zahlen = []

# Schleife läuft, bis drei gültige Zahlen eingegeben wurden
while len(zahlen) < 3:
    number = int(input(f"Bitte Zahl {len(zahlen) + 1} zwischen 1 und 49 eingeben: "))
    if 1 <= number <= 49:
        zahlen.append(number)  # Zahl zur Liste hinzufügen, wenn sie gültig ist
        print(f"Deine Zahl {len(zahlen)} ist {number}")
    else:
        print("Keine Zahl von 1-49 eingegeben!")
        print("Bitte Vorgang wiederholen!")

# Die gewonnenen Zahlen als Menge
gewinnzahlen = {3, 27, 40}

# Gewinnbedingung prüfen, unabhängig von der Reihenfolge
if set(zahlen) == gewinnzahlen:
    print("Herzlichen Glückwunsch, du hast die Lotterie gewonnen!")
else:
    print("Du hast leider verloren.")
