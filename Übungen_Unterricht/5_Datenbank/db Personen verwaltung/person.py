import sqlite3

class Person:
    def __init__(self, person_name=None, person_age=None):
        self.person_name = person_name
        self.person_age = person_age
        
    def new_person(self, cursor):
        cursor.execute('INSERT INTO person (name, age) VALUES (?, ?)', 
                       (self.person_name, self.person_age))
        print("Person hinzugefügt.")

    def del_person(self, cursor, person_id):
        cursor.execute('DELETE FROM person WHERE id = ?', (person_id,))
        print(f"Person mit der ID {person_id} wurde gelöscht.")
    
    def alter_person(self, cursor, person_id, new_name=None, new_age=None):
        if new_name and new_age:
            cursor.execute('UPDATE person SET name = ?, age = ? WHERE id = ?', 
                           (new_name, new_age, person_id))
            print(f"Name und Alter der Person mit der ID {person_id} wurden geändert.")
        elif new_name:
            cursor.execute('UPDATE person SET name = ? WHERE id = ?', 
                           (new_name, person_id))
            print(f"Name der Person mit der ID {person_id} wurde geändert.")
        elif new_age:
            cursor.execute('UPDATE person SET age = ? WHERE id = ?', 
                           (new_age, person_id))
            print(f"Alter der Person mit der ID {person_id} wurde geändert.")
        else:
            print("Keine Änderungen vorgenommen.")

# Verbindung zur Datenbank herstellen
connection = sqlite3.connect('test_with_class.db')
cursor = connection.cursor()

# Tabelle mit einer AUTOINCREMENT-Spalte für die ID erstellen
cursor.execute('''
CREATE TABLE IF NOT EXISTS person(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, 
    age INTEGER)
''')

# Benutzer fragen, ob er hinzufügen, löschen oder ändern möchte
aktion = input("Möchtest du eine Person hinzufügen, löschen oder ändern? (add/del/alt): ").lower()

if aktion == 'del':
    person_id = int(input("Gib die ID der zu löschenden Person ein: "))
    person = Person(None, None)
    person.del_person(cursor, person_id)

elif aktion == 'add':
    person_name = input("Gib den Namen ein: ")
    person_age = int(input("Gib das Alter ein: "))
    person = Person(person_name, person_age)
    person.new_person(cursor)

elif aktion == 'alt':
    person_id = int(input("Gib die ID der zu ändernden Person ein: "))
    new_name = input("Gib den neuen Namen ein (oder drücke Enter, um ihn nicht zu ändern): ")
    new_age = input("Gib das neue Alter ein (oder drücke Enter, um es nicht zu ändern): ")

    # Konvertiere das Alter nur, wenn es eingegeben wurde
    new_age = int(new_age) if new_age else None
    new_name = new_name if new_name else None

    person = Person()  # Name und Alter werden über die update Methode übergeben
    person.alter_person(cursor, person_id, new_name, new_age)

else:
    print("Ungültige Eingabe. Bitte 'add', 'del' oder 'alt' eingeben.")

# Änderungen speichern und Verbindung schließen
connection.commit()
connection.close()
