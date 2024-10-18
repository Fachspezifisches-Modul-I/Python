age = int (input("Bitte Alter eingben: "))

if age < 18:
    print("Person ist unter 18 Jahren")
elif age == 18:
    print("Person ist genau 18 Jahre alt.")
elif age == 19:
    print("Person ist genau 19 Jahre alt.")
elif age >= 100:
    print("Schreib am besten dein Testament")
else:
    print("Person ist Volljährig")
print("Programmende")