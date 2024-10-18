print("Wilkommen in der Lotterie")
number1 = int(input('Bitte eine Zahl zwischen 1 und 49 eingeben: '))
if number1 >= 1 and number1 <= 49:
    number1
else:
    print("Keine Zahl von 1-49 eingegeben!")
    print("Bitte vorgang wiederhohlen!")

number2 = int(input('Bitte eine Zahl zwischen 1 und 49 eingeben: '))
if number2 >= 1 and number2 <= 49:
    number2
else:
    print("Keine Zahl von 1-49 eingegeben!")
    print("Bitte vorgang wiederhohlen!")

number3 = int(input('Bitte eine Zahl zwischen 1 und 49 eingeben: '))
if number3 >= 1 and number1 <= 49:
    number3
else:
    print("Keine Zahl von 1-49 eingegeben!")
    print("Bitte vorgang wiederhohlen!")

if number1 == 3 and number2 == 27 and number3 == 40:
    print("Herzlichen Glückwunsch,du hast die Lotterie gewonnen!")
else:
    print("Du hast leider verloren")